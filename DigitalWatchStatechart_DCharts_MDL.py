"""
__DigitalWatchStatechart_DCharts_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: cshank1
Modified: Tue Mar 16 16:08:53 2010
____________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Composite import *
from Basic import *
from History import *
from Orthogonal import *
from contains import *
from Hyperedge import *
from graph_Basic import *
from graph_Orthogonal import *
from graph_Hyperedge import *
from graph_contains import *
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

def DigitalWatchStatechart_DCharts_MDL(self, rootNode, DChartsRootNode=None):

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


    self.obj70=Composite(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # auto_adjust
    self.obj70.auto_adjust.setValue((None, 1))
    self.obj70.auto_adjust.config = 0

    # name
    self.obj70.name.setValue('Chrono_On')

    # is_default
    self.obj70.is_default.setValue((None, 0))
    self.obj70.is_default.config = 0

    # visible
    self.obj70.visible.setValue((None, 1))
    self.obj70.visible.config = 0

    # exit_action
    self.obj70.exit_action.setValue('\n')
    self.obj70.exit_action.setHeight(15)

    # enter_action
    self.obj70.enter_action.setValue('\n')
    self.obj70.enter_action.setHeight(15)

    self.obj70.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(380.0,780.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,448.0,440.0,702.0,625.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='darkblue')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,448.0,433.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Chrono_On')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [0.20000000000000001, 3.2599999999999203]
       new_obj.layConstraints['Label Offset'] = [30.0, 15.0]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj731=Composite(self)
    self.obj731.isGraphObjectVisual = True

    if(hasattr(self.obj731, '_setHierarchicalLink')):
      self.obj731._setHierarchicalLink(False)

    # auto_adjust
    self.obj731.auto_adjust.setValue((None, 1))
    self.obj731.auto_adjust.config = 0

    # name
    self.obj731.name.setValue('Running')

    # is_default
    self.obj731.is_default.setValue((None, 1))
    self.obj731.is_default.config = 0

    # visible
    self.obj731.visible.setValue((None, 1))
    self.obj731.visible.config = 0

    # exit_action
    self.obj731.exit_action.setValue('\n')
    self.obj731.exit_action.setHeight(15)

    # enter_action
    self.obj731.enter_action.setValue('\n')
    self.obj731.enter_action.setHeight(15)

    self.obj731.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(680.0,200.0,self.obj731)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,97.0,38.0,766.0,359.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='darkgreen')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,97.0,31.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Running')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj731.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj731)
    self.globalAndLocalPostcondition(self.obj731, rootNode)
    self.obj731.postAction( rootNode.CREATE )

    self.obj742=Composite(self)
    self.obj742.isGraphObjectVisual = True

    if(hasattr(self.obj742, '_setHierarchicalLink')):
      self.obj742._setHierarchicalLink(False)

    # auto_adjust
    self.obj742.auto_adjust.setValue((None, 1))
    self.obj742.auto_adjust.config = 0

    # name
    self.obj742.name.setValue('Alarming')

    # is_default
    self.obj742.is_default.setValue((None, 0))
    self.obj742.is_default.config = 0

    # visible
    self.obj742.visible.setValue((None, 1))
    self.obj742.visible.config = 0

    # exit_action
    self.obj742.exit_action.setValue('\n')
    self.obj742.exit_action.setHeight(15)

    # enter_action
    self.obj742.enter_action.setValue('\n')
    self.obj742.enter_action.setHeight(15)

    self.obj742.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(840.0,240.0,self.obj742)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,863.0,241.0,1079.0,364.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='darkblue')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,863.0,234.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarming')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [0.87999999999999989, 1.0]
    else: new_obj = None
    self.obj742.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj742)
    self.globalAndLocalPostcondition(self.obj742, rootNode)
    self.obj742.postAction( rootNode.CREATE )

    self.obj1419=Composite(self)
    self.obj1419.isGraphObjectVisual = True

    if(hasattr(self.obj1419, '_setHierarchicalLink')):
      self.obj1419._setHierarchicalLink(False)

    # auto_adjust
    self.obj1419.auto_adjust.setValue((None, 1))
    self.obj1419.auto_adjust.config = 0

    # name
    self.obj1419.name.setValue('Edit Mode')

    # is_default
    self.obj1419.is_default.setValue((None, 0))
    self.obj1419.is_default.config = 0

    # visible
    self.obj1419.visible.setValue((None, 1))
    self.obj1419.visible.config = 0

    # exit_action
    self.obj1419.exit_action.setValue('\n')
    self.obj1419.exit_action.setHeight(15)

    # enter_action
    self.obj1419.enter_action.setValue('\n')
    self.obj1419.enter_action.setHeight(15)

    self.obj1419.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(40.0,240.0,self.obj1419)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,163.0,277.0,300.0,337.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='darkblue')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,163.0,270.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Edit Mode')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1419.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1419)
    self.globalAndLocalPostcondition(self.obj1419, rootNode)
    self.obj1419.postAction( rootNode.CREATE )

    self.obj29=Basic(self)
    self.obj29.isGraphObjectVisual = True

    if(hasattr(self.obj29, '_setHierarchicalLink')):
      self.obj29._setHierarchicalLink(False)

    # is_default
    self.obj29.is_default.setValue((None, 1))
    self.obj29.is_default.config = 0

    # name
    self.obj29.name.setValue('Setup')

    # exit_action
    self.obj29.exit_action.setValue('\n')
    self.obj29.exit_action.setHeight(15)

    # enter_action
    self.obj29.enter_action.setValue('\n')
    self.obj29.enter_action.setHeight(15)

    self.obj29.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(20.0,40.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,32.0,43.0,50.0,61.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,43.125,70.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Setup')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font-158692372')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj29.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.obj29.postAction( rootNode.CREATE )

    self.obj30=Basic(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    # is_default
    self.obj30.is_default.setValue((None, 0))
    self.obj30.is_default.config = 0

    # name
    self.obj30.name.setValue('Stopped')

    # exit_action
    self.obj30.exit_action.setValue('\n')
    self.obj30.exit_action.setHeight(15)

    # enter_action
    self.obj30.enter_action.setValue('\n')
    self.obj30.enter_action.setHeight(15)

    self.obj30.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(1040.0,40.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,1052.0,43.0,1070.0,61.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,1063.125,70.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Stopped')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font-159188692')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj30.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)
    self.obj30.postAction( rootNode.CREATE )

    self.obj31=Basic(self)
    self.obj31.isGraphObjectVisual = True

    if(hasattr(self.obj31, '_setHierarchicalLink')):
      self.obj31._setHierarchicalLink(False)

    # is_default
    self.obj31.is_default.setValue((None, 0))
    self.obj31.is_default.config = 0

    # name
    self.obj31.name.setValue('Indiglo_Off')

    # exit_action
    self.obj31.exit_action.setValue('\n')
    self.obj31.exit_action.setHeight(15)

    # enter_action
    self.obj31.enter_action.setValue('\n')
    self.obj31.enter_action.setHeight(15)

    self.obj31.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(150.0,468.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,162.0,471.0,180.0,489.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,109.125,501.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Indiglo_Off')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font169908684')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-64.0, 3.0]
    else: new_obj = None
    self.obj31.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)
    self.obj31.postAction( rootNode.CREATE )

    self.obj32=Basic(self)
    self.obj32.isGraphObjectVisual = True

    if(hasattr(self.obj32, '_setHierarchicalLink')):
      self.obj32._setHierarchicalLink(False)

    # is_default
    self.obj32.is_default.setValue((None, 0))
    self.obj32.is_default.config = 0

    # name
    self.obj32.name.setValue('Waiting')

    # exit_action
    self.obj32.exit_action.setValue('\n')
    self.obj32.exit_action.setHeight(15)

    # enter_action
    self.obj32.enter_action.setValue('\n')
    self.obj32.enter_action.setHeight(15)

    self.obj32.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(270.0,528.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,282.0,531.0,300.0,549.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,293.125,558.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Waiting')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font170086540')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj32.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)
    self.obj32.postAction( rootNode.CREATE )

    self.obj33=Basic(self)
    self.obj33.isGraphObjectVisual = True

    if(hasattr(self.obj33, '_setHierarchicalLink')):
      self.obj33._setHierarchicalLink(False)

    # is_default
    self.obj33.is_default.setValue((None, 0))
    self.obj33.is_default.config = 0

    # name
    self.obj33.name.setValue('Pressed')

    # exit_action
    self.obj33.exit_action.setValue('\n')
    self.obj33.exit_action.setHeight(15)

    # enter_action
    self.obj33.enter_action.setValue('\n')
    self.obj33.enter_action.setHeight(15)

    self.obj33.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(254.0,456.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,266.0,459.0,284.0,477.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,322.125,453.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Pressed')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font170089516')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [45.0, -33.0]
    else: new_obj = None
    self.obj33.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)
    self.obj33.postAction( rootNode.CREATE )

    self.obj34=Basic(self)
    self.obj34.isGraphObjectVisual = True

    if(hasattr(self.obj34, '_setHierarchicalLink')):
      self.obj34._setHierarchicalLink(False)

    # is_default
    self.obj34.is_default.setValue((None, 0))
    self.obj34.is_default.config = 0

    # name
    self.obj34.name.setValue('Update')

    # exit_action
    self.obj34.exit_action.setValue('\n')
    self.obj34.exit_action.setHeight(15)

    # enter_action
    self.obj34.enter_action.setValue('\n')
    self.obj34.enter_action.setHeight(15)

    self.obj34.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(160.0,640.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,172.0,643.0,190.0,661.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,226.125,653.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Update')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font176724012')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [43.0, -17.0]
    else: new_obj = None
    self.obj34.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)
    self.obj34.postAction( rootNode.CREATE )

    self.obj35=Basic(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    # is_default
    self.obj35.is_default.setValue((None, 0))
    self.obj35.is_default.config = 0

    # name
    self.obj35.name.setValue('Wait')

    # exit_action
    self.obj35.exit_action.setValue('\n')
    self.obj35.exit_action.setHeight(15)

    # enter_action
    self.obj35.enter_action.setValue('\n')
    self.obj35.enter_action.setHeight(15)

    self.obj35.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(54.0,724.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,66.0,727.0,84.0,745.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,77.125,754.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Wait')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font177887500')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj36=Basic(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    # is_default
    self.obj36.is_default.setValue((None, 0))
    self.obj36.is_default.config = 0

    # name
    self.obj36.name.setValue('Reset')

    # exit_action
    self.obj36.exit_action.setValue('\n')
    self.obj36.exit_action.setHeight(15)

    # enter_action
    self.obj36.enter_action.setValue('\n')
    self.obj36.enter_action.setHeight(15)

    self.obj36.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(960.0,460.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,986.116845723,470.233875745,989.716845723,473.833875745)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,1006.74184572,457.033875745)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Reset')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font171321996')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
       new_obj.layConstraints['Label Offset'] = [8.0, -49.0]
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj37=Basic(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # is_default
    self.obj37.is_default.setValue((None, 0))
    self.obj37.is_default.config = 0

    # name
    self.obj37.name.setValue('Running')

    # exit_action
    self.obj37.exit_action.setValue('\n')
    self.obj37.exit_action.setHeight(15)

    # enter_action
    self.obj37.enter_action.setValue('\n')
    self.obj37.enter_action.setHeight(15)

    self.obj37.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(537.448484379,487.679837711,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,561.868926855,493.849534681,565.468926855,497.449534681)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,529.493926855,512.649534681)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Running')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font184585676')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
       new_obj.layConstraints['Label Offset'] = [3.0, -1.0]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj38=Basic(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    # is_default
    self.obj38.is_default.setValue((None, 0))
    self.obj38.is_default.config = 0

    # name
    self.obj38.name.setValue('Paused')

    # exit_action
    self.obj38.exit_action.setValue('\n')
    self.obj38.exit_action.setHeight(15)

    # enter_action
    self.obj38.enter_action.setValue('\n')
    self.obj38.enter_action.setHeight(15)

    self.obj38.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(651.234160821,601.954103875,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,672.877093682,608.445625787,676.477093682,612.045625787)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,623.702093682,612.445625787)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Paused')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font183405612')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
       new_obj.layConstraints['Label Offset'] = [-21.0, -15.0]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj39=Basic(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # is_default
    self.obj39.is_default.setValue((None, 0))
    self.obj39.is_default.config = 0

    # name
    self.obj39.name.setValue('Alarm_Off')

    # exit_action
    self.obj39.exit_action.setValue('\n')
    self.obj39.exit_action.setHeight(15)

    # enter_action
    self.obj39.enter_action.setValue('\n')
    self.obj39.enter_action.setHeight(15)

    self.obj39.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(560.0,680.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,572.0,683.0,590.0,701.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,582.125,670.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarm_Off')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font190584076')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.11
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-1.0, -40.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=Basic(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # is_default
    self.obj40.is_default.setValue((None, 0))
    self.obj40.is_default.config = 0

    # name
    self.obj40.name.setValue('Alarming')

    # exit_action
    self.obj40.exit_action.setValue('\n')
    self.obj40.exit_action.setHeight(15)

    # enter_action
    self.obj40.enter_action.setValue('\n')
    self.obj40.enter_action.setHeight(15)

    self.obj40.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(920.0,860.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,932.0,863.0,950.0,881.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,962.125,896.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarming')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font189650604')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [19.0, 6.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=Basic(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # is_default
    self.obj41.is_default.setValue((None, 0))
    self.obj41.is_default.config = 0

    # name
    self.obj41.name.setValue('Set')

    # exit_action
    self.obj41.exit_action.setValue('\n')
    self.obj41.exit_action.setHeight(15)

    # enter_action
    self.obj41.enter_action.setValue('\n')
    self.obj41.enter_action.setHeight(15)

    self.obj41.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(560.0,820.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,572.0,823.0,590.0,841.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,556.125,828.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Set')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font190605676')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-27.0, -22.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj130=Basic(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    # is_default
    self.obj130.is_default.setValue((None, 1))
    self.obj130.is_default.config = 0

    # name
    self.obj130.name.setValue('Time')

    # exit_action
    self.obj130.exit_action.setValue('\n')
    self.obj130.exit_action.setHeight(15)

    # enter_action
    self.obj130.enter_action.setValue('\n')
    self.obj130.enter_action.setHeight(15)

    self.obj130.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(340.0,60.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,352.0,63.0,370.0,81.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,335.125,51.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Time')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font158360300')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-28.0, -39.0]
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj131=Basic(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    # is_default
    self.obj131.is_default.setValue((None, 0))
    self.obj131.is_default.config = 0

    # name
    self.obj131.name.setValue('Chrono')

    # exit_action
    self.obj131.exit_action.setValue('\n')
    self.obj131.exit_action.setHeight(15)

    # enter_action
    self.obj131.enter_action.setValue('\n')
    self.obj131.enter_action.setHeight(15)

    self.obj131.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(580.0,80.0,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,592.0,83.0,610.0,101.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,594.125,68.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Chrono')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font158389164')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-9.0, -42.0]
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=Basic(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    # is_default
    self.obj132.is_default.setValue((None, 0))
    self.obj132.is_default.config = 0

    # name
    self.obj132.name.setValue('Alarm')

    # exit_action
    self.obj132.exit_action.setValue('\n')
    self.obj132.exit_action.setHeight(15)

    # enter_action
    self.obj132.enter_action.setValue('\n')
    self.obj132.enter_action.setHeight(15)

    self.obj132.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(140.0,160.0,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,152.0,163.0,170.0,181.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,122.125,183.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarm')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font158345068')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-41.0, -7.0]
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj816=Basic(self)
    self.obj816.isGraphObjectVisual = True

    if(hasattr(self.obj816, '_setHierarchicalLink')):
      self.obj816._setHierarchicalLink(False)

    # is_default
    self.obj816.is_default.setValue((None, 0))
    self.obj816.is_default.config = 0

    # name
    self.obj816.name.setValue('Light_On')

    # exit_action
    self.obj816.exit_action.setValue('\n')
    self.obj816.exit_action.setHeight(15)

    # enter_action
    self.obj816.enter_action.setValue('\n')
    self.obj816.enter_action.setHeight(15)

    self.obj816.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(880.0,260.0,self.obj816)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,892.0,263.0,910.0,281.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,919.125,254.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Light_On')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font181540044')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [16.0, -36.0]
    else: new_obj = None
    self.obj816.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj816)
    self.globalAndLocalPostcondition(self.obj816, rootNode)
    self.obj816.postAction( rootNode.CREATE )

    self.obj818=Basic(self)
    self.obj818.isGraphObjectVisual = True

    if(hasattr(self.obj818, '_setHierarchicalLink')):
      self.obj818._setHierarchicalLink(False)

    # is_default
    self.obj818.is_default.setValue((None, 0))
    self.obj818.is_default.config = 0

    # name
    self.obj818.name.setValue('Light_Off')

    # exit_action
    self.obj818.exit_action.setValue('\n')
    self.obj818.exit_action.setHeight(15)

    # enter_action
    self.obj818.enter_action.setValue('\n')
    self.obj818.enter_action.setHeight(15)

    self.obj818.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(1020.0,320.0,self.obj818)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,1032.0,323.0,1050.0,341.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,1043.125,350.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Light_Off')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font181458828')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj818.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj818)
    self.globalAndLocalPostcondition(self.obj818, rootNode)
    self.obj818.postAction( rootNode.CREATE )

    self.obj951=Basic(self)
    self.obj951.isGraphObjectVisual = True

    if(hasattr(self.obj951, '_setHierarchicalLink')):
      self.obj951._setHierarchicalLink(False)

    # is_default
    self.obj951.is_default.setValue((None, 0))
    self.obj951.is_default.config = 0

    # name
    self.obj951.name.setValue('Time_Edit')

    # exit_action
    self.obj951.exit_action.setValue('\n')
    self.obj951.exit_action.setHeight(15)

    # enter_action
    self.obj951.enter_action.setValue('\n')
    self.obj951.enter_action.setHeight(15)

    self.obj951.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(260.0,160.0,self.obj951)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,272.0,163.0,290.0,181.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,239.125,161.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Time_Edit')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font188099372')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-44.0, -29.0]
    else: new_obj = None
    self.obj951.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj951)
    self.globalAndLocalPostcondition(self.obj951, rootNode)
    self.obj951.postAction( rootNode.CREATE )

    self.obj994=Basic(self)
    self.obj994.isGraphObjectVisual = True

    if(hasattr(self.obj994, '_setHierarchicalLink')):
      self.obj994._setHierarchicalLink(False)

    # is_default
    self.obj994.is_default.setValue((None, 0))
    self.obj994.is_default.config = 0

    # name
    self.obj994.name.setValue('Next_Select')

    # exit_action
    self.obj994.exit_action.setValue('\n')
    self.obj994.exit_action.setHeight(15)

    # enter_action
    self.obj994.enter_action.setValue('\n')
    self.obj994.enter_action.setHeight(15)

    self.obj994.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(320.0,200.0,self.obj994)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,332.0,203.0,350.0,221.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,320.125,192.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Next_Select')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font192455436')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-23.0, -38.0]
    else: new_obj = None
    self.obj994.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj994)
    self.globalAndLocalPostcondition(self.obj994, rootNode)
    self.obj994.postAction( rootNode.CREATE )

    self.obj1423=Basic(self)
    self.obj1423.isGraphObjectVisual = True

    if(hasattr(self.obj1423, '_setHierarchicalLink')):
      self.obj1423._setHierarchicalLink(False)

    # is_default
    self.obj1423.is_default.setValue((None, 0))
    self.obj1423.is_default.config = 0

    # name
    self.obj1423.name.setValue('Time Edit')

    # exit_action
    self.obj1423.exit_action.setValue('\n')
    self.obj1423.exit_action.setHeight(15)

    # enter_action
    self.obj1423.enter_action.setValue('\n')
    self.obj1423.enter_action.setHeight(15)

    self.obj1423.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(240.0,280.0,self.obj1423)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,252.0,283.0,270.0,301.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,263.125,310.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Time Edit')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font196507788')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1423.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1423)
    self.globalAndLocalPostcondition(self.obj1423, rootNode)
    self.obj1423.postAction( rootNode.CREATE )

    self.obj1426=Basic(self)
    self.obj1426.isGraphObjectVisual = True

    if(hasattr(self.obj1426, '_setHierarchicalLink')):
      self.obj1426._setHierarchicalLink(False)

    # is_default
    self.obj1426.is_default.setValue((None, 0))
    self.obj1426.is_default.config = 0

    # name
    self.obj1426.name.setValue('Alarm Edit')

    # exit_action
    self.obj1426.exit_action.setValue('\n')
    self.obj1426.exit_action.setHeight(15)

    # enter_action
    self.obj1426.enter_action.setValue('\n')
    self.obj1426.enter_action.setHeight(15)

    self.obj1426.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(180.0,280.0,self.obj1426)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,192.0,283.0,210.0,301.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,203.125,310.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarm Edit')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font187077420')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1426.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1426)
    self.globalAndLocalPostcondition(self.obj1426, rootNode)
    self.obj1426.postAction( rootNode.CREATE )

    self.obj710=History(self)
    self.obj710.isGraphObjectVisual = True

    if(hasattr(self.obj710, '_setHierarchicalLink')):
      self.obj710._setHierarchicalLink(False)

    # is_default
    self.obj710.is_default.setValue((None, 0))
    self.obj710.is_default.config = 0

    # star
    self.obj710.star.setValue((None, 1))
    self.obj710.star.config = 0

    # name
    self.obj710.name.setValue('Display State')

    self.obj710.graphClass_= graph_History
    if self.genGraphics:
       new_obj = graph_History(700.0,300.0,self.obj710)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("History", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf0.handler,704.0,303.0,740.0,338.0)
       self.UMLmodel.itemconfig(new_obj.gf0.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf0.handler, fill='lightblue')
       self.UMLmodel.coords(new_obj.gf1.handler,721.0,322.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='H')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf2.handler,729.0,322.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, text='*')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, justify='left')
       self.UMLmodel.coords(new_obj.gf3.handler,723.0,347.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='blue')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, text='Display State')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj710.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj710)
    self.globalAndLocalPostcondition(self.obj710, rootNode)
    self.obj710.postAction( rootNode.CREATE )

    self.obj42=Orthogonal(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # visible
    self.obj42.visible.setValue((None, 1))
    self.obj42.visible.config = 0

    # name
    self.obj42.name.setValue('Indiglo')

    # auto_adjust
    self.obj42.auto_adjust.setValue((None, 1))
    self.obj42.auto_adjust.config = 0

    self.obj42.graphClass_= graph_Orthogonal
    if self.genGraphics:
       new_obj = graph_Orthogonal(80.0,360.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,48.0,420.0,363.0,571.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,65.0,412.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Indiglo')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [14.639999999999933, 11.569999999999943]
       new_obj.layConstraints['Label Offset'] = [30.0, 13.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=Orthogonal(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # visible
    self.obj43.visible.setValue((None, 1))
    self.obj43.visible.config = 0

    # name
    self.obj43.name.setValue('Clock State')

    # auto_adjust
    self.obj43.auto_adjust.setValue((None, 1))
    self.obj43.auto_adjust.config = 0

    self.obj43.graphClass_= graph_Orthogonal
    if self.genGraphics:
       new_obj = graph_Orthogonal(-40.0,600.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,51.0,592.0,262.0,767.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,82.0,582.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Clock State')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [48.010000000000197, 3.5899999999999412]
       new_obj.layConstraints['Label Offset'] = [60.0, 7.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=Orthogonal(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # visible
    self.obj44.visible.setValue((None, 1))
    self.obj44.visible.config = 0

    # name
    self.obj44.name.setValue('Chrono State')

    # auto_adjust
    self.obj44.auto_adjust.setValue((None, 1))
    self.obj44.auto_adjust.config = 0

    self.obj44.graphClass_= graph_Orthogonal
    if self.genGraphics:
       new_obj = graph_Orthogonal(380.0,380.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,410.0,421.0,1038.0,632.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,444.0,414.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Chrono State')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [70.140000000000498, 11.019999999999978]
       new_obj.layConstraints['Label Offset'] = [87.0, 29.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=Orthogonal(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # visible
    self.obj45.visible.setValue((None, 1))
    self.obj45.visible.config = 0

    # name
    self.obj45.name.setValue('Alarm')

    # auto_adjust
    self.obj45.auto_adjust.setValue((None, 1))
    self.obj45.auto_adjust.config = 0

    self.obj45.graphClass_= graph_Orthogonal
    if self.genGraphics:
       new_obj = graph_Orthogonal(440.0,780.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,410.0,657.0,1008.0,909.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,426.0,648.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarm')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [5.3899999999999961, 3.9500000000000024]
       new_obj.layConstraints['Label Offset'] = [33.0, 11.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj745=Orthogonal(self)
    self.obj745.isGraphObjectVisual = True

    if(hasattr(self.obj745, '_setHierarchicalLink')):
      self.obj745._setHierarchicalLink(False)

    # visible
    self.obj745.visible.setValue((None, 1))
    self.obj745.visible.config = 0

    # name
    self.obj745.name.setValue('Watch_Running')

    # auto_adjust
    self.obj745.auto_adjust.setValue((None, 1))
    self.obj745.auto_adjust.config = 0

    self.obj745.graphClass_= graph_Orthogonal
    if self.genGraphics:
       new_obj = graph_Orthogonal(820.0,80.0,self.obj745)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,68.0,19.0,1086.0,371.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,68.0,12.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Watch_Running')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj745.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj745)
    self.globalAndLocalPostcondition(self.obj745, rootNode)
    self.obj745.postAction( rootNode.CREATE )

    self.obj118=contains(self)
    self.obj118.isGraphObjectVisual = True

    if(hasattr(self.obj118, '_setHierarchicalLink')):
      self.obj118._setHierarchicalLink(False)

    self.obj118.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(768.747046664,1405.10386365,self.obj118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj118)
    self.globalAndLocalPostcondition(self.obj118, rootNode)
    self.obj118.postAction( rootNode.CREATE )

    self.obj119=contains(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    self.obj119.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(775.935903088,1332.80314775,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj120=contains(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    self.obj120.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(1646.31331479,591.940906201,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj121=contains(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    self.obj121.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(1545.00095547,522.482510187,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj122=contains(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(False)

    self.obj122.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(1058.51538062,868.538474605,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    self.obj123=contains(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    self.obj123.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(1132.98966832,820.71762454,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=contains(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    self.obj124.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(1057.90317276,739.71762454,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj125=contains(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    self.obj125.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(-86.9028809302,654.585934982,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj126=contains(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    self.obj126.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(-276.999044526,660.982510187,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj127=contains(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    self.obj127.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(371.902885817,397.511654259,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj128=contains(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    self.obj128.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(345.138290478,387.443472332,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=contains(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    self.obj129.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(259.903172764,381.21762454,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj734=contains(self)
    self.obj734.isGraphObjectVisual = True

    if(hasattr(self.obj734, '_setHierarchicalLink')):
      self.obj734._setHierarchicalLink(False)

    self.obj734.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(232.0625,301.875,self.obj734)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj734.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj734)
    self.globalAndLocalPostcondition(self.obj734, rootNode)
    self.obj734.postAction( rootNode.CREATE )

    self.obj735=contains(self)
    self.obj735.isGraphObjectVisual = True

    if(hasattr(self.obj735, '_setHierarchicalLink')):
      self.obj735._setHierarchicalLink(False)

    self.obj735.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(168.28301645,228.943472332,self.obj735)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj735.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj735)
    self.globalAndLocalPostcondition(self.obj735, rootNode)
    self.obj735.postAction( rootNode.CREATE )

    self.obj736=contains(self)
    self.obj736.isGraphObjectVisual = True

    if(hasattr(self.obj736, '_setHierarchicalLink')):
      self.obj736._setHierarchicalLink(False)

    self.obj736.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(344.28301645,118.443472332,self.obj736)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj736.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj736)
    self.globalAndLocalPostcondition(self.obj736, rootNode)
    self.obj736.postAction( rootNode.CREATE )

    self.obj737=contains(self)
    self.obj737.isGraphObjectVisual = True

    if(hasattr(self.obj737, '_setHierarchicalLink')):
      self.obj737._setHierarchicalLink(False)

    self.obj737.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(560.78301645,148.943472332,self.obj737)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj737.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj737)
    self.globalAndLocalPostcondition(self.obj737, rootNode)
    self.obj737.postAction( rootNode.CREATE )

    self.obj746=contains(self)
    self.obj746.isGraphObjectVisual = True

    if(hasattr(self.obj746, '_setHierarchicalLink')):
      self.obj746._setHierarchicalLink(False)

    self.obj746.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(792.5,159.5,self.obj746)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj746.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj746)
    self.globalAndLocalPostcondition(self.obj746, rootNode)
    self.obj746.postAction( rootNode.CREATE )

    self.obj747=contains(self)
    self.obj747.isGraphObjectVisual = True

    if(hasattr(self.obj747, '_setHierarchicalLink')):
      self.obj747._setHierarchicalLink(False)

    self.obj747.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(809.0,236.5,self.obj747)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj747.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj747)
    self.globalAndLocalPostcondition(self.obj747, rootNode)
    self.obj747.postAction( rootNode.CREATE )

    self.obj817=contains(self)
    self.obj817.isGraphObjectVisual = True

    if(hasattr(self.obj817, '_setHierarchicalLink')):
      self.obj817._setHierarchicalLink(False)

    self.obj817.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(862.505748984,274.03909536,self.obj817)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj817.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj817)
    self.globalAndLocalPostcondition(self.obj817, rootNode)
    self.obj817.postAction( rootNode.CREATE )

    self.obj819=contains(self)
    self.obj819.isGraphObjectVisual = True

    if(hasattr(self.obj819, '_setHierarchicalLink')):
      self.obj819._setHierarchicalLink(False)

    self.obj819.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(918.588749759,295.01228148,self.obj819)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj819.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj819)
    self.globalAndLocalPostcondition(self.obj819, rootNode)
    self.obj819.postAction( rootNode.CREATE )

    self.obj1420=contains(self)
    self.obj1420.isGraphObjectVisual = True

    if(hasattr(self.obj1420, '_setHierarchicalLink')):
      self.obj1420._setHierarchicalLink(False)

    self.obj1420.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(175.0,277.75,self.obj1420)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1420.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1420)
    self.globalAndLocalPostcondition(self.obj1420, rootNode)
    self.obj1420.postAction( rootNode.CREATE )

    self.obj1429=contains(self)
    self.obj1429.isGraphObjectVisual = True

    if(hasattr(self.obj1429, '_setHierarchicalLink')):
      self.obj1429._setHierarchicalLink(False)

    self.obj1429.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(15.005748984,256.53909536,self.obj1429)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1429.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1429)
    self.globalAndLocalPostcondition(self.obj1429, rootNode)
    self.obj1429.postAction( rootNode.CREATE )

    self.obj1430=contains(self)
    self.obj1430.isGraphObjectVisual = True

    if(hasattr(self.obj1430, '_setHierarchicalLink')):
      self.obj1430._setHierarchicalLink(False)

    self.obj1430.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(126.005748984,269.53909536,self.obj1430)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj1430.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1430)
    self.globalAndLocalPostcondition(self.obj1430, rootNode)
    self.obj1430.postAction( rootNode.CREATE )

    self.obj47=Hyperedge(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # name
    self.obj47.name.setValue('')
    self.obj47.name.setNone()

    # broadcast
    self.obj47.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj47.broadcast.setHeight(15)

    # guard
    self.obj47.guard.setValue('1')

    # trigger
    self.obj47.trigger.setValue('topRightPressed')

    # action
    self.obj47.action.setValue('[DUMP("controller.setIndiglo()")]\n')
    self.obj47.action.setHeight(15)

    # broadcast_to
    self.obj47.broadcast_to.setValue('')
    self.obj47.broadcast_to.setNone()

    # display
    self.obj47.display.setValue('TRP / setIndiglo()')

    self.obj47.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(216.001910947,444.965020373,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-21.0, -20.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=Hyperedge(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # name
    self.obj48.name.setValue('')
    self.obj48.name.setNone()

    # broadcast
    self.obj48.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj48.broadcast.setHeight(15)

    # guard
    self.obj48.guard.setValue('1')

    # trigger
    self.obj48.trigger.setValue('AFTER(3)')

    # action
    self.obj48.action.setValue('[DUMP("controller.unsetIndiglo()")]\n')
    self.obj48.action.setHeight(15)

    # broadcast_to
    self.obj48.broadcast_to.setValue('')
    self.obj48.broadcast_to.setNone()

    # display
    self.obj48.display.setValue('tm(3) / unsetIndiglo()')

    self.obj48.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(199.343200014,538.619791667,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-41.0, 8.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=Hyperedge(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # name
    self.obj49.name.setValue('')
    self.obj49.name.setNone()

    # broadcast
    self.obj49.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj49.broadcast.setHeight(15)

    # guard
    self.obj49.guard.setValue('1')

    # trigger
    self.obj49.trigger.setValue('topRightReleased')

    # action
    self.obj49.action.setValue('[DUMP("Indiglo:  3 seconds till light off.")]\n')
    self.obj49.action.setHeight(15)

    # broadcast_to
    self.obj49.broadcast_to.setValue('')
    self.obj49.broadcast_to.setNone()

    # display
    self.obj49.display.setValue('TRR')

    self.obj49.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(252.0,504.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-44.0, -15.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=Hyperedge(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # name
    self.obj50.name.setValue('')
    self.obj50.name.setNone()

    # broadcast
    self.obj50.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj50.broadcast.setHeight(15)

    # guard
    self.obj50.guard.setValue('1')

    # trigger
    self.obj50.trigger.setValue('topRightPressed')

    # action
    self.obj50.action.setValue('[DUMP("Indiglo:  Back to pressed state.")]\n')
    self.obj50.action.setHeight(15)

    # broadcast_to
    self.obj50.broadcast_to.setValue('')
    self.obj50.broadcast_to.setNone()

    # display
    self.obj50.display.setValue('TRP')

    self.obj50.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(310.0,489.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-9.0, -6.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=Hyperedge(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # name
    self.obj51.name.setValue('')
    self.obj51.name.setNone()

    # broadcast
    self.obj51.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj51.broadcast.setHeight(15)

    # guard
    self.obj51.guard.setValue('1')

    # trigger
    self.obj51.trigger.setValue('timePause')

    # action
    self.obj51.action.setValue('[DUMP("Clock State: Edit Time.")]\n')
    self.obj51.action.setHeight(15)

    # broadcast_to
    self.obj51.broadcast_to.setValue('')
    self.obj51.broadcast_to.setNone()

    # display
    self.obj51.display.setValue('timePause')

    self.obj51.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(99.745614758,687.654452512,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-34.0, -33.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=Hyperedge(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # name
    self.obj52.name.setValue('')
    self.obj52.name.setNone()

    # broadcast
    self.obj52.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj52.broadcast.setHeight(15)

    # guard
    self.obj52.guard.setValue('1')

    # trigger
    self.obj52.trigger.setValue('timeStart')

    # action
    self.obj52.action.setValue('[DUMP("Clock State: Update time.")]\n')
    self.obj52.action.setHeight(15)

    # broadcast_to
    self.obj52.broadcast_to.setValue('')
    self.obj52.broadcast_to.setNone()

    # display
    self.obj52.display.setValue('timeStart')

    self.obj52.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.730994596,730.74938483,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-4.0, 1.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=Hyperedge(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # name
    self.obj53.name.setValue('')
    self.obj53.name.setNone()

    # broadcast
    self.obj53.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj53.broadcast.setHeight(15)

    # guard
    self.obj53.guard.setValue('1')

    # trigger
    self.obj53.trigger.setValue('AFTER(1)')

    # action
    self.obj53.action.setValue('[DUMP("controller.increaseTimeByOne()")]\n')
    self.obj53.action.setHeight(15)

    # broadcast_to
    self.obj53.broadcast_to.setValue('')
    self.obj53.broadcast_to.setNone()

    # display
    self.obj53.display.setValue('tm(1) / increaseTimeByOne()')

    self.obj53.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(153.6,611.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-13.0, -14.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=Hyperedge(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # name
    self.obj54.name.setValue('')
    self.obj54.name.setNone()

    # broadcast
    self.obj54.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj54.broadcast.setHeight(15)

    # guard
    self.obj54.guard.setValue('1')

    # trigger
    self.obj54.trigger.setValue('chrono')

    # action
    self.obj54.action.setValue('[DUMP("Event: chronoDisplay")]\n[EVENT("chronoDisplay")]\n')
    self.obj54.action.setHeight(15)

    # broadcast_to
    self.obj54.broadcast_to.setValue('')
    self.obj54.broadcast_to.setNone()

    # display
    self.obj54.display.setValue('chrono / chronoDisplay')

    self.obj54.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(776.919358343,449.590291152,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-106.0, -50.0]
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=Hyperedge(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # name
    self.obj55.name.setValue('')
    self.obj55.name.setNone()

    # broadcast
    self.obj55.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj55.broadcast.setHeight(15)

    # guard
    self.obj55.guard.setValue('1')

    # trigger
    self.obj55.trigger.setValue('chrono')

    # action
    self.obj55.action.setValue('[DUMP("Chrono:  Paused")]\n')
    self.obj55.action.setHeight(15)

    # broadcast_to
    self.obj55.broadcast_to.setValue('')
    self.obj55.broadcast_to.setNone()

    # display
    self.obj55.display.setValue('chrono')

    self.obj55.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(644.199250501,535.057293934,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [12.0, -17.0]
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=Hyperedge(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # name
    self.obj56.name.setValue('')
    self.obj56.name.setNone()

    # broadcast
    self.obj56.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj56.broadcast.setHeight(15)

    # guard
    self.obj56.guard.setValue('1')

    # trigger
    self.obj56.trigger.setValue('chrono')

    # action
    self.obj56.action.setValue('[DUMP("Chrono:  Running")]\n')
    self.obj56.action.setHeight(15)

    # broadcast_to
    self.obj56.broadcast_to.setValue('')
    self.obj56.broadcast_to.setNone()

    # display
    self.obj56.display.setValue('chrono')

    self.obj56.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(595.574777308,563.636034727,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-53.0, -2.0]
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj58=Hyperedge(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # name
    self.obj58.name.setValue('')
    self.obj58.name.setNone()

    # broadcast
    self.obj58.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj58.broadcast.setHeight(15)

    # guard
    self.obj58.guard.setValue('1')

    # trigger
    self.obj58.trigger.setValue('AFTER(0.01)')

    # action
    self.obj58.action.setValue('[DUMP("controller.increaseChronoByOne()")]\n[EVENT("chronoDisplay")]\n')
    self.obj58.action.setHeight(15)

    # broadcast_to
    self.obj58.broadcast_to.setValue('')
    self.obj58.broadcast_to.setNone()

    # display
    self.obj58.display.setValue('tm(0.01) / increaseChronoByOne(), chronoDisplay')

    self.obj58.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(500.625983896,463.704400671,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-47.0, -19.0]
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=Hyperedge(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # name
    self.obj59.name.setValue('')
    self.obj59.name.setNone()

    # broadcast
    self.obj59.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj59.broadcast.setHeight(15)

    # guard
    self.obj59.guard.setValue('1')

    # trigger
    self.obj59.trigger.setValue('setAlarm')

    # action
    self.obj59.action.setValue('[DUMP("controller.setAlarm()")]\n')
    self.obj59.action.setHeight(15)

    # broadcast_to
    self.obj59.broadcast_to.setValue('')
    self.obj59.broadcast_to.setNone()

    # display
    self.obj59.display.setValue('setAlarm / setAlarm()')

    self.obj59.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(556.0066653,757.965328216,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-90.0, -32.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=Hyperedge(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # name
    self.obj60.name.setValue('')
    self.obj60.name.setNone()

    # broadcast
    self.obj60.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj60.broadcast.setHeight(15)

    # guard
    self.obj60.guard.setValue('1')

    # trigger
    self.obj60.trigger.setValue('AFTER(1)')

    # action
    self.obj60.action.setValue('[DUMP("controller.checkTime()")]\n')
    self.obj60.action.setHeight(15)

    # broadcast_to
    self.obj60.broadcast_to.setValue('')
    self.obj60.broadcast_to.setNone()

    # display
    self.obj60.display.setValue('tm(1) / checkTime()')

    self.obj60.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(568.0,888.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-5.0, 2.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=Hyperedge(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # name
    self.obj61.name.setValue('')
    self.obj61.name.setNone()

    # broadcast
    self.obj61.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj61.broadcast.setHeight(15)

    # guard
    self.obj61.guard.setValue('1')

    # trigger
    self.obj61.trigger.setValue('alarmStart')

    # action
    self.obj61.action.setValue('[DUMP("Event:  alarming")]\n[EVENT("alarming")]\n')
    self.obj61.action.setHeight(15)

    # broadcast_to
    self.obj61.broadcast_to.setValue('')
    self.obj61.broadcast_to.setNone()

    # display
    self.obj61.display.setValue('alarmStart / alarming')

    self.obj61.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(755.0,877.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [9.0, -20.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=Hyperedge(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # name
    self.obj62.name.setValue('')
    self.obj62.name.setNone()

    # broadcast
    self.obj62.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj62.broadcast.setHeight(15)

    # guard
    self.obj62.guard.setValue('1')

    # trigger
    self.obj62.trigger.setValue('AFTER(4)')

    # action
    self.obj62.action.setValue('[DUMP("Event: alarming")]\n[EVENT("alarming")]\n')
    self.obj62.action.setHeight(15)

    # broadcast_to
    self.obj62.broadcast_to.setValue('')
    self.obj62.broadcast_to.setNone()

    # display
    self.obj62.display.setValue('tm(4) / alarming')

    self.obj62.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(905.0,680.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [11.0, -18.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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
    self.obj63.trigger.setValue('topRightPressed')

    # action
    self.obj63.action.setValue('[DUMP("Event: alarming")]\n[EVENT("alarming"]\n')
    self.obj63.action.setHeight(15)

    # broadcast_to
    self.obj63.broadcast_to.setValue('')
    self.obj63.broadcast_to.setNone()

    # display
    self.obj63.display.setValue('TRP / alarming')

    self.obj63.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(880.0,708.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-28.0, -23.0]
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
    self.obj64.trigger.setValue('setAlarm')

    # action
    self.obj64.action.setValue('[DUMP("Alarm:  Off")]\n')
    self.obj64.action.setHeight(15)

    # broadcast_to
    self.obj64.broadcast_to.setValue('')
    self.obj64.broadcast_to.setNone()

    # display
    self.obj64.display.setValue('setAlarm')

    self.obj64.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(591.0066653,761.965328216,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [2.0, 28.0]
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
    self.obj65.trigger.setValue('topLeftPressed')

    # action
    self.obj65.action.setValue('[DUMP("Event: alarming")]\n[EVENT("alarming")]\n')
    self.obj65.action.setHeight(15)

    # broadcast_to
    self.obj65.broadcast_to.setValue('')
    self.obj65.broadcast_to.setNone()

    # display
    self.obj65.display.setValue('TLP / alarming')

    self.obj65.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(822.343200014,736.61979167,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-9.0, -22.0]
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
    self.obj66.trigger.setValue('bottomLeftPressed')

    # action
    self.obj66.action.setValue('[DUMP("Event: alarming")]\n[EVENT("alarming")]\n')
    self.obj66.action.setHeight(15)

    # broadcast_to
    self.obj66.broadcast_to.setValue('')
    self.obj66.broadcast_to.setNone()

    # display
    self.obj66.display.setValue('BLP / alarming')

    self.obj66.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(778.343200014,768.61979167,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-3.0, -23.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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
    self.obj67.trigger.setValue('bottomRightPressed')

    # action
    self.obj67.action.setValue('[DUMP("Event: alarming")]\n[EVENT("alarming")]\n')
    self.obj67.action.setHeight(15)

    # broadcast_to
    self.obj67.broadcast_to.setValue('')
    self.obj67.broadcast_to.setNone()

    # display
    self.obj67.display.setValue('BRP / alarming')

    self.obj67.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(676.0,800.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [17.0, -16.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

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
    self.obj73.trigger.setValue('resetChrono')

    # action
    self.obj73.action.setValue('[DUMP("controller.resetChrono()")]\n[EVENT("chronoDisplay")]\n')
    self.obj73.action.setHeight(15)

    # broadcast_to
    self.obj73.broadcast_to.setValue('')
    self.obj73.broadcast_to.setNone()

    # display
    self.obj73.display.setValue('resetChrono / resetChrono(), chronoDisplay')

    self.obj73.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(882.752175605,544.698160088,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-148.0, 10.0]
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj569=Hyperedge(self)
    self.obj569.isGraphObjectVisual = True

    if(hasattr(self.obj569, '_setHierarchicalLink')):
      self.obj569._setHierarchicalLink(False)

    # name
    self.obj569.name.setValue('')
    self.obj569.name.setNone()

    # broadcast
    self.obj569.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj569.broadcast.setHeight(15)

    # guard
    self.obj569.guard.setValue('1')

    # trigger
    self.obj569.trigger.setValue('upperLeftPressed')

    # action
    self.obj569.action.setValue('[DUMP("controller.refreshChronoDisplay()")]\n')
    self.obj569.action.setHeight(15)

    # broadcast_to
    self.obj569.broadcast_to.setValue('')
    self.obj569.broadcast_to.setNone()

    # display
    self.obj569.display.setValue('ULP / refreshChronoDisplay()')

    self.obj569.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(469.006704458,63.0216055468,self.obj569)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-29.0, -17.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj569.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj569)
    self.globalAndLocalPostcondition(self.obj569, rootNode)
    self.obj569.postAction( rootNode.CREATE )

    self.obj574=Hyperedge(self)
    self.obj574.isGraphObjectVisual = True

    if(hasattr(self.obj574, '_setHierarchicalLink')):
      self.obj574._setHierarchicalLink(False)

    # name
    self.obj574.name.setValue('')
    self.obj574.name.setNone()

    # broadcast
    self.obj574.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj574.broadcast.setHeight(15)

    # guard
    self.obj574.guard.setValue('1')

    # trigger
    self.obj574.trigger.setValue('chronoDisplay')

    # action
    self.obj574.action.setValue('[DUMP("controller.refreshChronoDisplay()")]\n')
    self.obj574.action.setHeight(15)

    # broadcast_to
    self.obj574.broadcast_to.setValue('')
    self.obj574.broadcast_to.setNone()

    # display
    self.obj574.display.setValue('chronoDisplay / refreshChronoDisplay()')

    self.obj574.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(563.28301645,147.943472332,self.obj574)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [2.0, 2.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj574.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj574)
    self.globalAndLocalPostcondition(self.obj574, rootNode)
    self.obj574.postAction( rootNode.CREATE )

    self.obj581=Hyperedge(self)
    self.obj581.isGraphObjectVisual = True

    if(hasattr(self.obj581, '_setHierarchicalLink')):
      self.obj581._setHierarchicalLink(False)

    # name
    self.obj581.name.setValue('')
    self.obj581.name.setNone()

    # broadcast
    self.obj581.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj581.broadcast.setHeight(15)

    # guard
    self.obj581.guard.setValue('1')

    # trigger
    self.obj581.trigger.setValue('bottomRightPressed')

    # action
    self.obj581.action.setValue('[DUMP("Event: chrono")]\n[EVENT("chrono")]\n')
    self.obj581.action.setHeight(15)

    # broadcast_to
    self.obj581.broadcast_to.setValue('')
    self.obj581.broadcast_to.setNone()

    # display
    self.obj581.display.setValue('BRP / chrono')

    self.obj581.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(663.5,73.0,self.obj581)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-38.0, -23.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj581.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj581)
    self.globalAndLocalPostcondition(self.obj581, rootNode)
    self.obj581.postAction( rootNode.CREATE )

    self.obj586=Hyperedge(self)
    self.obj586.isGraphObjectVisual = True

    if(hasattr(self.obj586, '_setHierarchicalLink')):
      self.obj586._setHierarchicalLink(False)

    # name
    self.obj586.name.setValue('')
    self.obj586.name.setNone()

    # broadcast
    self.obj586.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj586.broadcast.setHeight(15)

    # guard
    self.obj586.guard.setValue('1')

    # trigger
    self.obj586.trigger.setValue('bottomLeftPressed')

    # action
    self.obj586.action.setValue('[DUMP("Event: resetChrono")]\n[EVENT("resetChrono")]\n')
    self.obj586.action.setHeight(15)

    # broadcast_to
    self.obj586.broadcast_to.setValue('')
    self.obj586.broadcast_to.setNone()

    # display
    self.obj586.display.setValue('BLP / resetChrono')

    self.obj586.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(648.0,139.0,self.obj586)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [19.0, -28.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj586.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj586)
    self.globalAndLocalPostcondition(self.obj586, rootNode)
    self.obj586.postAction( rootNode.CREATE )

    self.obj591=Hyperedge(self)
    self.obj591.isGraphObjectVisual = True

    if(hasattr(self.obj591, '_setHierarchicalLink')):
      self.obj591._setHierarchicalLink(False)

    # name
    self.obj591.name.setValue('')
    self.obj591.name.setNone()

    # broadcast
    self.obj591.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj591.broadcast.setHeight(15)

    # guard
    self.obj591.guard.setValue('1')

    # trigger
    self.obj591.trigger.setValue('upperLeftPressed')

    # action
    self.obj591.action.setValue('[DUMP("controller.refreshTimeDisplay()")]\n')
    self.obj591.action.setHeight(15)

    # broadcast_to
    self.obj591.broadcast_to.setValue('')
    self.obj591.broadcast_to.setNone()

    # display
    self.obj591.display.setValue('ULP / refreshTimeDisplay()')

    self.obj591.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(437.204460874,91.1283599501,self.obj591)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [10.0, 9.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj591.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj591)
    self.globalAndLocalPostcondition(self.obj591, rootNode)
    self.obj591.postAction( rootNode.CREATE )

    self.obj644=Hyperedge(self)
    self.obj644.isGraphObjectVisual = True

    if(hasattr(self.obj644, '_setHierarchicalLink')):
      self.obj644._setHierarchicalLink(False)

    # name
    self.obj644.name.setValue('')
    self.obj644.name.setNone()

    # broadcast
    self.obj644.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj644.broadcast.setHeight(15)

    # guard
    self.obj644.guard.setValue('1')

    # trigger
    self.obj644.trigger.setValue('bottomLeftPressed')

    # action
    self.obj644.action.setValue('[DUMP("controller.refreshAlarmDisplay()")]\n[DUMP("Event: setAlarm")]\n[EVENT("setAlarm")]\n')
    self.obj644.action.setHeight(15)

    # broadcast_to
    self.obj644.broadcast_to.setValue('')
    self.obj644.broadcast_to.setNone()

    # display
    self.obj644.display.setValue('BLP / refreshAlarmDisplay(), setAlarm')

    self.obj644.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(124.828499371,75.5137601866,self.obj644)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [57.0, -29.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj644.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj644)
    self.globalAndLocalPostcondition(self.obj644, rootNode)
    self.obj644.postAction( rootNode.CREATE )

    self.obj705=Hyperedge(self)
    self.obj705.isGraphObjectVisual = True

    if(hasattr(self.obj705, '_setHierarchicalLink')):
      self.obj705._setHierarchicalLink(False)

    # name
    self.obj705.name.setValue('')
    self.obj705.name.setNone()

    # broadcast
    self.obj705.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj705.broadcast.setHeight(15)

    # guard
    self.obj705.guard.setValue('1')

    # trigger
    self.obj705.trigger.setValue('bottomLeftReleased')

    # action
    self.obj705.action.setValue('[DUMP("controller.refreshTimeDisplay()")]\n')
    self.obj705.action.setHeight(15)

    # broadcast_to
    self.obj705.broadcast_to.setValue('')
    self.obj705.broadcast_to.setNone()

    # display
    self.obj705.display.setValue('BLR / refreshTimeDisplay()')

    self.obj705.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(160.006704458,86.99331296,self.obj705)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [32.0, 17.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj705.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj705)
    self.globalAndLocalPostcondition(self.obj705, rootNode)
    self.obj705.postAction( rootNode.CREATE )

    self.obj748=Hyperedge(self)
    self.obj748.isGraphObjectVisual = True

    if(hasattr(self.obj748, '_setHierarchicalLink')):
      self.obj748._setHierarchicalLink(False)

    # name
    self.obj748.name.setValue('')
    self.obj748.name.setNone()

    # broadcast
    self.obj748.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj748.broadcast.setHeight(15)

    # guard
    self.obj748.guard.setValue('1')

    # trigger
    self.obj748.trigger.setValue('alarming')

    # action
    self.obj748.action.setValue('[DUMP("Alarming")]\n')
    self.obj748.action.setHeight(15)

    # broadcast_to
    self.obj748.broadcast_to.setValue('')
    self.obj748.broadcast_to.setNone()

    # display
    self.obj748.display.setValue('alarming')

    self.obj748.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(870.5,202.5,self.obj748)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-27.0, -20.0]
    else: new_obj = None
    self.obj748.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj748)
    self.globalAndLocalPostcondition(self.obj748, rootNode)
    self.obj748.postAction( rootNode.CREATE )

    self.obj749=Hyperedge(self)
    self.obj749.isGraphObjectVisual = True

    if(hasattr(self.obj749, '_setHierarchicalLink')):
      self.obj749._setHierarchicalLink(False)

    # name
    self.obj749.name.setValue('')
    self.obj749.name.setNone()

    # broadcast
    self.obj749.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj749.broadcast.setHeight(15)

    # guard
    self.obj749.guard.setValue('1')

    # trigger
    self.obj749.trigger.setValue('alarming')

    # action
    self.obj749.action.setValue('[DUMP("Alarm Stop")]\n')
    self.obj749.action.setHeight(15)

    # broadcast_to
    self.obj749.broadcast_to.setValue('')
    self.obj749.broadcast_to.setNone()

    # display
    self.obj749.display.setValue('alarming')

    self.obj749.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(836.625,301.75,self.obj749)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-57.0, -20.0]
    else: new_obj = None
    self.obj749.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj749)
    self.globalAndLocalPostcondition(self.obj749, rootNode)
    self.obj749.postAction( rootNode.CREATE )

    self.obj830=Hyperedge(self)
    self.obj830.isGraphObjectVisual = True

    if(hasattr(self.obj830, '_setHierarchicalLink')):
      self.obj830._setHierarchicalLink(False)

    # name
    self.obj830.name.setValue('')
    self.obj830.name.setNone()

    # broadcast
    self.obj830.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj830.broadcast.setHeight(15)

    # guard
    self.obj830.guard.setValue('1')

    # trigger
    self.obj830.trigger.setValue('AFTER(0.5)')

    # action
    self.obj830.action.setValue('[DUMP("controller.unsetIndiglo()")]\n')
    self.obj830.action.setHeight(15)

    # broadcast_to
    self.obj830.broadcast_to.setValue('')
    self.obj830.broadcast_to.setNone()

    # display
    self.obj830.display.setValue('tm(0.5) / unsetIndiglo()')

    self.obj830.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(999.333855898,283.002029114,self.obj830)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-14.0, -24.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj830.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj830)
    self.globalAndLocalPostcondition(self.obj830, rootNode)
    self.obj830.postAction( rootNode.CREATE )

    self.obj831=Hyperedge(self)
    self.obj831.isGraphObjectVisual = True

    if(hasattr(self.obj831, '_setHierarchicalLink')):
      self.obj831._setHierarchicalLink(False)

    # name
    self.obj831.name.setValue('')
    self.obj831.name.setNone()

    # broadcast
    self.obj831.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj831.broadcast.setHeight(15)

    # guard
    self.obj831.guard.setValue('1')

    # trigger
    self.obj831.trigger.setValue('AFTER(0.5)')

    # action
    self.obj831.action.setValue('[DUMP("controller.setIndiglo()")]\n')
    self.obj831.action.setHeight(15)

    # broadcast_to
    self.obj831.broadcast_to.setValue('')
    self.obj831.broadcast_to.setNone()

    # display
    self.obj831.display.setValue('tm(0.5) / setIndiglo()')

    self.obj831.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(927.309890485,321.753368165,self.obj831)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-10.0, 18.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj831.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj831)
    self.globalAndLocalPostcondition(self.obj831, rootNode)
    self.obj831.postAction( rootNode.CREATE )

    self.obj954=Hyperedge(self)
    self.obj954.isGraphObjectVisual = True

    if(hasattr(self.obj954, '_setHierarchicalLink')):
      self.obj954._setHierarchicalLink(False)

    # name
    self.obj954.name.setValue('')
    self.obj954.name.setNone()

    # broadcast
    self.obj954.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj954.broadcast.setHeight(15)

    # guard
    self.obj954.guard.setValue('1')

    # trigger
    self.obj954.trigger.setValue('bottomRightPressed')

    # action
    self.obj954.action.setValue('[DUMP("Pending time edit mode")]\n')
    self.obj954.action.setHeight(15)

    # broadcast_to
    self.obj954.broadcast_to.setValue('')
    self.obj954.broadcast_to.setNone()

    # display
    self.obj954.display.setValue('BRP')

    self.obj954.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(302.949772771,107.965020373,self.obj954)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-32.0, -22.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj954.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj954)
    self.globalAndLocalPostcondition(self.obj954, rootNode)
    self.obj954.postAction( rootNode.CREATE )

    self.obj957=Hyperedge(self)
    self.obj957.isGraphObjectVisual = True

    if(hasattr(self.obj957, '_setHierarchicalLink')):
      self.obj957._setHierarchicalLink(False)

    # name
    self.obj957.name.setValue('')
    self.obj957.name.setNone()

    # broadcast
    self.obj957.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj957.broadcast.setHeight(15)

    # guard
    self.obj957.guard.setValue('1')

    # trigger
    self.obj957.trigger.setValue('bottomRightReleased')

    # action
    self.obj957.action.setValue('[DUMP("Time Mode")]\n')
    self.obj957.action.setHeight(15)

    # broadcast_to
    self.obj957.broadcast_to.setValue('')
    self.obj957.broadcast_to.setNone()

    # display
    self.obj957.display.setValue('BRR')

    self.obj957.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(347.949772771,114.965020373,self.obj957)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-23.0, 18.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj957.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj957)
    self.globalAndLocalPostcondition(self.obj957, rootNode)
    self.obj957.postAction( rootNode.CREATE )

    self.obj1003=Hyperedge(self)
    self.obj1003.isGraphObjectVisual = True

    if(hasattr(self.obj1003, '_setHierarchicalLink')):
      self.obj1003._setHierarchicalLink(False)

    # name
    self.obj1003.name.setValue('')
    self.obj1003.name.setNone()

    # broadcast
    self.obj1003.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj1003.broadcast.setHeight(15)

    # guard
    self.obj1003.guard.setValue('1')

    # trigger
    self.obj1003.trigger.setValue('AFTER(2)')

    # action
    self.obj1003.action.setValue('[DUMP("controller.refreshTimeDisplay()")]\n[DUMP("controller.refreshTimeDisplay()")]\n[DUMP("Event: startTime")]\n[EVENT("startTime")]\n')
    self.obj1003.action.setHeight(15)

    # broadcast_to
    self.obj1003.broadcast_to.setValue('')
    self.obj1003.broadcast_to.setNone()

    # display
    self.obj1003.display.setValue('tm(2) / refreshDisplay(), timeStart')

    self.obj1003.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(372.006704458,157.99331296,self.obj1003)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [64.0, 13.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1003.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1003)
    self.globalAndLocalPostcondition(self.obj1003, rootNode)
    self.obj1003.postAction( rootNode.CREATE )

    # Connections for obj70 (graphObject_: Obj63) named Chrono_On
    self.drawConnections(
(self.obj70,self.obj73,[702.0, 532.0, 811.99999999999909, 557.99999999999955, 882.75217560527221, 544.69816008841087],"bezier", 3),
(self.obj70,self.obj118,[575.0, 625.0, 768.74704666364494, 1405.1038636492826],"bezier", 2),
(self.obj70,self.obj119,[575.0, 625.0, 775.93590308835894, 1332.803147754154],"bezier", 2) )
    # Connections for obj731 (graphObject_: Obj129) named Running
    self.drawConnections(
(self.obj731,self.obj734,[431.0, 359.0, 264.5, 289.5, 232.06249999999997, 301.875],"bezier", 3),
(self.obj731,self.obj735,[96.999999999999986, 198.0, 168.28301644978399, 228.94347233175606],"bezier", 2),
(self.obj731,self.obj736,[431.0, 38.0, 344.28301644978393, 118.44347233175608],"bezier", 2),
(self.obj731,self.obj737,[765.99999999999989, 198.0, 560.78301644978399, 148.94347233175608],"bezier", 2),
(self.obj731,self.obj748,[765.99999999999989, 198.0, 870.49999999999636, 202.4999999999998],"bezier", 2),
(self.obj731,self.obj1420,[96.999999999999986, 198.0, 148.5, 252.0, 175.0, 277.75],"bezier", 3) )
    # Connections for obj742 (graphObject_: Obj136) named Alarming
    self.drawConnections(
(self.obj742,self.obj749,[863.0, 302.0, 836.6249999999992, 301.74999999999989],"bezier", 2),
(self.obj742,self.obj817,[863.0, 302.0, 862.50574898404352, 274.0390953601472],"bezier", 2),
(self.obj742,self.obj819,[863.0, 302.0, 918.58874975884646, 295.01228148002099],"bezier", 2) )
    # Connections for obj1419 (graphObject_: Obj203) named Edit Mode
    self.drawConnections(
(self.obj1419,self.obj1429,[163.0, 307.0, 15.005748984043249, 256.5390953601472],"bezier", 2),
(self.obj1419,self.obj1430,[163.0, 307.0, 126.00574898404334, 269.5390953601472],"bezier", 2) )
    # Connections for obj29 (graphObject_: Obj1) named Setup
    self.drawConnections(
 )
    # Connections for obj30 (graphObject_: Obj2) named Stopped
    self.drawConnections(
 )
    # Connections for obj31 (graphObject_: Obj3) named Indiglo_Off
    self.drawConnections(
(self.obj31,self.obj47,[175.33351264266952, 472.04309608307022, 189.9999999999996, 444.99999999999989, 216.00191094743761, 444.96502037329128],"bezier", 3) )
    # Connections for obj32 (graphObject_: Obj4) named Waiting
    self.drawConnections(
(self.obj32,self.obj48,[282.0114979680867, 540.07819072029463, 225.99999999999926, 548.99999999999977, 199.34320001431226, 538.61979166666606],"bezier", 3),
(self.obj32,self.obj50,[295.33351264266958, 532.04309608307028, 316.9999999999992, 504.99999999999989, 309.9999999999992, 488.99999999999955],"bezier", 3) )
    # Connections for obj33 (graphObject_: Obj5) named Pressed
    self.drawConnections(
(self.obj33,self.obj49,[266.97933664102652, 472.43524907991593, 249.99999999999989, 477.99999999999989, 251.99999999999849, 503.99999999999932],"bezier", 3) )
    # Connections for obj34 (graphObject_: Obj6) named Update
    self.drawConnections(
(self.obj34,self.obj51,[172.01149796808667, 652.07819072029429, 133.99999999999974, 658.99999999999795, 99.745614758024317, 687.65445251208052],"bezier", 3),
(self.obj34,self.obj53,[173.34320001431351, 647.61979166666652, 151.9999999999998, 635.99999999999955, 153.59999999999988, 610.99999999999989],"bezier", 3) )
    # Connections for obj35 (graphObject_: Obj7) named Wait
    self.drawConnections(
(self.obj35,self.obj52,[82.806345527924151, 740.43524907991605, 113.99999999999949, 747.99999999999966, 140.73099459623904, 730.7493848303568],"bezier", 3) )
    # Connections for obj36 (graphObject_: Obj8) named Reset
    self.drawConnections(
(self.obj36,self.obj54,[986.31271305144355, 472.92092556094815, 893.9999999999992, 451.9999999999979, 776.91935834310345, 449.59029115204243],"bezier", 3) )
    # Connections for obj37 (graphObject_: Obj9) named Running
    self.drawConnections(
(self.obj37,self.obj55,[564.52424304640203, 497.22692361359856, 618.76742662622576, 509.55551564207877, 644.19925050129598, 535.05729393384058],"bezier", 3),
(self.obj37,self.obj58,[561.8712264488131, 495.66517282495471, 502.99999999999977, 488.99999999999972, 500.62598389645723, 463.70440067124093],"bezier", 3) )
    # Connections for obj38 (graphObject_: Obj10) named Paused
    self.drawConnections(
(self.obj38,self.obj56,[673.14573368451738, 609.36958412035813, 621.0378511828992, 589.13781301846484, 595.57477730782898, 563.63603472670275],"bezier", 3) )
    # Connections for obj39 (graphObject_: Obj11) named Alarm_Off
    self.drawConnections(
(self.obj39,self.obj59,[576.56603289956774, 699.88694466351217, 554.99999999999829, 718.99999999999966, 556.00666530038598, 757.96532821597361],"bezier", 3) )
    # Connections for obj40 (graphObject_: Obj12) named Alarming
    self.drawConnections(
(self.obj40,self.obj62,[945.33351264266878, 864.0430960830704, 991.99999999999864, 677.99999999999909, 904.99999999999875, 679.99999999999977],"bezier", 3),
(self.obj40,self.obj63,[941.17749951769304, 863.02456296004186, 962.99999999999909, 745.9999999999992, 879.9999999999992, 707.99999999999977],"bezier", 3),
(self.obj40,self.obj65,[941.17749951769304, 863.02456296004186, 924.99999999999875, 763.9999999999992, 822.3432000140001, 736.61979166999993],"bezier", 3),
(self.obj40,self.obj66,[936.74796458621142, 864.16809608307051, 876.99999999999909, 808.9999999999992, 778.34320001399999, 768.61979166999993],"bezier", 3),
(self.obj40,self.obj67,[932.01149796808659, 872.07819072029429, 699.99999999999977, 827.9999999999992, 675.99999999999977, 799.99999999999977],"bezier", 3) )
    # Connections for obj41 (graphObject_: Obj13) named Set
    self.drawConnections(
(self.obj41,self.obj60,[585.27658095602601, 839.88694466351183, 601.99999999999932, 883.9999999999992, 567.99999999999443, 887.9999999999992],"bezier", 3),
(self.obj41,self.obj61,[590.00191094743764, 831.96502037329128, 682.99999999999977, 859.9999999999992, 754.99999999999977, 876.99999999999909], 0, 3),
(self.obj41,self.obj64,[581.1774995176927, 823.02456296004186, 591.09206283035576, 792.48095321597361, 591.0066653003903, 761.96532821597373],"bezier", 3) )
    # Connections for obj130 (graphObject_: Obj83) named Time
    self.drawConnections(
(self.obj130,self.obj569,[370.00191094743798, 71.96502037329131, 409.99999999999989, 59.999999999999986, 469.00670445776245, 63.021605546792884],"bezier", 3),
(self.obj130,self.obj644,[352.01149796808687, 72.078190720294444, 143.99999999999949, 53.99999999999995, 124.82849937144486, 75.513760186645641],"bezier", 3),
(self.obj130,self.obj954,[352.97933664102641, 76.435249079915849, 313.99999999999989, 81.999999999999972, 302.94977277111877, 107.96502037329121],"bezier", 3) )
    # Connections for obj131 (graphObject_: Obj84) named Chrono
    self.drawConnections(
(self.obj131,self.obj574,[596.56603289956809, 99.886944663512139, 586.99999999999977, 140.0, 563.28301644978387, 147.94347233175608],"bezier", 3),
(self.obj131,self.obj581,[610.00191094743786, 91.965020373291367, 661.9999999999992, 93.999999999999901, 663.49999999999989, 73.0],"bezier", 3),
(self.obj131,self.obj586,[605.27658095602624, 99.886944663512139, 616.99999999999977, 130.99999999999986, 648.0, 139.0],"bezier", 3),
(self.obj131,self.obj591,[592.01149796808681, 92.07819072029443, 478.00574898404341, 95.039095360147201, 437.20446087400273, 91.12835995005257],"bezier", 3) )
    # Connections for obj132 (graphObject_: Obj85) named Alarm
    self.drawConnections(
(self.obj132,self.obj705,[165.3335126426694, 164.04309608307042, 115.9999999999997, 98.999999999999787, 160.00670445776208, 86.993312960042019],"bezier", 3) )
    # Connections for obj816 (graphObject_: Obj147) named Light_On
    self.drawConnections(
(self.obj816,self.obj830,[910.00191094743786, 271.96502037329128, 942.99999999999841, 268.0, 999.33385589752504, 283.00202911409031],"bezier", 3) )
    # Connections for obj818 (graphObject_: Obj149) named Light_Off
    self.drawConnections(
(self.obj818,self.obj831,[1032.011497968087, 332.0781907202944, 972.99999999999966, 346.99999999999989, 927.30989048516778, 321.75336816508923],"bezier", 3) )
    # Connections for obj951 (graphObject_: Obj171) named Time_Edit
    self.drawConnections(
(self.obj951,self.obj957,[288.92020890121108, 167.49479166666663, 334.99999999999989, 154.99999999999994, 347.94977277111877, 114.96502037329115],"bezier", 3) )
    # Connections for obj994 (graphObject_: Obj194) named Next_Select
    self.drawConnections(
(self.obj994,self.obj1003,[348.92020890121108, 207.4947916666666, 360.99999999999989, 195.99999999999991, 372.00670445776234, 157.99331296004203],"bezier", 3) )
    # Connections for obj1423 (graphObject_: Obj205) named Time Edit
    self.drawConnections(
 )
    # Connections for obj1426 (graphObject_: Obj206) named Alarm Edit
    self.drawConnections(
 )
    # Connections for obj710 (graphObject_: Obj112) named Display State
    self.drawConnections(
 )
    # Connections for obj42 (graphObject_: Obj14) named Indiglo
    self.drawConnections(
(self.obj42,self.obj127,[362.99999999999994, 495.0, 371.90288581680306, 397.5116542591054],"bezier", 2),
(self.obj42,self.obj128,[362.99999999999994, 495.0, 345.138290478013, 387.44347233175608],"bezier", 2),
(self.obj42,self.obj129,[205.0, 420.0, 259.90317276396217, 381.21762453995802],"bezier", 2) )
    # Connections for obj43 (graphObject_: Obj15) named Clock State
    self.drawConnections(
(self.obj43,self.obj125,[50.999999999999993, 679.0, -86.902880930219681, 654.5859349816003],"bezier", 2),
(self.obj43,self.obj126,[50.999999999999993, 679.0, -276.99904452628107, 660.98251018664564],"bezier", 2) )
    # Connections for obj44 (graphObject_: Obj16) named Chrono State
    self.drawConnections(
(self.obj44,self.obj120,[1038.0, 526.0, 1646.3133147934668, 591.94090620103111],"bezier", 2),
(self.obj44,self.obj121,[1038.0, 526.0, 1545.0009554737189, 522.48251018664553],"bezier", 2) )
    # Connections for obj45 (graphObject_: Obj17) named Alarm
    self.drawConnections(
(self.obj45,self.obj122,[1008.0, 783.0, 1058.5153806194376, 868.53847460526322],"bezier", 2),
(self.obj45,self.obj123,[1008.0, 783.0, 1132.9896683205131, 820.71762453995757],"bezier", 2),
(self.obj45,self.obj124,[1008.0, 783.0, 1057.9031727639619, 739.71762453995791],"bezier", 2) )
    # Connections for obj745 (graphObject_: Obj137) named Watch_Running
    self.drawConnections(
(self.obj745,self.obj746,[68.0, 195.0, 792.5, 159.5],"bezier", 2),
(self.obj745,self.obj747,[1086.0, 195.0, 809.0, 236.49999999999997],"bezier", 2) )
    # Connections for obj118 (graphObject_: Obj71) of type contains
    self.drawConnections(
(self.obj118,self.obj38,[768.74704666364494, 1405.1038636492826, 674.64427556122087, 612.03803837903331],"bezier", 2) )
    # Connections for obj119 (graphObject_: Obj72) of type contains
    self.drawConnections(
(self.obj119,self.obj37,[775.93590308835894, 1332.803147754154, 564.52424304640203, 497.22692361359856],"bezier", 2) )
    # Connections for obj120 (graphObject_: Obj73) of type contains
    self.drawConnections(
(self.obj120,self.obj70,[1646.3133147934666, 591.94090620103111, 702.0, 532.0],"bezier", 2) )
    # Connections for obj121 (graphObject_: Obj74) of type contains
    self.drawConnections(
(self.obj121,self.obj36,[1545.0009554737189, 522.48251018664553, 989.71722791272566, 472.02687981962322],"bezier", 2) )
    # Connections for obj122 (graphObject_: Obj75) of type contains
    self.drawConnections(
(self.obj122,self.obj41,[1058.5153806194376, 868.53847460526322, 590.00191094743764, 831.96502037329128],"bezier", 2) )
    # Connections for obj123 (graphObject_: Obj76) of type contains
    self.drawConnections(
(self.obj123,self.obj40,[1132.9896683205131, 820.7176245399578, 948.92020890121091, 867.49479166666652],"bezier", 2) )
    # Connections for obj124 (graphObject_: Obj77) of type contains
    self.drawConnections(
(self.obj124,self.obj39,[1057.9031727639619, 739.71762453995791, 590.00191094743764, 691.96502037329128],"bezier", 2) )
    # Connections for obj125 (graphObject_: Obj78) of type contains
    self.drawConnections(
(self.obj125,self.obj35,[-86.902880930219681, 654.5859349816003, 67.343200014313652, 731.6197916666664],"bezier", 2) )
    # Connections for obj126 (graphObject_: Obj79) of type contains
    self.drawConnections(
(self.obj126,self.obj34,[-276.99904452628107, 660.98251018664564, 172.01149796808681, 652.0781907202944],"bezier", 2) )
    # Connections for obj127 (graphObject_: Obj80) of type contains
    self.drawConnections(
(self.obj127,self.obj32,[371.90288581680306, 397.5116542591054, 295.33351264266958, 532.04309608307051],"bezier", 2) )
    # Connections for obj128 (graphObject_: Obj81) of type contains
    self.drawConnections(
(self.obj128,self.obj33,[345.138290478013, 387.44347233175608, 279.33351264266952, 460.04309608307051],"bezier", 2) )
    # Connections for obj129 (graphObject_: Obj82) of type contains
    self.drawConnections(
(self.obj129,self.obj31,[259.90317276396217, 381.21762453995802, 175.33351264266958, 472.04309608307051],"bezier", 2) )
    # Connections for obj734 (graphObject_: Obj132) of type contains
    self.drawConnections(
(self.obj734,self.obj710,[232.06249999999997, 301.875, 199.62499999999997, 314.24999999999994, 704.25, 321.5],"bezier", 3) )
    # Connections for obj735 (graphObject_: Obj133) of type contains
    self.drawConnections(
(self.obj735,self.obj132,[168.28301644978399, 228.94347233175606, 160.83590939783176, 180.96206296004203],"bezier", 2) )
    # Connections for obj736 (graphObject_: Obj134) of type contains
    self.drawConnections(
(self.obj736,self.obj130,[344.28301644978393, 118.44347233175608, 356.56603289956797, 79.886944663512168],"bezier", 2) )
    # Connections for obj737 (graphObject_: Obj135) of type contains
    self.drawConnections(
(self.obj737,self.obj131,[560.78301644978399, 148.94347233175608, 596.56603289956809, 99.886944663512139],"bezier", 2) )
    # Connections for obj746 (graphObject_: Obj138) of type contains
    self.drawConnections(
(self.obj746,self.obj731,[792.5, 159.5, 765.99999999999989, 198.0],"bezier", 2) )
    # Connections for obj747 (graphObject_: Obj139) of type contains
    self.drawConnections(
(self.obj747,self.obj742,[809.0, 236.49999999999997, 863.0, 302.0],"bezier", 2) )
    # Connections for obj817 (graphObject_: Obj148) of type contains
    self.drawConnections(
(self.obj817,self.obj816,[862.50574898404352, 274.0390953601472, 892.01149796808693, 272.0781907202944],"bezier", 2) )
    # Connections for obj819 (graphObject_: Obj150) of type contains
    self.drawConnections(
(self.obj819,self.obj818,[918.58874975884646, 295.01228148002099, 1033.3432000143139, 327.61979166666657],"bezier", 2) )
    # Connections for obj1420 (graphObject_: Obj204) of type contains
    self.drawConnections(
(self.obj1420,self.obj1419,[175.0, 277.75, 201.49999999999997, 303.5, 163.0, 307.0],"bezier", 3) )
    # Connections for obj1429 (graphObject_: Obj207) of type contains
    self.drawConnections(
(self.obj1429,self.obj1423,[15.005748984043249, 256.5390953601472, 252.01149796808687, 292.0781907202944],"bezier", 2) )
    # Connections for obj1430 (graphObject_: Obj208) of type contains
    self.drawConnections(
(self.obj1430,self.obj1426,[126.00574898404339, 269.5390953601472, 193.34320001431371, 287.61979166666663],"bezier", 2) )
    # Connections for obj47 (graphObject_: Obj19) named 
    self.drawConnections(
(self.obj47,self.obj33,[216.00191094743761, 444.96502037329128, 252.99999999999898, 442.99999999999989, 270.74796458621131, 460.16809608307022],"bezier", 3) )
    # Connections for obj48 (graphObject_: Obj21) named 
    self.drawConnections(
(self.obj48,self.obj31,[199.34320001431226, 538.61979166666606, 161.9999999999998, 519.0, 170.83590939783173, 488.9620629600422],"bezier", 3) )
    # Connections for obj49 (graphObject_: Obj23) named 
    self.drawConnections(
(self.obj49,self.obj32,[251.99999999999977, 503.99999999999972, 256.9999999999992, 518.99999999999977, 283.34320001431354, 535.61979166666674],"bezier", 3) )
    # Connections for obj50 (graphObject_: Obj25) named 
    self.drawConnections(
(self.obj50,self.obj33,[309.9999999999992, 488.99999999999955, 307.99999999999903, 470.99999999999966, 282.80634552792378, 472.43524907991593],"bezier", 3) )
    # Connections for obj51 (graphObject_: Obj27) named 
    self.drawConnections(
(self.obj51,self.obj35,[99.745614758023919, 687.65445251207893, 79.999999999999687, 700.99999999999716, 75.177499517692993, 727.0245629600422],"bezier", 3) )
    # Connections for obj52 (graphObject_: Obj29) named 
    self.drawConnections(
(self.obj52,self.obj34,[140.73099459623904, 730.7493848303568, 187.99999999999989, 697.9999999999992, 180.83590939783173, 660.96206296004198],"bezier", 3) )
    # Connections for obj53 (graphObject_: Obj31) named 
    self.drawConnections(
(self.obj53,self.obj34,[153.59999999999988, 610.99999999999989, 182.99999999999986, 615.99999999999955, 181.17749951769289, 643.0245629600422],"bezier", 3) )
    # Connections for obj54 (graphObject_: Obj33) named 
    self.drawConnections(
(self.obj54,self.obj37,[776.91935834310345, 449.59029115204243, 624.99999999999977, 456.9999999999979, 565.23019596078177, 496.53658449687913],"bezier", 3) )
    # Connections for obj55 (graphObject_: Obj35) named 
    self.drawConnections(
(self.obj55,self.obj38,[644.19925050129598, 535.05729393384058, 669.63107437636552, 560.55907222560222, 673.82668659889669, 608.67924500363893],"bezier", 3) )
    # Connections for obj56 (graphObject_: Obj37) named 
    self.drawConnections(
(self.obj56,self.obj37,[595.57477730782898, 563.63603472670275, 570.11170343275876, 538.13425643494134, 563.63610873476262, 497.44194727290437],"bezier", 3) )
    # Connections for obj58 (graphObject_: Obj41) named 
    self.drawConnections(
(self.obj58,self.obj37,[500.62598389645723, 463.70440067124093, 518.62598389645723, 447.70440067124076, 563.70442675873528, 493.85444727290445],"bezier", 3) )
    # Connections for obj59 (graphObject_: Obj43) named 
    self.drawConnections(
(self.obj59,self.obj41,[556.00666530038598, 757.96532821597361, 552.99999999999784, 799.9999999999992, 576.74796458621131, 824.16809608307051],"bezier", 3) )
    # Connections for obj60 (graphObject_: Obj45) named 
    self.drawConnections(
(self.obj60,self.obj41,[567.99999999999443, 887.9999999999992, 547.99999999999864, 866.99999999999909, 576.56603289956774, 839.88694466351183],"bezier", 3) )
    # Connections for obj61 (graphObject_: Obj47) named 
    self.drawConnections(
(self.obj61,self.obj40,[754.99999999999977, 876.99999999999909, 828.9999999999992, 881.99999999999909, 932.01149796808659, 872.07819072029429], 0, 3) )
    # Connections for obj62 (graphObject_: Obj49) named 
    self.drawConnections(
(self.obj62,self.obj39,[904.99999999999875, 679.99999999999977, 771.99999999999977, 655.99999999999977, 590.00191094743764, 691.96502037329128],"bezier", 3) )
    # Connections for obj63 (graphObject_: Obj51) named 
    self.drawConnections(
(self.obj63,self.obj39,[879.9999999999992, 707.99999999999977, 807.9999999999992, 685.99999999999977, 590.00191094743764, 691.96502037329128],"bezier", 3) )
    # Connections for obj64 (graphObject_: Obj53) named 
    self.drawConnections(
(self.obj64,self.obj39,[591.0066653003903, 761.96532821597373, 590.92126777042517, 731.44970321597384, 580.83590939783153, 700.96206296004198],"bezier", 3) )
    # Connections for obj65 (graphObject_: Obj55) named 
    self.drawConnections(
(self.obj65,self.obj39,[822.3432000140001, 736.61979166999993, 590.00191094743764, 691.96502037329128],"bezier", 2) )
    # Connections for obj66 (graphObject_: Obj57) named 
    self.drawConnections(
(self.obj66,self.obj39,[778.34320001399999, 768.61979166999993, 588.8063455279239, 696.43524907991605],"bezier", 2) )
    # Connections for obj67 (graphObject_: Obj59) named 
    self.drawConnections(
(self.obj67,self.obj39,[675.99999999999977, 799.99999999999977, 617.99999999999977, 768.99999999999966, 585.27658095602601, 699.88694466351217],"bezier", 3) )
    # Connections for obj73 (graphObject_: Obj64) named 
    self.drawConnections(
(self.obj73,self.obj36,[882.75217560527221, 544.69816008841087, 969.0, 528.99999999999977, 987.03005230315182, 473.61126467766735],"bezier", 3) )
    # Connections for obj569 (graphObject_: Obj96) named 
    self.drawConnections(
(self.obj569,self.obj131,[469.00670445776245, 63.021605546792884, 522.99999999999966, 69.999999999999972, 592.01149796808681, 92.07819072029443],"bezier", 3) )
    # Connections for obj574 (graphObject_: Obj98) named 
    self.drawConnections(
(self.obj574,self.obj131,[563.28301644978387, 147.94347233175608, 562.28301644978376, 126.94347233175584, 592.97933664102641, 96.435249079915877],"bezier", 3) )
    # Connections for obj581 (graphObject_: Obj100) named 
    self.drawConnections(
(self.obj581,self.obj131,[663.49999999999989, 73.0, 664.99999999999932, 51.999999999999972, 608.92020890121103, 87.494791666666657],"bezier", 3) )
    # Connections for obj586 (graphObject_: Obj102) named 
    self.drawConnections(
(self.obj586,self.obj131,[647.99999999999784, 138.99999999999986, 635.99999999999977, 110.99999999999996, 608.80634552792412, 96.435249079915877],"bezier", 3) )
    # Connections for obj591 (graphObject_: Obj104) named 
    self.drawConnections(
(self.obj591,self.obj130,[437.20446087400273, 91.12835995005257, 396.40317276396195, 87.217624539957924, 368.80634552792418, 76.435249079915849],"bezier", 3) )
    # Connections for obj644 (graphObject_: Obj106) named 
    self.drawConnections(
(self.obj644,self.obj132,[124.82849937144486, 75.513760186645641, 113.99999999999963, 164.99999999999994, 152.01149796808681, 172.07819072029437],"bezier", 3) )
    # Connections for obj705 (graphObject_: Obj110) named 
    self.drawConnections(
(self.obj705,self.obj130,[160.00670445776177, 86.993312960041564, 213.99999999999949, 73.999999999999972, 352.97933664102641, 76.435249079915849],"bezier", 3) )
    # Connections for obj748 (graphObject_: Obj140) named 
    self.drawConnections(
(self.obj748,self.obj742,[870.49999999999636, 202.4999999999998, 943.99999999999352, 199.9999999999994, 970.99999999999989, 241.0],"bezier", 3) )
    # Connections for obj749 (graphObject_: Obj142) named 
    self.drawConnections(
(self.obj749,self.obj710,[836.62499999999989, 301.74999999999994, 739.25, 320.49999999999994],"bezier", 2) )
    # Connections for obj830 (graphObject_: Obj151) named 
    self.drawConnections(
(self.obj830,self.obj818,[999.33385589752504, 283.00202911409031, 1036.9999999999995, 297.99999999999989, 1041.1774995176931, 323.02456296004203],"bezier", 3) )
    # Connections for obj831 (graphObject_: Obj153) named 
    self.drawConnections(
(self.obj831,self.obj816,[927.30989048516778, 321.75336816508923, 890.99999999999864, 300.99999999999989, 900.83590939783198, 280.96206296004203],"bezier", 3) )
    # Connections for obj954 (graphObject_: Obj172) named 
    self.drawConnections(
(self.obj954,self.obj951,[302.94977277111877, 107.96502037329121, 285.99999999999989, 138.99999999999994, 281.17749951769298, 163.02456296004206],"bezier", 3) )
    # Connections for obj957 (graphObject_: Obj174) named 
    self.drawConnections(
(self.obj957,self.obj130,[347.94977277111877, 114.96502037329115, 356.56603289956797, 79.886944663512168],"bezier", 2) )
    # Connections for obj1003 (graphObject_: Obj199) named 
    self.drawConnections(
(self.obj1003,self.obj130,[372.00670445776228, 157.99331296004203, 380.99999999999989, 121.99999999999999, 365.27658095602618, 79.886944663512168],"bezier", 3) )

newfunction = DigitalWatchStatechart_DCharts_MDL

loadedMMName = 'DCharts'

atom3version = '0.3'
