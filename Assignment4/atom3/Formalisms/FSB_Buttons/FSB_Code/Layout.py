"""
Layout.py

2006 by Denis Dube
"""

from AToM3LayoutInterfaceModule.AbstractGraph import AbstractGraph

from HierarchicalLayoutModule.HierarchicalLayout import doHierarchicalLayout \
  as hierarchicalLayoutMethod

def toolbarLayout(self):
  """
  Intention in context:
    Perform all layout necessary for one button toolbar, includes:
      1) Relative ordering of icons (i.e., buttons should not be behind toolbar)
      2) Layered drawing technique (place icons in a row or column)
      3) Anchor (place toolbar at an (x, y) position)
      4) Shrink wrap (re-size toolbar to fit buttons)
  Parameter:
    self = a semantic object (i.e., Toolbar instance), with the following:
      1) It is hierarchical
      2) Has boolean attribute: enableLayout
      3) Has string attribute: layoutDirection
      4) Has integer attribute: layoutPadding
      5) Has integer attribute: layoutAnchorX
      6) Has integer attribute: layoutAnchorY
  """
  if(not self.enableLayout.getValueBoolean()):
    return
  
  atom3i = self.parent
  
  # Starting from the root, the following method is recursively 
  # propagated down the hierarchy tree
  def boundMethod(childNode):
    """ Raises the order of a graphical object associated with the ASGNode """
    if(childNode.graphObject_): 
      childNode.graphObject_.raiseItem()   
      
  self.hierPropagateMethodDown(boundMethod)
  
  # Layered layout
  characterString = self.layoutDirection.getValue()
  characterString = characterString.upper()
  if(len(characterString) != 1):
    characterString = 'E'
    self.layoutDirection.setValue(characterString)
  directionMap = {'E':'East', 'W':'West', 'N':'North', 'S':'South'}
  
  doHierarchicalLayout(self, direction=directionMap[characterString],
                             padding=self.layoutPadding.getValue())
          
  # Move everything away from the origin
  applyOffset(self, self.layoutAnchorX.getValue(), self.layoutAnchorY.getValue())
  
  # Shrink wrap
  shrinkWrapLayout(self, padding=5, includeArrows=False, 
                   polygonGF=self.graphObject_.gf5)
                   
  
  
def applyOffset(self, dx, dy):
  """ 
  Intention in context:
    Simply moves all the icons by dx and dy from where they were 
  Parameter:
    self, semantic object, assumed to be hierarchical
  """
  if(dx == 0 and dy == 0):
    return
  for child in self.getHierChildren(): # Could be empty: []
    child.graphObject_.Move(dx, dy, moveConn=False)
  
  
def doHierarchicalLayout(self, direction='East', padding=20):
  """
  Intention in context:
    Perform layered drawing layout
  Parameters:
    self, semantic object, assumed to be hierarchical
    direction, the direction the layout will be drawn in
    padding, additional space between the children icons
  """
  
  # Hierarchical Layout Options
  optionsDict = dict()
  optionsDict['Origin'] = True
  optionsDict['EdgePromotion'] = 'Never' # ['Never', 'Smart', 'Always']
  optionsDict['LayoutDirection'] = direction # ['North', 'East', 'South', 'West']
  optionsDict['yOffset'] = padding
  optionsDict['xOffset'] = padding
  optionsDict['layerAlg'] = 'BFS' # ['BFS', 'Longest-path', 'Minimum-width']
  optionsDict['maxTotalRounds'] = 1
  optionsDict['maxNoProgressRounds'] = 1
  optionsDict['crossAlgChoice'] = 'None' # ['None', 'Barycenter', 'Transpose', 'Both']
  optionsDict['randomRestartsWith'] = 'None' # ['None', 'Barycenter', 'Transpose', 'Both']
  optionsDict['baryPlaceMax'] = 1
  optionsDict['Arrow curvature'] = 0
  optionsDict['Spline optimization'] = False
  
  # Gather all children VERTICES and EDGES
  graphObjectList = [] # List of direct children graph objects
  for child in self.getHierChildren(): # Could be empty: []
    graphObjectList.append(child.graphObject_)
    for link in child.out_connections_: # For each arrow from child
      for nextchild in link.out_connections_: # For each arrow endpoint obj
        graphObjectList.append(link.graphObject_)
  
  abstractGraph = AbstractGraph(self.parent, graphObjectList) 
  hierarchicalLayoutMethod(abstractGraph, optionsDict)    
  abstractGraph.updateAToM3(quickUpdate=False)
  
  
def shrinkWrapLayout(self, padding=100, includeArrows=True, polygonGF=None):
  """
  Use: 
    Positions and scales the parent of hierarchical children to graphically
    contain the children. 
  Parameters: 
    self, semantic node entity
    padding, how many pixels larger than the children we are
    includeArrows, if true: expand enough to contain all arrows
    polygonGF, if the graphical form object is provided, wrap coordinates are
               directly set to the polygon object rather than using scale
               (i.e.: self.graphObject_.gf5)
  Return Values:
    True if no change occured in the size and position of this object
    False if a change occured
  """
  #print 'shrinkWrapLayout', self.name.toString()
  #return
  
  obj = self.graphObject_
  if(not obj): 
    return True
    
  # Do we even have children? Maybe we are barren... if so resume default size
  immediateChildren = self.getHierChildren()
  #print '\nshrinkwrapping', self.name.toString()
  if(not immediateChildren):
    oldSize = obj.getSize()
    obj.resetScale()
    newSize = obj.getSize()
    # If size really did change, return False
    if(oldSize[0] != newSize[0] or oldSize[1] != newSize[1]):
      return False
    return True
    
  if(includeArrows):
    childrenLinks = []
    for child in immediateChildren:
      for link in child.in_connections_:
        childrenLinks.append(link)
    immediateChildren += childrenLinks
    
  
  # Get boundary that includes all children (immediate children only)
  minx, miny, maxx, maxy = 10000, 10000, -10000, -10000
  for child in immediateChildren:
    if(child.graphObject_):           
      bbx = child.graphObject_.getbbox()
      if(bbx == [0, 0, 0, 0]):
        continue
            
      if bbx[0] < minx: 
        minx = bbx[0]
      if bbx[1] < miny: 
        miny = bbx[1]
      if bbx[2] > maxx: 
        maxx = bbx[2]
      if bbx[3] > maxy:         
        maxy = bbx[3]
        
  # Scale to fit all the children (plus a small offset to be larger)
  desiredWidth =  maxx - minx + padding
  desiredHeight = maxy - miny + padding
  obj.easyScale(desiredWidth, desiredHeight)

  # Maintain the top-left position (relative to all the children)
  oldCoords = obj.getbbox()[:2]
  halfPadding = padding / 2
  dx = minx - oldCoords[0] - halfPadding 
  dy = miny - oldCoords[1] - halfPadding
  obj.Move(dx, dy, moveConn=False)
    
  # This method is VERY precise for setting the box, however it does not work
  # when the model is saved and then re-loaded :(
  if(polygonGF):
    minx -= padding
    maxx += padding
    miny -= padding
    maxy += padding
    polygonGF.setCoords([maxx, miny, minx, miny, minx, maxy, maxx, maxy])    
    
  return False
  
