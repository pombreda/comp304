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
from ATOM3Text import *
from ATOM3Integer import *
from ATOM3List import *
from ATOM3Port import *
from ATOM3MSEnum import *

def TTPN_convertion_paper(self, rootNode):
    rootNode.description.setValue('')
    rootNode.author.setValue('')

    self.globalPrecondition( rootNode )

    self.obj29=TTPN_Place(self)

    self.obj29.tokens.setValue(0)
    self.obj29.name.setValue('Input')
    self.obj29.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(87.0,104.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)

    self.globalPrecondition( rootNode )

    self.obj30=TTPN_Place(self)

    self.obj30.tokens.setValue(0)
    self.obj30.name.setValue('Conveyor')
    self.obj30.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(439.0,133.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj30.graphObject_ = new_obj
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)

    self.globalPrecondition( rootNode )

    self.obj31=TTPN_Place(self)

    self.obj31.tokens.setValue(0)
    self.obj31.name.setValue('Output')
    self.obj31.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(672.0,229.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj31.graphObject_ = new_obj
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)

    self.globalPrecondition( rootNode )

    self.obj32=TTPN_Place(self)

    self.obj32.tokens.setValue(1)
    self.obj32.name.setValue('M2')
    self.obj32.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(285.0,259.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj32.graphObject_ = new_obj
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)

    self.globalPrecondition( rootNode )

    self.obj33=TTPN_Place(self)

    self.obj33.tokens.setValue(0)
    self.obj33.name.setValue('M2 \' ')
    self.obj33.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(284.0,178.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj33.graphObject_ = new_obj
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)

    self.globalPrecondition( rootNode )

    self.obj34=TTPN_Place(self)

    self.obj34.tokens.setValue(1)
    self.obj34.name.setValue('M1')
    self.obj34.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(278.0,35.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj34.graphObject_ = new_obj
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)

    self.globalPrecondition( rootNode )

    self.obj35=TTPN_Place(self)

    self.obj35.tokens.setValue(0)
    self.obj35.name.setValue('M1 \' ')
    self.obj35.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(279.0,105.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj35.graphObject_ = new_obj
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)

    self.globalPrecondition( rootNode )

    self.obj36=TTPN_Place(self)

    self.obj36.tokens.setValue(1)
    self.obj36.name.setValue('M3')
    self.obj36.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(620.0,86.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj36.graphObject_ = new_obj
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)

    self.globalPrecondition( rootNode )

    self.obj37=TTPN_Place(self)

    self.obj37.tokens.setValue(0)
    self.obj37.name.setValue('M3 \' ')
    self.obj37.graphClass_= graph_TTPN_Place
    if self.genGraphics:
       from graph_TTPN_Place import *
       new_obj = graph_TTPN_Place(624.0,152.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place", new_obj.tag)
    else: new_obj = None
    self.obj37.graphObject_ = new_obj
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)

    self.globalPrecondition( rootNode )

    self.obj38=TTPN_Transition(self)

    self.obj38.processes.setValue(1)
    self.obj38.atomic.setValue((None, 0))
    self.obj38.atomic.config = 0
    self.obj38.name.setValue('Generator0')
    self.obj38.time.setValue(4)
    self.obj38.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(56.0,33.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj38.graphObject_ = new_obj
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)

    self.globalPrecondition( rootNode )

    self.obj39=TTPN_Transition(self)

    self.obj39.processes.setValue(1)
    self.obj39.atomic.setValue((None, 0))
    self.obj39.atomic.config = 0
    self.obj39.name.setValue('Input2M1')
    self.obj39.time.setValue(0)
    self.obj39.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(139.0,58.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)

    self.globalPrecondition( rootNode )

    self.obj40=TTPN_Transition(self)

    self.obj40.processes.setValue(1)
    self.obj40.atomic.setValue((None, 0))
    self.obj40.atomic.config = 0
    self.obj40.name.setValue('Input2M2')
    self.obj40.time.setValue(0)
    self.obj40.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(150.0,208.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)

    self.globalPrecondition( rootNode )

    self.obj41=TTPN_Transition(self)

    self.obj41.processes.setValue(1)
    self.obj41.atomic.setValue((None, 0))
    self.obj41.atomic.config = 0
    self.obj41.name.setValue('Conveyor2M3')
    self.obj41.time.setValue(0)
    self.obj41.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(528.0,134.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj41.graphObject_ = new_obj
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)

    self.globalPrecondition( rootNode )

    self.obj42=TTPN_Transition(self)

    self.obj42.processes.setValue(1)
    self.obj42.atomic.setValue((None, 0))
    self.obj42.atomic.config = 0
    self.obj42.name.setValue('M22Conveyor')
    self.obj42.time.setValue(7)
    self.obj42.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(364.0,234.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj42.graphObject_ = new_obj
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)

    self.globalPrecondition( rootNode )

    self.obj43=TTPN_Transition(self)

    self.obj43.processes.setValue(1)
    self.obj43.atomic.setValue((None, 0))
    self.obj43.atomic.config = 0
    self.obj43.name.setValue('M12Conveyor')
    self.obj43.time.setValue(10)
    self.obj43.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(354.0,52.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
    else: new_obj = None
    self.obj43.graphObject_ = new_obj
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)

    self.globalPrecondition( rootNode )

    self.obj44=TTPN_Transition(self)

    self.obj44.processes.setValue(1)
    self.obj44.atomic.setValue((None, 0))
    self.obj44.atomic.config = 0
    self.obj44.name.setValue('M32Output')
    self.obj44.time.setValue(7)
    self.obj44.graphClass_= graph_TTPN_Transition
    if self.genGraphics:
       from graph_TTPN_Transition import *
       new_obj = graph_TTPN_Transition(692.0,117.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition", new_obj.tag)
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
       new_obj = graph_TTPN_Place_Transition_Rel(120.5,76.5,self.obj45)
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
       new_obj = graph_TTPN_Place_Transition_Rel(215.5,124.5,self.obj46)
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
       new_obj = graph_TTPN_Place_Transition_Rel(125.5,226.5,self.obj47)
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
       new_obj = graph_TTPN_Place_Transition_Rel(243.5,197.5,self.obj48)
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
       new_obj = graph_TTPN_Place_Transition_Rel(514.5,152.5,self.obj49)
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
       new_obj = graph_TTPN_Place_Transition_Rel(582.5,164.5,self.obj50)
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
       new_obj = graph_TTPN_Place_Transition_Rel(366.0,278.5,self.obj51)
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
       new_obj = graph_TTPN_Place_Transition_Rel(323.0,54.5,self.obj52)
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
       new_obj = graph_TTPN_Place_Transition_Rel(657.0,112.5,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Place_Transition_Rel", new_obj.tag)
    else: new_obj = None
    self.obj53.graphObject_ = new_obj
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)

    self.globalPrecondition( rootNode )

    self.obj54=TTPN_Transition_Place_Rel(self)

    self.obj54.weight.setValue(1)
    self.obj54.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(52.0,91.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj54.graphObject_ = new_obj
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)

    self.globalPrecondition( rootNode )

    self.obj55=TTPN_Transition_Place_Rel(self)

    self.obj55.weight.setValue(1)
    self.obj55.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(209.5,55.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj55.graphObject_ = new_obj
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)

    self.globalPrecondition( rootNode )

    self.obj56=TTPN_Transition_Place_Rel(self)

    self.obj56.weight.setValue(1)
    self.obj56.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(239.5,279.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj56.graphObject_ = new_obj
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)

    self.globalPrecondition( rootNode )

    self.obj57=TTPN_Transition_Place_Rel(self)

    self.obj57.weight.setValue(1)
    self.obj57.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(579.5,125.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj57.graphObject_ = new_obj
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)

    self.globalPrecondition( rootNode )

    self.obj58=TTPN_Transition_Place_Rel(self)

    self.obj58.weight.setValue(1)
    self.obj58.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(357.0,197.5,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj58.graphObject_ = new_obj
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)

    self.globalPrecondition( rootNode )

    self.obj59=TTPN_Transition_Place_Rel(self)

    self.obj59.weight.setValue(1)
    self.obj59.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(407.0,217.5,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj59.graphObject_ = new_obj
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)

    self.globalPrecondition( rootNode )

    self.obj60=TTPN_Transition_Place_Rel(self)

    self.obj60.weight.setValue(1)
    self.obj60.graphClass_= graph_TTPN_Transition_Place_Rel
    if self.genGraphics:
       from graph_TTPN_Transition_Place_Rel import *
       new_obj = graph_TTPN_Transition_Place_Rel(347.0,124.5,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
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
       new_obj = graph_TTPN_Transition_Place_Rel(387.0,82.5,self.obj61)
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
       new_obj = graph_TTPN_Transition_Place_Rel(659.0,165.5,self.obj62)
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
       new_obj = graph_TTPN_Transition_Place_Rel(716.0,181.5,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TTPN_Transition_Place_Rel", new_obj.tag)
    else: new_obj = None
    self.obj63.graphObject_ = new_obj
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.drawConnections((self.obj29,self.obj45,[127.0, 128.0, 146.5, 95.5], 0, 2), (self.obj29,self.obj47,[128.0, 158.0, 151.5, 245.5], 0, 2), (self.obj30,self.obj49,[486.0, 172.0, 540.5, 171.5], 0, 2), (self.obj32,self.obj51,[332.0, 298.0, 392.0, 297.5], 0, 2), (self.obj33,self.obj48,[289.0, 217.0, 269.5, 216.5], 0, 2), (self.obj34,self.obj52,[325.0, 74.0, 349.0, 73.5], 0, 2), (self.obj35,self.obj46,[284.0, 144.0, 241.5, 143.5], 0, 2), (self.obj36,self.obj53,[667.0, 125.0, 683.0, 131.5], 0, 2), (self.obj37,self.obj50,[629.0, 191.0, 608.5, 183.5], 0, 2), (self.obj38,self.obj54,[107.0, 71.0, 79.0, 110.0], 0, 2), (self.obj39,self.obj55,[190.0, 96.0, 236.5, 74.0], 0, 2), (self.obj40,self.obj56,[201.0, 246.0, 266.5, 298.0], 0, 2), (self.obj41,self.obj57,[579.0, 172.0, 606.5, 144.0], 0, 2), (self.obj42,self.obj58,[415.0, 272.0, 384.0, 216.5], 0, 2), (self.obj42,self.obj59,[415.0, 272.0, 434.0, 236.5], 0, 2), (self.obj43,self.obj60,[405.0, 90.0, 374.0, 143.5], 0, 2), (self.obj43,self.obj61,[405.0, 90.0, 414.0, 101.5], 0, 2), (self.obj44,self.obj62,[743.0, 155.0, 686.0, 184.5], 0, 2), (self.obj44,self.obj63,[743.0, 155.0, 743.0, 200.5], 0, 2), (self.obj45,self.obj39,[146.5, 95.5, 190.0, 96.0], 0, 2), (self.obj46,self.obj39,[241.5, 143.5, 190.0, 96.0], 0, 2), (self.obj47,self.obj40,[151.5, 245.5, 201.0, 246.0], 0, 2), (self.obj48,self.obj40,[269.5, 216.5, 201.0, 246.0], 0, 2), (self.obj49,self.obj41,[540.5, 171.5, 579.0, 172.0], 0, 2), (self.obj50,self.obj41,[608.5, 183.5, 579.0, 172.0], 0, 2), (self.obj51,self.obj42,[392.0, 297.5, 415.0, 272.0], 0, 2), (self.obj52,self.obj43,[349.0, 73.5, 405.0, 90.0], 0, 2), (self.obj53,self.obj44,[683.0, 131.5, 743.0, 155.0], 0, 2), (self.obj54,self.obj29,[79.0, 110.0, 98.0, 128.0], 0, 2), (self.obj55,self.obj34,[236.5, 74.0, 283.0, 74.0], 0, 2), (self.obj56,self.obj32,[266.5, 298.0, 290.0, 298.0], 0, 2), (self.obj57,self.obj36,[606.5, 144.0, 625.0, 125.0], 0, 2), (self.obj58,self.obj33,[384.0, 216.5, 331.0, 217.0], 0, 2), (self.obj59,self.obj30,[434.0, 236.5, 450.0, 187.0], 0, 2), (self.obj60,self.obj35,[374.0, 143.5, 326.0, 144.0], 0, 2), (self.obj61,self.obj30,[414.0, 101.5, 444.0, 172.0], 0, 2), (self.obj62,self.obj37,[686.0, 184.5, 671.0, 191.0], 0, 2), (self.obj63,self.obj31,[743.0, 200.5, 698.0, 247.0], 0, 2) )

newfunction = TTPN_convertion_paper

loadedMMName = 'TTPNModel'
