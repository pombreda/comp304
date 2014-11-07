"""
__DCharts_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Denis Dube
Modified: Wed Nov 30 11:44:26 2005
______________________________________________________________________
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

def DCharts_META(self, rootNode, ButtonsRootNode=None):

    # --- Generating attributes code for ASG Buttons ---
    if( ButtonsRootNode ): 
        # RowSize
        ButtonsRootNode.RowSize.setValue(1)

        # Formalism_File
        ButtonsRootNode.Formalism_File.setValue('DCharts/DCharts_MM.py')

        # Formalism_Name
        ButtonsRootNode.Formalism_Name.setValue('DCharts')
    # --- ASG attributes over ---


    self.obj48=ButtonConfig(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # Action
    self.obj48.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewBasic (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj48.Drawing_Mode.setValue((' ', 1))
    self.obj48.Drawing_Mode.config = 0

    # Contents
    self.obj48.Contents.Text.setValue('New Basic')
    self.obj48.Contents.Image.setValue('DCharts/Basic.gif')
    self.obj48.Contents.lastSelected= "Image"

    self.obj48.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(41.0,34.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9800000000000009, 0.94999999999999996]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)

    self.obj49=ButtonConfig(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # Action
    self.obj49.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewHistory (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj49.Drawing_Mode.setValue((' ', 1))
    self.obj49.Drawing_Mode.config = 0

    # Contents
    self.obj49.Contents.Text.setValue('New History')
    self.obj49.Contents.Image.setValue('DCharts/History.gif')
    self.obj49.Contents.lastSelected= "Image"

    self.obj49.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(281.0,36.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9800000000000009, 0.94999999999999996]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)

    self.obj50=ButtonConfig(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # Action
    self.obj50.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewComposite (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj50.Drawing_Mode.setValue((' ', 1))
    self.obj50.Drawing_Mode.config = 0

    # Contents
    self.obj50.Contents.Text.setValue('New Composite')
    self.obj50.Contents.Image.setValue('DCharts/Composite.gif')
    self.obj50.Contents.lastSelected= "Image"

    self.obj50.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(40.0,122.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9800000000000009, 0.94999999999999996]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)

    self.obj51=ButtonConfig(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # Action
    self.obj51.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewOrthogonal (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj51.Drawing_Mode.setValue((' ', 1))
    self.obj51.Drawing_Mode.config = 0

    # Contents
    self.obj51.Contents.Text.setValue('New Orthogonal')
    self.obj51.Contents.Image.setValue('DCharts/Orthogonal.gif')
    self.obj51.Contents.lastSelected= "Image"

    self.obj51.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(280.0,120.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9800000000000009, 0.94999999999999996]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)

    self.obj52=ButtonConfig(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # Action
    self.obj52.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewPort (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj52.Drawing_Mode.setValue((' ', 1))
    self.obj52.Drawing_Mode.config = 0

    # Contents
    self.obj52.Contents.Text.setValue('New Port')
    self.obj52.Contents.Image.setValue('DCharts/Port.gif')
    self.obj52.Contents.lastSelected= "Image"

    self.obj52.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(39.0,197.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9800000000000009, 0.94999999999999996]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)

    self.obj53=ButtonConfig(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # Action
    self.obj53.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewServer (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj53.Drawing_Mode.setValue((' ', 1))
    self.obj53.Drawing_Mode.config = 0

    # Contents
    self.obj53.Contents.Text.setValue('New Server')
    self.obj53.Contents.Image.setValue('DCharts/Server.gif')
    self.obj53.Contents.lastSelected= "Image"

    self.obj53.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(280.0,198.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9800000000000009, 0.94999999999999996]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)

    self.obj54=ButtonConfig(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # Action
    self.obj54.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewvisual_settings (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj54.Drawing_Mode.setValue((' ', 1))
    self.obj54.Drawing_Mode.config = 0

    # Contents
    self.obj54.Contents.Text.setValue('New visual_settings')
    self.obj54.Contents.Image.setValue('DCharts/VisualSettings.gif')
    self.obj54.Contents.lastSelected= "Image"

    self.obj54.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(38.0,332.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9800000000000009, 0.94999999999999996]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)

    self.obj55=ButtonConfig(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # Action
    self.obj55.Action.setValue(('Action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nimport SVMAToM3Plugin\nSVMAToM3Plugin.simulate(self)\n'))

    # Drawing_Mode
    self.obj55.Drawing_Mode.setValue((' ', 0))
    self.obj55.Drawing_Mode.config = 0

    # Contents
    self.obj55.Contents.Text.setValue('simulate in SVM')
    self.obj55.Contents.Image.setValue('')
    self.obj55.Contents.Image.setNone()
    self.obj55.Contents.lastSelected= "Text"

    self.obj55.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(38.0,265.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9800000000000009, 0.94999999999999996]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)

    self.obj56=ButtonConfig(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # Action
    #self.obj56.Action.setValue(('Action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nimport SVMAToM3Plugin\nimport sys, os, string, tkFileDialog\n\nsc = SVMAToM3Plugin.generate_description(self, savetofile=None)\ndesc = sc["desc"]\n\nmname=self.statusbar.getState(self.statusbar.MODEL)[1][0]\nif not mname or mname=="Nonamed":\n    mname=tkFileDialog.asksaveasfilename(\n                        filetypes=[("SVM descriptions", "*.des")],\n                        initialdir=self.initialDirectoryDict[ \'OpenSaveModel\' ])\nelse:\n    if( string.split( mname, \'.\' )[1] == \'py\' ): \n        mname=mname[:-2]+"des"\n    mname=os.path.split(mname)[1]\n    mname=tkFileDialog.asksaveasfilename(initialfile=mname, \n                    filetypes=[("SVM descriptions", "*.des")], \n                    initialdir=self.initialDirectoryDict[ \'OpenSaveModel\' ])\n\n# User cancelled\nif( not mname ): return\n\n# Force naming convention\nif( mname[-4:] != \'.des\' ): mname = mname + \'.des\'\n\nif( os.path.exists( mname ) ): os.remove( mname )\n\n# Save .des file\nmf=open(mname, "w")\nmf.write(desc)\nmf.close()\n# Print on success\nprint "SVM description saved to: " + mname\n\n\n\n'))
    self.obj56.Action.setValue(('Action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\nfrom GenerateButtonCode import generate\ngenerate(self)\n\n\n\n'))


    # Drawing_Mode
    self.obj56.Drawing_Mode.setValue((' ', 0))
    self.obj56.Drawing_Mode.config = 0

    # Contents
    self.obj56.Contents.Text.setValue('generate .des')
    self.obj56.Contents.Image.setValue('')
    self.obj56.Contents.Image.setNone()
    self.obj56.Contents.lastSelected= "Text"

    self.obj56.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(280.0,267.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9800000000000009, 0.94999999999999996]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)

    self.obj57=ButtonConfig(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # Action
    self.obj57.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\nimport gen_cpp\ngen_cpp.gen_cpp(self, self.ASGroot.getASGbyName(\'DCharts_META\'))\n'))

    # Drawing_Mode
    self.obj57.Drawing_Mode.setValue((' ', 0))
    self.obj57.Drawing_Mode.config = 0

    # Contents
    self.obj57.Contents.Text.setValue('generate .cpp')
    self.obj57.Contents.Image.setValue('')
    self.obj57.Contents.Image.setNone()
    self.obj57.Contents.lastSelected= "Text"

    self.obj57.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(280.0,340.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.9500000000000008, 0.97999999999999998]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)

    # Connections for obj48 (graphObject_: Obj0) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj49 (graphObject_: Obj1) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj50 (graphObject_: Obj2) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj51 (graphObject_: Obj3) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj52 (graphObject_: Obj4) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj53 (graphObject_: Obj5) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj54 (graphObject_: Obj6) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj55 (graphObject_: Obj7) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj56 (graphObject_: Obj8) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj57 (graphObject_: Obj9) of type ButtonConfig
    self.drawConnections(
 )

newfunction = DCharts_META

loadedMMName = 'Buttons'

atom3version = '0.3'
