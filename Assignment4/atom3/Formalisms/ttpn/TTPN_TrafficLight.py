from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_TTPNModel import *
from ASG_TTPNModel import *
from TTPN_Place import *
from TTPN_Transition import *
from TTPN_Place_Transition_Rel import *
from TTPN_Transition_Place_Rel import *
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

def TTPN_TrafficLight(self, rootNode):
    rootNode.author.setValue('')
    rootNode.description.setValue('')

    self.globalPrecondition( rootNode )

    self.obj26=TTPN_Place(self)

    self.obj26.name.setValue('red')
    self.obj26.tokens.setValue(0)
    self.obj26.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(229.0,165.0,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj26.graphObject_ = new_obj
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)

    self.globalPrecondition( rootNode )

    self.obj27=TTPN_Place(self)

    self.obj27.name.setValue('green')
    self.obj27.tokens.setValue(0)
    self.obj27.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(382.0,165.0,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj27.graphObject_ = new_obj
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)

    self.globalPrecondition( rootNode )

    self.obj28=TTPN_Place(self)

    self.obj28.name.setValue('yellow')
    self.obj28.tokens.setValue(0)
    self.obj28.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(543.0,167.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj28.graphObject_ = new_obj
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)

    self.globalPrecondition( rootNode )

    self.obj29=TTPN_Place(self)

    self.obj29.name.setValue('pedestrian')
    self.obj29.tokens.setValue(0)
    self.obj29.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(96.0,277.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)

    self.globalPrecondition( rootNode )

    self.obj30=TTPN_Place(self)

    self.obj30.name.setValue('policeman')
    self.obj30.tokens.setValue(0)
    self.obj30.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(656.0,-1.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj30.graphObject_ = new_obj
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)

    self.globalPrecondition( rootNode )

    self.obj31=TTPN_Place(self)

    self.obj31.name.setValue('flash')
    self.obj31.tokens.setValue(0)
    self.obj31.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(428.0,41.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj31.graphObject_ = new_obj
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)

    self.globalPrecondition( rootNode )

    self.obj32=TTPN_Transition(self)

    self.obj32.time.setValue(20)
    self.obj32.atomic.setValue((None, 0))
    self.obj32.atomic.config = 0
    self.obj32.name.setValue('chgGreen')
    self.obj32.processes.setValue(1)
    self.obj32.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(288.0,163.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj32.graphObject_ = new_obj
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)

    self.globalPrecondition( rootNode )

    self.obj33=TTPN_Transition(self)

    self.obj33.time.setValue(35)
    self.obj33.atomic.setValue((None, 0))
    self.obj33.atomic.config = 0
    self.obj33.name.setValue('chgYellow')
    self.obj33.processes.setValue(1)
    self.obj33.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(443.0,164.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj33.graphObject_ = new_obj
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)

    self.globalPrecondition( rootNode )

    self.obj34=TTPN_Transition(self)

    self.obj34.time.setValue(5)
    self.obj34.atomic.setValue((None, 0))
    self.obj34.atomic.config = 0
    self.obj34.name.setValue('chgRed')
    self.obj34.processes.setValue(1)
    self.obj34.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(613.0,166.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj34.graphObject_ = new_obj
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)

    self.globalPrecondition( rootNode )

    self.obj35=TTPN_Transition(self)

    self.obj35.time.setValue(120)
    self.obj35.atomic.setValue((None, 0))
    self.obj35.atomic.config = 0
    self.obj35.name.setValue('GenPed')
    self.obj35.processes.setValue(1)
    self.obj35.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(8.0,276.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj35.graphObject_ = new_obj
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)

    self.globalPrecondition( rootNode )

    self.obj36=TTPN_Transition(self)

    self.obj36.time.setValue(0)
    self.obj36.atomic.setValue((None, 0))
    self.obj36.atomic.config = 0
    self.obj36.name.setValue('pedred')
    self.obj36.processes.setValue(1)
    self.obj36.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(129.0,209.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj36.graphObject_ = new_obj
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)

    self.globalPrecondition( rootNode )

    self.obj37=TTPN_Transition(self)

    self.obj37.time.setValue(0)
    self.obj37.atomic.setValue((None, 0))
    self.obj37.atomic.config = 0
    self.obj37.name.setValue('pedgr')
    self.obj37.processes.setValue(1)
    self.obj37.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(245.0,290.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj37.graphObject_ = new_obj
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)

    self.globalPrecondition( rootNode )

    self.obj38=TTPN_Transition(self)

    self.obj38.time.setValue(0)
    self.obj38.atomic.setValue((None, 0))
    self.obj38.atomic.config = 0
    self.obj38.name.setValue('pedyel')
    self.obj38.processes.setValue(1)
    self.obj38.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(438.0,332.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj38.graphObject_ = new_obj
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)

    self.globalPrecondition( rootNode )

    self.obj39=TTPN_Transition(self)

    self.obj39.time.setValue(220)
    self.obj39.atomic.setValue((None, 0))
    self.obj39.atomic.config = 0
    self.obj39.name.setValue('GenPol')
    self.obj39.processes.setValue(1)
    self.obj39.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(710.0,-2.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)

    self.globalPrecondition( rootNode )

    self.obj40=TTPN_Transition(self)

    self.obj40.time.setValue(0)
    self.obj40.atomic.setValue((None, 0))
    self.obj40.atomic.config = 0
    self.obj40.name.setValue('fla2yel')
    self.obj40.processes.setValue(1)
    self.obj40.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(516.0,40.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)

    self.globalPrecondition( rootNode )

    self.obj41=TTPN_Transition(self)

    self.obj41.time.setValue(0)
    self.obj41.atomic.setValue((None, 0))
    self.obj41.atomic.config = 0
    self.obj41.name.setValue('red2fla')
    self.obj41.processes.setValue(1)
    self.obj41.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(106.0,41.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj41.graphObject_ = new_obj
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)

    self.globalPrecondition( rootNode )

    self.obj42=TTPN_Transition(self)

    self.obj42.time.setValue(0)
    self.obj42.atomic.setValue((None, 0))
    self.obj42.atomic.config = 0
    self.obj42.name.setValue('gre2fla')
    self.obj42.processes.setValue(1)
    self.obj42.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(236.0,89.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj42.graphObject_ = new_obj
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)

    self.globalPrecondition( rootNode )

    self.obj43=TTPN_Transition(self)

    self.obj43.time.setValue(0)
    self.obj43.atomic.setValue((None, 0))
    self.obj43.atomic.config = 0
    self.obj43.name.setValue('yel2fla')
    self.obj43.processes.setValue(1)
    self.obj43.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(570.0,91.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj43.graphObject_ = new_obj
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)

    self.globalPrecondition( rootNode )

    self.obj44=TTPN_Place_Transition_Rel(self)

    self.obj44.weight.setValue(1)
    self.obj44.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(278.0,181.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj44.graphObject_ = new_obj
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)

    self.globalPrecondition( rootNode )

    self.obj45=TTPN_Place_Transition_Rel(self)

    self.obj45.weight.setValue(1)
    self.obj45.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(431.0,181.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj45.graphObject_ = new_obj
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)

    self.globalPrecondition( rootNode )

    self.obj46=TTPN_Place_Transition_Rel(self)

    self.obj46.weight.setValue(1)
    self.obj46.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(602.0,182.5,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj46.graphObject_ = new_obj
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)

    self.globalPrecondition( rootNode )

    self.obj47=TTPN_Place_Transition_Rel(self)

    self.obj47.weight.setValue(1)
    self.obj47.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(137.5,243.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj47.graphObject_ = new_obj
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)

    self.globalPrecondition( rootNode )

    self.obj48=TTPN_Place_Transition_Rel(self)

    self.obj48.weight.setValue(1)
    self.obj48.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(196.0,224.5,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj48.graphObject_ = new_obj
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)

    self.globalPrecondition( rootNode )

    self.obj49=TTPN_Place_Transition_Rel(self)

    self.obj49.weight.setValue(1)
    self.obj49.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(145.5,307.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj49.graphObject_ = new_obj
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)

    self.globalPrecondition( rootNode )

    self.obj50=TTPN_Place_Transition_Rel(self)

    self.obj50.weight.setValue(1)
    self.obj50.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(97.0,349.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj50.graphObject_ = new_obj
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)

    self.globalPrecondition( rootNode )

    self.obj51=TTPN_Place_Transition_Rel(self)

    self.obj51.weight.setValue(1)
    self.obj51.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(358.0,264.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj51.graphObject_ = new_obj
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)

    self.globalPrecondition( rootNode )

    self.obj52=TTPN_Place_Transition_Rel(self)

    self.obj52.weight.setValue(1)
    self.obj52.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(543.5,348.5,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj52.graphObject_ = new_obj
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)

    self.globalPrecondition( rootNode )

    self.obj53=TTPN_Place_Transition_Rel(self)

    self.obj53.weight.setValue(1)
    self.obj53.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(489.0,57.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj53.graphObject_ = new_obj
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)

    self.globalPrecondition( rootNode )

    self.obj54=TTPN_Place_Transition_Rel(self)

    self.obj54.weight.setValue(1)
    self.obj54.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(594.5,40.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj54.graphObject_ = new_obj
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)

    self.globalPrecondition( rootNode )

    self.obj55=TTPN_Place_Transition_Rel(self)

    self.obj55.weight.setValue(1)
    self.obj55.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(333.0,121.5,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj55.graphObject_ = new_obj
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)

    self.globalPrecondition( rootNode )

    self.obj56=TTPN_Place_Transition_Rel(self)

    self.obj56.weight.setValue(1)
    self.obj56.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(189.5,155.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj56.graphObject_ = new_obj
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)

    self.globalPrecondition( rootNode )

    self.obj57=TTPN_Place_Transition_Rel(self)

    self.obj57.weight.setValue(1)
    self.obj57.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(579.0,121.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj57.graphObject_ = new_obj
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)

    self.globalPrecondition( rootNode )

    self.obj58=TTPN_Place_Transition_Rel(self)

    self.obj58.weight.setValue(1)
    self.obj58.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(656.5,108.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj58.graphObject_ = new_obj
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)

    self.globalPrecondition( rootNode )

    self.obj59=TTPN_Place_Transition_Rel(self)

    self.obj59.weight.setValue(1)
    self.obj59.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(339.0,14.5,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj59.graphObject_ = new_obj
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)

    self.globalPrecondition( rootNode )

    self.obj60=TTPN_Place_Transition_Rel(self)

    self.obj60.weight.setValue(1)
    self.obj60.graphClass_= graph_TTPN_Place_Transition_Rel
    if self.genGraphics:
       from graph_TTPN_Place_Transition_Rel import *
       new_obj = graph_TTPN_Place_Transition_Rel(261.5,-0.5,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj60.graphObject_ = new_obj
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)

    self.globalPrecondition( rootNode )

    self.obj61=TTPN_Transition_Place_Rel(self)

    self.obj61.weight.setValue(1)
    self.obj61.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(340.0,183.5,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj61.graphObject_ = new_obj
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)

    self.globalPrecondition( rootNode )

    self.obj62=TTPN_Transition_Place_Rel(self)

    self.obj62.weight.setValue(1)
    self.obj62.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(493.0,187.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj62.graphObject_ = new_obj
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)

    self.globalPrecondition( rootNode )

    self.obj63=TTPN_Transition_Place_Rel(self)

    self.obj63.weight.setValue(1)
    self.obj63.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(658.5,236.5,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj63.graphObject_ = new_obj
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)

    self.globalPrecondition( rootNode )

    self.obj64=TTPN_Transition_Place_Rel(self)

    self.obj64.weight.setValue(1)
    self.obj64.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(49.5,297.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj64.graphObject_ = new_obj
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)

    self.globalPrecondition( rootNode )

    self.obj65=TTPN_Transition_Place_Rel(self)

    self.obj65.weight.setValue(1)
    self.obj65.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(152.0,184.5,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj65.graphObject_ = new_obj
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)

    self.globalPrecondition( rootNode )

    self.obj66=TTPN_Transition_Place_Rel(self)

    self.obj66.weight.setValue(1)
    self.obj66.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(388.0,310.5,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj66.graphObject_ = new_obj
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)

    self.globalPrecondition( rootNode )

    self.obj67=TTPN_Transition_Place_Rel(self)

    self.obj67.weight.setValue(1)
    self.obj67.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(542.5,352.5,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj67.graphObject_ = new_obj
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)

    self.globalPrecondition( rootNode )

    self.obj68=TTPN_Transition_Place_Rel(self)

    self.obj68.weight.setValue(1)
    self.obj68.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(706.5,18.5,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj68.graphObject_ = new_obj
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)

    self.globalPrecondition( rootNode )

    self.obj69=TTPN_Transition_Place_Rel(self)

    self.obj69.weight.setValue(1)
    self.obj69.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(540.0,133.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj69.graphObject_ = new_obj
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)

    self.globalPrecondition( rootNode )

    self.obj70=TTPN_Transition_Place_Rel(self)

    self.obj70.weight.setValue(1)
    self.obj70.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(325.0,94.5,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj70.graphObject_ = new_obj
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)

    self.globalPrecondition( rootNode )

    self.obj71=TTPN_Transition_Place_Rel(self)

    self.obj71.weight.setValue(1)
    self.obj71.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(264.5,60.5,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj71.graphObject_ = new_obj
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)

    self.globalPrecondition( rootNode )

    self.obj72=TTPN_Transition_Place_Rel(self)

    self.obj72.weight.setValue(1)
    self.obj72.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(471.5,112.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj72.graphObject_ = new_obj
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.drawConnections((self.obj26,self.obj44,[276.0, 205.0, 304.0, 205.0], 0, 2), (self.obj26,self.obj48,[240.0, 220.0, 222.0, 248.5], 0, 2), (self.obj26,self.obj56,[234.0, 205.0, 215.5, 179.0], 0, 2), (self.obj27,self.obj45,[429.0, 205.0, 457.0, 205.0], 0, 2), (self.obj27,self.obj51,[409.0, 227.0, 384.0, 288.0], 0, 2), (self.obj27,self.obj55,[393.0, 190.0, 359.0, 145.5], 0, 2), (self.obj28,self.obj46,[590.0, 207.0, 628.0, 206.5], 0, 2), (self.obj28,self.obj52,[570.0, 229.0, 569.5, 372.5], 0, 2), (self.obj28,self.obj57,[583.0, 192.0, 605.0, 145.0], 0, 2), (self.obj29,self.obj47,[143.0, 317.0, 163.5, 267.0], 0, 2), (self.obj29,self.obj49,[137.0, 332.0, 171.5, 331.0], 0, 2), (self.obj29,self.obj50,[123.0, 339.0, 123.0, 373.0], 0, 2), (self.obj30,self.obj54,[667.0, 54.0, 620.5, 64.0], 0, 2), (self.obj30,self.obj58,[683.0, 61.0, 682.5, 132.0], 0, 2), (self.obj30,self.obj59,[661.0, 39.0, 365.0, 38.5], 0, 2), (self.obj30,self.obj60,[667.0, 24.0, 287.5, 23.5], 0, 2), (self.obj31,self.obj53,[475.0, 81.0, 515.0, 81.0], 0, 2), (self.obj32,self.obj61,[339.0, 204.0, 367.0, 203.5], 0, 2), (self.obj33,self.obj62,[494.0, 205.0, 520.0, 207.0], 0, 2), (self.obj34,self.obj63,[664.0, 207.0, 686.0, 207.0, 685.5, 256.5], 0, 3), (self.obj35,self.obj64,[59.0, 317.0, 76.5, 317.0], 0, 2), (self.obj36,self.obj65,[180.0, 250.0, 179.0, 204.5], 0, 2), (self.obj37,self.obj66,[296.0, 331.0, 415.0, 330.5], 0, 2), (self.obj38,self.obj67,[489.0, 373.0, 569.5, 372.5], 0, 2), (self.obj39,self.obj68,[761.0, 39.0, 733.5, 38.5], 0, 2), (self.obj40,self.obj69,[567.0, 81.0, 567.0, 153.0], 0, 2), (self.obj41,self.obj71,[157.0, 82.0, 291.5, 80.5], 0, 2), (self.obj42,self.obj70,[287.0, 130.0, 352.0, 114.5], 0, 2), (self.obj43,self.obj72,[621.0, 132.0, 498.5, 132.0], 0, 2), (self.obj44,self.obj32,[304.0, 205.0, 339.0, 204.0], 0, 2), (self.obj45,self.obj33,[457.0, 205.0, 494.0, 205.0], 0, 2), (self.obj46,self.obj34,[628.0, 206.5, 664.0, 207.0], 0, 2), (self.obj47,self.obj36,[163.5, 267.0, 180.0, 250.0], 0, 2), (self.obj48,self.obj36,[222.0, 248.5, 180.0, 250.0], 0, 2), (self.obj49,self.obj37,[171.5, 331.0, 296.0, 331.0], 0, 2), (self.obj50,self.obj38,[123.0, 373.0, 489.0, 373.0], 0, 2), (self.obj51,self.obj37,[384.0, 288.0, 296.0, 331.0], 0, 2), (self.obj52,self.obj38,[569.5, 372.5, 489.0, 373.0], 0, 2), (self.obj53,self.obj40,[515.0, 81.0, 567.0, 81.0], 0, 2), (self.obj54,self.obj40,[620.5, 64.0, 567.0, 81.0], 0, 2), (self.obj55,self.obj42,[359.0, 145.5, 287.0, 130.0], 0, 2), (self.obj56,self.obj41,[215.5, 179.0, 157.0, 82.0], 0, 2), (self.obj57,self.obj43,[605.0, 145.0, 621.0, 132.0], 0, 2), (self.obj58,self.obj43,[682.5, 132.0, 621.0, 132.0], 0, 2), (self.obj59,self.obj42,[365.0, 38.5, 287.0, 130.0], 0, 2), (self.obj60,self.obj41,[287.5, 23.5, 157.0, 82.0], 0, 2), (self.obj61,self.obj27,[367.0, 203.5, 387.0, 205.0], 0, 2), (self.obj62,self.obj28,[520.0, 207.0, 548.0, 207.0], 0, 2), (self.obj63,self.obj26,[685.5, 256.5, 256.0, 257.0, 256.0, 227.0], 0, 3), (self.obj64,self.obj29,[76.5, 317.0, 101.0, 317.0], 0, 2), (self.obj65,self.obj26,[179.0, 204.5, 234.0, 205.0], 0, 2), (self.obj66,self.obj28,[415.0, 330.5, 554.0, 222.0], 0, 2), (self.obj67,self.obj28,[569.5, 372.5, 570.0, 229.0], 0, 2), (self.obj68,self.obj30,[733.5, 38.5, 703.0, 39.0], 0, 2), (self.obj69,self.obj28,[567.0, 153.0, 569.0, 185.0], 0, 2), (self.obj70,self.obj31,[352.0, 114.5, 439.0, 96.0], 0, 2), (self.obj71,self.obj31,[291.5, 80.5, 433.0, 81.0], 0, 2), (self.obj72,self.obj31,[498.5, 132.0, 469.0, 96.0], 0, 2) )

newfunction = TTPN_TrafficLight

loadedMMName = 'TTPNModel'
