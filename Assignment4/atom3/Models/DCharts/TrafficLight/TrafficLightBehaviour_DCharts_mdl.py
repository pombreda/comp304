"""
__TrafficLightBehaviour_DCharts_mdl.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: ujean
Modified: Tue Feb 09 17:49:39 2010
___________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Composite import *
from Basic import *
from History import *
from contains import *
from Hyperedge import *
from graph_Basic import *
from graph_contains import *
from graph_Hyperedge import *
from graph_History import *
from graph_Composite import *
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

def TrafficLightBehaviour_DCharts_mdl(self, rootNode, DChartsRootNode=None):

    # --- Generating attributes code for ASG DCharts ---
    if( DChartsRootNode ): 
        # variables
        DChartsRootNode.variables.setValue('\n')
        DChartsRootNode.variables.setHeight(15)

        # misc
        DChartsRootNode.misc.setValue('\n')
        DChartsRootNode.misc.setHeight(15)

        # event_clauses
        DChartsRootNode.event_clauses.setValue('\n')
        DChartsRootNode.event_clauses.setHeight(15)
    # --- ASG attributes over ---


    self.obj40=Composite(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # auto_adjust
    self.obj40.auto_adjust.setValue((None, 1))
    self.obj40.auto_adjust.config = 0

    # name
    self.obj40.name.setValue('ON')

    # is_default
    self.obj40.is_default.setValue((None, 1))
    self.obj40.is_default.config = 0

    # visible
    self.obj40.visible.setValue((None, 1))
    self.obj40.visible.config = 0

    # exit_action
    self.obj40.exit_action.setValue('\n')
    self.obj40.exit_action.setHeight(15)

    # enter_action
    self.obj40.enter_action.setValue('\n')
    self.obj40.enter_action.setHeight(15)

    self.obj40.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(68.0,175.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,94.0,75.0,554.0,649.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,94.0,68.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='ON')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=Composite(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # auto_adjust
    self.obj41.auto_adjust.setValue((None, 1))
    self.obj41.auto_adjust.config = 0

    # name
    self.obj41.name.setValue('NORMAL')

    # is_default
    self.obj41.is_default.setValue((None, 1))
    self.obj41.is_default.config = 0

    # visible
    self.obj41.visible.setValue((None, 1))
    self.obj41.visible.config = 0

    # exit_action
    self.obj41.exit_action.setValue('\n')
    self.obj41.exit_action.setHeight(15)

    # enter_action
    self.obj41.enter_action.setValue('\n')
    self.obj41.enter_action.setHeight(15)

    self.obj41.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(272.0,124.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,158.0,94.0,422.0,451.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,158.0,87.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='NORMAL')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=Composite(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # auto_adjust
    self.obj42.auto_adjust.setValue((None, 1))
    self.obj42.auto_adjust.config = 0

    # name
    self.obj42.name.setValue('FLASHING')

    # is_default
    self.obj42.is_default.setValue((None, 0))
    self.obj42.is_default.config = 0

    # visible
    self.obj42.visible.setValue((None, 1))
    self.obj42.visible.config = 0

    # exit_action
    self.obj42.exit_action.setValue('\n')
    self.obj42.exit_action.setHeight(15)

    # enter_action
    self.obj42.enter_action.setValue('\n')
    self.obj42.enter_action.setHeight(15)

    self.obj42.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(272.0,407.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,172.0,530.0,414.0,642.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,172.0,523.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='FLASHING')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=Composite(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # auto_adjust
    self.obj43.auto_adjust.setValue((None, 1))
    self.obj43.auto_adjust.config = 0

    # name
    self.obj43.name.setValue('RED')

    # is_default
    self.obj43.is_default.setValue((None, 1))
    self.obj43.is_default.config = 0

    # visible
    self.obj43.visible.setValue((None, 1))
    self.obj43.visible.config = 0

    # exit_action
    self.obj43.exit_action.setValue('\n')
    self.obj43.exit_action.setHeight(15)

    # enter_action
    self.obj43.enter_action.setValue('\n')
    self.obj43.enter_action.setHeight(15)

    self.obj43.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(223.0,47.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,177.0,113.0,415.0,190.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,177.0,106.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='RED')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=Basic(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # is_default
    self.obj44.is_default.setValue((None, 0))
    self.obj44.is_default.config = 0

    # name
    self.obj44.name.setValue('GREEN')

    # exit_action
    self.obj44.exit_action.setValue('\n')
    self.obj44.exit_action.setHeight(15)

    # enter_action
    self.obj44.enter_action.setValue('\n')
    self.obj44.enter_action.setHeight(15)

    self.obj44.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(274.0,408.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,286.0,411.0,304.0,429.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,297.0,438.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='GREEN')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=Basic(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # is_default
    self.obj45.is_default.setValue((None, 0))
    self.obj45.is_default.config = 0

    # name
    self.obj45.name.setValue('YELLOW')

    # exit_action
    self.obj45.exit_action.setValue('\n')
    self.obj45.exit_action.setHeight(15)

    # enter_action
    self.obj45.enter_action.setValue('\n')
    self.obj45.enter_action.setHeight(15)

    self.obj45.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(274.0,319.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,286.0,322.0,304.0,340.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,297.0,349.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='YELLOW')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=Basic(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # is_default
    self.obj46.is_default.setValue((None, 1))
    self.obj46.is_default.config = 0

    # name
    self.obj46.name.setValue('RED_WAIT')

    # exit_action
    self.obj46.exit_action.setValue('\n')
    self.obj46.exit_action.setHeight(15)

    # enter_action
    self.obj46.enter_action.setValue('\n')
    self.obj46.enter_action.setHeight(15)

    self.obj46.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(355.0,147.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,367.0,150.0,385.0,168.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,378.0,177.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='RED_WAIT')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=Basic(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # is_default
    self.obj47.is_default.setValue((None, 0))
    self.obj47.is_default.config = 0

    # name
    self.obj47.name.setValue('GREEN_SOON')

    # exit_action
    self.obj47.exit_action.setValue('\n')
    self.obj47.exit_action.setHeight(15)

    # enter_action
    self.obj47.enter_action.setValue('\n')
    self.obj47.enter_action.setHeight(15)

    self.obj47.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(202.0,146.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,214.0,149.0,232.0,167.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,225.0,176.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='GREEN_SOON')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=Basic(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # is_default
    self.obj48.is_default.setValue((None, 1))
    self.obj48.is_default.config = 0

    # name
    self.obj48.name.setValue('YELLOW_ON')

    # exit_action
    self.obj48.exit_action.setValue('\n')
    self.obj48.exit_action.setHeight(15)

    # enter_action
    self.obj48.enter_action.setValue('\n')
    self.obj48.enter_action.setHeight(15)

    self.obj48.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(263.0,533.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,275.0,536.0,293.0,554.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,286.0,563.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='YELLOW_ON')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=Basic(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # is_default
    self.obj49.is_default.setValue((None, 0))
    self.obj49.is_default.config = 0

    # name
    self.obj49.name.setValue('YELLOW_OFF')

    # exit_action
    self.obj49.exit_action.setValue('\n')
    self.obj49.exit_action.setHeight(15)

    # enter_action
    self.obj49.enter_action.setValue('\n')
    self.obj49.enter_action.setHeight(15)

    self.obj49.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(269.0,599.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,281.0,602.0,299.0,620.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,292.0,629.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='YELLOW_OFF')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=Basic(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # is_default
    self.obj50.is_default.setValue((None, 0))
    self.obj50.is_default.config = 0

    # name
    self.obj50.name.setValue('OFF')

    # exit_action
    self.obj50.exit_action.setValue('\n')
    self.obj50.exit_action.setHeight(15)

    # enter_action
    self.obj50.enter_action.setValue('\n')
    self.obj50.enter_action.setHeight(15)

    self.obj50.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(400.0,13.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,412.0,16.0,430.0,34.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,423.0,43.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='OFF')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=Basic(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # is_default
    self.obj51.is_default.setValue((None, 0))
    self.obj51.is_default.config = 0

    # name
    self.obj51.name.setValue('DEAD')

    # exit_action
    self.obj51.exit_action.setValue('\n')
    self.obj51.exit_action.setHeight(15)

    # enter_action
    self.obj51.enter_action.setValue('\n')
    self.obj51.enter_action.setHeight(15)

    self.obj51.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(624.0,349.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,636.0,352.0,654.0,370.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,647.0,379.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='DEAD')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=History(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # is_default
    self.obj52.is_default.setValue((None, 0))
    self.obj52.is_default.config = 0

    # star
    self.obj52.star.setValue((None, 1))
    self.obj52.star.config = 0

    # name
    self.obj52.name.setValue('')
    self.obj52.name.setNone()

    self.obj52.graphClass_= graph_History
    if self.genGraphics:
       new_obj = graph_History(477.0,180.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("History", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf0.handler,480.0,183.0,516.0,218.0)
       self.UMLmodel.itemconfig(new_obj.gf0.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, fill='lightblue')
       self.UMLmodel.coords(new_obj.gf1.handler,497.0,202.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='H')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf2.handler,505.0,202.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, text='*')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf3.handler,500.0,227.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='blue')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, text='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=contains(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    self.obj53.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(217.5,242.5,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=contains(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    self.obj54.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(318.0,250.5,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=contains(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    self.obj55.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(275.0,352.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=contains(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    self.obj56.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(303.0,260.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=contains(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    self.obj57.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(282.0,263.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=contains(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    self.obj58.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(352.0,-327.5,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=contains(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    self.obj59.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(290.0,-327.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=contains(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    self.obj60.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(303.5,248.5,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=contains(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    self.obj61.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(165.0,504.5,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=contains(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    self.obj62.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(167.0,544.5,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=Hyperedge(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # name
    self.obj63.name.setValue('')
    self.obj63.name.setNone()

    # broadcast
    self.obj63.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj63.broadcast.setHeight(15)

    # guard
    self.obj63.guard.setValue('1')

    # trigger
    self.obj63.trigger.setValue('AFTER(6)')

    # action
    self.obj63.action.setValue('\n')
    self.obj63.action.setHeight(15)

    # broadcast_to
    self.obj63.broadcast_to.setValue('')
    self.obj63.broadcast_to.setNone()

    # display
    self.obj63.display.setValue('AFTER(6)')

    self.obj63.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(274.0,158.5,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=Hyperedge(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # name
    self.obj64.name.setValue('')
    self.obj64.name.setNone()

    # broadcast
    self.obj64.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj64.broadcast.setHeight(15)

    # guard
    self.obj64.guard.setValue('1')

    # trigger
    self.obj64.trigger.setValue('CROSSWALK')

    # action
    self.obj64.action.setValue('\n')
    self.obj64.action.setHeight(15)

    # broadcast_to
    self.obj64.broadcast_to.setValue('')
    self.obj64.broadcast_to.setNone()

    # display
    self.obj64.display.setValue('CROSSWALK')

    self.obj64.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(271.0,121.5,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=Hyperedge(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # name
    self.obj65.name.setValue('')
    self.obj65.name.setNone()

    # broadcast
    self.obj65.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj65.broadcast.setHeight(15)

    # guard
    self.obj65.guard.setValue('1')

    # trigger
    self.obj65.trigger.setValue('AFTER(5)')

    # action
    self.obj65.action.setValue('\n')
    self.obj65.action.setHeight(15)

    # broadcast_to
    self.obj65.broadcast_to.setValue('')
    self.obj65.broadcast_to.setNone()

    # display
    self.obj65.display.setValue('AFTER(5)')

    self.obj65.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(296.0,374.5,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=Hyperedge(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # name
    self.obj66.name.setValue('')
    self.obj66.name.setNone()

    # broadcast
    self.obj66.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj66.broadcast.setHeight(15)

    # guard
    self.obj66.guard.setValue('1')

    # trigger
    self.obj66.trigger.setValue('AFTER(2)')

    # action
    self.obj66.action.setValue('\n')
    self.obj66.action.setHeight(15)

    # broadcast_to
    self.obj66.broadcast_to.setValue('')
    self.obj66.broadcast_to.setNone()

    # display
    self.obj66.display.setValue('AFTER(2)')

    self.obj66.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(294.5,259.5,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.6785714285714286, 2.5714285714285716]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj67=Hyperedge(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # name
    self.obj67.name.setValue('')
    self.obj67.name.setNone()

    # broadcast
    self.obj67.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj67.broadcast.setHeight(15)

    # guard
    self.obj67.guard.setValue('1')

    # trigger
    self.obj67.trigger.setValue('AFTER(2)')

    # action
    self.obj67.action.setValue('\n')
    self.obj67.action.setHeight(15)

    # broadcast_to
    self.obj67.broadcast_to.setValue('')
    self.obj67.broadcast_to.setNone()

    # display
    self.obj67.display.setValue('AFTER(2)')

    self.obj67.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(223.0,225.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=Hyperedge(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # name
    self.obj68.name.setValue('')
    self.obj68.name.setNone()

    # broadcast
    self.obj68.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj68.broadcast.setHeight(15)

    # guard
    self.obj68.guard.setValue('1')

    # trigger
    self.obj68.trigger.setValue('AFTER(0.5)')

    # action
    self.obj68.action.setValue('\n')
    self.obj68.action.setHeight(15)

    # broadcast_to
    self.obj68.broadcast_to.setValue('')
    self.obj68.broadcast_to.setNone()

    # display
    self.obj68.display.setValue('AFTER(0.5)')

    self.obj68.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(348.0,584.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=Hyperedge(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # name
    self.obj69.name.setValue('')
    self.obj69.name.setNone()

    # broadcast
    self.obj69.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj69.broadcast.setHeight(15)

    # guard
    self.obj69.guard.setValue('1')

    # trigger
    self.obj69.trigger.setValue('ON-OFF')

    # action
    self.obj69.action.setValue('\n')
    self.obj69.action.setHeight(15)

    # broadcast_to
    self.obj69.broadcast_to.setValue('')
    self.obj69.broadcast_to.setNone()

    # display
    self.obj69.display.setValue('ON-OFF')

    self.obj69.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(497.0,144.5,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=Hyperedge(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # name
    self.obj70.name.setValue('')
    self.obj70.name.setNone()

    # broadcast
    self.obj70.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj70.broadcast.setHeight(15)

    # guard
    self.obj70.guard.setValue('1')

    # trigger
    self.obj70.trigger.setValue('ON-OFF')

    # action
    self.obj70.action.setValue('\n')
    self.obj70.action.setHeight(15)

    # broadcast_to
    self.obj70.broadcast_to.setValue('')
    self.obj70.broadcast_to.setNone()

    # display
    self.obj70.display.setValue('ON-OFF')

    self.obj70.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(325.0,25.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=Hyperedge(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # name
    self.obj71.name.setValue('')
    self.obj71.name.setNone()

    # broadcast
    self.obj71.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj71.broadcast.setHeight(15)

    # guard
    self.obj71.guard.setValue('1')

    # trigger
    self.obj71.trigger.setValue('POLICE')

    # action
    self.obj71.action.setValue('\n')
    self.obj71.action.setHeight(15)

    # broadcast_to
    self.obj71.broadcast_to.setValue('')
    self.obj71.broadcast_to.setNone()

    # display
    self.obj71.display.setValue('POLICE')

    self.obj71.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(466.0,464.5,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=Hyperedge(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # name
    self.obj72.name.setValue('')
    self.obj72.name.setNone()

    # broadcast
    self.obj72.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj72.broadcast.setHeight(15)

    # guard
    self.obj72.guard.setValue('1')

    # trigger
    self.obj72.trigger.setValue('POLICE')

    # action
    self.obj72.action.setValue('\n')
    self.obj72.action.setHeight(15)

    # broadcast_to
    self.obj72.broadcast_to.setValue('')
    self.obj72.broadcast_to.setNone()

    # display
    self.obj72.display.setValue('POLICE')

    self.obj72.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(102.0,466.5,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=Hyperedge(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # name
    self.obj73.name.setValue('')
    self.obj73.name.setNone()

    # broadcast
    self.obj73.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj73.broadcast.setHeight(15)

    # guard
    self.obj73.guard.setValue('1')

    # trigger
    self.obj73.trigger.setValue('QUIT')

    # action
    self.obj73.action.setValue('\n')
    self.obj73.action.setHeight(15)

    # broadcast_to
    self.obj73.broadcast_to.setValue('')
    self.obj73.broadcast_to.setNone()

    # display
    self.obj73.display.setValue('QUIT')

    self.obj73.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(565.5,360.5,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=Hyperedge(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # name
    self.obj74.name.setValue('')
    self.obj74.name.setNone()

    # broadcast
    self.obj74.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj74.broadcast.setHeight(15)

    # guard
    self.obj74.guard.setValue('1')

    # trigger
    self.obj74.trigger.setValue('AFTER(0.5)')

    # action
    self.obj74.action.setValue('\n')
    self.obj74.action.setHeight(15)

    # broadcast_to
    self.obj74.broadcast_to.setValue('')
    self.obj74.broadcast_to.setNone()

    # display
    self.obj74.display.setValue('AFTER(0.5)')

    self.obj74.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(181.0,579.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    # Connections for obj40 (graphObject_: Obj0) named ON
    self.drawConnections(
(self.obj40,self.obj53,[121.0, 201.0, 217.49999999999997, 242.49999999999997], 0, 2),
(self.obj40,self.obj54,[325.0, 75.0, 318.0, 250.49999999999997], 0, 2),
(self.obj40,self.obj55,[195.99999999999997, 267.99999999999994, 275.0, 352.0], 0, 2),
(self.obj40,self.obj70,[325.0, 75.0, 325.0, 25.0], 0, 2),
(self.obj40,self.obj73,[556.0, 361.0, 565.5, 360.5], 0, 2) )
    # Connections for obj41 (graphObject_: Obj1) named NORMAL
    self.drawConnections(
(self.obj41,self.obj56,[290.0, 450.0, 303.0, 260.0], 0, 2),
(self.obj41,self.obj57,[290.0, 450.0, 282.0, 263.5], 0, 2),
(self.obj41,self.obj60,[158.0, 272.0, 303.5, 248.49999999999994], 0, 2),
(self.obj41,self.obj72,[158.0, 272.0, 103.0, 273.0, 102.0, 466.49999999999989], 0, 3) )
    # Connections for obj42 (graphObject_: Obj2) named FLASHING
    self.drawConnections(
(self.obj42,self.obj61,[170.99999999999997, 585.0, 164.99999999999997, 504.5], 0, 2),
(self.obj42,self.obj62,[292.99999999999994, 530.0, 166.99999999999997, 544.5], 0, 2),
(self.obj42,self.obj71,[415.00000000000006, 585.0, 465.99999999999994, 583.99999999999989, 465.99999999999994, 464.50000000000006], 0, 3) )
    # Connections for obj43 (graphObject_: Obj3) named RED
    self.drawConnections(
(self.obj43,self.obj58,[415.00000000000006, 178.0, 352.0, -327.5], 0, 2),
(self.obj43,self.obj59,[176.0, 178.0, 290.0, -327.0], 0, 2) )
    # Connections for obj44 (graphObject_: Obj4) named GREEN
    self.drawConnections(
(self.obj44,self.obj65,[295.0, 411.0, 296.0, 374.5], 0, 2) )
    # Connections for obj45 (graphObject_: Obj5) named YELLOW
    self.drawConnections(
(self.obj45,self.obj66,[295.17749951769309, 322.02456296004203, 294.49999999999994, 259.5], 0, 2) )
    # Connections for obj46 (graphObject_: Obj6) named RED_WAIT
    self.drawConnections(
(self.obj46,self.obj63,[368.0, 159.0, 274.0, 158.49999999999997], 0, 2),
(self.obj46,self.obj64,[376.0, 150.0, 376.0, 121.0, 271.0, 121.5], 0, 3) )
    # Connections for obj47 (graphObject_: Obj7) named GREEN_SOON
    self.drawConnections(
(self.obj47,self.obj67,[223.0, 166.99999999999997, 223.0, 225.0], 0, 2) )
    # Connections for obj48 (graphObject_: Obj8) named YELLOW_ON
    self.drawConnections(
(self.obj48,self.obj74,[276.0, 545.0, 181.00000000000003, 545.0, 181.00000000000003, 578.99999999999989], 0, 3) )
    # Connections for obj49 (graphObject_: Obj9) named YELLOW_OFF
    self.drawConnections(
(self.obj49,self.obj68,[299.0, 611.0, 348.0, 612.0, 348.0, 583.99999999999989], 0, 3) )
    # Connections for obj50 (graphObject_: Obj10) named OFF
    self.drawConnections(
(self.obj50,self.obj69,[429.99999999999994, 25.0, 497.99999999999983, 25.0, 496.99999999999989, 144.5], 0, 3) )
    # Connections for obj51 (graphObject_: Obj11) named DEAD
    self.drawConnections(
 )
    # Connections for obj52 (graphObject_: Obj12) named 
    self.drawConnections(
 )
    # Connections for obj53 (graphObject_: Obj13) of type contains
    self.drawConnections(
(self.obj53,self.obj41,[217.49999999999997, 242.49999999999997, 158.0, 272.0], 0, 2) )
    # Connections for obj54 (graphObject_: Obj14) of type contains
    self.drawConnections(
(self.obj54,self.obj42,[318.0, 250.49999999999997, 253.99999999999997, 538.0], 0, 2) )
    # Connections for obj55 (graphObject_: Obj15) of type contains
    self.drawConnections(
(self.obj55,self.obj52,[275.0, 352.0, 479.99999999999994, 202.0], 0, 2) )
    # Connections for obj56 (graphObject_: Obj16) of type contains
    self.drawConnections(
(self.obj56,self.obj44,[303.0, 260.0, 295.0, 411.0], 0, 2) )
    # Connections for obj57 (graphObject_: Obj17) of type contains
    self.drawConnections(
(self.obj57,self.obj45,[282.0, 263.5, 295.0, 322.0], 0, 2) )
    # Connections for obj58 (graphObject_: Obj18) of type contains
    self.drawConnections(
(self.obj58,self.obj46,[352.0, -327.5, 368.0, 159.0], 0, 2) )
    # Connections for obj59 (graphObject_: Obj19) of type contains
    self.drawConnections(
(self.obj59,self.obj47,[290.0, -327.0, 223.0, 149.0], 0, 2) )
    # Connections for obj60 (graphObject_: Obj20) of type contains
    self.drawConnections(
(self.obj60,self.obj43,[303.5, 248.49999999999994, 295.0, 112.99999999999999], 0, 2) )
    # Connections for obj61 (graphObject_: Obj21) of type contains
    self.drawConnections(
(self.obj61,self.obj48,[164.99999999999997, 504.5, 292.99999999999994, 545.0], 0, 2) )
    # Connections for obj62 (graphObject_: Obj22) of type contains
    self.drawConnections(
(self.obj62,self.obj49,[166.99999999999997, 544.5, 299.0, 611.0], 0, 2) )
    # Connections for obj63 (graphObject_: Obj23) named 
    self.drawConnections(
(self.obj63,self.obj47,[274.0, 158.49999999999997, 232.0, 158.0], 0, 2) )
    # Connections for obj64 (graphObject_: Obj25) named 
    self.drawConnections(
(self.obj64,self.obj47,[271.0, 121.5, 223.0, 122.0, 223.0, 149.0], 0, 3) )
    # Connections for obj65 (graphObject_: Obj27) named 
    self.drawConnections(
(self.obj65,self.obj45,[296.0, 374.5, 295.0, 340.0], 0, 2) )
    # Connections for obj66 (graphObject_: Obj29) named 
    self.drawConnections(
(self.obj66,self.obj43,[294.49999999999994, 259.5, 296.0, 190.0], 0, 2) )
    # Connections for obj67 (graphObject_: Obj31) named 
    self.drawConnections(
(self.obj67,self.obj44,[223.0, 225.0, 222.0, 354.0, 223.0, 420.0, 287.0, 420.0], 0, 4) )
    # Connections for obj68 (graphObject_: Obj33) named 
    self.drawConnections(
(self.obj68,self.obj48,[348.0, 583.99999999999989, 346.99999999999994, 545.0, 292.99999999999994, 545.0], 0, 3) )
    # Connections for obj69 (graphObject_: Obj35) named 
    self.drawConnections(
(self.obj69,self.obj52,[496.99999999999989, 144.5, 497.99999999999983, 183.0], 0, 2) )
    # Connections for obj70 (graphObject_: Obj37) named 
    self.drawConnections(
(self.obj70,self.obj50,[325.0, 25.0, 412.99999999999994, 25.0], 0, 2) )
    # Connections for obj71 (graphObject_: Obj39) named 
    self.drawConnections(
(self.obj71,self.obj41,[465.99999999999994, 464.50000000000006, 465.0, 272.0, 421.99999999999989, 272.0], 0, 3) )
    # Connections for obj72 (graphObject_: Obj41) named 
    self.drawConnections(
(self.obj72,self.obj42,[102.0, 466.49999999999989, 103.0, 581.0, 170.99999999999997, 581.0], 0, 3) )
    # Connections for obj73 (graphObject_: Obj43) named 
    self.drawConnections(
(self.obj73,self.obj51,[565.5, 360.5, 637.0, 361.0], 0, 2) )
    # Connections for obj74 (graphObject_: Obj45) named 
    self.drawConnections(
(self.obj74,self.obj49,[181.00000000000003, 578.99999999999989, 181.00000000000003, 612.0, 282.0, 611.0], 0, 3) )

newfunction = TrafficLightBehaviour_DCharts_mdl

loadedMMName = 'DCharts'

atom3version = '0.3'
