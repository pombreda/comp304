"""
__FSB_Toolbar.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: Denis Dube
Modified: Mon May 29 12:29:46 2006
_____________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Boolean import *
from ATOM3Integer import *
from graph_FSB_Toolbar import *
class FSB_Toolbar(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_FSB_Toolbar
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(True)
      self.parent = parent
      self.FormalismName=ATOM3String('', 20)
      self.enableLayout=ATOM3Boolean()
      self.enableLayout.setValue((None, 0))
      self.enableLayout.config = 0
      self.layoutAnchorX=ATOM3Integer(0)
      self.layoutAnchorY=ATOM3Integer(0)
      self.layoutDirection=ATOM3String('E', 20)
      self.layoutPadding=ATOM3Integer(10)
      self.generatedAttributes = {'FormalismName': ('ATOM3String', ),
                                  'enableLayout': ('ATOM3Boolean', ),
                                  'layoutAnchorX': ('ATOM3Integer', ),
                                  'layoutAnchorY': ('ATOM3Integer', ),
                                  'layoutDirection': ('ATOM3String', ),
                                  'layoutPadding': ('ATOM3Integer', )      }
      self.realOrder = ['FormalismName','enableLayout','layoutAnchorX','layoutAnchorY','layoutDirection','layoutPadding']
      self.directEditing = [1,1,1,1,1,1]
   def clone(self):
      cloneObject = FSB_Toolbar( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def preAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if actionID == self.CREATE:
         self.create(params)
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None
   def QOCA(self, params):
      """
      QOCA Constraint Template
      NOTE: DO NOT select a POST/PRE action trigger
      Constraints will be added/removed in a logical manner by other mechanisms.
      """
      return # <---- Remove this to use QOCA
      
      """ Get the high level constraint helper and solver """
      from Qoca.atom3constraints.OffsetConstraints import OffsetConstraints
      oc = OffsetConstraints(self.parent.qocaSolver)  
      
      """
      Example constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py
      For more types of constraints
      """
      oc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)
      oc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)
      
      

   def create(self, params):
      from FSB_Code.Constructor import toolbarCreate
      toolbarCreate(self)
      



