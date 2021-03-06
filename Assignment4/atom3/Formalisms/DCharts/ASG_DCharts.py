"""
__ASG_DCharts.py_____________________________________________________

Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)
Author: Denis Dube
Modified: Wed Nov 30 11:48:19 2005
_____________________________________________________________________
"""
from ASG import *
from ATOM3Type       import *
from ATOM3Text import *
class ASG_DCharts(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'DCharts', ASGroot, ['ASG_DCharts' ,'Composite' ,'Basic' ,'History' ,'Orthogonal' ,'visual_settings' ,'Port' ,'Server' ,'contains' ,'Hyperedge' ,'orthogonality' ,'connection'])

      ATOM3Type.__init__(self)
      self.parent = parent
      self.variables=ATOM3Text('\n', 80,15 )
      self.event_clauses=ATOM3Text('\n', 80,15 )
      self.misc=ATOM3Text('\n', 80,15 )
      self.generatedAttributes = {'variables': ('ATOM3Text', ),
                                  'event_clauses': ('ATOM3Text', ),
                                  'misc': ('ATOM3Text', )      }
      self.realOrder = ['variables','event_clauses','misc']
      self.directEditing = [1,1,0]
   def clone(self):
      return self
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
   def open(self, parent, topWindowParent):
       from ATOM3 import *
       a = ATOM3(topWindowParent, 'DCharts', 0, 1, self)
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
   def preAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None


