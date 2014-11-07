from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_TTPNModel import *
from ASG_TTPNModel import *
from TTPN_Place import *
from TTPN_Transition import *
from TTPN_Place_Transition_Rel import *
from TTPN_Transition_Place_Rel import *
from ATOM3BottomType import *
from ATOM3String import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Enum import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Link import *
from ATOM3Integer import *
from ATOM3List import *
from ATOM3Port import *

def _Example2_sencillo(self, rootNode):
    rootNode.description.setValue('')
    rootNode.author.setValue('')

    self.globalPrecondition( rootNode )

    self.obj24=TTPN_Place(self)

    self.obj24.tokens.setValue(1)
    self.obj24.name.setValue('P0')
    self.obj24.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(42.0,127.0,self.obj24)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj24.graphObject_ = new_obj
    rootNode.addNode(self.obj24)
    self.globalAndLocalPostcondition(self.obj24, rootNode)

    self.globalPrecondition( rootNode )

    self.obj25=TTPN_Place(self)

    self.obj25.tokens.setValue(1)
    self.obj25.name.setValue('P1')
    self.obj25.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(286.0,49.0,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj25.graphObject_ = new_obj
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)

    self.globalPrecondition( rootNode )

    self.obj26=TTPN_Place(self)

    self.obj26.tokens.setValue(1)
    self.obj26.name.setValue('P2')
    self.obj26.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(287.0,142.0,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj26.graphObject_ = new_obj
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)

    self.globalPrecondition( rootNode )

    self.obj27=TTPN_Place(self)

    self.obj27.tokens.setValue(0)
    self.obj27.name.setValue('P3')
    self.obj27.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(481.0,96.0,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj27.graphObject_ = new_obj
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)

    self.globalPrecondition( rootNode )

    self.obj28=TTPN_Place(self)

    self.obj28.tokens.setValue(1)
    self.obj28.name.setValue('P4')
    self.obj28.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(39.0,34.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj28.graphObject_ = new_obj
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)

    self.globalPrecondition( rootNode )

    self.obj29=TTPN_Transition(self)

    self.obj29.processes.setValue(1)
    self.obj29.name.setValue('T0')
    self.obj29.time.setValue(3)
    self.obj29.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(138.0,46.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)

    self.globalPrecondition( rootNode )

    self.obj30=TTPN_Transition(self)

    self.obj30.processes.setValue(1)
    self.obj30.name.setValue('T1')
    self.obj30.time.setValue(7)
    self.obj30.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(139.0,140.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj30.graphObject_ = new_obj
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)

    self.globalPrecondition( rootNode )

    self.obj31=TTPN_Transition(self)

    self.obj31.processes.setValue(1)
    self.obj31.name.setValue('T2')
    self.obj31.time.setValue(10)
    self.obj31.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(364.0,96.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj31.graphObject_ = new_obj
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)

    self.globalPrecondition( rootNode )

    self.obj32=TTPN_Place_Transition_Rel(self)

    self.obj32.weight.setValue(1)
    self.obj32.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(108.5,155.5,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj32.graphObject_ = new_obj
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)

    self.globalPrecondition( rootNode )

    self.obj33=TTPN_Place_Transition_Rel(self)

    self.obj33.weight.setValue(1)
    self.obj33.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(334.0,94.5,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj33.graphObject_ = new_obj
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)

    self.globalPrecondition( rootNode )

    self.obj34=TTPN_Place_Transition_Rel(self)

    self.obj34.weight.setValue(1)
    self.obj34.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(333.5,143.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj34.graphObject_ = new_obj
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)

    self.globalPrecondition( rootNode )

    self.obj35=TTPN_Place_Transition_Rel(self)

    self.obj35.weight.setValue(1)
    self.obj35.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(103.5,57.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj35.graphObject_ = new_obj
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)

    self.globalPrecondition( rootNode )

    self.obj36=TTPN_Transition_Place_Rel(self)

    self.obj36.weight.setValue(1)
    self.obj36.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(183.0,64.5,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj36.graphObject_ = new_obj
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)

    self.globalPrecondition( rootNode )

    self.obj37=TTPN_Transition_Place_Rel(self)

    self.obj37.weight.setValue(1)
    self.obj37.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(184.5,87.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj37.graphObject_ = new_obj
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)

    self.globalPrecondition( rootNode )

    self.obj38=TTPN_Transition_Place_Rel(self)

    self.obj38.weight.setValue(2)
    self.obj38.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(185.5,145.5,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj38.graphObject_ = new_obj
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)

    self.globalPrecondition( rootNode )

    self.obj39=TTPN_Transition_Place_Rel(self)

    self.obj39.weight.setValue(1)
    self.obj39.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(193.0,168.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)

    self.globalPrecondition( rootNode )

    self.obj40=TTPN_Transition_Place_Rel(self)

    self.obj40.weight.setValue(1)
    self.obj40.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(421.5,122.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.drawConnections((self.obj24,self.obj32,[83.0, 182.0, 134.5, 179.5], 0, 2), (self.obj25,self.obj33,[327.0, 104.0, 360.0, 118.5], 0, 2), (self.obj26,self.obj34,[334.0, 182.0, 359.5, 167.0], 0, 2), (self.obj28,self.obj35,[86.0, 74.0, 129.5, 81.0], 0, 2), (self.obj29,self.obj36,[188.0, 85.0, 210.0, 84.5], 0, 2), (self.obj29,self.obj37,[188.0, 85.0, 211.5, 107.0], 0, 2), (self.obj30,self.obj38,[189.0, 179.0, 212.5, 165.5], 0, 2), (self.obj30,self.obj39,[189.0, 179.0, 220.0, 188.0], 0, 2), (self.obj31,self.obj40,[414.0, 135.0, 448.5, 142.0], 0, 2), (self.obj32,self.obj30,[134.5, 179.5, 189.0, 179.0], 0, 2), (self.obj33,self.obj31,[360.0, 118.5, 414.0, 135.0], 0, 2), (self.obj34,self.obj31,[359.5, 167.0, 414.0, 135.0], 0, 2), (self.obj35,self.obj29,[129.5, 81.0, 188.0, 85.0], 0, 2), (self.obj36,self.obj25,[210.0, 84.5, 291.0, 89.0], 0, 2), (self.obj37,self.obj26,[211.5, 107.0, 292.0, 182.0], 0, 2), (self.obj38,self.obj25,[212.5, 165.5, 291.0, 89.0], 0, 2), (self.obj39,self.obj26,[220.0, 188.0, 292.0, 182.0], 0, 2), (self.obj40,self.obj27,[448.5, 142.0, 486.0, 136.0], 0, 2) )

newfunction = _Example2_sencillo

loadedMMName = 'TTPNModel'
