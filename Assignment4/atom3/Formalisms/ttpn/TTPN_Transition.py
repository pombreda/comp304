# __TTPN_Transition.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Integer import *
from ATOM3Boolean import *
from graph_TTPN_Transition import *
class TTPN_Transition(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_TTPN_Transition
      self.parent = parent
      self.name=ATOM3String('T')
      self.keyword_= self.name
      self.time=ATOM3Integer(0)
      self.processes=ATOM3Integer(1)
      self.atomic=ATOM3Boolean()
      self.atomic.setValue((None, 1))
      self.atomic.config = 0
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'time': ('ATOM3Integer', ),
                                  'processes': ('ATOM3Integer', ),
                                  'atomic': ('ATOM3Boolean', )      }
      self.realOrder = ['name','time','processes','atomic']
      self.directEditing = [1,1,1,1]
   def clone(self):
      cloneObject = TTPN_Transition( self.parent )
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


