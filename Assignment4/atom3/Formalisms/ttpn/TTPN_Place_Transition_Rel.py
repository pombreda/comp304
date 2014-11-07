# __TTPN_Place_Transition_Rel.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3Integer import *
from graph_TTPN_Place_Transition_Rel import *
class TTPN_Place_Transition_Rel(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_TTPN_Place_Transition_Rel
      self.parent = parent
      self.weight=ATOM3Integer(1)
      self.generatedAttributes = {'weight': ('ATOM3Integer', )      }
      self.realOrder = ['weight']
      self.directEditing = [1]
   def clone(self):
      cloneObject = TTPN_Place_Transition_Rel( self.parent )
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


