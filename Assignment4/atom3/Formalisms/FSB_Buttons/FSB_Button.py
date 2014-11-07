"""
__FSB_Button.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: Denis Dube
Modified: Mon May 29 12:29:46 2006
____________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from FSB_Button_TYPE import *
from graph_FSB_Button import *
class FSB_Button(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_FSB_Button
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(True)
      self.parent = parent
      self.info= iconPathXaction()
      self.info.iconPath=ATOM3String('', 20)
      self.info.action=ATOM3Text('# Button action code\n# The following is generated for you: \n# def action(self): # self = ATOM3 instance\n# Typical contents of action:\n# newPlace = self.createNew<CLASS NAME IN META-MODEL>(self, wherex, wherey)\n# Action that shows dialog to edit ASG attributes:\n# self.modelAttributes(self.ASGroot.getASGbyName("<META-MODEL NAME>_META")) \n', 80,15 )
      self.info.takesActionImmediately=ATOM3Boolean()
      self.info.takesActionImmediately.setValue((None, 0))
      self.info.takesActionImmediately.config = 0
      self.generatedAttributes = {'info': ('ATOM3FSB_Button_TYPE', )      }
      self.realOrder = ['info']
      self.directEditing = [1]
   def clone(self):
      cloneObject = FSB_Button( self.parent )
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
      if actionID == self.EDIT or actionID == self.CREATE:
         self.Edit_Create(params)
      if actionID == self.CREATE:
         self.Create(params)
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
      
      

   def Edit_Create(self, params):
      from FSB_Code.IconExchange import iconExchanger
      iconExchanger(self)
      
      

   def Create(self, params):
      from FSB_Code.Constructor import buttonCreate
      buttonCreate(self)
      
      
      



