"""
__TransformationToolbar_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Ujean
Modified: Sun Oct 05 12:06:53 2008
____________________________________________________________________________________
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

def TransformationToolbar_META(self, rootNode, ButtonsRootNode=None):

    # --- Generating attributes code for ASG Buttons ---
    if( ButtonsRootNode ): 
        # RowSize
        ButtonsRootNode.RowSize.setValue(4)

        # Formalism_File
        ButtonsRootNode.Formalism_File.setValue('TransformationToolbar_MM.py')

        # Formalism_Name
        ButtonsRootNode.Formalism_Name.setValue('TransformationToolbar')
    # --- ASG attributes over ---


    self.obj479=ButtonConfig(self)
    self.obj479.isGraphObjectVisual = True

    if(hasattr(self.obj479, '_setHierarchicalLink')):
      self.obj479._setHierarchicalLink(False)

    # Action
    self.obj479.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nself.editTrans()\n'))

    # Drawing_Mode
    self.obj479.Drawing_Mode.setValue((' ', 0))
    self.obj479.Drawing_Mode.config = 0

    # Contents
    self.obj479.Contents.Text.setValue('Create/Edit')
    self.obj479.Contents.Image.setValue('TransformationToolbar/edit.gif')
    self.obj479.Contents.lastSelected= "Image"

    self.obj479.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(160.0,140.0,self.obj479)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9300000000000006, 1.04]
    else: new_obj = None
    self.obj479.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj479)
    self.globalAndLocalPostcondition(self.obj479, rootNode)
    self.obj479.postAction( rootNode.CREATE )

    self.obj480=ButtonConfig(self)
    self.obj480.isGraphObjectVisual = True

    if(hasattr(self.obj480, '_setHierarchicalLink')):
      self.obj480._setHierarchicalLink(False)

    # Action
    self.obj480.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nself.loadTrans()\n\n'))

    # Drawing_Mode
    self.obj480.Drawing_Mode.setValue((' ', 0))
    self.obj480.Drawing_Mode.config = 0

    # Contents
    self.obj480.Contents.Text.setValue('TransformationToolbar/load.gif')
    self.obj480.Contents.Image.setValue('TransformationToolbar/load.gif')
    self.obj480.Contents.lastSelected= "Image"

    self.obj480.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(160.0,60.0,self.obj480)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9300000000000006, 1.04]
    else: new_obj = None
    self.obj480.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj480)
    self.globalAndLocalPostcondition(self.obj480, rootNode)
    self.obj480.postAction( rootNode.CREATE )

    self.obj481=ButtonConfig(self)
    self.obj481.isGraphObjectVisual = True

    if(hasattr(self.obj481, '_setHierarchicalLink')):
      self.obj481._setHierarchicalLink(False)

    # Action
    self.obj481.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nself.saveTrans()\n'))

    # Drawing_Mode
    self.obj481.Drawing_Mode.setValue((' ', 0))
    self.obj481.Drawing_Mode.config = 0

    # Contents
    self.obj481.Contents.Text.setValue('TransformationToolbar/save')
    self.obj481.Contents.Image.setValue('TransformationToolbar/save.gif')
    self.obj481.Contents.lastSelected= "Image"

    self.obj481.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(160.0,220.0,self.obj481)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9300000000000006, 1.04]
    else: new_obj = None
    self.obj481.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj481)
    self.globalAndLocalPostcondition(self.obj481, rootNode)
    self.obj481.postAction( rootNode.CREATE )

    self.obj482=ButtonConfig(self)
    self.obj482.isGraphObjectVisual = True

    if(hasattr(self.obj482, '_setHierarchicalLink')):
      self.obj482._setHierarchicalLink(False)

    # Action
    self.obj482.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nself.genCode4Trans()\n\n\n'))

    # Drawing_Mode
    self.obj482.Drawing_Mode.setValue((' ', 0))
    self.obj482.Drawing_Mode.config = 0

    # Contents
    self.obj482.Contents.Text.setValue('Generate Code')
    self.obj482.Contents.Image.setValue('TransformationToolbar/gen.gif')
    self.obj482.Contents.lastSelected= "Image"

    self.obj482.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(420.0,60.0,self.obj482)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9300000000000006, 1.04]
    else: new_obj = None
    self.obj482.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj482)
    self.globalAndLocalPostcondition(self.obj482, rootNode)
    self.obj482.postAction( rootNode.CREATE )

    self.obj483=ButtonConfig(self)
    self.obj483.isGraphObjectVisual = True

    if(hasattr(self.obj483, '_setHierarchicalLink')):
      self.obj483._setHierarchicalLink(False)

    # Action
    self.obj483.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nself.executeTrans()\n\n\n'))

    # Drawing_Mode
    self.obj483.Drawing_Mode.setValue((' ', 0))
    self.obj483.Drawing_Mode.config = 0

    # Contents
    self.obj483.Contents.Text.setValue('Execute Code')
    self.obj483.Contents.Image.setValue('TransformationToolbar/exec.gif')
    self.obj483.Contents.lastSelected= "Image"

    self.obj483.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(420.0,140.0,self.obj483)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9300000000000006, 1.04]
    else: new_obj = None
    self.obj483.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj483)
    self.globalAndLocalPostcondition(self.obj483, rootNode)
    self.obj483.postAction( rootNode.CREATE )

    self.obj484=ButtonConfig(self)
    self.obj484.isGraphObjectVisual = True

    if(hasattr(self.obj484, '_setHierarchicalLink')):
      self.obj484._setHierarchicalLink(False)

    # Action
    self.obj484.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nself.genTransDocumentation()\n\n\n\n'))

    # Drawing_Mode
    self.obj484.Drawing_Mode.setValue((' ', 0))
    self.obj484.Drawing_Mode.config = 0

    # Contents
    self.obj484.Contents.Text.setValue('TransformationToolbar/edit.gif')
    self.obj484.Contents.Image.setValue('TransformationToolbar/doc.gif')
    self.obj484.Contents.lastSelected= "Image"

    self.obj484.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(420.0,220.0,self.obj484)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9300000000000006, 1.04]
    else: new_obj = None
    self.obj484.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj484)
    self.globalAndLocalPostcondition(self.obj484, rootNode)
    self.obj484.postAction( rootNode.CREATE )

    self.obj485=ButtonConfig(self)
    self.obj485.isGraphObjectVisual = True

    if(hasattr(self.obj485, '_setHierarchicalLink')):
      self.obj485._setHierarchicalLink(False)

    # Action
    self.obj485.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nfrom HelpDialog import HelpDialog\nHelpDialog( [\'GraphGrammarsTutorial.txt\'] )\n\n'))

    # Drawing_Mode
    self.obj485.Drawing_Mode.setValue((' ', 0))
    self.obj485.Drawing_Mode.config = 0

    # Contents
    self.obj485.Contents.Text.setValue('TransformationToolbar/edit.gif')
    self.obj485.Contents.Image.setValue('TransformationToolbar/help.gif')
    self.obj485.Contents.lastSelected= "Image"

    self.obj485.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(160.0,300.0,self.obj485)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9300000000000006, 1.04]
    else: new_obj = None
    self.obj485.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj485)
    self.globalAndLocalPostcondition(self.obj485, rootNode)
    self.obj485.postAction( rootNode.CREATE )

    self.obj486=ButtonConfig(self)
    self.obj486.isGraphObjectVisual = True

    if(hasattr(self.obj486, '_setHierarchicalLink')):
      self.obj486._setHierarchicalLink(False)

    # Action
    self.obj486.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nimport os\nimport Tkinter\nimport tkFileDialog\nfrom GGCompiler import GGCompiler\n\nif not self.EditingGraphGrammar:\n    tkMessageBox.showerror( "Couldn\'t compile graph grammar generation",\n                            "There is no transformation loaded",\n                            parent = self)\n    return\nroot = Tkinter.Tk()\nroot.title(\'Compile Rule\')\n\n\ngen_env = Tkinter.IntVar(master=root, name=\'gen_env\')\n\ndef promptTarget():\n    directory = self.initialDirectoryDict[\'Documentation\']\n    out_path = tkFileDialog.askdirectory(title="Target folder", initialdir=directory)\n    ETarget.delete(0, Tkinter.END)\n    ETarget.insert(0, out_path)\n\ndef compile():\n    if(not ETarget.get()):\n        return\n\n\n    GGCompiler(self.EditingGraphGrammar, ETarget.get(), EPrefix.get()).compileGG()\n\nLPrefix = Tkinter.Label(root, text=\'Prefix for the Meta-Model module: \').grid(row=0, sticky=Tkinter.W)\nEPrefix = Tkinter.Entry(root, width=30)\n\n\n\nEPrefix.insert(0,\'ATOM3\')\nEPrefix.grid(row=0, column=1)\n\n\n\nLTarget = Tkinter.Label(root, text=\'Choose the target folder for compilation: \').grid(row=1, sticky=Tkinter.W)\nETarget = Tkinter.Entry(root, width=30)\nETarget.grid(row=1, column=1)\nETarget.insert(0, \'C:/Users/Ujean/Desktop/MoTifModel/rules\')\nBTarget = Tkinter.Button(root, text=\'Browse\', command=promptTarget).grid(row=1, column=2)\n\nBGenerate = Tkinter.Button(root, text=\'Compile\', command=compile).grid(row=2, column=1, columnspan=2, pady=5)\n\nroot.mainloop()\n'))

    # Drawing_Mode
    self.obj486.Drawing_Mode.setValue((' ', 0))
    self.obj486.Drawing_Mode.config = 0

    # Contents
    self.obj486.Contents.Text.setValue('TransformationToolbar/edit.gif')
    self.obj486.Contents.Image.setValue('TransformationToolbar/cgen.gif')
    self.obj486.Contents.lastSelected= "Image"

    self.obj486.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(420.0,300.0,self.obj486)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9300000000000006, 1.04]
    else: new_obj = None
    self.obj486.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj486)
    self.globalAndLocalPostcondition(self.obj486, rootNode)
    self.obj486.postAction( rootNode.CREATE )

    # Connections for obj479 (graphObject_: Obj338) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj480 (graphObject_: Obj339) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj481 (graphObject_: Obj340) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj482 (graphObject_: Obj341) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj483 (graphObject_: Obj342) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj484 (graphObject_: Obj343) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj485 (graphObject_: Obj344) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj486 (graphObject_: Obj345) of type ButtonConfig
    self.drawConnections(
 )

newfunction = TransformationToolbar_META

loadedMMName = 'Buttons'

atom3version = '0.3'
