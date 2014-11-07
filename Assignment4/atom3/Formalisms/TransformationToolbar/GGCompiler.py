import os
import time
from traceback import print_exc
from GGMatcher import *
from ASGNode import *
from Tkinter import *


class GGCompiler:
    def __init__(self, graphGrammar, outputFolder, prefix=''):
        self.GG = graphGrammar
        self.outputFolder = outputFolder
        self.output = None
        self.prefix = prefix

    def compileGG(self):
        print 'Generating rule of the grammar', self.GG.Name.getValue(), '...'
        # Generate all the rules of the grammar in sorted order
        ruleList = self.GG.Rules.getValue()
        ruleDict = {}
        for rule in ruleList:
            orderInt = rule.Order.getValue()
            if not ruleDict.has_key(orderInt):
                ruleDict[orderInt] = [rule]
            else:
                ruleDict[orderInt].append(rule)

        sortedKeys = ruleDict.keys()
        sortedKeys.sort()
        
        # This is a window that will pop up at the end of the compilation
        window = Tk()
        window.title('Click on Close')
        frame = Frame(window)           # Temporary frame, used to hide all UI elements thrown to the display during compilation
        outputFrame = Frame(window)
        Button(outputFrame, command=lambda: window.destroy(), text='Close').grid(row=1,column=0,sticky=W)
        
        result = 'The Graph Grammar has been compiled successfully.'
        for key in sortedKeys:
            for rule in ruleDict[key]:
                self.output = open(os.path.join(self.outputFolder, rule.Name.toString().capitalize() + '.py'), "w")
                try:
                    self.compileRule(rule, frame)
                    print 'Generated', os.path.join(self.outputFolder, rule.Name.toString().capitalize() + '.py')
                except:
                    result = 'An error has occurred in rule ' + rule.Name.toString()
                    print_exc()
                finally:
                    self.output.close()
        
        label = Label(outputFrame, text=result)
        label.grid(row=0,column=0,sticky=W)
        outputFrame.pack()
        window.mainloop()

    def compileRule(self, rule, frame):
        LHS = rule.LHS
        RHS = rule.RHS
        NAC = rule.NAC
        
        # Collect a dictionary of all the LHS nodes with their label as key
        LHS_labels = []
        for nt in LHS.listNodes:
            for node in LHS.listNodes[nt]:
                node.editGGLabel = ASGNode.INLHS    # There should be a better way of doing it
                LHS_labels += [node.GGLabel.getValue()]
    
        # Collect a dictionary of all the RHS nodes with their label as key
        RHS_labels = []
        for nt in RHS.listNodes:
            for node in RHS.listNodes[nt]:
                node.editGGLabel = ASGNode.INRHS    # There should be a better way of doing it
                RHS_labels += [node.GGLabel.getValue()]
    
        # Collect a dictionary of all the NAC nodes with their label as key
        NAC_labels = []
        for nt in NAC.listNodes:
            for node in NAC.listNodes[nt]:
                node.editGGLabel = ASGNode.INNAC    # There should be a better way of doing it
                NAC_labels += [node.GGLabel.getValue()]
        
        self.output.write("""'''
_____________________________________________________________

Generated File by the Rule Compiler Generator.
Written by Eugene Syriani

File generated on %s
_____________________________________________________________
'''
""" % (time.ctime()))
        for className in LHS.listNodes:
            self.output.write("""
from %s.%s import *""" % (self.prefix, className))

        self.output.write("""
from copy import deepcopy
from SeededRandom import *


class %s:
  def __init__(self, name='%s'):
    self.name = name
    self.pivot = None           # the pivot node, if any    
    self.graph = None           # the current graph to execute
    self.executed = False       # if the rule has executed after a match or not
    self.Match = []             # the list of the set of all the matched nodes with the corresponding label as key

  def __str__(self):
    return self.name

  def match(self, graph, pivot=None, findAll=False):
    ''' Finds a match for the rule to be applied with the pivot to guide where the matching should start.
        A pivot node can be passed to the rule to optimize matching.
        Finding a single match or all matches can be toggled
    '''
    
    # Constraint for LHS
    def LHSContsraint(Match):
    """ % ((rule.Name.toString().capitalize(), ) * 2))
    
        # Handle transformation pre-condition
        constraint = rule.Condition.getValue()[4] 
        for line in constraint.splitlines():
            self.write('    ' + line + '\n')
