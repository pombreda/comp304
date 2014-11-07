"""
IconExchange.py

2006 by Denis Dube
"""

import os

from graph_FSB_Button import graph_FSB_Button


def iconExchanger(self):
  """
  Parameter:
    self, is a semantic object (FSB_Button).
  """
  cx, cy = self.graphObject_.x, self.graphObject_.y
  oldObject = self.graphObject_
  
  iconPath = self.info.iconPath.getValue()
  if(iconPath):                                  # formalism/graph_FOOBAR.py
    importName = os.path.split(iconPath)[1][:-3] # Get graph_FOOBAR
    exec 'from ' + importName + ' import ' + importName + '\n'
    self.graphObject_ = eval(importName + '(cx, cy, self)')
 
  else:
    self.graphObject_ = graph_FSB_Button(cx, cy, self)
      
    
  self.graphObject_.connections = [] + oldObject.connections
  oldObject.erase(self.parent, 0)
  self.graphObject_.DrawObject(self.parent.UMLmodel, self.parent.editGGLabel)
  self.parent.UMLmodel.addtag_withtag(self.__class__.__name__, 
                                      self.graphObject_.tag)
  self.graphObject_.semanticObject = oldObject.semanticObject

  
  