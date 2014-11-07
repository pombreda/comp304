"""
__Hyperedge.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: Denis Dube
Modified: Wed Nov 30 11:48:19 2005
___________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Text import *
from graph_Hyperedge import *
class Hyperedge(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_Hyperedge
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(False)
      self.parent = parent
      self.trigger=ATOM3String('')
      self.guard=ATOM3String('1')
      self.action=ATOM3Text('', 60,15 )
      self.broadcast=ATOM3Text('# return an instance of DEVSevent or None\nreturn None\n', 60,15 )
      self.broadcast_to=ATOM3String('')
      self.name=ATOM3String('')
      self.display=ATOM3String('')
      self.generatedAttributes = {'trigger': ('ATOM3String', ),
                                  'guard': ('ATOM3String', ),
                                  'action': ('ATOM3Text', ),
                                  'broadcast': ('ATOM3Text', ),
                                  'broadcast_to': ('ATOM3String', ),
                                  'name': ('ATOM3String', ),
                                  'display': ('ATOM3String', )      }
      self.realOrder = ['trigger','guard','action','broadcast','broadcast_to','name','display']
      self.directEditing = [1,1,1,1,1,1,1]
   def clone(self):
      cloneObject = Hyperedge( self.parent )
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
      if actionID == self.DELETE:
         res = self.Hyperedge_DELETE(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if actionID == self.CREATE:
         res = self.Hyperedge_CREATE(params)
         if res: return res
      if actionID == self.CONNECT:
         res = self.Hyperedge_CONNECT(params)
         if res: return res
      if actionID == self.DROP:
         res = self.Hyperedge_DROP(params)
         if res: return res
      if actionID == self.MOVE:
         res = self.Hyperedge_MOVE(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def Hyperedge_CREATE(self, params):
      import DCharts_utils
      DCharts_utils.Hyperedge_CREATE(self)
      

   def Hyperedge_CONNECT(self, params):
      import DCharts_utils
      DCharts_utils.Hyperedge_CONNECT(self)
      

   def Hyperedge_DELETE(self, params):
      import DCharts_utils
      DCharts_utils.Hyperedge_DELETE(self)
      
      

   def Hyperedge_DROP(self, params):
      import DCharts_utils
      DCharts_utils.Hyperedge_DROP(self)
      

   def Hyperedge_MOVE(self, params):
      import DCharts_utils
      DCharts_utils.Hyperedge_MOVE(self)
      

   def preAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None


