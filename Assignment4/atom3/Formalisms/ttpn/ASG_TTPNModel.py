# __ASG_TTPNModel.py_____________________________________________________
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
class ASG_TTPNModel(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'TTPNModel', ASGroot, ['ASG_TTPNModel' ,'TTPN_Place' ,'TTPN_Transition' ,'TTPN_Place_Transition_Rel' ,'TTPN_Transition_Place_Rel'])

      ATOM3Type.__init__(self)
      self.parent = parent
      self.author=ATOM3String('')
      self.description=ATOM3String('')
      self.generatedAttributes = {'author': ('ATOM3String', ),
                                  'description': ('ATOM3String', )      }
      self.realOrder = ['author','description']
      self.directEditing = [1,1]
   def clone(self):
      return self
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
   def open(self, parent, topWindowParent):
       from ATOM3 import *
       a = ATOM3(topWindowParent, 'TTPNModel', 0, 1, self)
       #self.writeContents(a)
       return a
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


