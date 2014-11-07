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

def _Example3(self, rootNode):
    rootNode.description.setValue('')
    rootNode.author.setValue('')

    self.globalPrecondition( rootNode )

    self.obj235=TTPN_Place(self)

    self.obj235.tokens.setValue(1)
    self.obj235.name.setValue('P0')
    self.obj235.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(42.0,127.0,self.obj235)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj235.graphObject_ = new_obj
    rootNode.addNode(self.obj235)
    self.globalAndLocalPostcondition(self.obj235, rootNode)

    self.globalPrecondition( rootNode )

    self.obj236=TTPN_Place(self)

    self.obj236.tokens.setValue(2)
    self.obj236.name.setValue('P1')
    self.obj236.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(286.0,49.0,self.obj236)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj236.graphObject_ = new_obj
    rootNode.addNode(self.obj236)
    self.globalAndLocalPostcondition(self.obj236, rootNode)

    self.globalPrecondition( rootNode )

    self.obj237=TTPN_Place(self)

    self.obj237.tokens.setValue(2)
    self.obj237.name.setValue('P2')
    self.obj237.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(287.0,142.0,self.obj237)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj237.graphObject_ = new_obj
    rootNode.addNode(self.obj237)
    self.globalAndLocalPostcondition(self.obj237, rootNode)

    self.globalPrecondition( rootNode )

    self.obj238=TTPN_Place(self)

    self.obj238.tokens.setValue(0)
    self.obj238.name.setValue('P3')
    self.obj238.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(481.0,96.0,self.obj238)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj238.graphObject_ = new_obj
    rootNode.addNode(self.obj238)
    self.globalAndLocalPostcondition(self.obj238, rootNode)

    self.globalPrecondition( rootNode )

    self.obj239=TTPN_Place(self)

    self.obj239.tokens.setValue(1)
    self.obj239.name.setValue('P4')
    self.obj239.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(39.0,34.0,self.obj239)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj239.graphObject_ = new_obj
    rootNode.addNode(self.obj239)
    self.globalAndLocalPostcondition(self.obj239, rootNode)

    self.globalPrecondition( rootNode )

    self.obj240=TTPN_Transition(self)

    self.obj240.processes.setValue(1)
    self.obj240.name.setValue('T0')
    self.obj240.time.setValue(3)
    self.obj240.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(138.0,46.0,self.obj240)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj240.graphObject_ = new_obj
    rootNode.addNode(self.obj240)
    self.globalAndLocalPostcondition(self.obj240, rootNode)

    self.globalPrecondition( rootNode )

    self.obj241=TTPN_Transition(self)

    self.obj241.processes.setValue(1)
    self.obj241.name.setValue('T1')
    self.obj241.time.setValue(7)
    self.obj241.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(139.0,140.0,self.obj241)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj241.graphObject_ = new_obj
    rootNode.addNode(self.obj241)
    self.globalAndLocalPostcondition(self.obj241, rootNode)

    self.globalPrecondition( rootNode )

    self.obj242=TTPN_Transition(self)

    self.obj242.processes.setValue(2)
    self.obj242.name.setValue('T2')
    self.obj242.time.setValue(10)
    self.obj242.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(364.0,96.0,self.obj242)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj242.graphObject_ = new_obj
    rootNode.addNode(self.obj242)
    self.globalAndLocalPostcondition(self.obj242, rootNode)

    self.globalPrecondition( rootNode )

    self.obj243=TTPN_Place_Transition_Rel(self)

    self.obj243.weight.setValue(1)
    self.obj243.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(108.5,155.5,self.obj243)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj243.graphObject_ = new_obj
    rootNode.addNode(self.obj243)
    self.globalAndLocalPostcondition(self.obj243, rootNode)

    self.globalPrecondition( rootNode )

    self.obj244=TTPN_Place_Transition_Rel(self)

    self.obj244.weight.setValue(1)
    self.obj244.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(334.0,94.5,self.obj244)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj244.graphObject_ = new_obj
    rootNode.addNode(self.obj244)
    self.globalAndLocalPostcondition(self.obj244, rootNode)

    self.globalPrecondition( rootNode )

    self.obj245=TTPN_Place_Transition_Rel(self)

    self.obj245.weight.setValue(1)
    self.obj245.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(333.5,143.0,self.obj245)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj245.graphObject_ = new_obj
    rootNode.addNode(self.obj245)
    self.globalAndLocalPostcondition(self.obj245, rootNode)

    self.globalPrecondition( rootNode )

    self.obj246=TTPN_Place_Transition_Rel(self)

    self.obj246.weight.setValue(1)
    self.obj246.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(103.5,57.0,self.obj246)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj246.graphObject_ = new_obj
    rootNode.addNode(self.obj246)
    self.globalAndLocalPostcondition(self.obj246, rootNode)

    self.globalPrecondition( rootNode )

    self.obj247=TTPN_Transition_Place_Rel(self)

    self.obj247.weight.setValue(1)
    self.obj247.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(183.0,64.5,self.obj247)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj247.graphObject_ = new_obj
    rootNode.addNode(self.obj247)
    self.globalAndLocalPostcondition(self.obj247, rootNode)

    self.globalPrecondition( rootNode )

    self.obj248=TTPN_Transition_Place_Rel(self)

    self.obj248.weight.setValue(1)
    self.obj248.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(184.5,87.0,self.obj248)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj248.graphObject_ = new_obj
    rootNode.addNode(self.obj248)
    self.globalAndLocalPostcondition(self.obj248, rootNode)

    self.globalPrecondition( rootNode )

    self.obj249=TTPN_Transition_Place_Rel(self)

    self.obj249.weight.setValue(2)
    self.obj249.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(185.5,145.5,self.obj249)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj249.graphObject_ = new_obj
    rootNode.addNode(self.obj249)
    self.globalAndLocalPostcondition(self.obj249, rootNode)

    self.globalPrecondition( rootNode )

    self.obj250=TTPN_Transition_Place_Rel(self)

    self.obj250.weight.setValue(1)
    self.obj250.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(193.0,168.0,self.obj250)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj250.graphObject_ = new_obj
    rootNode.addNode(self.obj250)
    self.globalAndLocalPostcondition(self.obj250, rootNode)

    self.globalPrecondition( rootNode )

    self.obj251=TTPN_Transition_Place_Rel(self)

    self.obj251.weight.setValue(1)
    self.obj251.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(421.5,122.0,self.obj251)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj251.graphObject_ = new_obj
    rootNode.addNode(self.obj251)
    self.globalAndLocalPostcondition(self.obj251, rootNode)
    self.drawConnections((self.obj235,self.obj243,[83.0, 182.0, 134.5, 179.5], 0, 2), (self.obj236,self.obj244,[327.0, 104.0, 360.0, 118.5], 0, 2), (self.obj237,self.obj245,[334.0, 182.0, 359.5, 167.0], 0, 2), (self.obj239,self.obj246,[86.0, 74.0, 129.5, 81.0], 0, 2), (self.obj240,self.obj247,[188.0, 85.0, 210.0, 84.5], 0, 2), (self.obj240,self.obj248,[188.0, 85.0, 211.5, 107.0], 0, 2), (self.obj241,self.obj249,[189.0, 179.0, 212.5, 165.5], 0, 2), (self.obj241,self.obj250,[189.0, 179.0, 220.0, 188.0], 0, 2), (self.obj242,self.obj251,[414.0, 135.0, 448.5, 142.0], 0, 2), (self.obj243,self.obj241,[134.5, 179.5, 189.0, 179.0], 0, 2), (self.obj244,self.obj242,[360.0, 118.5, 414.0, 135.0], 0, 2), (self.obj245,self.obj242,[359.5, 167.0, 414.0, 135.0], 0, 2), (self.obj246,self.obj240,[129.5, 81.0, 188.0, 85.0], 0, 2), (self.obj247,self.obj236,[210.0, 84.5, 291.0, 89.0], 0, 2), (self.obj248,self.obj237,[211.5, 107.0, 292.0, 182.0], 0, 2), (self.obj249,self.obj236,[212.5, 165.5, 291.0, 89.0], 0, 2), (self.obj250,self.obj237,[220.0, 188.0, 292.0, 182.0], 0, 2), (self.obj251,self.obj238,[448.5, 142.0, 486.0, 136.0], 0, 2) )

newfunction = _Example3

loadedMMName = 'TTPNModel'
