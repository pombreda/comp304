from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_ERmetaMetaModel import *
from ERentity import *
from ERrelationship import *
from ASG_ERmetaMetaModel import *
from ATOM3MSEnum import *
from ATOM3Port import *
from ATOM3Integer import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Link import *
from ATOM3Boolean import *
from ATOM3Connection import *
from ATOM3List import *
from ATOM3Enum import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Text import *

def TTPN_mdl_ER(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('description', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    rootNode.attributes.setValue(lcobj1)
    rootNode.name.setValue('TTPNModel')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.constraints.setValue(lcobj1)
    rootNode.graphClass_= graph_ASG_ERmetaMetaModel

    self.globalPrecondition( rootNode )

    self.obj20=ERentity(self)

    self.obj20.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20.constraints.setValue(lcobj2)
    self.obj20.name.setValue('TTPN_Place')
    self.obj20.appearance.setValue( ('TTPN_Place', self.obj20))
    self.obj20.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('TTPN_Place_Transition_Rel', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('TTPN_Transition_Place_Rel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj20.cardinality.setValue(lcobj2)
    self.obj20.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('P')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('tokens', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    lcobj2.append(cobj2)
    self.obj20.attributes.setValue(lcobj2)
    self.obj20.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(73.0,132.0,self.obj20)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj20.graphObject_ = new_obj
    rootNode.addNode(self.obj20)
    self.globalAndLocalPostcondition(self.obj20, rootNode)

    self.globalPrecondition( rootNode )

    self.obj21=ERentity(self)

    self.obj21.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj21.constraints.setValue(lcobj2)
    self.obj21.name.setValue('TTPN_Transition')
    self.obj21.appearance.setValue( ('TTPN_Transition', self.obj21))
    self.obj21.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('TTPN_Place_Transition_Rel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('TTPN_Transition_Place_Rel', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj21.cardinality.setValue(lcobj2)
    self.obj21.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('T')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('time', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('processes', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(1)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('atomic', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    self.obj21.attributes.setValue(lcobj2)
    self.obj21.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(483.0,135.0,self.obj21)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj21.graphObject_ = new_obj
    rootNode.addNode(self.obj21)
    self.globalAndLocalPostcondition(self.obj21, rootNode)

    self.globalPrecondition( rootNode )

    self.obj22=ERrelationship(self)

    self.obj22.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj22.constraints.setValue(lcobj2)
    self.obj22.name.setValue('TTPN_Place_Transition_Rel')
    self.obj22.appearance.setValue( ('TTPN_Place_Transition_Rel', self.obj22))
    self.obj22.appearance.linkInfo=linkEditor(self,self.obj22.appearance.semObject, "TTPN_Place_Transition_Rel")
    self.obj22.appearance.linkInfo.FirstLink= stickylink()
    self.obj22.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj22.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj22.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj22.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj22.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj22.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj22.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj22.appearance.linkInfo.FirstLink.decoration.setValue( ('TTPN_Place_Transition_Rel_1stLink', self.obj22.appearance.linkInfo.FirstLink))
    self.obj22.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj22.appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj22.appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
    self.obj22.appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj22.appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj22.appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj22.appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj22.appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj22.appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj22.appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj22.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj22.appearance.linkInfo.FirstSegment.decoration.setValue( ('TTPN_Place_Transition_Rel_1stSegment', self.obj22.appearance.linkInfo.FirstSegment))
    self.obj22.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj22.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj22.appearance.linkInfo.Center.setValue( ('TTPN_Place_Transition_Rel_Center', self.obj22.appearance.linkInfo))
    self.obj22.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj22.appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj22.appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
    self.obj22.appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj22.appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj22.appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj22.appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj22.appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj22.appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj22.appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj22.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj22.appearance.linkInfo.SecondSegment.decoration.setValue( ('TTPN_Place_Transition_Rel_2ndSegment', self.obj22.appearance.linkInfo.SecondSegment))
    self.obj22.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj22.appearance.linkInfo.SecondLink= stickylink()
    self.obj22.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj22.appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj22.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj22.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(3)
    self.obj22.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(6)
    self.obj22.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(6)
    self.obj22.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj22.appearance.linkInfo.SecondLink.decoration.setValue( ('TTPN_Place_Transition_Rel_2ndLink', self.obj22.appearance.linkInfo.SecondLink))
    self.obj22.appearance.linkInfo.FirstLink.decoration.semObject=self.obj22.appearance.semObject
    self.obj22.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj22.appearance.semObject
    self.obj22.appearance.linkInfo.Center.semObject=self.obj22.appearance.semObject
    self.obj22.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj22.appearance.semObject
    self.obj22.appearance.linkInfo.SecondLink.decoration.semObject=self.obj22.appearance.semObject
    self.obj22.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('TTPN_Place', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('TTPN_Transition', (('Source', 'Destination'), 0), '1', '1'))
    lcobj2.append(cobj2)
    self.obj22.cardinality.setValue(lcobj2)
    self.obj22.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('weight', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(1)
    lcobj2.append(cobj2)
    self.obj22.attributes.setValue(lcobj2)
    self.obj22.graphClass_= graph_ERrelationship
    if self.genGraphics:
       from graph_ERrelationship import *
       new_obj = graph_ERrelationship(311.0,70.5,self.obj22)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    else: new_obj = None
    self.obj22.graphObject_ = new_obj
    rootNode.addNode(self.obj22)
    self.globalAndLocalPostcondition(self.obj22, rootNode)

    self.globalPrecondition( rootNode )

    self.obj23=ERrelationship(self)

    self.obj23.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj23.constraints.setValue(lcobj2)
    self.obj23.name.setValue('TTPN_Transition_Place_Rel')
    self.obj23.appearance.setValue( ('TTPN_Transition_Place_Rel', self.obj23))
    self.obj23.appearance.linkInfo=linkEditor(self,self.obj23.appearance.semObject, "TTPN_Transition_Place_Rel")
    self.obj23.appearance.linkInfo.FirstLink= stickylink()
    self.obj23.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj23.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj23.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj23.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj23.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj23.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj23.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj23.appearance.linkInfo.FirstLink.decoration.setValue( ('TTPN_Transition_Place_Rel_1stLink', self.obj23.appearance.linkInfo.FirstLink))
    self.obj23.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj23.appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj23.appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
    self.obj23.appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj23.appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj23.appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj23.appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj23.appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj23.appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj23.appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj23.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj23.appearance.linkInfo.FirstSegment.decoration.setValue( ('TTPN_Transition_Place_Rel_1stSegment', self.obj23.appearance.linkInfo.FirstSegment))
    self.obj23.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj23.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj23.appearance.linkInfo.Center.setValue( ('TTPN_Transition_Place_Rel_Center', self.obj23.appearance.linkInfo))
    self.obj23.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj23.appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj23.appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
    self.obj23.appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj23.appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj23.appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj23.appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj23.appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj23.appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj23.appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj23.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj23.appearance.linkInfo.SecondSegment.decoration.setValue( ('TTPN_Transition_Place_Rel_2ndSegment', self.obj23.appearance.linkInfo.SecondSegment))
    self.obj23.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj23.appearance.linkInfo.SecondLink= stickylink()
    self.obj23.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj23.appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj23.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj23.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(3)
    self.obj23.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(6)
    self.obj23.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(6)
    self.obj23.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj23.appearance.linkInfo.SecondLink.decoration.setValue( ('TTPN_Transition_Place_Rel_2ndLink', self.obj23.appearance.linkInfo.SecondLink))
    self.obj23.appearance.linkInfo.FirstLink.decoration.semObject=self.obj23.appearance.semObject
    self.obj23.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj23.appearance.semObject
    self.obj23.appearance.linkInfo.Center.semObject=self.obj23.appearance.semObject
    self.obj23.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj23.appearance.semObject
    self.obj23.appearance.linkInfo.SecondLink.decoration.semObject=self.obj23.appearance.semObject
    self.obj23.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('TTPN_Transition', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('TTPN_Place', (('Source', 'Destination'), 0), '1', '1'))
    lcobj2.append(cobj2)
    self.obj23.cardinality.setValue(lcobj2)
    self.obj23.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('weight', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(1)
    lcobj2.append(cobj2)
    self.obj23.attributes.setValue(lcobj2)
    self.obj23.graphClass_= graph_ERrelationship
    if self.genGraphics:
       from graph_ERrelationship import *
       new_obj = graph_ERrelationship(312.0,201.5,self.obj23)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    else: new_obj = None
    self.obj23.graphObject_ = new_obj
    rootNode.addNode(self.obj23)
    self.globalAndLocalPostcondition(self.obj23, rootNode)
    self.drawConnections((self.obj20,self.obj22,[223.0, 158.0, 314.0, 118.5], 0, 2), (self.obj21,self.obj23,[486.0, 207.0, 405.0, 249.5], 0, 2), (self.obj22,self.obj21,[404.0, 118.5, 486.0, 161.0], 0, 2), (self.obj23,self.obj20,[315.0, 249.5, 223.0, 205.0], 0, 2) )

newfunction = TTPN_mdl_ER

loadedMMName = 'EntityRelationship'
