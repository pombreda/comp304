# __TTPN_Place.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Integer import *
from graph_TTPN_Place import *
class TTPN_Place(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_TTPN_Place
      self.parent = parent
      self.name=ATOM3String('P')
      self.keyword_= self.name
      self.tokens=ATOM3Integer(0)
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'tokens': ('ATOM3Integer', )      }
      self.realOrder = ['name','tokens']
      self.directEditing = [1,1]
   def clone(self):
      cloneObject = TTPN_Place( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      cloneObject.keyword_ = cloneObject.name
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.name
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


