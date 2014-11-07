
class NodeMatcher:
    def __init__(self, nodeListName, matchListName, constraintName):
        self.nodeListName = nodeListName
        self.matchListName = matchListName
        self.constraintName = constraintName
        self.code = ''
        self.ind = '  '
        self.matches = []   # list of matched labels
    
    
    def match(self, node, otherMatches=([],0), previous=[], direction='', indent=0, matchedConn=False):
        ''' node: node to match
            otherMatches: list of the labels of nodes of other matched subgraph
            previous: queue of (n,l) where:
                n: variable name of previously matched nodes
                l: label of n
            direction: direction form n to node
            indent: for formatting code generation
            
            Returns the list of matched labels
        '''
        
        # Preprocessing
        label = str(node.GGLabel.getValue())
        var = node.getClass().lower() + label       # the variable name
        
        node.eval = True
        originalIndent = indent
        
        self.declareNode(node, var, label, otherMatches, previous, indent)
        if previous:
            indent += 1
        
        # Check conditions on attributes
        cond = ''
        for attrName in node.realOrder:
            attr = node.getAttrValue(attrName)
            if not attr.isNone():    # if it is not set to <ANY>
                cond += self.getAttributeValue(var, attr, attrName)
        if cond:
            indent += 1
            self.code += self.ind * indent + """if %s:
""" % (cond[:len(cond) - 5])
        
        if previous and direction:
            indent += 1
            self.code += self.ind * indent + """if %s in %s.%s_connections_:
""" % (var, previous[-1][0], direction)
        
        # Match the nodes connected to this node
        indent += 1
        isLeaf, matchedConn, indent = self._matchConnections(otherMatches, previous, indent, 'in', node.in_connections_, var, label, originalIndent, matchedConn)
        isLeaf1, matchedConn, indent = self._matchConnections(otherMatches, previous, indent, 'out', node.out_connections_, var, label, originalIndent, matchedConn)
        isLeaf = isLeaf and isLeaf1
        
        # Store the nodes if match succeeded
        if isLeaf:
            self.matches = []
            listName = self.matchListName
            if matchedConn:
                indent, listName = self._beforeMatch(indent)
            for n,l in previous:
                self.matches.append((n,l))
                self.code += self.ind * indent + self.assignMatch(listName, l, n)
                self.code += self.ind * indent + """_%s[%s] = %s
""" % (listName, l, n)
            if not matchedConn:
                self.code += self.ind * indent + self.assignMatch(listName, label, var)
                self.code += self.ind * indent + """_%s[%s] = %s
""" % (listName, label, var)
            if previous:
                self.code += self.ind * indent + """if not %s(_%s):
""" % (self.constraintName, self.matchListName)
                self.code += self.ind * (indent + 1) + """del %s[%s]
""" % (self.matchListName, label) 
        self.matches.append((var,label))
        self.code += self._afterMatch(originalIndent, label)
        
        return self.matches, indent
    
    
    def getAttributeValue(self, var, attr, attrName):
        val = attr.getValue()
        if attr.getTypeName() == 'ATOM3Boolean':
            val = attr.getValueBoolean()
            return "%s.%s == %s and " % (var, attrName, str(val))
        elif attr.getTypeName() == 'ATOM3String':
            return "%s.%s == '%s' and " % (var, attrName, str(val))
        elif attr.getTypeName() == 'ATOM3Text':
            return '''%s.%s == """%s""" and ''' % (var, attrName, str(val))
        elif attr.getTypeName() == 'ATOM3Enum':
            index = val[1]
            val = val[0][index]
            return "%s.%s == '%s' and " % (var, attrName, str(val))
        else:
            return "%s.%s == %s and " % (var, attrName, str(val))
        
    def _matchConnections(self, otherMatches, previous, indent, direction, connections, var, label, originalIndent, matchedConn=False):
        isLeaf = True
        countConn = 0
        for node in connections:
            lbl = str(node.GGLabel.getValue())
            # Check if already visited. This is the case if is in an undirected cycle
            if (not node.eval) and not (lbl in map(lambda x: x[1], previous)):
                isLeaf = False
                self.match(node, otherMatches, previous + [(var, label)], direction, indent, matchedConn)
                countConn += 1
            elif lbl in map(lambda x: x[1], previous[:-1]):
                # The current node (var, label) is connected to a previously matched node, anterior to the node matched just before
                prevVar = node.getClass().lower() + lbl
                self.code += self.ind * indent + """if %s in %s.%s_connections_:
""" % (prevVar, var, direction)
                indent += 1
        matchedConn = countConn > 1
        return isLeaf, matchedConn, indent
    
    
    def declareNode(self, node, var, label, otherMatches, previous, indent):
        self.code += self.ind * indent + """for %s in %s[%s]:
""" % (var, self.nodeListName, label)
        if node.GGPivot.getValue()[1] == 1:
            self.code += self.ind * (indent + 1) + """if self.pivot and %s._id != self.pivot._id:
""" % (var) + self.ind * (indent + 2) + """continue    # only choose the pivot, if provided
"""     
        if self.identificationConstraint(var, previous, indent):
            indent += 1
        # self.code += self.ind * (indent + 1) + """if findAll and %s.has_key(%s):
