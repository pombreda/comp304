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

def _Example2_multiple_3fases(self, rootNode):
    rootNode.description.setValue('')
    rootNode.author.setValue('')

    self.globalPrecondition( rootNode )

    self.obj76=TTPN_Place(self)

    self.obj76.tokens.setValue(1)
    self.obj76.name.setValue('P0')
    self.obj76.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(42.0,127.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj76.graphObject_ = new_obj
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)

    self.globalPrecondition( rootNode )

    self.obj77=TTPN_Place(self)

    self.obj77.tokens.setValue(1)
    self.obj77.name.setValue('P1')
    self.obj77.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(286.0,49.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj77.graphObject_ = new_obj
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)

    self.globalPrecondition( rootNode )

    self.obj78=TTPN_Place(self)

    self.obj78.tokens.setValue(1)
    self.obj78.name.setValue('P2')
    self.obj78.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(287.0,142.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj78.graphObject_ = new_obj
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)

    self.globalPrecondition( rootNode )

    self.obj79=TTPN_Place(self)

    self.obj79.tokens.setValue(0)
    self.obj79.name.setValue('P3')
    self.obj79.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(481.0,96.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj79.graphObject_ = new_obj
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)

    self.globalPrecondition( rootNode )

    self.obj80=TTPN_Place(self)

    self.obj80.tokens.setValue(1)
    self.obj80.name.setValue('P4')
    self.obj80.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(39.0,34.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj80.graphObject_ = new_obj
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)

    self.globalPrecondition( rootNode )

    self.obj81=TTPN_Transition(self)

    self.obj81.processes.setValue(1)
    self.obj81.atomic.setValue((None, 1))
    self.obj81.atomic.config = 0
    self.obj81.name.setValue('T0')
    self.obj81.time.setValue(3)
    self.obj81.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(138.0,46.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj81.graphObject_ = new_obj
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)

    self.globalPrecondition( rootNode )

    self.obj82=TTPN_Transition(self)

    self.obj82.processes.setValue(1)
    self.obj82.atomic.setValue((None, 1))
    self.obj82.atomic.config = 0
    self.obj82.name.setValue('T1')
    self.obj82.time.setValue(7)
    self.obj82.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(139.0,140.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj82.graphObject_ = new_obj
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)

    self.globalPrecondition( rootNode )

    self.obj83=TTPN_Transition(self)

    self.obj83.processes.setValue(2)
    self.obj83.atomic.setValue((None, 0))
    self.obj83.atomic.config = 0
    self.obj83.name.setValue('T2')
    self.obj83.time.setValue(10)
    self.obj83.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(364.0,96.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj83.graphObject_ = new_obj
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)

    self.globalPrecondition( rootNode )

    self.obj84=TTPN_Place_Transition_Rel(self)

    self.obj84.weight.setValue(1)
    self.obj84.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(108.5,155.5,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj84.graphObject_ = new_obj
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)

    self.globalPrecondition( rootNode )

    self.obj85=TTPN_Place_Transition_Rel(self)

    self.obj85.weight.setValue(1)
    self.obj85.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(334.0,94.5,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj85.graphObject_ = new_obj
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)

    self.globalPrecondition( rootNode )

    self.obj86=TTPN_Place_Transition_Rel(self)

    self.obj86.weight.setValue(1)
    self.obj86.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(333.5,143.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj86.graphObject_ = new_obj
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)

    self.globalPrecondition( rootNode )

    self.obj87=TTPN_Place_Transition_Rel(self)

    self.obj87.weight.setValue(1)
    self.obj87.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(103.5,57.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj87.graphObject_ = new_obj
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)

    self.globalPrecondition( rootNode )

    self.obj88=TTPN_Transition_Place_Rel(self)

    self.obj88.weight.setValue(1)
    self.obj88.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(183.0,64.5,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj88.graphObject_ = new_obj
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)

    self.globalPrecondition( rootNode )

    self.obj89=TTPN_Transition_Place_Rel(self)

    self.obj89.weight.setValue(1)
    self.obj89.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(184.5,87.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj89.graphObject_ = new_obj
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)

    self.globalPrecondition( rootNode )

    self.obj90=TTPN_Transition_Place_Rel(self)

    self.obj90.weight.setValue(2)
    self.obj90.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(185.5,145.5,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj90.graphObject_ = new_obj
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)

    self.globalPrecondition( rootNode )

    self.obj91=TTPN_Transition_Place_Rel(self)

    self.obj91.weight.setValue(1)
    self.obj91.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(193.0,168.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj91.graphObject_ = new_obj
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)

    self.globalPrecondition( rootNode )

    self.obj92=TTPN_Transition_Place_Rel(self)

    self.obj92.weight.setValue(1)
    self.obj92.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(421.5,122.0,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj92.graphObject_ = new_obj
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.drawConnections((self.obj76,self.obj84,[83.0, 182.0, 134.5, 179.5], 0, 2), (self.obj77,self.obj85,[327.0, 104.0, 360.0, 118.5], 0, 2), (self.obj78,self.obj86,[334.0, 182.0, 359.5, 167.0], 0, 2), (self.obj80,self.obj87,[86.0, 74.0, 129.5, 81.0], 0, 2), (self.obj81,self.obj88,[188.0, 85.0, 210.0, 84.5], 0, 2), (self.obj81,self.obj89,[188.0, 85.0, 211.5, 107.0], 0, 2), (self.obj82,self.obj90,[189.0, 179.0, 212.5, 165.5], 0, 2), (self.obj82,self.obj91,[189.0, 179.0, 220.0, 188.0], 0, 2), (self.obj83,self.obj92,[414.0, 135.0, 448.5, 142.0], 0, 2), (self.obj84,self.obj82,[134.5, 179.5, 189.0, 179.0], 0, 2), (self.obj85,self.obj83,[360.0, 118.5, 414.0, 135.0], 0, 2), (self.obj86,self.obj83,[359.5, 167.0, 414.0, 135.0], 0, 2), (self.obj87,self.obj81,[129.5, 81.0, 188.0, 85.0], 0, 2), (self.obj88,self.obj77,[210.0, 84.5, 291.0, 89.0], 0, 2), (self.obj89,self.obj78,[211.5, 107.0, 292.0, 182.0], 0, 2), (self.obj90,self.obj77,[212.5, 165.5, 291.0, 89.0], 0, 2), (self.obj91,self.obj78,[220.0, 188.0, 292.0, 182.0], 0, 2), (self.obj92,self.obj79,[448.5, 142.0, 486.0, 136.0], 0, 2) )

newfunction = _Example2_multiple_3fases

loadedMMName = 'TTPNModel'
