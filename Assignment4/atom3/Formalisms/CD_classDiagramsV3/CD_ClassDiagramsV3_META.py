"""
__CD_ClassDiagramsV3_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Ujean
Modified: Fri May 15 13:53:07 2009
_________________________________________________________________________________
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

def CD_ClassDiagramsV3_META(self, rootNode, ButtonsRootNode=None):

    # --- Generating attributes code for ASG Buttons ---
    if( ButtonsRootNode ): 
        # RowSize
        ButtonsRootNode.RowSize.setValue(4)

        # Formalism_File
        ButtonsRootNode.Formalism_File.setValue('CD_ClassDiagramsV3_MM.py')

        # Formalism_Name
        ButtonsRootNode.Formalism_Name.setValue('CD_ClassDiagramsV3')
    # --- ASG attributes over ---


    self.obj36=ButtonConfig(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    # Action
    self.obj36.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nself.modelAttributes(self.ASGroot.getASGbyName("CD_ClassDiagramsV3_META")) \n\n'))

    # Drawing_Mode
    self.obj36.Drawing_Mode.setValue((' ', 0))
    self.obj36.Drawing_Mode.config = 0

    # Contents
    self.obj36.Contents.Text.setValue('New Edit')
    self.obj36.Contents.Image.setValue('CD_classDiagramsV3/icons/edit.gif')
    self.obj36.Contents.lastSelected= "Image"

    self.obj36.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(380.0,60.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.3000000000000007, 1.2200000000000002]
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj37=ButtonConfig(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # Action
    self.obj37.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nfrom HelpDialog import HelpDialog\nHelpDialog(["CD_ClassDiagramsV3Help.txt"])\n\n'))

    # Drawing_Mode
    self.obj37.Drawing_Mode.setValue((' ', 0))
    self.obj37.Drawing_Mode.config = 0

    # Contents
    self.obj37.Contents.Text.setValue('New Help')
    self.obj37.Contents.Image.setValue('CD_classDiagramsV3/icons/help.gif')
    self.obj37.Contents.lastSelected= "Image"

    self.obj37.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(380.0,180.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.3000000000000007, 1.2200000000000002]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj38=ButtonConfig(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    # Action
    self.obj38.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewCD_Association3 (self, wherex, wherey)\n\n'))

    # Drawing_Mode
    self.obj38.Drawing_Mode.setValue((' ', 1))
    self.obj38.Drawing_Mode.config = 0

    # Contents
    self.obj38.Contents.Text.setValue('New Association3')
    self.obj38.Contents.Image.setValue('CD_classDiagramsV3/icons/Association.gif')
    self.obj38.Contents.lastSelected= "Image"

    self.obj38.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(80.0,180.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.3000000000000007, 1.2200000000000002]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj39=ButtonConfig(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # Action
    self.obj39.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewCD_Inheritance3 (self, wherex, wherey)\n\n'))

    # Drawing_Mode
    self.obj39.Drawing_Mode.setValue((' ', 1))
    self.obj39.Drawing_Mode.config = 0

    # Contents
    self.obj39.Contents.Text.setValue('New Inheritance3')
    self.obj39.Contents.Image.setValue('CD_classDiagramsV3/icons/Inherits.gif')
    self.obj39.Contents.lastSelected= "Image"

    self.obj39.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(80.0,300.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.3000000000000007, 1.2200000000000002]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=ButtonConfig(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # Action
    self.obj40.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewCD_Class3 (self, wherex, wherey)\n\n'))

    # Drawing_Mode
    self.obj40.Drawing_Mode.setValue((' ', 1))
    self.obj40.Drawing_Mode.config = 0

    # Contents
    self.obj40.Contents.Text.setValue('New Class3')
    self.obj40.Contents.Image.setValue('CD_classDiagramsV3/icons/Class.gif')
    self.obj40.Contents.lastSelected= "Image"

    self.obj40.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(80.0,60.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.3000000000000007, 1.2200000000000002]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=ButtonConfig(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # Action
    self.obj41.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from inheritanceGenerator import genCode\ngenCode( self )\n\n'))

    # Drawing_Mode
    self.obj41.Drawing_Mode.setValue((' ', 0))
    self.obj41.Drawing_Mode.config = 0

    # Contents
    self.obj41.Contents.Text.setValue('')
    self.obj41.Contents.Text.setNone()
    self.obj41.Contents.Image.setValue('CD_classDiagramsV3/icons/gen.gif')
    self.obj41.Contents.lastSelected= "Image"

    self.obj41.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(379.11173714,293.813565352,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.3000000000000012, 1.1600000000000001]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=ButtonConfig(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # Action
    self.obj42.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from AToM3LayoutInterfaceModule.AbstractGraph import AbstractGraph\n\nfrom HierarchicalLayoutModule.HierarchicalLayout import doHierarchicalLayout \\\n  as hierarchicalLayoutMethod\n\n\n# Hierarchical Layout Options\noptionsDict = dict()\noptionsDict[\'Origin\'] = True\noptionsDict[\'EdgePromotion\'] = \'Always\' # [\'Never\', \'Smart\', \'Always\']\noptionsDict[\'LayoutDirection\'] = \'South\' # [\'North\', \'East\', \'South\', \'West\']\noptionsDict[\'yOffset\'] = 20\noptionsDict[\'xOffset\'] = 20\noptionsDict[\'layerAlg\'] = \'BFS\' # [\'BFS\', \'Longest-path\', \'Minimum-width\']\noptionsDict[\'maxTotalRounds\'] = 50\noptionsDict[\'maxNoProgressRounds\'] = 10\noptionsDict[\'crossAlgChoice\'] = \'Both\' # [\'None\', \'Barycenter\', \'Transpose\', \'Both\']\noptionsDict[\'randomRestartsWith\'] = \'Both\' # [\'None\', \'Barycenter\', \'Transpose\', \'Both\']\noptionsDict[\'baryPlaceMax\'] = 100\noptionsDict[\'Arrow curvature\'] = 3\noptionsDict[\'Spline optimization\'] = True\n\nabstractGraph = AbstractGraph(self, [])\nhierarchicalLayoutMethod(abstractGraph, optionsDict)    \nabstractGraph.updateAToM3(quickUpdate=False)\n\n'))

    # Drawing_Mode
    self.obj42.Drawing_Mode.setValue((' ', 0))
    self.obj42.Drawing_Mode.config = 0

    # Contents
    self.obj42.Contents.Text.setValue('')
    self.obj42.Contents.Text.setNone()
    self.obj42.Contents.Image.setValue('CD_classDiagramsV3/icons/layered.gif')
    self.obj42.Contents.lastSelected= "Image"

    self.obj42.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(80.0,380,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.2972972972972974, 1.0892857142857142]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=ButtonConfig(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # Action
    self.obj43.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from AToM3LayoutInterfaceModule.AbstractGraph import AbstractGraph\n\nfrom ForceTransferModule.ForceTransfer import doForceTransfer \\\n  as forceTransferMethod\\\n\nfrom SpringLayoutModule.SpringLayout import doSpringLayout \\\n  as springElectricalMethod\n\nfrom CircleLayoutModule.CircleLayout import doCircleLayout \\\n  as circleLayoutMethod\n\n# Circle Layout Options\noptionsDict = dict()\noptionsDict[\'Origin\'] = True\noptionsDict[\'Spline optimization\'] = False\noptionsDict[\'Offset\'] = 0\noptionsDict[\'EdgePromotion\'] = \'Always\' # [\'Never\', \'Smart\', \'Always\']\noptionsDict[\'Arrow curvature\'] = 0\n\nabstractGraph = AbstractGraph(self, [])\ncircleLayoutMethod(abstractGraph, optionsDict)    \nabstractGraph.updateInternally()\n\n# Spring Layout Options\noptionsDict = dict()\noptionsDict[\'Origin\'] = True\noptionsDict[\'Random amount\'] = 0\noptionsDict[\'Maximum iterations\'] = 100\noptionsDict[\'Forgiveness rounds\'] = 2\noptionsDict[\'Minimum force\'] = 10.0\noptionsDict[\'Arrow curvature\'] = 0\noptionsDict[\'Spring rest length\'] = 100\noptionsDict[\'EdgePromotion\'] = \'Always\' # [\'Never\', \'Smart\', \'Always\']\noptionsDict[\'Gravity strength\'] = 10\noptionsDict[\'Charge strength\'] = 10.0\noptionsDict[\'Charge threshold\'] = 300\noptionsDict[\'Spring constant\'] = 0.1\noptionsDict[\'Spline optimization\'] = False\n\nfrom SpringLayoutModule.AToM3SpringOptions \\\n  import showSpringOptions \noptionsDict = showSpringOptions(self)\nspringElectricalMethod(abstractGraph, optionsDict)    \nabstractGraph.updateInternally()\n\n# Force-Transfer Layout Options\noptionsDict = dict()\noptionsDict[\'EdgePromotion\'] = \'Always\' # [\'Never\', \'Smart\', \'Always\']\noptionsDict[\'Minimum link distance\'] = 20\noptionsDict[\'Minimum node distance\'] = 20\noptionsDict[\'Max Total Iterations\'] = 100\noptionsDict[\'Seperation Force\'] = 0.2\noptionsDict[\'Arrow curvature\'] = 5\noptionsDict[\'Border Distance\'] = -1\noptionsDict[\'Spline optimization\'] = True\n\n\nforceTransferMethod(abstractGraph, optionsDict)    \nabstractGraph.updateAToM3(quickUpdate=False)\n\n'))

    # Drawing_Mode
    self.obj43.Drawing_Mode.setValue((' ', 0))
    self.obj43.Drawing_Mode.config = 0

    # Contents
    self.obj43.Contents.Text.setValue('')
    self.obj43.Contents.Text.setNone()
    self.obj43.Contents.Image.setValue('CD_classDiagramsV3/icons/circleSpringFTA.gif')
    self.obj43.Contents.lastSelected= "Image"

    self.obj43.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(380.0,380,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.2792792792792791, 1.0714285714285714]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=ButtonConfig(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # Action
    self.obj44.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nimport Tkinter\nfrom RAM import RAM\n\nroot = Tkinter.Tk()\nroot.title(\'Relax/Augment/Modify the meta-model\')\n\ndef run():\n    path = RAM(self, mode.get())\n    if path:\n        root.withdraw()\n\nTkinter.Label(root, text=\'Choose the RAM mode:\').grid(row=0, column=0, columnspan=2, sticky=Tkinter.W)\n\nMODES = [ ("PRE", "1"), ("POST", "0") ]\nmode = Tkinter.StringVar()\nmode.set("0")  # initialize\nfor i,m in enumerate(MODES):\n    text, value = m\n    rb = Tkinter.Radiobutton(root, text=text, variable=mode, value=value)\n    rb.grid(row=1, column=i, sticky=Tkinter.W)\n    if i == 0:\n        rb.select()\n\nTkinter.Button(root, text=\'Run\', command=run).grid(row=2, column=0, sticky=Tkinter.W)\n\nroot.mainloop()\n\nself.ASGroot.listNodes[\'CD_Class3\'][0].attributes.getValue()[1].getValue()\n'))

    # Drawing_Mode
    self.obj44.Drawing_Mode.setValue((' ', 0))
    self.obj44.Drawing_Mode.config = 0

    # Contents
    self.obj44.Contents.Text.setValue('RAM')
    self.obj44.Contents.Image.setValue('')
    self.obj44.Contents.Image.setNone()
    self.obj44.Contents.lastSelected= "Text"

    self.obj44.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(160.0,520.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    # Connections for obj36 (graphObject_: Obj4) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj37 (graphObject_: Obj5) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj38 (graphObject_: Obj6) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj39 (graphObject_: Obj7) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj40 (graphObject_: Obj8) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj41 (graphObject_: Obj9) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj42 (graphObject_: Obj10) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj43 (graphObject_: Obj11) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj44 (graphObject_: Obj12) of type ButtonConfig
    self.drawConnections(
 )

newfunction = CD_ClassDiagramsV3_META

loadedMMName = 'Buttons'

atom3version = '0.3'
