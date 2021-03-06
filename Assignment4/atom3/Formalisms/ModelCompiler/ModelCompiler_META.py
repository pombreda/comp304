"""
__ModelCompiler_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Uj
Modified: Mon Oct 22 18:24:10 2007
____________________________________________________________________________
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

def ModelCompiler_META(self, rootNode, ButtonsRootNode=None):

    # --- Generating attributes code for ASG Buttons ---
    if( ButtonsRootNode ): 
        # RowSize
        ButtonsRootNode.RowSize.setValue(4)

        # Formalism_File
        ButtonsRootNode.Formalism_File.setValue('ModelCompiler_MM.py')

        # Formalism_Name
        ButtonsRootNode.Formalism_Name.setValue('ModelCompiler_META')
    # --- ASG attributes over ---


    self.obj21=ButtonConfig(self)
    self.obj21.isGraphObjectVisual = True

    if(hasattr(self.obj21, '_setHierarchicalLink')):
      self.obj21._setHierarchicalLink(False)

    # Action
    self.obj21.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import tkFileDialog\nimport genModel\n\npath = tkFileDialog.askdirectory(title="Choose the output folder", initialdir=self.initialDirectoryDict[\'OpenSaveModel\'])\npath += "\\\\model.py"\n\ngenModel.Compile(self, path)\n\n'))

    # Drawing_Mode
    self.obj21.Drawing_Mode.setValue((' ', 0))
    self.obj21.Drawing_Mode.config = 0

    # Contents
    self.obj21.Contents.Text.setValue('COMPILE')
    self.obj21.Contents.Image.setValue('ModelCompiler/compile.gif')
    self.obj21.Contents.lastSelected= "Image"

    self.obj21.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(140.0,40.0,self.obj21)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21)
    self.globalAndLocalPostcondition(self.obj21, rootNode)
    self.obj21.postAction( rootNode.CREATE )

    # Connections for obj21 (graphObject_: Obj0) of type ButtonConfig
    self.drawConnections(
 )

newfunction = ModelCompiler_META

loadedMMName = 'Buttons'

atom3version = '0.3'
