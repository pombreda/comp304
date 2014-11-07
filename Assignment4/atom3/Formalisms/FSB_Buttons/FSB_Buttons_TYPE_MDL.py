"""
__FSB_Buttons_TYPE_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Denis Dube
Modified: Sun Apr 09 21:28:18 2006
______________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from TypeName import *
from LeafType import *
from Operator import *
from graph_TypeName import *
from graph_LeafType import *
from graph_Operator import *
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

def FSB_Buttons_TYPE_MDL(self, rootNode, TypesMetaModelRootNode=None):

    # --- Generating attributes code for ASG TypesMetaModel ---
    if( TypesMetaModelRootNode ): 
        # Comments
        TypesMetaModelRootNode.Comments.setValue('')
        TypesMetaModelRootNode.Comments.setNone()

        # Author
        TypesMetaModelRootNode.Author.setValue('')
        TypesMetaModelRootNode.Author.setNone()
    # --- ASG attributes over ---


    self.obj23=TypeName(self)
    self.obj23.isGraphObjectVisual = True

    if(hasattr(self.obj23, '_setHierarchicalLink')):
      self.obj23._setHierarchicalLink(False)

    # Name
    self.obj23.Name.setValue('FSB_Button_TYPE')

    self.obj23.graphClass_= graph_TypeName
    if self.genGraphics:
       new_obj = graph_TypeName(60.0,80.0,self.obj23)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TypeName", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj23.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj23)
    self.globalAndLocalPostcondition(self.obj23, rootNode)
    self.obj23.postAction( rootNode.CREATE )

    self.obj24=LeafType(self)
    self.obj24.isGraphObjectVisual = True

    if(hasattr(self.obj24, '_setHierarchicalLink')):
      self.obj24._setHierarchicalLink(False)

    # TypeConstraint
    self.obj24.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))

    # Type
    self.obj24.Type.setValue(('iconPath', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj24.Type.initialValue=ATOM3String('', 20)
    self.obj24.Type.isDerivedAttribute = False

    self.obj24.graphClass_= graph_LeafType
    if self.genGraphics:
       new_obj = graph_LeafType(220.0,100.0,self.obj24)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj24.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24)
    self.globalAndLocalPostcondition(self.obj24, rootNode)
    self.obj24.postAction( rootNode.CREATE )

    self.obj25=LeafType(self)
    self.obj25.isGraphObjectVisual = True

    if(hasattr(self.obj25, '_setHierarchicalLink')):
      self.obj25._setHierarchicalLink(False)

    # TypeConstraint
    self.obj25.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))

    # Type
    self.obj25.Type.setValue(('action', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj25.Type.initialValue=ATOM3Text('# Button action code\n# The following is generated for you: \n# def action(self): # self = ATOM3 instance\n# Typical contents of action:\n# newPlace = self.createNew<CLASS NAME IN META-MODEL>(self, wherex, wherey)\n# Action that shows dialog to edit ASG attributes:\n# self.modelAttributes(self.ASGroot.getASGbyName("<META-MODEL NAME>_META")) \n', 80,15 )
    self.obj25.Type.isDerivedAttribute = False

    self.obj25.graphClass_= graph_LeafType
    if self.genGraphics:
       new_obj = graph_LeafType(220.0,180.0,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj25.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)
    self.obj25.postAction( rootNode.CREATE )

    self.obj40=LeafType(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # TypeConstraint
    self.obj40.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))

    # Type
    self.obj40.Type.setValue(('takesActionImmediately', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj40.Type.initialValue=ATOM3Boolean()
    self.obj40.Type.initialValue.setValue(('', 0))
    self.obj40.Type.initialValue.config = 1
    self.obj40.Type.isDerivedAttribute = False

    self.obj40.graphClass_= graph_LeafType
    if self.genGraphics:
       new_obj = graph_LeafType(220.0,240.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj26=Operator(self)
    self.obj26.isGraphObjectVisual = True

    if(hasattr(self.obj26, '_setHierarchicalLink')):
      self.obj26._setHierarchicalLink(False)

    # type
    self.obj26.type.setValue( (['X', 'U', '->'], 0) )
    self.obj26.type.config = 0

    self.obj26.graphClass_= graph_Operator
    if self.genGraphics:
       new_obj = graph_Operator(188.0,107.5,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Operator", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj26.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)
    self.obj26.postAction( rootNode.CREATE )

    # Connections for obj23 (graphObject_: Obj0) of type TypeName
    self.drawConnections(
(self.obj23,self.obj26,[136.0, 96.0, 188.0, 107.5],"bezier", 2) )
    # Connections for obj24 (graphObject_: Obj1) of type LeafType
    self.drawConnections(
 )
    # Connections for obj25 (graphObject_: Obj2) of type LeafType
    self.drawConnections(
 )
    # Connections for obj40 (graphObject_: Obj5) of type LeafType
    self.drawConnections(
 )
    # Connections for obj26 (graphObject_: Obj3) of type Operator
    self.drawConnections(
(self.obj26,self.obj24,[188.0, 107.5, 240.0, 119.0],"bezier", 2),
(self.obj26,self.obj25,[188.0, 107.5, 240.0, 199.0],"bezier", 2),
(self.obj26,self.obj40,[188.0, 107.5, 240.0, 259.0],"bezier", 2) )

newfunction = FSB_Buttons_TYPE_MDL

loadedMMName = 'TypesMetaModel'

atom3version = '0.3'