# """ % (self.matchListName, label)
        self.code += self.ind * (indent + 1) + """if %s.has_key(%s):
""" % (self.matchListName, label)
        indent = self.ind * (indent + 2)
        self.code += indent + """# Keep previously matched nodes only
""" + indent + """cpy = dict()
"""
        for n,l in otherMatches[0]:
            self.code += indent + """if %s.has_key(%s):
""" % (self.matchListName, l) + indent + """  cpy[%s] = %s[%s]
""" % (l, self.matchListName, l)
        for n,l in previous:
            self.code += indent + """cpy[%s] = %s[%s]
""" % (l, self.matchListName, l)
        
        listName = self.matchListName
        if listName.find('[-1]'):       # for list of dict
            listName = listName[:-4]
        self.code += indent + """%s.append(cpy)
""" % (listName)

    def identificationConstraint(self, var, previous, indent):
        if previous:
            # Identification constraint
            cond = ''
            for prev in previous:
                cond += var + ' != ' + prev[0] + ' and '
            indent += 1
            self.code += self.ind * indent + """if %s:
""" % (cond[:-5])
        return len(previous) > 0
    
    
    def assignMatch(self, listName, label, var):
        return """%s[%s] = %s._id
""" % (listName, label, var)

    
    def end(self, indent):
        return '\n'
    
    
    def _beforeMatch(self, indent):
        listName = self.matchListName
        if listName.find('[-1]'):       # only for list of dict
            listName = listName[:-4]
            self.code += self.ind * indent + """for m in %s:
""" % (listName) + self.ind * (indent + 1) + """if m.has_key(%s):
""" % (previous[0][1])
            return indent + 2
        return indent, 'm'
    
    def resetMatch(self):
        return '[dict()]'
    
    
    def _afterMatch(self, indent, label):
        # return self.ind * (indent + 1) + """if (not findAll) and %s.has_key(%s):
# """ % (self.matchListName, label) + self.ind * (indent + 2) + """break
# """
        return ''


class NACNodeMatcher(NodeMatcher):
    def __init__(self, nodeListName, matchListName, constraintName, neutralLabels=[]):
        NodeMatcher.__init__(self, nodeListName, matchListName, constraintName)
        self.neutralLabels = neutralLabels
    
    
    def declareNode(self, node, var, label, otherMatches, previous, indent):
        if label in self.neutralLabels:
            self.code += self.ind * indent + """for n in PACNodes[%s]:
""" % (label) + self.ind * (indent + 1) + """if Match[%s] == n._id:
""" % (label) + self.ind * (indent + 2) + """%s = n    # this node is bound to a matched node
""" % (var) + self.ind * (indent + 1) + """else: continue
"""
        else:
            self.code += self.ind * indent + """for %s in %s[%s]:
""" % (var, self.nodeListName, label)
        
        self.identificationConstraint(var, previous, indent)
    
    
    def assignMatch(self, listName, label, var):
        return """%s[%s] = True
""" % (listName, label)

    
    def end(self, indent):
        s = self.ind * indent + 'if '
        import math
        last = int(math.ceil(len(self.matches) / 2.0))
        for i,m in enumerate(self.matches[:last]):
            label = int(m[1])
            s += '%s.has_key(%s)' % (self.matchListName, label)
            if i < last - 1:
                s += ' \\\n' + self.ind * (indent + 1) + ' and '
            else: s += ':\n'
        s += self.ind * (indent + 1) + """matches2remove.append(matchIndex)
""" + self.ind * (indent + 1) + 'continue'
        return s
    
    
    def _beforeMatch(self, indent):
        return indent, ''
    
    def resetMatch(self):
        return '{}'
    
    
    def _afterMatch(self, indent, label):
        return self.ind * (indent + 1) + """if %s.has_key(%s):
""" % (self.matchListName, label) + self.ind * (indent + 2) + """break
"""
