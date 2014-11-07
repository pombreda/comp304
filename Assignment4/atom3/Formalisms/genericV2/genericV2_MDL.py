"""
__genericV2_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Denis Dube
Modified: Tue Jul 26 10:41:39 2005
_______________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Class3 import *
from Association3 import *
from graph_Association3 import *
from graph_Class3 import *
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

def genericV2_MDL(self, rootNode, ClassDiagramsV3RootNode=None):

    # --- Generating attributes code for ASG ClassDiagramsV3 ---
    if( ClassDiagramsV3RootNode ): 
        # name
        ClassDiagramsV3RootNode.name.setValue('')
        ClassDiagramsV3RootNode.name.setNone()

        # author
        ClassDiagramsV3RootNode.author.setValue('Annonymous')

        # showCardinalities
        ClassDiagramsV3RootNode.showCardinalities.setValue((None, 1))
        ClassDiagramsV3RootNode.showCardinalities.config = 0

        # showAssociationBox
        ClassDiagramsV3RootNode.showAssociationBox.setValue((None, 1))
        ClassDiagramsV3RootNode.showAssociationBox.config = 0

        # showAttributes
        ClassDiagramsV3RootNode.showAttributes.setValue((None, 1))
        ClassDiagramsV3RootNode.showAttributes.config = 0

        # showActions
        ClassDiagramsV3RootNode.showActions.setValue((None, 1))
        ClassDiagramsV3RootNode.showActions.config = 0

        # showConditions
        ClassDiagramsV3RootNode.showConditions.setValue((None, 1))
        ClassDiagramsV3RootNode.showConditions.config = 0

        # attributes
        ClassDiagramsV3RootNode.attributes.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('')
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('Annonymous')
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Text('\n', 60,15 )
        lcobj1.append(cobj1)
        ClassDiagramsV3RootNode.attributes.setValue(lcobj1)

        # constraints
        ClassDiagramsV3RootNode.constraints.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        ClassDiagramsV3RootNode.constraints.setValue(lcobj1)

        # description
        ClassDiagramsV3RootNode.description.setValue('\n')
    # --- ASG attributes over ---


    self.obj24=Class3(self)
    self.obj24.isGraphObjectVisual = True


    # QOCA
    self.obj24.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))

    # name
    self.obj24.name.setValue('genericEntityV2')

    # Abstract
    self.obj24.Abstract.setValue((None, 0))
    self.obj24.Abstract.config = 0

    # Actions
    self.obj24.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj24.Actions.setValue(lcobj2)

    # Graphical_Appearance
    self.obj24.Graphical_Appearance.setValue( ('genericEntityV2', self.obj24))

    # attributes
    self.obj24.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('E')
    lcobj2.append(cobj2)
    self.obj24.attributes.setValue(lcobj2)

    # cardinality
    self.obj24.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('genericLinkV2', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('genericLinkV2', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj24.cardinality.setValue(lcobj2)

    # display
    self.obj24.display.setValue('Attributes:\n  - name :: String\nCardinalities:\n  - To genericLinkV2: 0 to N\n  - From genericLinkV2: 0 to N\n')

    # Constraints
    self.obj24.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj24.Constraints.setValue(lcobj2)

    self.obj24.graphClass_= graph_Class3
    if self.genGraphics:
       new_obj = graph_Class3(120.0,200.0,self.obj24)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.1375, 1.0]
    else: new_obj = None
    self.obj24.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24)
    self.globalAndLocalPostcondition(self.obj24, rootNode)

    self.obj25=Association3(self)
    self.obj25.isGraphObjectVisual = True


    # QOCA
    self.obj25.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))

    # name
    self.obj25.name.setValue('genericLinkV2')

    # displaySelect
    self.obj25.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj25.displaySelect.config = 0

    # Actions
    self.obj25.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj25.Actions.setValue(lcobj2)

    # Graphical_Appearance
    self.obj25.Graphical_Appearance.setValue( ('genericLinkV2', self.obj25))
    self.obj25.Graphical_Appearance.linkInfo=linkEditor(self,self.obj25.Graphical_Appearance.semObject, "genericLinkV2")
    self.obj25.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('genericLinkV2_1stLink', self.obj25.Graphical_Appearance.linkInfo.FirstLink))
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('genericLinkV2_1stSegment', self.obj25.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj25.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj25.Graphical_Appearance.linkInfo.Center.setValue( ('genericLinkV2_Center', self.obj25.Graphical_Appearance.linkInfo))
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('genericLinkV2_2ndSegment', self.obj25.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj25.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('genericLinkV2_2ndLink', self.obj25.Graphical_Appearance.linkInfo.SecondLink))
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj25.Graphical_Appearance.semObject
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj25.Graphical_Appearance.semObject
    self.obj25.Graphical_Appearance.linkInfo.Center.semObject=self.obj25.Graphical_Appearance.semObject
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj25.Graphical_Appearance.semObject
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj25.Graphical_Appearance.semObject

    # attributes
    self.obj25.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('L')
    lcobj2.append(cobj2)
    self.obj25.attributes.setValue(lcobj2)

    # cardinality
    self.obj25.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('genericEntityV2', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('genericEntityV2', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj25.cardinality.setValue(lcobj2)

    # display
    self.obj25.display.setValue('Attributes:\n  - name :: String\nCardinalities:\n  - To genericEntityV2: 0 to N\n  - From genericEntityV2: 0 to N\n')

    # Constraints
    self.obj25.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj25.Constraints.setValue(lcobj2)

    self.obj25.graphClass_= graph_Association3
    if self.genGraphics:
       new_obj = graph_Association3(499.0,271.0,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.5190000000000001, 1.0161290322580647]
    else: new_obj = None
    self.obj25.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)

    # Connections for obj24 (graphObject_: Obj0) of type Class3
    self.drawConnections(
(self.obj24,self.obj25,[332.3125, 321.0, 499.0, 408.0, 499.0, 271.0],"bezier", 3) )
    # Connections for obj25 (graphObject_: Obj1) of type Association3
    self.drawConnections(
(self.obj25,self.obj24,[499.0, 271.0, 499.0, 134.0, 332.3125, 241.0],"bezier", 3) )

newfunction = genericV2_MDL

loadedMMName = 'ClassDiagramsV3_META'

atom3version = '0.3'
