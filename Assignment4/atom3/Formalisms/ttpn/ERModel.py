from ASG_Buttons import *
from ButtonConfig import *
from ATOM3Enum import *
from ATOM3List import *
from ATOM3Float import *
from ATOM3Integer import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Link import *
def ERModel(self, rootNode):
   rootNode.Formalism_Name.setValue('ERModel')
   rootNode.RowSize.setValue(1)
   rootNode.Formalism_File.setValue('TTPN/ERModel_MM.py')
   self.globalPrecondition(rootNode)

   self.objTTPN_Place=ButtonConfig(self)
   self.objTTPN_Place.Contents.Text.setValue('New TTPN_Place')
   self.objTTPN_Place.Contents.Image.setValue('')
   self.objTTPN_Place.Contents.lastSelected= 'Text'
   self.objTTPN_Place.Drawing_Mode.setValue(1)
   self.objTTPN_Place.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewTTPN_Place (self, wherex, wherey)\n'))
   self.objTTPN_Place.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objTTPN_Place)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objTTPN_Place.graphObject_ = new_obj
   rootNode.addNode(self.objTTPN_Place)
   self.globalAndLocalPostcondition(self.objTTPN_Place, rootNode)
   self.globalPrecondition(rootNode)

   self.objTTPN_Transition=ButtonConfig(self)
   self.objTTPN_Transition.Contents.Text.setValue('New TTPN_Transition')
   self.objTTPN_Transition.Contents.Image.setValue('')
   self.objTTPN_Transition.Contents.lastSelected= 'Text'
   self.objTTPN_Transition.Drawing_Mode.setValue(1)
   self.objTTPN_Transition.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewTTPN_Transition (self, wherex, wherey)\n'))
   self.objTTPN_Transition.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 10,self.objTTPN_Transition)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objTTPN_Transition.graphObject_ = new_obj
   rootNode.addNode(self.objTTPN_Transition)
   self.globalAndLocalPostcondition(self.objTTPN_Transition, rootNode)
   self.globalPrecondition(rootNode)

   self.objrelationship0=ButtonConfig(self)
   self.objrelationship0.Contents.Text.setValue('New relationship0')
   self.objrelationship0.Contents.Image.setValue('')
   self.objrelationship0.Contents.lastSelected= 'Text'
   self.objrelationship0.Drawing_Mode.setValue(1)
   self.objrelationship0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewrelationship0 (self, wherex, wherey)\n'))
   self.objrelationship0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 10,self.objrelationship0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objrelationship0.graphObject_ = new_obj
   rootNode.addNode(self.objrelationship0)
   self.globalAndLocalPostcondition(self.objrelationship0, rootNode)
   self.globalPrecondition(rootNode)

   self.objrelationship1=ButtonConfig(self)
   self.objrelationship1.Contents.Text.setValue('New relationship1')
   self.objrelationship1.Contents.Image.setValue('')
   self.objrelationship1.Contents.lastSelected= 'Text'
   self.objrelationship1.Drawing_Mode.setValue(1)
   self.objrelationship1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewrelationship1 (self, wherex, wherey)\n'))
   self.objrelationship1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 80,self.objrelationship1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objrelationship1.graphObject_ = new_obj
   rootNode.addNode(self.objrelationship1)
   self.globalAndLocalPostcondition(self.objrelationship1, rootNode)
newfunction = ERModel
loadedMMName = 'Buttons'
