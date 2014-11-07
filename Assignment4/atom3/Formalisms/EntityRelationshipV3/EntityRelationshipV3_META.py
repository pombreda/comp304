"""
__EntityRelationshipV3_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Denis Dube
Modified: Mon Mar 28 15:57:38 2005
___________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from ButtonConfig import *
from graph_ButtonConfig import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def EntityRelationshipV3_META(self, rootNode):

    # RowSize
    try:
        rootNode.RowSize.setValue(4)
    except:
        print "Root model attribute RowSize could not be loaded (most likely cause: the formalism it needs is not open).\n"

    # Formalism_File
    try:
        rootNode.Formalism_File.setValue('EntityRelationshipV3/EntityRelationshipV3_MM.py')
    except:
        print "Root model attribute Formalism_File could not be loaded (most likely cause: the formalism it needs is not open).\n"

    # Formalism_Name
    try:
        rootNode.Formalism_Name.setValue('EntityRelationshipV3')
    except:
        print "Root model attribute Formalism_Name could not be loaded (most likely cause: the formalism it needs is not open).\n"


    self.obj20=ButtonConfig(self)
    self.obj20.isGraphObjectVisual = True


    # Action
    self.obj20.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewEntity3 (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj20.Drawing_Mode.setValue((' ', 1))
    self.obj20.Drawing_Mode.config = 0

    # Contents
    self.obj20.Contents.Text.setValue('New Entity3')
    self.obj20.Contents.Image.setValue('EntityRelationshipV3/Entity.gif')
    self.obj20.Contents.lastSelected= "Image"

    self.obj20.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(240.0,40.0,self.obj20)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.8199999999999985, 0.97999999999999998]
    else: new_obj = None
    self.obj20.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20)
    self.globalAndLocalPostcondition(self.obj20, rootNode)

    self.obj21=ButtonConfig(self)
    self.obj21.isGraphObjectVisual = True


    # Action
    self.obj21.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewRelationship3 (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj21.Drawing_Mode.setValue((' ', 1))
    self.obj21.Drawing_Mode.config = 0

    # Contents
    self.obj21.Contents.Text.setValue('EntityRelationshipV3/relationship.gif')
    self.obj21.Contents.Image.setValue('EntityRelationshipV3/Relationship.gif')
    self.obj21.Contents.lastSelected= "Image"

    self.obj21.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(240.0,100.0,self.obj21)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.8199999999999985, 0.97999999999999998]
    else: new_obj = None
    self.obj21.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21)
    self.globalAndLocalPostcondition(self.obj21, rootNode)

    self.obj22=ButtonConfig(self)
    self.obj22.isGraphObjectVisual = True


    # Action
    self.obj22.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.modelAttributes()\n\n'))

    # Drawing_Mode
    self.obj22.Drawing_Mode.setValue((' ', 0))
    self.obj22.Drawing_Mode.config = 0

    # Contents
    self.obj22.Contents.Text.setValue('')
    self.obj22.Contents.Text.setNone()
    self.obj22.Contents.Image.setValue('EntityRelationshipV3/edit.gif')
    self.obj22.Contents.lastSelected= "Image"

    self.obj22.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(240.0,160.0,self.obj22)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.8199999999999985, 0.97999999999999998]
    else: new_obj = None
    self.obj22.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj22)
    self.globalAndLocalPostcondition(self.obj22, rootNode)

    self.obj23=ButtonConfig(self)
    self.obj23.isGraphObjectVisual = True


    # Action
    self.obj23.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.genCode()\n'))

    # Drawing_Mode
    self.obj23.Drawing_Mode.setValue((' ', 0))
    self.obj23.Drawing_Mode.config = 0

    # Contents
    self.obj23.Contents.Text.setValue('')
    self.obj23.Contents.Text.setNone()
    self.obj23.Contents.Image.setValue('EntityRelationshipV3/gen.gif')
    self.obj23.Contents.lastSelected= "Image"

    self.obj23.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(240.0,220.0,self.obj23)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.8199999999999985, 0.97999999999999998]
    else: new_obj = None
    self.obj23.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj23)
    self.globalAndLocalPostcondition(self.obj23, rootNode)

    self.obj24=ButtonConfig(self)
    self.obj24.isGraphObjectVisual = True


    # Action
    self.obj24.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nfrom HelpDialog import HelpDialog\nHelpDialog( [   \'FormalismsMakingTutorial.txt\',\n                \'GraphGrammarsTutorial.txt\',\n                \'ConstraintsActionsTutorial.txt\',\n                \'ColorAndStippleNames.txt\'          ] )\n\n\n\n'))

    # Drawing_Mode
    self.obj24.Drawing_Mode.setValue((' ', 0))
    self.obj24.Drawing_Mode.config = 0

    # Contents
    self.obj24.Contents.Text.setValue('')
    self.obj24.Contents.Text.setNone()
    self.obj24.Contents.Image.setValue('EntityRelationshipV3/help.gif')
    self.obj24.Contents.lastSelected= "Image"

    self.obj24.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(240.0,280.0,self.obj24)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.8199999999999985, 0.97999999999999998]
    else: new_obj = None
    self.obj24.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24)
    self.globalAndLocalPostcondition(self.obj24, rootNode)
    self.drawConnections( )

newfunction = EntityRelationshipV3_META

loadedMMName = 'Buttons'