#===============================================================================
#        import re
#        lbl = re.search('Match\[(\d+)\]', x)
#        self.code += self.ind * indent + '\n'
#        cond = re.sub('Match\[(\d+)\]', '\g<1>', constraint) + ' and '
#        cond = '(' + constraint.replace('self', var) + ') and '
#===============================================================================
        self.write("""
# Constraint for NAC
def NACContsraint(Match):
""")
    
        # Handle transformation pre-condition
        constraint = rule.NACCondition.getValue()[4] 
        for line in constraint.splitlines():
            self.write('    ' + line + '\n')

        self.write("""
if not graph: raise Exception('Graph was not specified')    # method pre-condition
self.graph = graph                                          # matching on a new graph
self.pivot = pivot                                          # with possibly a new pivot

PACClasses = {}
PACNodes = {}""")
        
        code = '\n'
        # Build PACNodes={label:[Nodes]} the list of the potential nodes of the isomorphic subgraph
        # with the LHS label as key
        for nt in LHS.listNodes:
            for node in LHS.listNodes[nt]:
                classList = "'" + nt + "'"
                if node.GGSubTypeMatching.getValueBoolean():
                    exec 'from ' + nt + ' import ' + nt in globals(), locals()
                    for nst in LHS.listNodes:
                        if nst != nt:
                            exec 'from ' + nst + ' import ' + nst in globals(), locals()
                            #if issubclass(eval(nst), eval(nt)):
                            if eval(nst + '().isSubType(' + nt + '())'):
                                classList += ", '" + nst + "'"
                code += "PACClasses[%s] = [%s]\n" % (node.GGLabel.getValue(), classList)
                code += "PACNodes[%s] = []\n" % (node.GGLabel.getValue())
        # Build NACNodes={label:[Nodes]} the list of the potential unbound (not matched by LHS) nodes of the isomorphic subgraph
        # with the NAC label as key
        code += """
NACClasses = {}
NACNodes = {}
"""
        for nt in NAC.listNodes:
            for node in NAC.listNodes[nt]:
                if node.GGLabel.getValue() not in LHS_labels:
                    classList = "'" + nt + "'"
                    if node.GGSubTypeMatching.getValueBoolean():
                        exec 'from ' + nt + ' import ' + nt in globals(), locals()
                        for nst in LHS.listNodes:
                            exec 'from ' + nst + ' import ' + nst in globals(), locals()
                            #if issubclass(eval(nst), eval(nt)):
                            if eval(nst + '().isSubType(' + nt + '())'):
                                classList += ", '" + nst + "'"
                    code += "NACClasses[%s] = [%s]\n" % (node.GGLabel.getValue(), classList)
                    code += "NACNodes[%s] = []\n" % (node.GGLabel.getValue())
        
        code += """
# Build PACNodes={label:[Nodes]} the list of the potential nodes
# of the isomorphic subgraph with the LHS label as key.
for label in PACClasses:
  for cls in PACClasses[label]:
    if not self.graph.listNodes.has_key(cls):
      self.graph.listNodes[cls] = []
    PACNodes[label] += self.graph.listNodes[cls]
for label in NACClasses:
  for cls in NACClasses[label]:
    if not self.graph.listNodes.has_key(cls):
      self.graph.listNodes[cls] = []
    NACNodes[label] += self.graph.listNodes[cls]

# Sort all nodes to have repeatable rule matching
for label in PACNodes:
  PACNodes[label].sort(key=lambda n: n._id)
for label in NACNodes:
  NACNodes[label].sort(key=lambda n: n._id)

################
# LHS Matching
    
# Check if all nodes in LHS are in the host graph
for k in PACNodes:
  if not PACNodes[k]:
    return
"""
        # Find the LHS pivot
        for nt in LHS.listNodes:
            for node in LHS.listNodes[nt]:
                if node.GGPivot.getValueBoolean():
                    code += """
# Check if the pivot exists in the host graph
if self.pivot:
  for n in PACNodes[%s]:
    if n._id == self.pivot._id:
        break
  else:
    return
""" % (node.GGLabel.getValue())
        
        self.write(code)
        code = ""
        
        # Add the eval attribute to the LHS nodes
        # flag to know if it has been evaluated
        for nt in LHS.listNodes:
            for node in LHS.listNodes[nt]:
                node.eval = False
        
        # Add the eval attribute to the NAC nodes
        # flag to know if it has been evaluated
        for nt in NAC.listNodes:
            for node in NAC.listNodes[nt]:
                node.eval = False
        
        self.write("""
# Verify links between nodes
Match = [ dict() ]      # collector that holds all the matched nodes (by id) with the corresponding label as key
_Match = [ dict() ]     # collector that holds all the matched nodes (actual reference) with the corresponding label as key, used for constraints

""")   # the matched nodes with the corresponding label as key
        
        #################### Match ####################
        
        # Sort nodes by increasing connections
        sortedNodes = []
        for label in LHS_labels:
            sortedNodes.append(LHS.nodeWithLabel(label))
        sortedNodes.sort(key=lambda n: len(n.in_connections_) + len(n.out_connections_))
        
        otherMatches = []       # keeps track of the labels of nodes of each isolated subgraph
        indent = 0
        for node in sortedNodes:
            if not node.eval:
                matcher = NodeMatcher('PACNodes', 'Match[-1]', 'LHSContsraint')
                result = matcher.match(node, (otherMatches, indent), indent=indent)
                otherMatches += result[0]
                indent = result[1]
                self.write(matcher.code)
        self.write("""
self.Match = Match


# Last check if all the nodes in LHS are matched
# And only keep the matches where the pivot is present
i = 0
while i < len(self.Match):
  if len(self.Match[i]) != len(PACNodes):
    del self.Match[i]   # clean
  else: i += 1
""")
        # Find all connected neutral labels (in LHS n NAC)
        NEUTRAL_labels = [str(label) for label in NAC_labels if label in LHS_labels]
        
        # Reset eval before the matching
        for nt in NAC.listNodes:
            for node in NAC.listNodes[nt]:
                node.eval = False
        
        # Sort nodes by increasing connections
        sortedNodes = []
        for label in NAC_labels:
            sortedNodes.append(NAC.nodeWithLabel(label))
        sortedNodes.sort(key=lambda n: len(n.in_connections_) + len(n.out_connections_))
        
        # Perform the remaining NAC matchings
        first = True        # for aesthetic reasons...
        for node in sortedNodes:
            if not node.eval:
                if first:
                    first = False
                    self.write("""
# Check for NACs
matches2remove = []
for matchIndex, Match in enumerate(self.Match):""")
                else:
                    self.write('\n')
                self.write("""
  NACMatch = {}           # reset the NAC collector
  _NACMatch = {}          # reset the NAC collector (used for constraints)
""")
                matcher = NACNodeMatcher('NACNodes', 'NACMatch', 'NACContsraint', NEUTRAL_labels)
                matcher.match(node, indent=1)
                self.write(matcher.code)
                self.write(matcher.end(1))
        
        if NAC_labels: self.write("""

matches2remove.reverse()    # to avoid indexing problems
for i in matches2remove:
    del self.Match[i]
""")
        
        #################### Execute ####################
        
        self.defExec()
        
        if rule.TestRule.getValueBoolean():
            self.end()
            return
        
        self.write("""
# Get the corresponding the nodes of the graph
for nt in self.graph.listNodes:
    for n in self.graph.listNodes[nt]:
""")
        i = 0
        for lab in LHS_labels:
            cond = 'elif'
            if i == 0:
                cond = 'if'
                i += 1
            self.write("""        %s n._id == Match[%s]: Match[%s] = n
""" % (cond, lab, lab))
        del i
        
        # Modify attributes
        self.write("""
# Modify attributes

""")
        for label in LHS_labels:
            rhsNode = RHS.nodeWithLabel(label)
            if not rhsNode: continue        # not in the gluing part (LHS n RHS)
            passed = False                  # for esthetics
            for attrName in rhsNode.generatedAttributes.keys():
                attr = rhsNode.getAttrValue(attrName)
                ASGNode.setGGAnyWidget(rhsNode, frame, None, attrName, 0, 2)    # There should be a better way of doing it
                if rhsNode.GGset2Any and attrName in rhsNode.GGset2Any.keys():
                    atrc = rhsNode.GGset2Any[attrName]
                    # Attribute is to be copied
                    if atrc and atrc.Copy.getValue()[1] == 1:
                        pass
                    else:
                        if not passed:
                            self.write("""# %s
""" % (LHS.nodeWithLabel(label).getClass()))
                            passed = True
                        # Code is specified for this attribute
                        if atrc and atrc.Specify:              
                            name, lang, kind, act, code = atrc.Specify.getValue()
                            if not code:
                                self.writeAttribute(label, attr, attrName)
                            else:
                                self.write(code + '\n')
                        # Just in case, modify directly the value with the one provided
                        else:
                            self.writeAttribute(label, attr, attrName)
                # Modify directly the value
                else:
                    self.write("""# %s
""" % (LHS.nodeWithLabel(label).getClass()))
                    self.writeAttribute(label, attr, attrName)
        
        # Create new nodes
        self.write("""
# Create new nodes

""")
        new_labels = []
        for label in RHS_labels:
            rhsNode = RHS.nodeWithLabel(label)
            if label not in LHS_labels:
                # Add the conn attribute to the RHS nodes to create
                # flag to know if it has been connected to the rest of the graph
                rhsNode.conn = False
                new_labels += [label]
                className = rhsNode.getClass()
                self.write("""# %s
Match[%s] = %s()
self.graph.maxId += 1
Match[%s]._id = self.graph.maxId
if not self.graph.listNodes.has_key('%s'): self.graph.listNodes['%s'] = []
self.graph.listNodes['%s'].append(Match[%s])
""" % (className, label, className, label, className, className, className, label))
                for attrName in rhsNode.generatedAttributes.keys():
                    attr = rhsNode.getAttrValue(attrName)
                    ASGNode.setGGAnyWidget(rhsNode, frame, None, attrName, 0, 2)    # There should be a better way of doing it
                    if rhsNode.GGset2Any and attrName in rhsNode.GGset2Any.keys():
                        atrc = rhsNode.GGset2Any[attrName]
                        # Attribute is to be copied
                        if atrc and atrc.Copy.getValue()[1] == 1:
                            pass
                        else:
                            # Code is specified for this attribute
                            if atrc and atrc.Specify:              
                                name, lang, kind, act, code = atrc.Specify.getValue()
                                if not code:
                                    self.writeAttribute(label, attr, attrName)
                                else:
                                    self.write(code + '\n')
                            # Just in case, modify directly the value with the one provided
                            else:
                                self.writeAttribute(label, attr, attrName)
                    # Modify directly the value
                    else:
                        self.writeAttribute(label, attr, attrName)
        
        # Link the new nodes
        for label in new_labels:
            rhsNode = RHS.nodeWithLabel(label)
            for out in rhsNode.out_connections_:
                if not rhsNode.conn:
                    outLabel = out.GGLabel.getValue()
                    self.write("""# %s -> %s
Match[%s].out_connections_.append(Match[%s])
""" % (rhsNode.getClass(), out.getClass(), label, outLabel))
                    if outLabel not in new_labels:
                        self.write("""Match[%s].in_connections_.append(Match[%s])
""" % (outLabel, label))
            for inp in rhsNode.in_connections_:
                if not rhsNode.conn:
                    inpLabel = inp.GGLabel.getValue()
                    self.write("""# %s -> %s
Match[%s].in_connections_.append(Match[%s])
""" % (rhsNode.getClass(), inp.getClass(), label, inpLabel))
                    if inpLabel not in new_labels:
                        self.write("""Match[%s].out_connections_.append(Match[%s])
""" % (inpLabel, label))
            rhsNode.conn = True

        # Remove
        self.write("""
# Remove nodes

""")
        for label in LHS_labels:
            if label not in RHS_labels:
                # Remove connections and node
                self.write("""# %s
for node in Match[%s].in_connections_:
  node.out_connections_.remove(Match[%s])
for node in Match[%s].out_connections_:
  node.in_connections_.remove(Match[%s])
self.graph.listNodes['%s'].remove(Match[%s])

""" % (LHS.nodeWithLabel(label).getClass(), label, label, label, label, LHS.nodeWithLabel(label).getClass(), label))
        
        new_pivot = None
        for nt in RHS.listNodes:
            for n in RHS.listNodes[nt]:
                if n.GGPivot.getValue()[1] == 1:
                    new_pivot = n
                    break;
            if new_pivot:
                break
        self.end(new_pivot)
    
    
    def writeAttribute(self, label, attr, attrName):
        val = attr.getValue()
        if attr.getTypeName() == 'ATOM3Boolean':
            val = attr.getValueBoolean()
            self.write("""Match[%s].%s = %s
""" % (label, attrName, str(val)))
        elif attr.getTypeName() == 'ATOM3String':
            self.write("""Match[%s].%s = '%s'
""" % (label, attrName, str(val)))
        elif attr.getTypeName() == 'ATOM3Text':
            self.write('''Match[%s].%s = """%s"""
''' % (label, attrName, str(val)))
        elif attr.getTypeName() == 'ATOM3Enum':
            index = val[1]
            val = val[0][index]
            self.write("""Match[%s].%s = '%s'
""" % (label, attrName, str(val)))
        else:
            self.write("""Match[%s].%s = %s
""" % (label, attrName, str(val)))
    
    
    def write(self, code):
        code = code.replace('\n', '\n    ')
        self.output.write(code)

    
    def defExecOld(self):
        self.output.write("""
  
  def execute(self, undoLast=False):
    ''' undoLast: Optional, if true then this is equivalent to an undo of the last transformation and try a different match,
                    otherwise the transformation uses the previously transformed graph.
        Returns a new graph, applying the transformation to the next matched subgraph.
        Returns None if LHS didn't match.
        A pivot may also be returned.
    '''
    
    if not self.hasMatch(): return None, self.pivot
    Match = self.Match.pop(Random.randint(0, len(self.Match) - 1))      # choose a match randomly
    if undoLast: self.graph = deepcopy(self.original_graph)
    self.executed = True
""")

    
    def defExec(self):
        self.output.write("""
  
  def execute(self):
    ''' Returns a new graph, applying the transformation to the next matched subgraph.
        Returns None if LHS didn't match.
        A pivot may also be returned.
    '''
    
    if not self.hasMatch(): return None, self.pivot
    Match = self.Match.pop(Random.randint(0, len(self.Match) - 1))      # choose a match randomly
    self.executed = True
""")


    def end(self, pivot=None):
        if pivot:
            self.write("""
return self.graph, Match[%s]
""" % (pivot.GGLabel.getValue()))
        else:
            self.write("""
return self.graph, self.pivot
""")
        self.output.write("""
  def executeAll(self):
    execResult = None, self.pivot
    while self.hasMatch():
        execResult = self.execute()
    return execResult
  
  def hasMatch(self):
    return len(self.Match) > 0
    
  def hasExecuted(self):
    return self.executed

  def reset(self):
    self.Match = []
    self.graph = None
    self.pivot = None
    self.executed = False

  def rollBack(self, graph):
    self.graph = graph
""")
