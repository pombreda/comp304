"""
__DigitalWatchStatechart_DCharts_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: cshank1
Modified: Tue Mar 16 19:07:56 2010
____________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Composite import *
from Basic import *
from Orthogonal import *
from contains import *
from Hyperedge import *
from orthogonality import *
from graph_Basic import *
from graph_Orthogonal import *
from graph_Hyperedge import *
from graph_orthogonality import *
from graph_contains import *
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


    self.obj28=Composite(self)
    self.obj28.isGraphObjectVisual = True

    if(hasattr(self.obj28, '_setHierarchicalLink')):
      self.obj28._setHierarchicalLink(False)

    # auto_adjust
    self.obj28.auto_adjust.setValue((None, 1))
    self.obj28.auto_adjust.config = 0

    # name
    self.obj28.name.setValue('Chrono_On')

    # is_default
    self.obj28.is_default.setValue((None, 0))
    self.obj28.is_default.config = 0

    # visible
    self.obj28.visible.setValue((None, 1))
    self.obj28.visible.config = 0

    # exit_action
    self.obj28.exit_action.setValue('\n')
    self.obj28.exit_action.setHeight(15)

    # enter_action
    self.obj28.enter_action.setValue('\n')
    self.obj28.enter_action.setHeight(15)

    self.obj28.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(40.0,780.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,191.0,452.0,382.0,594.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='darkblue')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,191.0,445.0)
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
    self.obj28.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)
    self.obj28.postAction( rootNode.CREATE )

    self.obj29=Composite(self)
    self.obj29.isGraphObjectVisual = True

    if(hasattr(self.obj29, '_setHierarchicalLink')):
      self.obj29._setHierarchicalLink(False)

    # auto_adjust
    self.obj29.auto_adjust.setValue((None, 1))
    self.obj29.auto_adjust.config = 0

    # name
    self.obj29.name.setValue('Running')

    # is_default
    self.obj29.is_default.setValue((None, 1))
    self.obj29.is_default.config = 0

    # visible
    self.obj29.visible.setValue((None, 1))
    self.obj29.visible.config = 0

    # exit_action
    self.obj29.exit_action.setValue('\n')
    self.obj29.exit_action.setHeight(15)

    # enter_action
    self.obj29.enter_action.setValue('\n')
    self.obj29.enter_action.setHeight(15)

    self.obj29.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(760.0,240.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,142.0,68.0,928.0,404.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='darkgreen')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,142.0,61.0)
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
    self.obj29.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.obj29.postAction( rootNode.CREATE )

    self.obj30=Composite(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    # auto_adjust
    self.obj30.auto_adjust.setValue((None, 1))
    self.obj30.auto_adjust.config = 0

    # name
    self.obj30.name.setValue('Watch')

    # is_default
    self.obj30.is_default.setValue((None, 1))
    self.obj30.is_default.config = 0

    # visible
    self.obj30.visible.setValue((None, 1))
    self.obj30.visible.config = 0

    # exit_action
    self.obj30.exit_action.setValue('\n')
    self.obj30.exit_action.setHeight(15)

    # enter_action
    self.obj30.enter_action.setValue('\n')
    self.obj30.enter_action.setHeight(15)

    self.obj30.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(100.0,-20.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,63.0,30.0,1330.0,656.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='darkgreen')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,63.0,23.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Watch')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
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
    self.obj31.is_default.setValue((None, 1))
    self.obj31.is_default.config = 0

    # name
    self.obj31.name.setValue('Setup')

    # exit_action
    self.obj31.exit_action.setValue('\n')
    self.obj31.exit_action.setHeight(15)

    # enter_action
    self.obj31.enter_action.setValue('\n')
    self.obj31.enter_action.setHeight(15)

    self.obj31.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(20.0,40.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,32.0,43.0,50.0,61.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,35.125,32.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Setup')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font-158692372')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-8.0, -38.0]
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
    self.obj32.name.setValue('Stopped')

    # exit_action
    self.obj32.exit_action.setValue('\n')
    self.obj32.exit_action.setHeight(15)

    # enter_action
    self.obj32.enter_action.setValue('\n')
    self.obj32.enter_action.setHeight(15)

    self.obj32.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(1340.0,40.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,1352.0,43.0,1370.0,61.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,1372.125,32.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Stopped')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font-159188692')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, -38.0]
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
    self.obj33.is_default.setValue((None, 1))
    self.obj33.is_default.config = 0

    # name
    self.obj33.name.setValue('Indiglo_Off')

    # exit_action
    self.obj33.exit_action.setValue('\n')
    self.obj33.exit_action.setHeight(15)

    # enter_action
    self.obj33.enter_action.setValue('\n')
    self.obj33.enter_action.setHeight(15)

    self.obj33.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(1110.0,448.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,1122.0,451.0,1140.0,469.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,1069.125,481.0)
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
    self.obj34.name.setValue('Waiting')

    # exit_action
    self.obj34.exit_action.setValue('\n')
    self.obj34.exit_action.setHeight(15)

    # enter_action
    self.obj34.enter_action.setValue('\n')
    self.obj34.enter_action.setHeight(15)

    self.obj34.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(1230.0,508.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,1242.0,511.0,1260.0,529.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,1253.125,538.0)
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
    self.obj35.name.setValue('Pressed')

    # exit_action
    self.obj35.exit_action.setValue('\n')
    self.obj35.exit_action.setHeight(15)

    # enter_action
    self.obj35.enter_action.setValue('\n')
    self.obj35.enter_action.setHeight(15)

    self.obj35.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(1214.0,436.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,1226.0,439.0,1244.0,457.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,1282.125,433.0)
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
    self.obj36.is_default.setValue((None, 1))
    self.obj36.is_default.config = 0

    # name
    self.obj36.name.setValue('Update')

    # exit_action
    self.obj36.exit_action.setValue('\n')
    self.obj36.exit_action.setHeight(15)

    # enter_action
    self.obj36.enter_action.setValue('\n')
    self.obj36.enter_action.setHeight(15)

    self.obj36.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(1060.0,100.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,1072.0,103.0,1090.0,121.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,1126.125,113.0)
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
    self.obj37.name.setValue('Wait')

    # exit_action
    self.obj37.exit_action.setValue('\n')
    self.obj37.exit_action.setHeight(15)

    # enter_action
    self.obj37.enter_action.setValue('\n')
    self.obj37.enter_action.setHeight(15)

    self.obj37.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(954.0,184.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,966.0,187.0,984.0,205.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,977.125,214.0)
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
    self.obj38.is_default.setValue((None, 1))
    self.obj38.is_default.config = 0

    # name
    self.obj38.name.setValue('Reset')

    # exit_action
    self.obj38.exit_action.setValue('\n')
    self.obj38.exit_action.setHeight(15)

    # enter_action
    self.obj38.enter_action.setValue('\n')
    self.obj38.enter_action.setHeight(15)

    self.obj38.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(460.0,500.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,486.11684572,510.233875745,489.71684572,513.833875745)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,506.74184572,497.033875745)
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
    self.obj39.is_default.setValue((None, 1))
    self.obj39.is_default.config = 0

    # name
    self.obj39.name.setValue('Running')

    # exit_action
    self.obj39.exit_action.setValue('\n')
    self.obj39.exit_action.setHeight(15)

    # enter_action
    self.obj39.enter_action.setValue('\n')
    self.obj39.enter_action.setHeight(15)

    self.obj39.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(240.0,500.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,264.420442476,506.16969697,268.020442476,509.76969697)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,232.045442476,524.96969697)
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
    self.obj40.name.setValue('Paused')

    # exit_action
    self.obj40.exit_action.setValue('\n')
    self.obj40.exit_action.setHeight(15)

    # enter_action
    self.obj40.enter_action.setValue('\n')
    self.obj40.enter_action.setHeight(15)

    self.obj40.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(300.0,560.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,321.642932861,566.491521912,325.242932861,570.091521912)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,331.467932861,581.491521912)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Paused')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font183405612')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
       new_obj.layConstraints['Label Offset'] = [38.0, -4.0]
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
    self.obj41.is_default.setValue((None, 1))
    self.obj41.is_default.config = 0

    # name
    self.obj41.name.setValue('Time')

    # exit_action
    self.obj41.exit_action.setValue('\n')
    self.obj41.exit_action.setHeight(15)

    # enter_action
    self.obj41.enter_action.setValue('\n')
    self.obj41.enter_action.setHeight(15)

    self.obj41.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(420.0,100.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,432.0,103.0,450.0,121.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,415.125,91.0)
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
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=Basic(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # is_default
    self.obj42.is_default.setValue((None, 0))
    self.obj42.is_default.config = 0

    # name
    self.obj42.name.setValue('Chrono')

    # exit_action
    self.obj42.exit_action.setValue('\n')
    self.obj42.exit_action.setHeight(15)

    # enter_action
    self.obj42.enter_action.setValue('\n')
    self.obj42.enter_action.setHeight(15)

    self.obj42.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(680.0,120.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,692.0,123.0,710.0,141.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,694.125,108.0)
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
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=Basic(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # is_default
    self.obj43.is_default.setValue((None, 0))
    self.obj43.is_default.config = 0

    # name
    self.obj43.name.setValue('View Alarm')

    # exit_action
    self.obj43.exit_action.setValue('\n')
    self.obj43.exit_action.setHeight(15)

    # enter_action
    self.obj43.enter_action.setValue('\n')
    self.obj43.enter_action.setHeight(15)

    self.obj43.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(220.0,200.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,232.0,203.0,250.0,221.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,202.125,223.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='View Alarm')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font158345068')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-41.0, -7.0]
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
    self.obj44.name.setValue('Time_Edit')

    # exit_action
    self.obj44.exit_action.setValue('\n')
    self.obj44.exit_action.setHeight(15)

    # enter_action
    self.obj44.enter_action.setValue('\n')
    self.obj44.enter_action.setHeight(15)

    self.obj44.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(520.0,220.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,532.0,223.0,550.0,241.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,476.125,242.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Time_Edit')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font188099372')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-67.0, -8.0]
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
    self.obj45.name.setValue('Next_Select_Time')

    # exit_action
    self.obj45.exit_action.setValue('\n')
    self.obj45.exit_action.setHeight(15)

    # enter_action
    self.obj45.enter_action.setValue('\n')
    self.obj45.enter_action.setHeight(15)

    self.obj45.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(760.0,280.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,772.0,283.0,790.0,301.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,842.125,272.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Next_Select_Time')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font192455436')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [59.0, -38.0]
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
    self.obj46.is_default.setValue((None, 0))
    self.obj46.is_default.config = 0

    # name
    self.obj46.name.setValue('Time Edit')

    # exit_action
    self.obj46.exit_action.setValue('\n')
    self.obj46.exit_action.setHeight(15)

    # enter_action
    self.obj46.enter_action.setValue('\n')
    self.obj46.enter_action.setHeight(15)

    self.obj46.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(500.0,260.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,512.0,263.0,530.0,281.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,474.125,285.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Time Edit')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font196507788')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-49.0, -5.0]
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
    self.obj47.name.setValue('Alarm Edit')

    # exit_action
    self.obj47.exit_action.setValue('\n')
    self.obj47.exit_action.setHeight(15)

    # enter_action
    self.obj47.enter_action.setValue('\n')
    self.obj47.enter_action.setHeight(15)

    self.obj47.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(200.0,340.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,212.0,343.0,230.0,361.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,223.125,370.0)
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
    self.obj48.is_default.setValue((None, 0))
    self.obj48.is_default.config = 0

    # name
    self.obj48.name.setValue('Next_Select_Alarm')

    # exit_action
    self.obj48.exit_action.setValue('\n')
    self.obj48.exit_action.setHeight(15)

    # enter_action
    self.obj48.enter_action.setValue('\n')
    self.obj48.enter_action.setHeight(15)

    self.obj48.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(340.0,220.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,352.0,223.0,370.0,241.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,385.125,213.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Next_Select_Alarm')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font192455436')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [22.0, -37.0]
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
    self.obj49.name.setValue('Alarm Increase')

    # exit_action
    self.obj49.exit_action.setValue('\n')
    self.obj49.exit_action.setHeight(15)

    # enter_action
    self.obj49.enter_action.setValue('\n')
    self.obj49.enter_action.setHeight(15)

    self.obj49.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(340.0,280.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,352.0,283.0,370.0,301.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,436.125,307.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarm Increase')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font201886988')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [73.0, -3.0]
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
    self.obj50.name.setValue('Alarm Increase Auto')

    # exit_action
    self.obj50.exit_action.setValue('\n')
    self.obj50.exit_action.setHeight(15)

    # enter_action
    self.obj50.enter_action.setValue('\n')
    self.obj50.enter_action.setHeight(15)

    self.obj50.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(320.0,360.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,332.0,363.0,350.0,381.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,343.125,390.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarm Increase Auto')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font201844652')
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
    self.obj51.name.setValue('Time Increase')

    # exit_action
    self.obj51.exit_action.setValue('\n')
    self.obj51.exit_action.setHeight(15)

    # enter_action
    self.obj51.enter_action.setValue('\n')
    self.obj51.enter_action.setHeight(15)

    self.obj51.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(500.0,360.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,512.0,363.0,530.0,381.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,523.125,390.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Time Increase')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font204031404')
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

    self.obj52=Basic(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # is_default
    self.obj52.is_default.setValue((None, 0))
    self.obj52.is_default.config = 0

    # name
    self.obj52.name.setValue('Time Increase Auto')

    # exit_action
    self.obj52.exit_action.setValue('\n')
    self.obj52.exit_action.setHeight(15)

    # enter_action
    self.obj52.enter_action.setValue('\n')
    self.obj52.enter_action.setHeight(15)

    self.obj52.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(680.0,340.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,692.0,343.0,710.0,361.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,712.125,374.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Time Increase Auto')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font204114444')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [9.0, 4.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=Basic(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # is_default
    self.obj53.is_default.setValue((None, 1))
    self.obj53.is_default.config = 0

    # name
    self.obj53.name.setValue('Alarm Off')

    # exit_action
    self.obj53.exit_action.setValue('\n')
    self.obj53.exit_action.setHeight(15)

    # enter_action
    self.obj53.enter_action.setValue('\n')
    self.obj53.enter_action.setHeight(15)

    self.obj53.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(980.0,300.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,992.0,303.0,1010.0,321.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,1003.125,330.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarm Off')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font149664140')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=Basic(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # is_default
    self.obj54.is_default.setValue((None, 0))
    self.obj54.is_default.config = 0

    # name
    self.obj54.name.setValue('Light On')

    # exit_action
    self.obj54.exit_action.setValue('\n')
    self.obj54.exit_action.setHeight(15)

    # enter_action
    self.obj54.enter_action.setValue('\n')
    self.obj54.enter_action.setHeight(15)

    self.obj54.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(1100.0,260.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,1112.0,263.0,1130.0,281.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,1126.125,253.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Light On')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font220429900')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [3.0, -37.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=Basic(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # is_default
    self.obj55.is_default.setValue((None, 0))
    self.obj55.is_default.config = 0

    # name
    self.obj55.name.setValue('Light Off')

    # exit_action
    self.obj55.exit_action.setValue('\n')
    self.obj55.exit_action.setHeight(15)

    # enter_action
    self.obj55.enter_action.setValue('\n')
    self.obj55.enter_action.setHeight(15)

    self.obj55.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(1140.0,300.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,1152.0,303.0,1170.0,321.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,1183.125,340.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Light Off')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font220479596')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [20.0, 10.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=Basic(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # is_default
    self.obj56.is_default.setValue((None, 0))
    self.obj56.is_default.config = 0

    # name
    self.obj56.name.setValue('Alarming')

    # exit_action
    self.obj56.exit_action.setValue('\n')
    self.obj56.exit_action.setHeight(15)

    # enter_action
    self.obj56.enter_action.setValue('[DUMP("ALARM RUNNING")]\n')
    self.obj56.enter_action.setHeight(15)

    self.obj56.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(860.0,520.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,872.0,523.0,890.0,541.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,883.125,550.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarming')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font232681004')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=Basic(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # is_default
    self.obj57.is_default.setValue((None, 1))
    self.obj57.is_default.config = 0

    # name
    self.obj57.name.setValue('Alarm Unset')

    # exit_action
    self.obj57.exit_action.setValue('\n')
    self.obj57.exit_action.setHeight(15)

    # enter_action
    self.obj57.enter_action.setValue('[DUMP("ALARM UNSET")]\n')
    self.obj57.enter_action.setHeight(15)

    self.obj57.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(620.0,460.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,632.0,463.0,650.0,481.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,645.125,454.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarm Unset')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font232707532')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [2.0, -36.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=Basic(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # is_default
    self.obj58.is_default.setValue((None, 0))
    self.obj58.is_default.config = 0

    # name
    self.obj58.name.setValue('Alarm Set')

    # exit_action
    self.obj58.exit_action.setValue('\n')
    self.obj58.exit_action.setHeight(15)

    # enter_action
    self.obj58.enter_action.setValue('[DUMP("ALARM SET")]\n')
    self.obj58.enter_action.setHeight(15)

    self.obj58.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(640.0,560.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,652.0,563.0,670.0,581.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,663.125,590.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarm Set')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font233451564')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=Orthogonal(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # visible
    self.obj59.visible.setValue((None, 1))
    self.obj59.visible.config = 0

    # name
    self.obj59.name.setValue('Indiglo')

    # auto_adjust
    self.obj59.auto_adjust.setValue((None, 1))
    self.obj59.auto_adjust.config = 0

    self.obj59.graphClass_= graph_Orthogonal
    if self.genGraphics:
       new_obj = graph_Orthogonal(1040.0,340.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,1008.0,400.0,1323.0,551.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,1024.0,390.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Indiglo')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [14.639999999999933, 11.569999999999943]
       new_obj.layConstraints['Label Offset'] = [46.0, 10.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=Orthogonal(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # visible
    self.obj60.visible.setValue((None, 1))
    self.obj60.visible.config = 0

    # name
    self.obj60.name.setValue('Clock State')

    # auto_adjust
    self.obj60.auto_adjust.setValue((None, 1))
    self.obj60.auto_adjust.config = 0

    self.obj60.graphClass_= graph_Orthogonal
    if self.genGraphics:
       new_obj = graph_Orthogonal(860.0,60.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,951.0,52.0,1162.0,227.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,979.0,44.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Clock State')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [48.010000000000197, 3.5899999999999412]
       new_obj.layConstraints['Label Offset'] = [88.0, 6.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=Orthogonal(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # visible
    self.obj61.visible.setValue((None, 1))
    self.obj61.visible.config = 0

    # name
    self.obj61.name.setValue('Chrono State')

    # auto_adjust
    self.obj61.auto_adjust.setValue((None, 1))
    self.obj61.auto_adjust.config = 0

    self.obj61.graphClass_= graph_Orthogonal
    if self.genGraphics:
       new_obj = graph_Orthogonal(40.0,380.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,153.0,433.0,542.0,601.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,157.0,422.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Chrono State')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [70.140000000000498, 11.019999999999978]
       new_obj.layConstraints['Label Offset'] = [91.0, 25.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=Orthogonal(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # visible
    self.obj62.visible.setValue((None, 1))
    self.obj62.visible.config = 0

    # name
    self.obj62.name.setValue('Alarm State')

    # auto_adjust
    self.obj62.auto_adjust.setValue((None, 1))
    self.obj62.auto_adjust.config = 0

    self.obj62.graphClass_= graph_Orthogonal
    if self.genGraphics:
       new_obj = graph_Orthogonal(560.0,560.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,564.0,441.0,992.0,649.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,595.0,426.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarm State')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [5.3899999999999961, 3.9500000000000024]
       new_obj.layConstraints['Label Offset'] = [64.0, 3.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=Orthogonal(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # visible
    self.obj63.visible.setValue((None, 1))
    self.obj63.visible.config = 0

    # name
    self.obj63.name.setValue('Watch_Running')

    # auto_adjust
    self.obj63.auto_adjust.setValue((None, 1))
    self.obj63.auto_adjust.config = 0

    self.obj63.graphClass_= graph_Orthogonal
    if self.genGraphics:
       new_obj = graph_Orthogonal(900.0,120.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,113.0,49.0,935.0,411.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,113.0,42.0)
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
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=Orthogonal(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # visible
    self.obj64.visible.setValue((None, 1))
    self.obj64.visible.config = 0

    # name
    self.obj64.name.setValue('Alarming State')

    # auto_adjust
    self.obj64.auto_adjust.setValue((None, 1))
    self.obj64.auto_adjust.config = 0

    self.obj64.graphClass_= graph_Orthogonal
    if self.genGraphics:
       new_obj = graph_Orthogonal(940.0,220.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf5.handler,952.0,239.0,1234.0,353.0)
       self.UMLmodel.itemconfig(new_obj.gf5.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, outline='darkgray')
       self.UMLmodel.itemconfig(new_obj.gf5.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,985.0,233.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Alarming State')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [33.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=contains(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    self.obj65.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(428.747046664,1405.10386365,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=contains(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    self.obj66.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(435.935903088,1332.80314775,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj67=contains(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    self.obj67.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(926.31331479,751.940906201,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=contains(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    self.obj68.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(825.00095547,682.482510187,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=contains(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    self.obj69.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(1673.09711907,-265.41406502,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=contains(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    self.obj70.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(1483.00095547,-259.01748981,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=contains(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    self.obj71.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(2251.90288582,517.511654259,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=contains(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    self.obj72.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(2225.13829048,507.443472332,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=contains(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    self.obj73.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(2139.90317276,501.21762454,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=contains(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    self.obj74.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(248.28301645,268.943472332,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=contains(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    self.obj75.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(424.28301645,158.443472332,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=contains(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    self.obj76.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(640.78301645,188.943472332,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=contains(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    self.obj77.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(912.5,399.5,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj78=contains(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    self.obj78.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(523.78301645,369.443472332,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj79=contains(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    self.obj79.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(571.989668321,377.71762454,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj80=contains(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    self.obj80.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(439.903172764,377.71762454,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=contains(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    self.obj81.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(439.903172764,347.71762454,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=contains(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    self.obj82.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(216.873982293,281.084048042,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj83=contains(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    self.obj83.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(264.505748984,235.03909536,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj84=contains(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    self.obj84.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(505.917954699,329.98103148,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj85=contains(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    self.obj85.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(748.000955474,254.982510187,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=contains(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    self.obj86.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(1767.98966832,-243.28237546,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj87=contains(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    self.obj87.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(1948.37398229,-268.915951958,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj88=contains(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    self.obj88.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(1999.08874976,-222.98771852,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=contains(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    self.obj89.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(795.989668321,402.71762454,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj90=contains(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    self.obj90.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(611.460104451,212.247395833,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=contains(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    self.obj91.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(544.005748984,306.03909536,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj92=Hyperedge(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(False)

    # name
    self.obj92.name.setValue('')
    self.obj92.name.setNone()

    # broadcast
    self.obj92.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj92.broadcast.setHeight(15)

    # guard
    self.obj92.guard.setValue('1')

    # trigger
    self.obj92.trigger.setValue('topRightPressed')

    # action
    self.obj92.action.setValue('[DUMP("controller.setIndiglo()")]\ncontroller.setIndiglo()\n')
    self.obj92.action.setHeight(15)

    # broadcast_to
    self.obj92.broadcast_to.setValue('')
    self.obj92.broadcast_to.setNone()

    # display
    self.obj92.display.setValue('TRP / setIndiglo()')

    self.obj92.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(1176.00191095,424.965020373,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-21.0, -20.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj93=Hyperedge(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(False)

    # name
    self.obj93.name.setValue('')
    self.obj93.name.setNone()

    # broadcast
    self.obj93.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj93.broadcast.setHeight(15)

    # guard
    self.obj93.guard.setValue('1')

    # trigger
    self.obj93.trigger.setValue('AFTER(3)')

    # action
    self.obj93.action.setValue('[DUMP("controller.unsetIndiglo()")]\ncontroller.unsetIndiglo()\n')
    self.obj93.action.setHeight(15)

    # broadcast_to
    self.obj93.broadcast_to.setValue('')
    self.obj93.broadcast_to.setNone()

    # display
    self.obj93.display.setValue('tm(3) / unsetIndiglo()')

    self.obj93.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(1159.34320001,518.619791667,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-41.0, 8.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj94=Hyperedge(self)
    self.obj94.isGraphObjectVisual = True

    if(hasattr(self.obj94, '_setHierarchicalLink')):
      self.obj94._setHierarchicalLink(False)

    # name
    self.obj94.name.setValue('')
    self.obj94.name.setNone()

    # broadcast
    self.obj94.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj94.broadcast.setHeight(15)

    # guard
    self.obj94.guard.setValue('1')

    # trigger
    self.obj94.trigger.setValue('topRightReleased')

    # action
    self.obj94.action.setValue('[DUMP("Indiglo:  3 seconds till light off.")]\n')
    self.obj94.action.setHeight(15)

    # broadcast_to
    self.obj94.broadcast_to.setValue('')
    self.obj94.broadcast_to.setNone()

    # display
    self.obj94.display.setValue('TRR')

    self.obj94.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(1212.0,484.0,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-44.0, -15.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj94.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)
    self.obj94.postAction( rootNode.CREATE )

    self.obj95=Hyperedge(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(False)

    # name
    self.obj95.name.setValue('')
    self.obj95.name.setNone()

    # broadcast
    self.obj95.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj95.broadcast.setHeight(15)

    # guard
    self.obj95.guard.setValue('1')

    # trigger
    self.obj95.trigger.setValue('topRightPressed')

    # action
    self.obj95.action.setValue('[DUMP("Indiglo:  Back to pressed state.")]\n')
    self.obj95.action.setHeight(15)

    # broadcast_to
    self.obj95.broadcast_to.setValue('')
    self.obj95.broadcast_to.setNone()

    # display
    self.obj95.display.setValue('TRP')

    self.obj95.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(1270.0,469.0,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-9.0, -6.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj96=Hyperedge(self)
    self.obj96.isGraphObjectVisual = True

    if(hasattr(self.obj96, '_setHierarchicalLink')):
      self.obj96._setHierarchicalLink(False)

    # name
    self.obj96.name.setValue('')
    self.obj96.name.setNone()

    # broadcast
    self.obj96.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj96.broadcast.setHeight(15)

    # guard
    self.obj96.guard.setValue('1')

    # trigger
    self.obj96.trigger.setValue('timePause')

    # action
    self.obj96.action.setValue('[DUMP("Clock State: Edit Time.")]\n')
    self.obj96.action.setHeight(15)

    # broadcast_to
    self.obj96.broadcast_to.setValue('')
    self.obj96.broadcast_to.setNone()

    # display
    self.obj96.display.setValue('timePause')

    self.obj96.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(999.745614758,147.654452512,self.obj96)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-34.0, -33.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj96.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj96)
    self.globalAndLocalPostcondition(self.obj96, rootNode)
    self.obj96.postAction( rootNode.CREATE )

    self.obj97=Hyperedge(self)
    self.obj97.isGraphObjectVisual = True

    if(hasattr(self.obj97, '_setHierarchicalLink')):
      self.obj97._setHierarchicalLink(False)

    # name
    self.obj97.name.setValue('')
    self.obj97.name.setNone()

    # broadcast
    self.obj97.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj97.broadcast.setHeight(15)

    # guard
    self.obj97.guard.setValue('1')

    # trigger
    self.obj97.trigger.setValue('timeStart')

    # action
    self.obj97.action.setValue('[DUMP("Clock State: Update time.")]\n')
    self.obj97.action.setHeight(15)

    # broadcast_to
    self.obj97.broadcast_to.setValue('')
    self.obj97.broadcast_to.setNone()

    # display
    self.obj97.display.setValue('timeStart')

    self.obj97.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(1040.7309946,190.74938483,self.obj97)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-4.0, 1.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj97.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj97)
    self.globalAndLocalPostcondition(self.obj97, rootNode)
    self.obj97.postAction( rootNode.CREATE )

    self.obj98=Hyperedge(self)
    self.obj98.isGraphObjectVisual = True

    if(hasattr(self.obj98, '_setHierarchicalLink')):
      self.obj98._setHierarchicalLink(False)

    # name
    self.obj98.name.setValue('')
    self.obj98.name.setNone()

    # broadcast
    self.obj98.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj98.broadcast.setHeight(15)

    # guard
    self.obj98.guard.setValue('1')

    # trigger
    self.obj98.trigger.setValue('AFTER(1)')

    # action
    self.obj98.action.setValue('[DUMP("controller.increaseTimeByOne()")]\ncontroller.increaseTimeByOne()\n')
    self.obj98.action.setHeight(15)

    # broadcast_to
    self.obj98.broadcast_to.setValue('')
    self.obj98.broadcast_to.setNone()

    # display
    self.obj98.display.setValue('tm(1) / increaseTimeByOne()')

    self.obj98.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(1053.6,71.0,self.obj98)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-13.0, -14.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj98.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj98)
    self.globalAndLocalPostcondition(self.obj98, rootNode)
    self.obj98.postAction( rootNode.CREATE )

    self.obj99=Hyperedge(self)
    self.obj99.isGraphObjectVisual = True

    if(hasattr(self.obj99, '_setHierarchicalLink')):
      self.obj99._setHierarchicalLink(False)

    # name
    self.obj99.name.setValue('')
    self.obj99.name.setNone()

    # broadcast
    self.obj99.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj99.broadcast.setHeight(15)

    # guard
    self.obj99.guard.setValue('1')

    # trigger
    self.obj99.trigger.setValue('toggleChrono')

    # action
    self.obj99.action.setValue('[DUMP("Chrono:  Paused")]\n')
    self.obj99.action.setHeight(15)

    # broadcast_to
    self.obj99.broadcast_to.setValue('')
    self.obj99.broadcast_to.setNone()

    # display
    self.obj99.display.setValue('chrono')

    self.obj99.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(304.199250501,535.057293934,self.obj99)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-15.0, -21.0]
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
    else: new_obj = None
    self.obj99.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj99)
    self.globalAndLocalPostcondition(self.obj99, rootNode)
    self.obj99.postAction( rootNode.CREATE )

    self.obj100=Hyperedge(self)
    self.obj100.isGraphObjectVisual = True

    if(hasattr(self.obj100, '_setHierarchicalLink')):
      self.obj100._setHierarchicalLink(False)

    # name
    self.obj100.name.setValue('')
    self.obj100.name.setNone()

    # broadcast
    self.obj100.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj100.broadcast.setHeight(15)

    # guard
    self.obj100.guard.setValue('1')

    # trigger
    self.obj100.trigger.setValue('toggleChrono')

    # action
    self.obj100.action.setValue('[DUMP("Chrono:  Running")]\n')
    self.obj100.action.setHeight(15)

    # broadcast_to
    self.obj100.broadcast_to.setValue('')
    self.obj100.broadcast_to.setNone()

    # display
    self.obj100.display.setValue('chrono')

    self.obj100.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(288.574777308,547.636034727,self.obj100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-52.0, -2.0]
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
    else: new_obj = None
    self.obj100.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj100)
    self.globalAndLocalPostcondition(self.obj100, rootNode)
    self.obj100.postAction( rootNode.CREATE )

    self.obj101=Hyperedge(self)
    self.obj101.isGraphObjectVisual = True

    if(hasattr(self.obj101, '_setHierarchicalLink')):
      self.obj101._setHierarchicalLink(False)

    # name
    self.obj101.name.setValue('')
    self.obj101.name.setNone()

    # broadcast
    self.obj101.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj101.broadcast.setHeight(15)

    # guard
    self.obj101.guard.setValue('1')

    # trigger
    self.obj101.trigger.setValue('AFTER(0.01)')

    # action
    self.obj101.action.setValue('[DUMP("controller.increaseChronoByOne()")]\ncontroller.increaseChronoByOne()\n[EVENT("chronoDisplay")]\n')
    self.obj101.action.setHeight(15)

    # broadcast_to
    self.obj101.broadcast_to.setValue('')
    self.obj101.broadcast_to.setNone()

    # display
    self.obj101.display.setValue('tm(0.01) / increaseChronoByOne(), chronoDisplay')

    self.obj101.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(203.177499517,476.02456296,self.obj101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [72.0, -14.0]
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
    else: new_obj = None
    self.obj101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj101)
    self.globalAndLocalPostcondition(self.obj101, rootNode)
    self.obj101.postAction( rootNode.CREATE )

    self.obj102=Hyperedge(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    # name
    self.obj102.name.setValue('')
    self.obj102.name.setNone()

    # broadcast
    self.obj102.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj102.broadcast.setHeight(15)

    # guard
    self.obj102.guard.setValue('1')

    # trigger
    self.obj102.trigger.setValue('resetChrono')

    # action
    self.obj102.action.setValue('[DUMP("controller.resetChrono()")]\ncontroller.resetChrono()\n[EVENT("chronoDisplay")]\n')
    self.obj102.action.setHeight(15)

    # broadcast_to
    self.obj102.broadcast_to.setValue('')
    self.obj102.broadcast_to.setNone()

    # display
    self.obj102.display.setValue('resetChrono / resetChrono(), chronoDisplay')

    self.obj102.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(441.75217561,530.698160088,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-8.0, 5.0]
       new_obj.layConstraints['scale'] = [0.20000000000000001, 0.20000000000000001]
    else: new_obj = None
    self.obj102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)
    self.obj102.postAction( rootNode.CREATE )

    self.obj103=Hyperedge(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(False)

    # name
    self.obj103.name.setValue('')
    self.obj103.name.setNone()

    # broadcast
    self.obj103.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj103.broadcast.setHeight(15)

    # guard
    self.obj103.guard.setValue('1')

    # trigger
    self.obj103.trigger.setValue('topLeftPressed')

    # action
    self.obj103.action.setValue('[DUMP("controller.refreshChronoDisplay()")]\ncontroller.refreshChronoDisplay()\n')
    self.obj103.action.setHeight(15)

    # broadcast_to
    self.obj103.broadcast_to.setValue('')
    self.obj103.broadcast_to.setNone()

    # display
    self.obj103.display.setValue('TLP / refreshChronoDisplay()')

    self.obj103.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(549.006704458,103.021605547,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-29.0, -17.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    self.obj104=Hyperedge(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    # name
    self.obj104.name.setValue('')
    self.obj104.name.setNone()

    # broadcast
    self.obj104.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj104.broadcast.setHeight(15)

    # guard
    self.obj104.guard.setValue('1')

    # trigger
    self.obj104.trigger.setValue('chronoDisplay')

    # action
    self.obj104.action.setValue('[DUMP("controller.refreshChronoDisplay()")]\ncontroller.refreshChronoDisplay()\n')
    self.obj104.action.setHeight(15)

    # broadcast_to
    self.obj104.broadcast_to.setValue('')
    self.obj104.broadcast_to.setNone()

    # display
    self.obj104.display.setValue('chronoDisplay / refreshChronoDisplay()')

    self.obj104.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(663.28301645,187.943472332,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [2.0, 2.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj105=Hyperedge(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # name
    self.obj105.name.setValue('')
    self.obj105.name.setNone()

    # broadcast
    self.obj105.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj105.broadcast.setHeight(15)

    # guard
    self.obj105.guard.setValue('1')

    # trigger
    self.obj105.trigger.setValue('bottomRightPressed')

    # action
    self.obj105.action.setValue('[DUMP("Event: chrono")]\n[EVENT("toggleChrono")]\n')
    self.obj105.action.setHeight(15)

    # broadcast_to
    self.obj105.broadcast_to.setValue('')
    self.obj105.broadcast_to.setNone()

    # display
    self.obj105.display.setValue('BRP / chrono')

    self.obj105.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(763.5,113.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-38.0, -23.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=Hyperedge(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    # name
    self.obj106.name.setValue('')
    self.obj106.name.setNone()

    # broadcast
    self.obj106.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj106.broadcast.setHeight(15)

    # guard
    self.obj106.guard.setValue('1')

    # trigger
    self.obj106.trigger.setValue('bottomLeftPressed')

    # action
    self.obj106.action.setValue('[DUMP("Event: resetChrono")]\n[EVENT("resetChrono")]\n')
    self.obj106.action.setHeight(15)

    # broadcast_to
    self.obj106.broadcast_to.setValue('')
    self.obj106.broadcast_to.setNone()

    # display
    self.obj106.display.setValue('BLP / resetChrono')

    self.obj106.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(748.0,179.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [19.0, -28.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj107=Hyperedge(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    # name
    self.obj107.name.setValue('')
    self.obj107.name.setNone()

    # broadcast
    self.obj107.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj107.broadcast.setHeight(15)

    # guard
    self.obj107.guard.setValue('1')

    # trigger
    self.obj107.trigger.setValue('topLeftPressed')

    # action
    self.obj107.action.setValue('[DUMP("controller.refreshTimeDisplay()")]\ncontroller.refreshTimeDisplay()\ncontroller.refreshDateDisplay()\n')
    self.obj107.action.setHeight(15)

    # broadcast_to
    self.obj107.broadcast_to.setValue('')
    self.obj107.broadcast_to.setNone()

    # display
    self.obj107.display.setValue('TLP / refreshTimeDisplay()')

    self.obj107.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(517.204460874,131.12835995,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [10.0, 9.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj108=Hyperedge(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    # name
    self.obj108.name.setValue('')
    self.obj108.name.setNone()

    # broadcast
    self.obj108.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj108.broadcast.setHeight(15)

    # guard
    self.obj108.guard.setValue('1')

    # trigger
    self.obj108.trigger.setValue('bottomLeftPressed')

    # action
    self.obj108.action.setValue('[DUMP("controller.refreshAlarmDisplay()")]\ncontroller.refreshAlarmDisplay()\n[DUMP("Event: setAlarm")]\n[EVENT("setAlarm")]\n')
    self.obj108.action.setHeight(15)

    # broadcast_to
    self.obj108.broadcast_to.setValue('')
    self.obj108.broadcast_to.setNone()

    # display
    self.obj108.display.setValue('BLP / refreshAlarmDisplay(), setAlarm')

    self.obj108.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(204.828499371,115.513760187,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [57.0, -29.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=Hyperedge(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # name
    self.obj109.name.setValue('')
    self.obj109.name.setNone()

    # broadcast
    self.obj109.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj109.broadcast.setHeight(15)

    # guard
    self.obj109.guard.setValue('1')

    # trigger
    self.obj109.trigger.setValue('bottomLeftReleased')

    # action
    self.obj109.action.setValue('[DUMP("controller.refreshTimeDisplay()")]\ncontroller.refreshTimeDisplay()\ncontroller.refreshDateDisplay()\n')
    self.obj109.action.setHeight(15)

    # broadcast_to
    self.obj109.broadcast_to.setValue('')
    self.obj109.broadcast_to.setNone()

    # display
    self.obj109.display.setValue('BLR / refreshTimeDisplay()')

    self.obj109.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(240.006704458,126.99331296,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [32.0, 17.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=Hyperedge(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # name
    self.obj110.name.setValue('')
    self.obj110.name.setNone()

    # broadcast
    self.obj110.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj110.broadcast.setHeight(15)

    # guard
    self.obj110.guard.setValue('1')

    # trigger
    self.obj110.trigger.setValue('bottomRightPressed')

    # action
    self.obj110.action.setValue('[DUMP("Pending time edit mode")]\n')
    self.obj110.action.setHeight(15)

    # broadcast_to
    self.obj110.broadcast_to.setValue('')
    self.obj110.broadcast_to.setNone()

    # display
    self.obj110.display.setValue('BRP')

    self.obj110.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(481.949772771,213.965020373,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-16.0, -19.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=Hyperedge(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # name
    self.obj111.name.setValue('')
    self.obj111.name.setNone()

    # broadcast
    self.obj111.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj111.broadcast.setHeight(15)

    # guard
    self.obj111.guard.setValue('1')

    # trigger
    self.obj111.trigger.setValue('bottomRightReleased')

    # action
    self.obj111.action.setValue('[DUMP("Time Mode")]\ncontroller.refreshTimeDisplay()\ncontroller.refreshDateDisplay()\n')
    self.obj111.action.setHeight(15)

    # broadcast_to
    self.obj111.broadcast_to.setValue('')
    self.obj111.broadcast_to.setNone()

    # display
    self.obj111.display.setValue('BRR')

    self.obj111.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(530.949772771,206.965020373,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-11.0, -10.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    self.obj112=Hyperedge(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    # name
    self.obj112.name.setValue('')
    self.obj112.name.setNone()

    # broadcast
    self.obj112.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj112.broadcast.setHeight(15)

    # guard
    self.obj112.guard.setValue('1')

    # trigger
    self.obj112.trigger.setValue('AFTER(2)')

    # action
    self.obj112.action.setValue('[DUMP("controller.refreshTimeDisplay()")]\ncontroller.stopSelection()\ncontroller.refreshTimeDisplay()\ncontroller.refreshDateDisplay()\n[DUMP("Event: startTime")]\n[EVENT("startTime")]\n')
    self.obj112.action.setHeight(15)

    # broadcast_to
    self.obj112.broadcast_to.setValue('')
    self.obj112.broadcast_to.setNone()

    # display
    self.obj112.display.setValue('tm(2) / refreshDisplay(), timeStart')

    self.obj112.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(610.006704458,228.99331296,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [76.0, -6.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj113=Hyperedge(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    # name
    self.obj113.name.setValue('')
    self.obj113.name.setNone()

    # broadcast
    self.obj113.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj113.broadcast.setHeight(15)

    # guard
    self.obj113.guard.setValue('1')

    # trigger
    self.obj113.trigger.setValue('AFTER(1.5)')

    # action
    self.obj113.action.setValue('[DUMP("controller.startSelection()")]\ncontroller.startSelection()\n')
    self.obj113.action.setHeight(15)

    # broadcast_to
    self.obj113.broadcast_to.setValue('')
    self.obj113.broadcast_to.setNone()

    # display
    self.obj113.display.setValue('tm(1.5) / startSelection()')

    self.obj113.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(184.006704458,281.99331296,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj114=Hyperedge(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # name
    self.obj114.name.setValue('')
    self.obj114.name.setNone()

    # broadcast
    self.obj114.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj114.broadcast.setHeight(15)

    # guard
    self.obj114.guard.setValue('1')

    # trigger
    self.obj114.trigger.setValue('AFTER(2)')

    # action
    self.obj114.action.setValue('[DUMP("controller.refreshTimeDisplay()")]\ncontroller.stopSelection()\ncontroller.refreshTimeDisplay()\ncontroller.refreshDateDisplay()\n[DUMP("Event: startTime")]\n[EVENT("startTime")]\n')
    self.obj114.action.setHeight(15)

    # broadcast_to
    self.obj114.broadcast_to.setValue('')
    self.obj114.broadcast_to.setNone()

    # display
    self.obj114.display.setValue('tm(2) / refreshDisplay(), timeStart')

    self.obj114.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(400.949772771,171.965020373,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj115=Hyperedge(self)
    self.obj115.isGraphObjectVisual = True

    if(hasattr(self.obj115, '_setHierarchicalLink')):
      self.obj115._setHierarchicalLink(False)

    # name
    self.obj115.name.setValue('')
    self.obj115.name.setNone()

    # broadcast
    self.obj115.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj115.broadcast.setHeight(15)

    # guard
    self.obj115.guard.setValue('1')

    # trigger
    self.obj115.trigger.setValue('bottomRightPressed')

    # action
    self.obj115.action.setValue('\n')
    self.obj115.action.setHeight(15)

    # broadcast_to
    self.obj115.broadcast_to.setValue('')
    self.obj115.broadcast_to.setNone()

    # display
    self.obj115.display.setValue('BRP')

    self.obj115.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(285.949772771,246.965020373,self.obj115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.11
       new_obj.layConstraints['Label Offset'] = [-39.0, -14.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115)
    self.globalAndLocalPostcondition(self.obj115, rootNode)
    self.obj115.postAction( rootNode.CREATE )

    self.obj116=Hyperedge(self)
    self.obj116.isGraphObjectVisual = True

    if(hasattr(self.obj116, '_setHierarchicalLink')):
      self.obj116._setHierarchicalLink(False)

    # name
    self.obj116.name.setValue('')
    self.obj116.name.setNone()

    # broadcast
    self.obj116.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj116.broadcast.setHeight(15)

    # guard
    self.obj116.guard.setValue('1')

    # trigger
    self.obj116.trigger.setValue('bottomRightReleased')

    # action
    self.obj116.action.setValue('[DUMP("controller.nextSelection()")]\ncontroller.selectNext()\ncontroller.refreshAlarmDisplay()\n')
    self.obj116.action.setHeight(15)

    # broadcast_to
    self.obj116.broadcast_to.setValue('')
    self.obj116.broadcast_to.setNone()

    # display
    self.obj116.display.setValue('BRR')

    self.obj116.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(344.949772771,263.965020373,self.obj116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-54.0, -2.0]
    else: new_obj = None
    self.obj116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj116)
    self.globalAndLocalPostcondition(self.obj116, rootNode)
    self.obj116.postAction( rootNode.CREATE )

    self.obj117=Hyperedge(self)
    self.obj117.isGraphObjectVisual = True

    if(hasattr(self.obj117, '_setHierarchicalLink')):
      self.obj117._setHierarchicalLink(False)

    # name
    self.obj117.name.setValue('')
    self.obj117.name.setNone()

    # broadcast
    self.obj117.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj117.broadcast.setHeight(15)

    # guard
    self.obj117.guard.setValue('1')

    # trigger
    self.obj117.trigger.setValue('bottomRightPressed')

    # action
    self.obj117.action.setValue('\n')
    self.obj117.action.setHeight(15)

    # broadcast_to
    self.obj117.broadcast_to.setValue('')
    self.obj117.broadcast_to.setNone()

    # display
    self.obj117.display.setValue('BRP')

    self.obj117.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(611.7431209,262.690868165,self.obj117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-6.0, 5.0]
       new_obj.layConstraints['scale'] = [1.2299999999999998, 1.240000000000004]
    else: new_obj = None
    self.obj117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj117)
    self.globalAndLocalPostcondition(self.obj117, rootNode)
    self.obj117.postAction( rootNode.CREATE )

    self.obj118=Hyperedge(self)
    self.obj118.isGraphObjectVisual = True

    if(hasattr(self.obj118, '_setHierarchicalLink')):
      self.obj118._setHierarchicalLink(False)

    # name
    self.obj118.name.setValue('')
    self.obj118.name.setNone()

    # broadcast
    self.obj118.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj118.broadcast.setHeight(15)

    # guard
    self.obj118.guard.setValue('1')

    # trigger
    self.obj118.trigger.setValue('bottomRightReleased')

    # action
    self.obj118.action.setValue('[DUMP("controller.nextSelection()")]\ncontroller.selectNext()\ncontroller.refreshTimeDisplay()\ncontroller.refreshDateDisplay()\n')
    self.obj118.action.setHeight(15)

    # broadcast_to
    self.obj118.broadcast_to.setValue('')
    self.obj118.broadcast_to.setNone()

    # display
    self.obj118.display.setValue('BRR')

    self.obj118.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(553.7431209,285.690868165,self.obj118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [5.0, 3.0]
    else: new_obj = None
    self.obj118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj118)
    self.globalAndLocalPostcondition(self.obj118, rootNode)
    self.obj118.postAction( rootNode.CREATE )

    self.obj119=Hyperedge(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    # name
    self.obj119.name.setValue('')
    self.obj119.name.setNone()

    # broadcast
    self.obj119.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj119.broadcast.setHeight(15)

    # guard
    self.obj119.guard.setValue('1')

    # trigger
    self.obj119.trigger.setValue('AFTER(1.5)')

    # action
    self.obj119.action.setValue('[DUMP("controller.startSelection()")]\ncontroller.startSelection()\n[EVENT("timePause")]\n')
    self.obj119.action.setHeight(15)

    # broadcast_to
    self.obj119.broadcast_to.setValue('')
    self.obj119.broadcast_to.setNone()

    # display
    self.obj119.display.setValue('tm(1.5) / startSelection()')

    self.obj119.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(529.074772771,253.027520373,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [43.0, -4.0]
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj120=Hyperedge(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # name
    self.obj120.name.setValue('')
    self.obj120.name.setNone()

    # broadcast
    self.obj120.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj120.broadcast.setHeight(15)

    # guard
    self.obj120.guard.setValue('1')

    # trigger
    self.obj120.trigger.setValue('bottomLeftPressed')

    # action
    self.obj120.action.setValue('[DUMP("controller.increaseSelection()")]\ncontroller.increaseSelection()\ncontroller.refreshAlarmDisplay()\n')
    self.obj120.action.setHeight(15)

    # broadcast_to
    self.obj120.broadcast_to.setValue('')
    self.obj120.broadcast_to.setNone()

    # display
    self.obj120.display.setValue('BLP')

    self.obj120.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(311.949772771,301.965020373,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-29.0, 7.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj121=Hyperedge(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # name
    self.obj121.name.setValue('')
    self.obj121.name.setNone()

    # broadcast
    self.obj121.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj121.broadcast.setHeight(15)

    # guard
    self.obj121.guard.setValue('1')

    # trigger
    self.obj121.trigger.setValue('AFTER(2)')

    # action
    self.obj121.action.setValue('[DUMP("controller.increaseSelection()")]\ncontroller.increaseSelection()\ncontroller.refreshAlarmDisplay()\n')
    self.obj121.action.setHeight(15)

    # broadcast_to
    self.obj121.broadcast_to.setValue('')
    self.obj121.broadcast_to.setNone()

    # display
    self.obj121.display.setValue('tm(2)')

    self.obj121.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(361.006704458,321.99331296,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-17.0, 9.0]
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj122=Hyperedge(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(False)

    # name
    self.obj122.name.setValue('')
    self.obj122.name.setNone()

    # broadcast
    self.obj122.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj122.broadcast.setHeight(15)

    # guard
    self.obj122.guard.setValue('1')

    # trigger
    self.obj122.trigger.setValue('AFTER(0.25)')

    # action
    self.obj122.action.setValue('[DUMP("controller.increaseSelection()")]\ncontroller.increaseSelection()\ncontroller.refreshAlarmDisplay()\n')
    self.obj122.action.setHeight(15)

    # broadcast_to
    self.obj122.broadcast_to.setValue('')
    self.obj122.broadcast_to.setNone()

    # display
    self.obj122.display.setValue('tm(0.25)')

    self.obj122.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(426.500955474,380.982510187,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-7.0, -16.0]
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    self.obj123=Hyperedge(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # name
    self.obj123.name.setValue('')
    self.obj123.name.setNone()

    # broadcast
    self.obj123.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj123.broadcast.setHeight(15)

    # guard
    self.obj123.guard.setValue('1')

    # trigger
    self.obj123.trigger.setValue('bottomLeftReleased')

    # action
    self.obj123.action.setValue('\n')
    self.obj123.action.setHeight(15)

    # broadcast_to
    self.obj123.broadcast_to.setValue('')
    self.obj123.broadcast_to.setNone()

    # display
    self.obj123.display.setValue('BLR')

    self.obj123.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(311.006704458,342.021605547,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-38.0, 7.0]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=Hyperedge(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # name
    self.obj124.name.setValue('')
    self.obj124.name.setNone()

    # broadcast
    self.obj124.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj124.broadcast.setHeight(15)

    # guard
    self.obj124.guard.setValue('1')

    # trigger
    self.obj124.trigger.setValue('bottomLeftReleased')

    # action
    self.obj124.action.setValue('\n')
    self.obj124.action.setHeight(15)

    # broadcast_to
    self.obj124.broadcast_to.setValue('')
    self.obj124.broadcast_to.setNone()

    # display
    self.obj124.display.setValue('BLR')

    self.obj124.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(315.949772771,324.965020373,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-9.0, -6.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj125=Hyperedge(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # name
    self.obj125.name.setValue('')
    self.obj125.name.setNone()

    # broadcast
    self.obj125.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj125.broadcast.setHeight(15)

    # guard
    self.obj125.guard.setValue('1')

    # trigger
    self.obj125.trigger.setValue('bottomLeftPressed')

    # action
    self.obj125.action.setValue('[DUMP("controller.increaseSelection()")]\ncontroller.increaseSelection()\ncontroller.refreshTimeDisplay()\ncontroller.refreshDateDisplay()\n')
    self.obj125.action.setHeight(15)

    # broadcast_to
    self.obj125.broadcast_to.setValue('')
    self.obj125.broadcast_to.setNone()

    # display
    self.obj125.display.setValue('BLP')

    self.obj125.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(496.490623794,331.200134727,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-44.0, -9.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj126=Hyperedge(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # name
    self.obj126.name.setValue('')
    self.obj126.name.setNone()

    # broadcast
    self.obj126.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj126.broadcast.setHeight(15)

    # guard
    self.obj126.guard.setValue('1')

    # trigger
    self.obj126.trigger.setValue('bottomLeftReleased')

    # action
    self.obj126.action.setValue('\n')
    self.obj126.action.setHeight(15)

    # broadcast_to
    self.obj126.broadcast_to.setValue('')
    self.obj126.broadcast_to.setNone()

    # display
    self.obj126.display.setValue('BLR')

    self.obj126.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(537.490623794,343.200134727,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-7.0, -4.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj127=Hyperedge(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    # name
    self.obj127.name.setValue('')
    self.obj127.name.setNone()

    # broadcast
    self.obj127.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj127.broadcast.setHeight(15)

    # guard
    self.obj127.guard.setValue('1')

    # trigger
    self.obj127.trigger.setValue('AFTER(2)')

    # action
    self.obj127.action.setValue('[DUMP("controller.increaseSelected()")]\ncontroller.increaseSelected()\ncontroller.refreshTimeDisplay()\ncontroller.refreshDateDisplay()\n')
    self.obj127.action.setHeight(15)

    # broadcast_to
    self.obj127.broadcast_to.setValue('')
    self.obj127.broadcast_to.setNone()

    # display
    self.obj127.display.setValue('tm(2)')

    self.obj127.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(550.074772771,376.027520373,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj128=Hyperedge(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    # name
    self.obj128.name.setValue('')
    self.obj128.name.setNone()

    # broadcast
    self.obj128.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj128.broadcast.setHeight(15)

    # guard
    self.obj128.guard.setValue('1')

    # trigger
    self.obj128.trigger.setValue('AFTER(0.25)')

    # action
    self.obj128.action.setValue('[DUMP("controller.increaseSelected()")]\ncontroller.increaseSelected()\ncontroller.refreshTimeDisplay()\ncontroller.refreshDateDisplay()\n')
    self.obj128.action.setHeight(15)

    # broadcast_to
    self.obj128.broadcast_to.setValue('')
    self.obj128.broadcast_to.setNone()

    # display
    self.obj128.display.setValue('tm(0.25)')

    self.obj128.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(791.460104451,353.247395833,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=Hyperedge(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # name
    self.obj129.name.setValue('')
    self.obj129.name.setNone()

    # broadcast
    self.obj129.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj129.broadcast.setHeight(15)

    # guard
    self.obj129.guard.setValue('1')

    # trigger
    self.obj129.trigger.setValue('bottomLeftReleased')

    # action
    self.obj129.action.setValue('\n')
    self.obj129.action.setHeight(15)

    # broadcast_to
    self.obj129.broadcast_to.setValue('')
    self.obj129.broadcast_to.setNone()

    # display
    self.obj129.display.setValue('BLR')

    self.obj129.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(590.012272771,346.027520373,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-12.0, -16.0]
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=Hyperedge(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    # name
    self.obj130.name.setValue('')
    self.obj130.name.setNone()

    # broadcast
    self.obj130.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj130.broadcast.setHeight(15)

    # guard
    self.obj130.guard.setValue('1')

    # trigger
    self.obj130.trigger.setValue('AFTER(1)')

    # action
    self.obj130.action.setValue('[DUMP("controller.refreshDisplay()")]\ncontroller.refreshTimeDisplay()\ncontroller.refreshDateDisplay()\n')
    self.obj130.action.setHeight(15)

    # broadcast_to
    self.obj130.broadcast_to.setValue('')
    self.obj130.broadcast_to.setNone()

    # display
    self.obj130.display.setValue('tm(1)')

    self.obj130.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(460.000955474,77.4825101866,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-9.0, -4.0]
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj131=Hyperedge(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    # name
    self.obj131.name.setValue('')
    self.obj131.name.setNone()

    # broadcast
    self.obj131.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj131.broadcast.setHeight(15)

    # guard
    self.obj131.guard.setValue('1')

    # trigger
    self.obj131.trigger.setValue('toggleChrono')

    # action
    self.obj131.action.setValue('\n')
    self.obj131.action.setHeight(15)

    # broadcast_to
    self.obj131.broadcast_to.setValue('')
    self.obj131.broadcast_to.setNone()

    # display
    self.obj131.display.setValue('toggleChrono')

    self.obj131.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(413.05957266,514.024756945,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-17.0, -18.0]
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=Hyperedge(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    # name
    self.obj132.name.setValue('')
    self.obj132.name.setNone()

    # broadcast
    self.obj132.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj132.broadcast.setHeight(15)

    # guard
    self.obj132.guard.setValue('1')

    # trigger
    self.obj132.trigger.setValue('start')

    # action
    self.obj132.action.setValue('[DUMP("Starting Watch")]\ncontroller=[PARAMS]\n')
    self.obj132.action.setHeight(15)

    # broadcast_to
    self.obj132.broadcast_to.setValue('')
    self.obj132.broadcast_to.setNone()

    # display
    self.obj132.display.setValue('start')

    self.obj132.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(46.4179546989,97.98103148,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj133=Hyperedge(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    # name
    self.obj133.name.setValue('')
    self.obj133.name.setNone()

    # broadcast
    self.obj133.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj133.broadcast.setHeight(15)

    # guard
    self.obj133.guard.setValue('1')

    # trigger
    self.obj133.trigger.setValue('stop')

    # action
    self.obj133.action.setValue('[DUMP("Stopping watch")]\n')
    self.obj133.action.setHeight(15)

    # broadcast_to
    self.obj133.broadcast_to.setValue('')
    self.obj133.broadcast_to.setNone()

    # display
    self.obj133.display.setValue('stop')

    self.obj133.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(1351.48966832,142.71762454,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj134=Hyperedge(self)
    self.obj134.isGraphObjectVisual = True

    if(hasattr(self.obj134, '_setHierarchicalLink')):
      self.obj134._setHierarchicalLink(False)

    # name
    self.obj134.name.setValue('')
    self.obj134.name.setNone()

    # broadcast
    self.obj134.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj134.broadcast.setHeight(15)

    # guard
    self.obj134.guard.setValue('1')

    # trigger
    self.obj134.trigger.setValue('AFTER(5)')

    # action
    self.obj134.action.setValue('controller.stopSelection()\ncontroller.refreshDateDisplay()\ncontroller.refreshTimeDisplay()\n')
    self.obj134.action.setHeight(15)

    # broadcast_to
    self.obj134.broadcast_to.setValue('')
    self.obj134.broadcast_to.setNone()

    # display
    self.obj134.display.setValue('tm(5)')

    self.obj134.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(272.949772771,185.965020373,self.obj134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj134)
    self.globalAndLocalPostcondition(self.obj134, rootNode)
    self.obj134.postAction( rootNode.CREATE )

    self.obj135=Hyperedge(self)
    self.obj135.isGraphObjectVisual = True

    if(hasattr(self.obj135, '_setHierarchicalLink')):
      self.obj135._setHierarchicalLink(False)

    # name
    self.obj135.name.setValue('')
    self.obj135.name.setNone()

    # broadcast
    self.obj135.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj135.broadcast.setHeight(15)

    # guard
    self.obj135.guard.setValue('1')

    # trigger
    self.obj135.trigger.setValue('AFTER(5)')

    # action
    self.obj135.action.setValue('controller.stopSelection()\ncontroller.refreshDateDisplay()\ncontroller.refreshTimeDisplay()\n')
    self.obj135.action.setHeight(15)

    # broadcast_to
    self.obj135.broadcast_to.setValue('')
    self.obj135.broadcast_to.setNone()

    # display
    self.obj135.display.setValue('tm(5)')

    self.obj135.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(409.012272771,273.027520373,self.obj135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-39.0, -12.0]
    else: new_obj = None
    self.obj135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj135)
    self.globalAndLocalPostcondition(self.obj135, rootNode)
    self.obj135.postAction( rootNode.CREATE )

    self.obj136=Hyperedge(self)
    self.obj136.isGraphObjectVisual = True

    if(hasattr(self.obj136, '_setHierarchicalLink')):
      self.obj136._setHierarchicalLink(False)

    # name
    self.obj136.name.setValue('')
    self.obj136.name.setNone()

    # broadcast
    self.obj136.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj136.broadcast.setHeight(15)

    # guard
    self.obj136.guard.setValue('1')

    # trigger
    self.obj136.trigger.setValue('AFTER(0.25)')

    # action
    self.obj136.action.setValue('controller.unsetIndiglo()\n')
    self.obj136.action.setHeight(15)

    # broadcast_to
    self.obj136.broadcast_to.setValue('')
    self.obj136.broadcast_to.setNone()

    # display
    self.obj136.display.setValue('tm(0.5)')

    self.obj136.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(1152.77715506,285.301672581,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-6.0, -13.0]
    else: new_obj = None
    self.obj136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)
    self.obj136.postAction( rootNode.CREATE )

    self.obj137=Hyperedge(self)
    self.obj137.isGraphObjectVisual = True

    if(hasattr(self.obj137, '_setHierarchicalLink')):
      self.obj137._setHierarchicalLink(False)

    # name
    self.obj137.name.setValue('')
    self.obj137.name.setNone()

    # broadcast
    self.obj137.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj137.broadcast.setHeight(15)

    # guard
    self.obj137.guard.setValue('1')

    # trigger
    self.obj137.trigger.setValue('AFTER(0.25)')

    # action
    self.obj137.action.setValue('controller.setIndiglo()\n')
    self.obj137.action.setHeight(15)

    # broadcast_to
    self.obj137.broadcast_to.setValue('')
    self.obj137.broadcast_to.setNone()

    # display
    self.obj137.display.setValue('tm(0.5)')

    self.obj137.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(1137.30989048,299.753368165,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-50.0, -8.0]
    else: new_obj = None
    self.obj137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)
    self.obj137.postAction( rootNode.CREATE )

    self.obj138=Hyperedge(self)
    self.obj138.isGraphObjectVisual = True

    if(hasattr(self.obj138, '_setHierarchicalLink')):
      self.obj138._setHierarchicalLink(False)

    # name
    self.obj138.name.setValue('')
    self.obj138.name.setNone()

    # broadcast
    self.obj138.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj138.broadcast.setHeight(15)

    # guard
    self.obj138.guard.setValue('1')

    # trigger
    self.obj138.trigger.setValue('alarmStop')

    # action
    self.obj138.action.setValue('[DUMP("Stop Alarm")]\n')
    self.obj138.action.setHeight(15)

    # broadcast_to
    self.obj138.broadcast_to.setValue('')
    self.obj138.broadcast_to.setNone()

    # display
    self.obj138.display.setValue('alarmStop')

    self.obj138.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(999.949772771,260.965020373,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-18.0, -17.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)
    self.obj138.postAction( rootNode.CREATE )

    self.obj139=Hyperedge(self)
    self.obj139.isGraphObjectVisual = True

    if(hasattr(self.obj139, '_setHierarchicalLink')):
      self.obj139._setHierarchicalLink(False)

    # name
    self.obj139.name.setValue('')
    self.obj139.name.setNone()

    # broadcast
    self.obj139.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj139.broadcast.setHeight(15)

    # guard
    self.obj139.guard.setValue('1')

    # trigger
    self.obj139.trigger.setValue('alarmStop')

    # action
    self.obj139.action.setValue('[DUMP("Stop Alarm")]\n')
    self.obj139.action.setHeight(15)

    # broadcast_to
    self.obj139.broadcast_to.setValue('')
    self.obj139.broadcast_to.setNone()

    # display
    self.obj139.display.setValue('alarmStop')

    self.obj139.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(1071.00670446,328.021605547,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-24.0, -21.0]
    else: new_obj = None
    self.obj139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)
    self.obj139.postAction( rootNode.CREATE )

    self.obj140=Hyperedge(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    # name
    self.obj140.name.setValue('')
    self.obj140.name.setNone()

    # broadcast
    self.obj140.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj140.broadcast.setHeight(15)

    # guard
    self.obj140.guard.setValue('1')

    # trigger
    self.obj140.trigger.setValue('alarmStart')

    # action
    self.obj140.action.setValue('controller.setIndiglo()\n')
    self.obj140.action.setHeight(15)

    # broadcast_to
    self.obj140.broadcast_to.setValue('')
    self.obj140.broadcast_to.setNone()

    # display
    self.obj140.display.setValue('alarmStart')

    self.obj140.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(1060.94977277,291.965020373,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-48.0, -16.0]
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj141=Hyperedge(self)
    self.obj141.isGraphObjectVisual = True

    if(hasattr(self.obj141, '_setHierarchicalLink')):
      self.obj141._setHierarchicalLink(False)

    # name
    self.obj141.name.setValue('')
    self.obj141.name.setNone()

    # broadcast
    self.obj141.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj141.broadcast.setHeight(15)

    # guard
    self.obj141.guard.setValue('1')

    # trigger
    self.obj141.trigger.setValue('setAlarm')

    # action
    self.obj141.action.setValue('[DUMP("controller.setAlarm()")]\ncontroller.setAlarm()\n')
    self.obj141.action.setHeight(15)

    # broadcast_to
    self.obj141.broadcast_to.setValue('')
    self.obj141.broadcast_to.setNone()

    # display
    self.obj141.display.setValue('setAlarm / setAlarm()')

    self.obj141.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(617.006704458,523.99331296,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-17.0, 20.0]
    else: new_obj = None
    self.obj141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)
    self.obj141.postAction( rootNode.CREATE )

    self.obj142=Hyperedge(self)
    self.obj142.isGraphObjectVisual = True

    if(hasattr(self.obj142, '_setHierarchicalLink')):
      self.obj142._setHierarchicalLink(False)

    # name
    self.obj142.name.setValue('')
    self.obj142.name.setNone()

    # broadcast
    self.obj142.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj142.broadcast.setHeight(15)

    # guard
    self.obj142.guard.setValue('1')

    # trigger
    self.obj142.trigger.setValue('alarmStart')

    # action
    self.obj142.action.setValue('\n')
    self.obj142.action.setHeight(15)

    # broadcast_to
    self.obj142.broadcast_to.setValue('')
    self.obj142.broadcast_to.setNone()

    # display
    self.obj142.display.setValue('alarmStart')

    self.obj142.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(809.006704458,607.021605547,self.obj142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj142)
    self.globalAndLocalPostcondition(self.obj142, rootNode)
    self.obj142.postAction( rootNode.CREATE )

    self.obj143=Hyperedge(self)
    self.obj143.isGraphObjectVisual = True

    if(hasattr(self.obj143, '_setHierarchicalLink')):
      self.obj143._setHierarchicalLink(False)

    # name
    self.obj143.name.setValue('')
    self.obj143.name.setNone()

    # broadcast
    self.obj143.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj143.broadcast.setHeight(15)

    # guard
    self.obj143.guard.setValue('1')

    # trigger
    self.obj143.trigger.setValue('AFTER(1)')

    # action
    self.obj143.action.setValue('[DUMP("controller.checkTime()")]\ncontroller.checkTime()\n')
    self.obj143.action.setHeight(15)

    # broadcast_to
    self.obj143.broadcast_to.setValue('')
    self.obj143.broadcast_to.setNone()

    # display
    self.obj143.display.setValue('tm(1) / checkTime()')

    self.obj143.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(708.138290478,629.943472332,self.obj143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj143.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj143)
    self.globalAndLocalPostcondition(self.obj143, rootNode)
    self.obj143.postAction( rootNode.CREATE )

    self.obj145=Hyperedge(self)
    self.obj145.isGraphObjectVisual = True

    if(hasattr(self.obj145, '_setHierarchicalLink')):
      self.obj145._setHierarchicalLink(False)

    # name
    self.obj145.name.setValue('')
    self.obj145.name.setNone()

    # broadcast
    self.obj145.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj145.broadcast.setHeight(15)

    # guard
    self.obj145.guard.setValue('1')

    # trigger
    self.obj145.trigger.setValue('AFTER(8)')

    # action
    self.obj145.action.setValue('[DUMP("Event: alarmStop")]\n[EVENT("alarmStop")]\n')
    self.obj145.action.setHeight(15)

    # broadcast_to
    self.obj145.broadcast_to.setValue('')
    self.obj145.broadcast_to.setNone()

    # display
    self.obj145.display.setValue('tm(8) / alarmStop')

    self.obj145.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(893.006704458,470.021605547,self.obj145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [18.0, -19.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj145)
    self.globalAndLocalPostcondition(self.obj145, rootNode)
    self.obj145.postAction( rootNode.CREATE )

    self.obj1170=Hyperedge(self)
    self.obj1170.isGraphObjectVisual = True

    if(hasattr(self.obj1170, '_setHierarchicalLink')):
      self.obj1170._setHierarchicalLink(False)

    # name
    self.obj1170.name.setValue('')
    self.obj1170.name.setNone()

    # broadcast
    self.obj1170.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj1170.broadcast.setHeight(15)

    # guard
    self.obj1170.guard.setValue('1')

    # trigger
    self.obj1170.trigger.setValue('topRightPressed')

    # action
    self.obj1170.action.setValue('[DUMP("Event: alarmStop")]\n[EVENT("alarmStop")]\n')
    self.obj1170.action.setHeight(15)

    # broadcast_to
    self.obj1170.broadcast_to.setValue('')
    self.obj1170.broadcast_to.setNone()

    # display
    self.obj1170.display.setValue('TRP / alarmStop')

    self.obj1170.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(790.006704458,487.021605547,self.obj1170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [14.0, -5.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1170)
    self.globalAndLocalPostcondition(self.obj1170, rootNode)
    self.obj1170.postAction( rootNode.CREATE )

    self.obj1173=Hyperedge(self)
    self.obj1173.isGraphObjectVisual = True

    if(hasattr(self.obj1173, '_setHierarchicalLink')):
      self.obj1173._setHierarchicalLink(False)

    # name
    self.obj1173.name.setValue('')
    self.obj1173.name.setNone()

    # broadcast
    self.obj1173.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj1173.broadcast.setHeight(15)

    # guard
    self.obj1173.guard.setValue('1')

    # trigger
    self.obj1173.trigger.setValue('setAlarm')

    # action
    self.obj1173.action.setValue('[DUMP("controller.setAlarm()")]\ncontroller.setAlarm()\n')
    self.obj1173.action.setHeight(15)

    # broadcast_to
    self.obj1173.broadcast_to.setValue('')
    self.obj1173.broadcast_to.setNone()

    # display
    self.obj1173.display.setValue('setAlarm / setAlarm()')

    self.obj1173.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(651.006704458,521.99331296,self.obj1173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [11.0, -16.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1173.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1173)
    self.globalAndLocalPostcondition(self.obj1173, rootNode)
    self.obj1173.postAction( rootNode.CREATE )

    self.obj1176=Hyperedge(self)
    self.obj1176.isGraphObjectVisual = True

    if(hasattr(self.obj1176, '_setHierarchicalLink')):
      self.obj1176._setHierarchicalLink(False)

    # name
    self.obj1176.name.setValue('')
    self.obj1176.name.setNone()

    # broadcast
    self.obj1176.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj1176.broadcast.setHeight(15)

    # guard
    self.obj1176.guard.setValue('1')

    # trigger
    self.obj1176.trigger.setValue('topLeftPressed')

    # action
    self.obj1176.action.setValue('[DUMP("Event: alarmStop")]\n[EVENT("alarmStop")]\n')
    self.obj1176.action.setHeight(15)

    # broadcast_to
    self.obj1176.broadcast_to.setValue('')
    self.obj1176.broadcast_to.setNone()

    # display
    self.obj1176.display.setValue('TLP / alarmStop')

    self.obj1176.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(714.006704458,564.021605547,self.obj1176)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1176.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1176)
    self.globalAndLocalPostcondition(self.obj1176, rootNode)
    self.obj1176.postAction( rootNode.CREATE )

    self.obj1183=Hyperedge(self)
    self.obj1183.isGraphObjectVisual = True

    if(hasattr(self.obj1183, '_setHierarchicalLink')):
      self.obj1183._setHierarchicalLink(False)

    # name
    self.obj1183.name.setValue('')
    self.obj1183.name.setNone()

    # broadcast
    self.obj1183.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj1183.broadcast.setHeight(15)

    # guard
    self.obj1183.guard.setValue('1')

    # trigger
    self.obj1183.trigger.setValue('bottomRightPressed')

    # action
    self.obj1183.action.setValue('[DUMP("Event: alarmStop")]\n[EVENT("alarmStop")]\n')
    self.obj1183.action.setHeight(15)

    # broadcast_to
    self.obj1183.broadcast_to.setValue('')
    self.obj1183.broadcast_to.setNone()

    # display
    self.obj1183.display.setValue('BRP / alarmStop')

    self.obj1183.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(735.006704458,539.021605547,self.obj1183)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1183.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1183)
    self.globalAndLocalPostcondition(self.obj1183, rootNode)
    self.obj1183.postAction( rootNode.CREATE )

    self.obj1187=Hyperedge(self)
    self.obj1187.isGraphObjectVisual = True

    if(hasattr(self.obj1187, '_setHierarchicalLink')):
      self.obj1187._setHierarchicalLink(False)

    # name
    self.obj1187.name.setValue('')
    self.obj1187.name.setNone()

    # broadcast
    self.obj1187.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj1187.broadcast.setHeight(15)

    # guard
    self.obj1187.guard.setValue('1')

    # trigger
    self.obj1187.trigger.setValue('bottomLeftPressed')

    # action
    self.obj1187.action.setValue('[DUMP("Event: alarmStop")]\n[EVENT("alarmStop")]\n')
    self.obj1187.action.setHeight(15)

    # broadcast_to
    self.obj1187.broadcast_to.setValue('')
    self.obj1187.broadcast_to.setNone()

    # display
    self.obj1187.display.setValue('BLP / alarmStop')

    self.obj1187.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(761.006704458,502.021605547,self.obj1187)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj1187.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj1187)
    self.globalAndLocalPostcondition(self.obj1187, rootNode)
    self.obj1187.postAction( rootNode.CREATE )

    self.obj146=orthogonality(self)
    self.obj146.isGraphObjectVisual = True

    if(hasattr(self.obj146, '_setHierarchicalLink')):
      self.obj146._setHierarchicalLink(False)

    self.obj146.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(92.0,60.5,self.obj146)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj146.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj146)
    self.globalAndLocalPostcondition(self.obj146, rootNode)
    self.obj146.postAction( rootNode.CREATE )

    self.obj147=orthogonality(self)
    self.obj147.isGraphObjectVisual = True

    if(hasattr(self.obj147, '_setHierarchicalLink')):
      self.obj147._setHierarchicalLink(False)

    self.obj147.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(127.5,325.5,self.obj147)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj147.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj147)
    self.globalAndLocalPostcondition(self.obj147, rootNode)
    self.obj147.postAction( rootNode.CREATE )

    self.obj148=orthogonality(self)
    self.obj148.isGraphObjectVisual = True

    if(hasattr(self.obj148, '_setHierarchicalLink')):
      self.obj148._setHierarchicalLink(False)

    self.obj148.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(306.5,256.0,self.obj148)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj148.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj148)
    self.globalAndLocalPostcondition(self.obj148, rootNode)
    self.obj148.postAction( rootNode.CREATE )

    self.obj149=orthogonality(self)
    self.obj149.isGraphObjectVisual = True

    if(hasattr(self.obj149, '_setHierarchicalLink')):
      self.obj149._setHierarchicalLink(False)

    self.obj149.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(239.0,411.5,self.obj149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj149)
    self.globalAndLocalPostcondition(self.obj149, rootNode)
    self.obj149.postAction( rootNode.CREATE )

    self.obj150=orthogonality(self)
    self.obj150.isGraphObjectVisual = True

    if(hasattr(self.obj150, '_setHierarchicalLink')):
      self.obj150._setHierarchicalLink(False)

    self.obj150.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(374.0,384.0,self.obj150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj150.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj150)
    self.globalAndLocalPostcondition(self.obj150, rootNode)
    self.obj150.postAction( rootNode.CREATE )

    self.obj151=orthogonality(self)
    self.obj151.isGraphObjectVisual = True

    if(hasattr(self.obj151, '_setHierarchicalLink')):
      self.obj151._setHierarchicalLink(False)

    self.obj151.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(89.0,415.0,self.obj151)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj151.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj151)
    self.globalAndLocalPostcondition(self.obj151, rootNode)
    self.obj151.postAction( rootNode.CREATE )

    self.obj152=orthogonality(self)
    self.obj152.isGraphObjectVisual = True

    if(hasattr(self.obj152, '_setHierarchicalLink')):
      self.obj152._setHierarchicalLink(False)

    self.obj152.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(89.0,415.0,self.obj152)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj152.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj152)
    self.globalAndLocalPostcondition(self.obj152, rootNode)
    self.obj152.postAction( rootNode.CREATE )

    self.obj153=orthogonality(self)
    self.obj153.isGraphObjectVisual = True

    if(hasattr(self.obj153, '_setHierarchicalLink')):
      self.obj153._setHierarchicalLink(False)

    self.obj153.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(89.0,415.0,self.obj153)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj153.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj153)
    self.globalAndLocalPostcondition(self.obj153, rootNode)
    self.obj153.postAction( rootNode.CREATE )

    self.obj154=orthogonality(self)
    self.obj154.isGraphObjectVisual = True

    if(hasattr(self.obj154, '_setHierarchicalLink')):
      self.obj154._setHierarchicalLink(False)

    self.obj154.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(89.0,415.0,self.obj154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj154)
    self.globalAndLocalPostcondition(self.obj154, rootNode)
    self.obj154.postAction( rootNode.CREATE )

    self.obj155=orthogonality(self)
    self.obj155.isGraphObjectVisual = True

    if(hasattr(self.obj155, '_setHierarchicalLink')):
      self.obj155._setHierarchicalLink(False)

    self.obj155.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(127.0,325.5,self.obj155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj155)
    self.globalAndLocalPostcondition(self.obj155, rootNode)
    self.obj155.postAction( rootNode.CREATE )

    self.obj156=orthogonality(self)
    self.obj156.isGraphObjectVisual = True

    if(hasattr(self.obj156, '_setHierarchicalLink')):
      self.obj156._setHierarchicalLink(False)

    self.obj156.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(373.5,384.0,self.obj156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj156)
    self.globalAndLocalPostcondition(self.obj156, rootNode)
    self.obj156.postAction( rootNode.CREATE )

    self.obj157=orthogonality(self)
    self.obj157.isGraphObjectVisual = True

    if(hasattr(self.obj157, '_setHierarchicalLink')):
      self.obj157._setHierarchicalLink(False)

    self.obj157.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(373.5,384.0,self.obj157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157)
    self.globalAndLocalPostcondition(self.obj157, rootNode)
    self.obj157.postAction( rootNode.CREATE )

    self.obj630=orthogonality(self)
    self.obj630.isGraphObjectVisual = True

    if(hasattr(self.obj630, '_setHierarchicalLink')):
      self.obj630._setHierarchicalLink(False)

    self.obj630.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(393.5,394.0,self.obj630)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj630.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj630)
    self.globalAndLocalPostcondition(self.obj630, rootNode)
    self.obj630.postAction( rootNode.CREATE )

    self.obj631=orthogonality(self)
    self.obj631.isGraphObjectVisual = True

    if(hasattr(self.obj631, '_setHierarchicalLink')):
      self.obj631._setHierarchicalLink(False)

    self.obj631.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(393.5,394.0,self.obj631)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj631.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj631)
    self.globalAndLocalPostcondition(self.obj631, rootNode)
    self.obj631.postAction( rootNode.CREATE )

    self.obj867=orthogonality(self)
    self.obj867.isGraphObjectVisual = True

    if(hasattr(self.obj867, '_setHierarchicalLink')):
      self.obj867._setHierarchicalLink(False)

    self.obj867.graphClass_= graph_orthogonality
    if self.genGraphics:
       new_obj = graph_orthogonality(393.5,394.0,self.obj867)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj867.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj867)
    self.globalAndLocalPostcondition(self.obj867, rootNode)
    self.obj867.postAction( rootNode.CREATE )

    # Connections for obj28 (graphObject_: Obj0) named Chrono_On
    self.drawConnections(
(self.obj28,self.obj102,[381.99999999999983, 523.0, 441.752175609993, 530.6981600879999],"bezier", 2),
(self.obj28,self.obj65,[285.99999999999966, 594.0, 428.7470466639997, 1405.10386365],"bezier", 2),
(self.obj28,self.obj66,[285.99999999999966, 594.0, 435.93590308799998, 1332.8031477499999],"bezier", 2) )
    # Connections for obj29 (graphObject_: Obj1) named Running
    self.drawConnections(
(self.obj29,self.obj74,[177.0, 236.0, 248.28301644978399, 268.94347233175597],"bezier", 2),
(self.obj29,self.obj75,[505.0, 69.0, 424.28301644978393, 158.44347233175608],"bezier", 2),
(self.obj29,self.obj76,[535.0, 68.0, 640.78301644999999, 188.94347233199997],"bezier", 2),
(self.obj29,self.obj78,[535.0, 404.0, 523.78301644999999, 369.443472332],"bezier", 2),
(self.obj29,self.obj79,[535.0, 404.0, 571.98966832099995, 377.71762453999997],"bezier", 2),
(self.obj29,self.obj80,[535.0, 404.0, 439.90317276399998, 377.71762453999997],"bezier", 2),
(self.obj29,self.obj81,[505.0, 404.0, 439.90317276396206, 347.71762453995785],"bezier", 2),
(self.obj29,self.obj82,[142.0, 236.0, 216.87398229299998, 281.08404804200001],"bezier", 2),
(self.obj29,self.obj83,[177.0, 236.0, 264.50574898404341, 235.03909536014723],"bezier", 2),
(self.obj29,self.obj84,[535.0, 404.0, 505.91795469899995, 329.98103148000001],"bezier", 2),
(self.obj29,self.obj85,[928.0, 236.0, 748.00095547371893, 254.98251018664564],"bezier", 2) )
    # Connections for obj30 (graphObject_: Obj2) named Watch
    self.drawConnections(
(self.obj30,self.obj146,[63.0, 342.99999999999994, 91.999999999999986, 60.5],"bezier", 2),
(self.obj30,self.obj147,[63.0, 342.99999999999994, 127.5, 325.49999999999994],"bezier", 2),
(self.obj30,self.obj148,[63.0, 342.99999999999994, 306.5, 256.0],"bezier", 2),
(self.obj30,self.obj149,[63.0, 342.99999999999994, 238.99999999999997, 411.5],"bezier", 2),
(self.obj30,self.obj150,[63.0, 342.99999999999994, 381.74999999999989, 416.74999999999989, 373.99999999999994, 384.0],"bezier", 3),
(self.obj30,self.obj133,[1330.0, 342.99999999999994, 1351.4896683205129, 142.717624539957],"bezier", 2),
(self.obj30,self.obj151,[63.0, 342.99999999999994, 89.0, 415.0],"bezier", 2),
(self.obj30,self.obj152,[63.0, 342.99999999999994, 89.0, 415.0],"bezier", 2),
(self.obj30,self.obj153,[63.0, 342.99999999999994, 89.0, 415.0],"bezier", 2),
(self.obj30,self.obj154,[63.0, 342.99999999999994, 89.0, 415.0],"bezier", 2),
(self.obj30,self.obj155,[63.0, 342.99999999999994, 126.99999999999999, 325.49999999999994],"bezier", 2),
(self.obj30,self.obj156,[63.0, 342.99999999999994, 373.49999999999994, 384.0],"bezier", 2),
(self.obj30,self.obj157,[63.0, 342.99999999999994, 373.49999999999994, 384.0],"bezier", 2),
(self.obj30,self.obj630,[63.0, 342.99999999999994, 393.49999999999994, 394.0],"bezier", 2),
(self.obj30,self.obj631,[63.0, 342.99999999999994, 393.49999999999994, 394.0],"bezier", 2),
(self.obj30,self.obj867,[63.0, 342.99999999999994, 393.49999999999994, 394.0],"bezier", 2) )
    # Connections for obj31 (graphObject_: Obj3) named Setup
    self.drawConnections(
(self.obj31,self.obj132,[40.835909397831792, 60.962062960042068, 46.417954698899997, 97.981031480000013],"bezier", 2) )
    # Connections for obj32 (graphObject_: Obj4) named Stopped
    self.drawConnections(
 )
    # Connections for obj33 (graphObject_: Obj5) named Indiglo_Off
    self.drawConnections(
(self.obj33,self.obj92,[1135.3335126426696, 452.04309608307005, 1149.9999999999993, 424.99999999999989, 1176.0019109474374, 424.96502037329128],"bezier", 3) )
    # Connections for obj34 (graphObject_: Obj6) named Waiting
    self.drawConnections(
(self.obj34,self.obj93,[1242.0114979680868, 520.07819072029451, 1185.9999999999993, 528.99999999999955, 1159.3432000143121, 518.61979166666606],"bezier", 3),
(self.obj34,self.obj95,[1255.3335126426696, 512.04309608307017, 1276.9999999999991, 484.99999999999989, 1269.9999999999989, 468.99999999999955],"bezier", 3) )
    # Connections for obj35 (graphObject_: Obj7) named Pressed
    self.drawConnections(
(self.obj35,self.obj94,[1226.9793366410265, 452.43524907991593, 1209.9999999999998, 457.99999999999989, 1211.9999999999986, 483.99999999999932],"bezier", 3) )
    # Connections for obj36 (graphObject_: Obj8) named Update
    self.drawConnections(
(self.obj36,self.obj96,[1072.0114979680868, 112.0781907202941, 1033.9999999999995, 118.99999999999771, 999.7456147580242, 147.65445251208052],"bezier", 3),
(self.obj36,self.obj98,[1073.3432000143134, 107.61979166666632, 1051.9999999999995, 95.999999999999559, 1053.5999999999999, 70.999999999999716],"bezier", 3) )
    # Connections for obj37 (graphObject_: Obj9) named Wait
    self.drawConnections(
(self.obj37,self.obj97,[982.8063455279239, 200.43524907991596, 1013.9999999999997, 207.99999999999943, 1040.7309945962388, 190.74938483035629],"bezier", 3) )
    # Connections for obj38 (graphObject_: Obj10) named Reset
    self.drawConnections(
(self.obj38,self.obj131,[486.11914531361685, 512.04951388905874, 413.05957265999996, 514.02475694499992],"bezier", 2) )
    # Connections for obj39 (graphObject_: Obj11) named Running
    self.drawConnections(
(self.obj39,self.obj99,[268.02082466548757, 507.96270104465799, 278.76742662622553, 509.55551564207877, 304.1992505009996, 535.05729393399997],"bezier", 3),
(self.obj39,self.obj101,[264.42274206961713, 507.9853351140589, 205.55151562099974, 501.3201622889996, 203.177499517, 476.02456295999986],"bezier", 3) )
    # Connections for obj40 (graphObject_: Obj12) named Paused
    self.drawConnections(
(self.obj40,self.obj100,[321.83880018920479, 569.17857172798324, 314.03785118289863, 573.13781301846484, 288.57477730799985, 547.63603472700004],"bezier", 3) )
    # Connections for obj41 (graphObject_: Obj13) named Time
    self.drawConnections(
(self.obj41,self.obj103,[450.00191094743781, 111.96502037329128, 489.99999999999989, 100.0, 549.00670445799994, 103.0216055468],"bezier", 3),
(self.obj41,self.obj108,[432.01149796808687, 112.07819072029432, 223.99999999999949, 93.999999999999943, 204.82849937144488, 115.51376018664565],"bezier", 3),
(self.obj41,self.obj110,[445.27658095602618, 119.88694466351211, 481.94977277100003, 213.96502037299999],"bezier", 2),
(self.obj41,self.obj130,[448.92020890121103, 107.49479166666657, 465.99999999999977, 96.0, 460.00095547371774, 77.482510186645584],"bezier", 3) )
    # Connections for obj42 (graphObject_: Obj14) named Chrono
    self.drawConnections(
(self.obj42,self.obj104,[696.56603289956809, 139.88694466351211, 686.99999999999977, 180.0, 663.28301644999999, 187.943472332],"bezier", 3),
(self.obj42,self.obj105,[710.00191094743798, 131.96502037329128, 761.9999999999992, 133.99999999999989, 763.49999999999989, 113.0],"bezier", 3),
(self.obj42,self.obj106,[705.27658095602601, 139.88694466351211, 716.99999999999977, 170.99999999999991, 748.0, 178.99999999999997],"bezier", 3),
(self.obj42,self.obj107,[692.01149796808693, 132.07819072029437, 558.00574898404341, 135.0390953601472, 517.20446087400001, 131.12835995],"bezier", 3) )
    # Connections for obj43 (graphObject_: Obj15) named View Alarm
    self.drawConnections(
(self.obj43,self.obj109,[245.3335126426694, 204.04309608307042, 195.99999999999972, 138.99999999999972, 240.00670445776211, 126.99331296004205],"bezier", 3),
(self.obj43,self.obj113,[236.56603289956794, 219.88694466351211, 184.00670445799966, 281.99331295999997],"bezier", 2) )
    # Connections for obj44 (graphObject_: Obj16) named Time_Edit
    self.drawConnections(
(self.obj44,self.obj111,[536.74796458621154, 224.16809608307048, 530.94977277099997, 206.96502037299999],"bezier", 2),
(self.obj44,self.obj119,[536.56603289956797, 239.88694466351214, 529.07477277099997, 253.02752037299999],"bezier", 2) )
    # Connections for obj45 (graphObject_: Obj17) named Next_Select_Time
    self.drawConnections(
(self.obj45,self.obj112,[773.34320001431377, 287.61979166666669, 610.00670445799994, 228.99331296],"bezier", 2),
(self.obj45,self.obj118,[772.01149796808681, 292.07819072029446, 553.74312089999989, 285.69086816499998],"bezier", 2) )
    # Connections for obj46 (graphObject_: Obj18) named Time Edit
    self.drawConnections(
(self.obj46,self.obj117,[528.92020890121103, 267.49479166666663, 611.74312089999978, 262.69086816499993],"bezier", 2),
(self.obj46,self.obj125,[516.56603289956809, 279.88694466351211, 496.49062379399982, 331.20013472699992],"bezier", 2),
(self.obj46,self.obj135,[512.01149796808681, 272.0781907202944, 409.01227277111786, 273.02752037329111],"bezier", 2) )
    # Connections for obj47 (graphObject_: Obj19) named Alarm Edit
    self.drawConnections(
(self.obj47,self.obj115,[225.33351264266952, 344.04309608307045, 285.94977277100003, 246.96502037299996],"bezier", 2),
(self.obj47,self.obj120,[228.92020890121108, 347.49479166666663, 311.94977277111877, 301.96502037329117],"bezier", 2),
(self.obj47,self.obj134,[225.33351264266952, 344.04309608307045, 272.94977277100003, 185.96502037299999],"bezier", 2) )
    # Connections for obj48 (graphObject_: Obj20) named Next_Select_Alarm
    self.drawConnections(
(self.obj48,self.obj114,[365.33351264266958, 224.04309608307051, 400.94977277111877, 171.96502037329134],"bezier", 2),
(self.obj48,self.obj116,[356.56603289956797, 239.88694466351214, 344.94977277100003, 263.96502037300002],"bezier", 2) )
    # Connections for obj49 (graphObject_: Obj21) named Alarm Increase
    self.drawConnections(
(self.obj49,self.obj121,[360.83590939783181, 300.96206296004203, 361.00670445776245, 321.99331296004198],"bezier", 2),
(self.obj49,self.obj124,[352.97933664102646, 296.43524907991571, 315.94977277100003, 324.96502037299996],"bezier", 2) )
    # Connections for obj50 (graphObject_: Obj22) named Alarm Increase Auto
    self.drawConnections(
(self.obj50,self.obj122,[350.00191094743792, 371.96502037329128, 425.50095547371876, 367.98251018664558, 426.50095547371882, 380.98251018664564],"bezier", 3),
(self.obj50,self.obj123,[336.74796458621142, 364.16809608307045, 311.006704458, 342.02160554699998],"bezier", 2) )
    # Connections for obj51 (graphObject_: Obj23) named Time Increase
    self.drawConnections(
(self.obj51,self.obj126,[525.33351264266958, 364.04309608307045, 537.49062379400004, 343.20013472699986],"bezier", 2),
(self.obj51,self.obj127,[530.00191094743798, 371.96502037329128, 550.07477277099997, 376.02752037300002],"bezier", 2) )
    # Connections for obj52 (graphObject_: Obj24) named Time Increase Auto
    self.drawConnections(
(self.obj52,self.obj128,[708.92020890121103, 347.49479166666663, 753.99999999999977, 335.99999999999977, 791.46010445100001, 353.24739583299993],"bezier", 3),
(self.obj52,self.obj129,[692.01149796808693, 352.0781907202944, 590.01227277099997, 346.02752037299996],"bezier", 2) )
    # Connections for obj53 (graphObject_: Obj25) named Alarm Off
    self.drawConnections(
(self.obj53,self.obj140,[1008.920208901211, 307.49479166666663, 1060.9497727711187, 291.96502037329128],"bezier", 2) )
    # Connections for obj54 (graphObject_: Obj26) named Light On
    self.drawConnections(
(self.obj54,self.obj136,[1128.8063455279241, 276.43524907991593, 1152.7771550570678, 285.30167258149254],"bezier", 2),
(self.obj54,self.obj138,[1112.0114979680868, 272.07819072029417, 999.94977277111855, 260.96502037329105],"bezier", 2) )
    # Connections for obj55 (graphObject_: Obj27) named Light Off
    self.drawConnections(
(self.obj55,self.obj137,[1153.3432000143137, 307.61979166666674, 1137.3098904851695, 299.75336816508843],"bezier", 2),
(self.obj55,self.obj139,[1152.0114979680868, 312.0781907202944, 1071.0067044577622, 328.02160554679187],"bezier", 2) )
    # Connections for obj56 (graphObject_: Obj28) named Alarming
    self.drawConnections(
(self.obj56,self.obj145,[881.17749951769304, 523.02456296004175, 893.00670445799597, 470.02160554699987],"bezier", 2),
(self.obj56,self.obj1170,[873.3432000143132, 527.61979166666674, 790.00670445776132, 487.02160554679244],"bezier", 2),
(self.obj56,self.obj1176,[872.01149796808681, 532.07819072029429, 714.00670445776109, 564.02160554679199],"bezier", 2),
(self.obj56,self.obj1183,[872.01149796808681, 532.07819072029429, 735.00670445775836, 539.02160554679199],"bezier", 2),
(self.obj56,self.obj1187,[872.01149796808681, 532.07819072029429, 761.00670445776245, 502.02160554679267],"bezier", 2) )
    # Connections for obj57 (graphObject_: Obj29) named Alarm Unset
    self.drawConnections(
(self.obj57,self.obj141,[636.56603289956797, 479.88694466351194, 617.00670445799994, 523.99331295999991],"bezier", 2) )
    # Connections for obj58 (graphObject_: Obj30) named Alarm Set
    self.drawConnections(
(self.obj58,self.obj142,[670.00191094743786, 571.96502037329128, 809.00670445799835, 607.02160554699981],"bezier", 2),
(self.obj58,self.obj143,[665.27658095602601, 579.88694466351217, 690.138290478013, 632.94347233175563, 708.13829047799993, 629.94347233200006],"bezier", 3),
(self.obj58,self.obj1173,[661.17749951769292, 563.02456296004175, 651.00670445776245, 521.99331296004186],"bezier", 2) )
    # Connections for obj59 (graphObject_: Obj31) named Indiglo
    self.drawConnections(
(self.obj59,self.obj71,[1323.0, 475.0, 2251.9028858168031, 517.51165425910517],"bezier", 2),
(self.obj59,self.obj72,[1323.0, 475.0, 2225.138290478013, 507.44347233175608],"bezier", 2),
(self.obj59,self.obj73,[1323.0, 475.0, 2139.9031727639999, 501.21762453999986],"bezier", 2) )
    # Connections for obj60 (graphObject_: Obj32) named Clock State
    self.drawConnections(
(self.obj60,self.obj69,[1161.9999999999998, 139.0, 1673.09711907, -265.41406501999995],"bezier", 2),
(self.obj60,self.obj70,[1161.9999999999998, 139.0, 1483.000955474, -259.01748980999992],"bezier", 2) )
    # Connections for obj61 (graphObject_: Obj33) named Chrono State
    self.drawConnections(
(self.obj61,self.obj67,[542.0, 517.0, 926.31331478999971, 751.94090620099973],"bezier", 2),
(self.obj61,self.obj68,[542.0, 517.0, 825.00095546999989, 682.48251018699989],"bezier", 2) )
    # Connections for obj62 (graphObject_: Obj34) named Alarm State
    self.drawConnections(
(self.obj62,self.obj89,[778.0, 441.0, 795.98966832099995, 402.71762453999997],"bezier", 2),
(self.obj62,self.obj90,[778.0, 441.0, 611.46010445100001, 212.24739583300001],"bezier", 2),
(self.obj62,self.obj91,[564.0, 545.0, 544.00574898399998, 306.03909536000003],"bezier", 2) )
    # Connections for obj63 (graphObject_: Obj35) named Watch_Running
    self.drawConnections(
(self.obj63,self.obj77,[658.0, 410.99999999999977, 912.5, 399.5],"bezier", 2) )
    # Connections for obj64 (graphObject_: Obj36) named Alarming State
    self.drawConnections(
(self.obj64,self.obj86,[1234.0, 296.0, 1767.9896683204997, -243.28237546000003],"bezier", 2),
(self.obj64,self.obj87,[1234.0, 296.0, 1948.3739822929997, -268.91595195800005],"bezier", 2),
(self.obj64,self.obj88,[1234.0, 296.0, 1999.0887497589997, -222.98771852000016],"bezier", 2) )
    # Connections for obj65 (graphObject_: Obj37) of type contains
    self.drawConnections(
(self.obj65,self.obj40,[428.7470466639997, 1405.10386365, 323.41011474056586, 570.08393450400843],"bezier", 2) )
    # Connections for obj66 (graphObject_: Obj38) of type contains
    self.drawConnections(
(self.obj66,self.obj39,[435.93590308799998, 1332.8031477499999, 266.18762435556636, 509.76210956200839],"bezier", 2) )
    # Connections for obj67 (graphObject_: Obj39) of type contains
    self.drawConnections(
(self.obj67,self.obj28,[926.31331478999971, 751.94090620099996, 382.0, 523.0],"bezier", 2) )
    # Connections for obj68 (graphObject_: Obj40) of type contains
    self.drawConnections(
(self.obj68,self.obj38,[825.00095546999989, 682.482510187, 489.47811482558473, 512.92092556098305],"bezier", 2) )
    # Connections for obj69 (graphObject_: Obj41) of type contains
    self.drawConnections(
(self.obj69,self.obj37,[1673.09711907, -265.41406501999995, 982.92020890121091, 191.49479166666674],"bezier", 2) )
    # Connections for obj70 (graphObject_: Obj42) of type contains
    self.drawConnections(
(self.obj70,self.obj36,[1483.000955474, -259.01748980999992, 1088.920208901211, 107.49479166666674],"bezier", 2) )
    # Connections for obj71 (graphObject_: Obj43) of type contains
    self.drawConnections(
(self.obj71,self.obj34,[2251.902885817, 517.5116542589999, 1260.0019109474379, 519.96502037329128],"bezier", 2) )
    # Connections for obj72 (graphObject_: Obj44) of type contains
    self.drawConnections(
(self.obj72,self.obj35,[2225.1382904780003, 507.44347233200006, 1244.0019109474376, 447.96502037329122],"bezier", 2) )
    # Connections for obj73 (graphObject_: Obj45) of type contains
    self.drawConnections(
(self.obj73,self.obj33,[2139.9031727639999, 501.21762453999986, 1140.0019109474379, 459.96502037329128],"bezier", 2) )
    # Connections for obj74 (graphObject_: Obj46) of type contains
    self.drawConnections(
(self.obj74,self.obj43,[248.28301644978399, 268.94347233175597, 240.83590939783173, 220.96206296004206],"bezier", 2) )
    # Connections for obj75 (graphObject_: Obj47) of type contains
    self.drawConnections(
(self.obj75,self.obj41,[424.28301644978393, 158.44347233175608, 436.56603289956797, 119.8869446635121],"bezier", 2) )
    # Connections for obj76 (graphObject_: Obj48) of type contains
    self.drawConnections(
(self.obj76,self.obj42,[640.78301644999999, 188.94347233199997, 692.97933664102641, 136.43524907991582],"bezier", 2) )
    # Connections for obj77 (graphObject_: Obj49) of type contains
    self.drawConnections(
(self.obj77,self.obj29,[912.5, 399.5, 928.0, 236.0],"bezier", 2) )
    # Connections for obj78 (graphObject_: Obj50) of type contains
    self.drawConnections(
(self.obj78,self.obj51,[523.78301644999999, 369.443472332, 528.92020890121103, 367.49479166666663],"bezier", 2) )
    # Connections for obj79 (graphObject_: Obj51) of type contains
    self.drawConnections(
(self.obj79,self.obj52,[571.98966832099995, 377.71762453999997, 692.01149796808693, 352.0781907202944],"bezier", 2) )
    # Connections for obj80 (graphObject_: Obj52) of type contains
    self.drawConnections(
(self.obj80,self.obj50,[439.90317276399998, 377.71762453999997, 350.00191094743792, 371.96502037329128],"bezier", 2) )
    # Connections for obj81 (graphObject_: Obj53) of type contains
    self.drawConnections(
(self.obj81,self.obj49,[439.90317276396206, 347.71762453995785, 368.80634552792418, 296.43524907991565],"bezier", 2) )
    # Connections for obj82 (graphObject_: Obj54) of type contains
    self.drawConnections(
(self.obj82,self.obj47,[216.87398229299998, 281.08404804200001, 221.17749951769304, 343.02456296004203],"bezier", 2) )
    # Connections for obj83 (graphObject_: Obj55) of type contains
    self.drawConnections(
(self.obj83,self.obj48,[264.50574898404341, 235.03909536014723, 352.01149796808693, 232.07819072029451],"bezier", 2) )
    # Connections for obj84 (graphObject_: Obj56) of type contains
    self.drawConnections(
(self.obj84,self.obj44,[505.91795469899995, 329.98103148000001, 536.56603289956797, 239.88694466351214],"bezier", 2) )
    # Connections for obj85 (graphObject_: Obj57) of type contains
    self.drawConnections(
(self.obj85,self.obj45,[748.00095547399997, 254.982510187, 776.74796458621154, 284.16809608307045],"bezier", 2) )
    # Connections for obj86 (graphObject_: Obj58) of type contains
    self.drawConnections(
(self.obj86,self.obj53,[1767.9896683204997, -243.28237546000003, 1008.920208901211, 307.49479166666669],"bezier", 2) )
    # Connections for obj87 (graphObject_: Obj59) of type contains
    self.drawConnections(
(self.obj87,self.obj54,[1948.3739822929999, -268.91595195800005, 1128.920208901211, 267.49479166666669],"bezier", 2) )
    # Connections for obj88 (graphObject_: Obj60) of type contains
    self.drawConnections(
(self.obj88,self.obj55,[1999.0887497589997, -222.98771852000004, 1168.920208901211, 307.49479166666669],"bezier", 2) )
    # Connections for obj89 (graphObject_: Obj61) of type contains
    self.drawConnections(
(self.obj89,self.obj56,[795.98966832099995, 402.71762453999997, 876.74796458621154, 524.1680960830704],"bezier", 2) )
    # Connections for obj90 (graphObject_: Obj62) of type contains
    self.drawConnections(
(self.obj90,self.obj57,[611.46010445100001, 212.24739583300001, 641.17749951769304, 463.02456296004169],"bezier", 2) )
    # Connections for obj91 (graphObject_: Obj63) of type contains
    self.drawConnections(
(self.obj91,self.obj58,[544.00574898399998, 306.03909536000003, 656.74796458621154, 564.16809608307051],"bezier", 2) )
    # Connections for obj92 (graphObject_: Obj64) named 
    self.drawConnections(
(self.obj92,self.obj35,[1176.0019109474374, 424.96502037329128, 1212.9999999999991, 422.99999999999989, 1230.7479645862113, 440.16809608307005],"bezier", 3) )
    # Connections for obj93 (graphObject_: Obj66) named 
    self.drawConnections(
(self.obj93,self.obj33,[1159.3432000143121, 518.61979166666606, 1121.9999999999995, 499.0, 1130.8359093978315, 468.96206296004215],"bezier", 3) )
    # Connections for obj94 (graphObject_: Obj68) named 
    self.drawConnections(
(self.obj94,self.obj34,[1211.9999999999995, 483.99999999999955, 1216.9999999999991, 498.99999999999955, 1243.3432000143134, 515.61979166666674],"bezier", 3) )
    # Connections for obj95 (graphObject_: Obj70) named 
    self.drawConnections(
(self.obj95,self.obj35,[1269.9999999999989, 468.99999999999955, 1267.9999999999991, 450.99999999999966, 1242.8063455279239, 452.43524907991593],"bezier", 3) )
    # Connections for obj96 (graphObject_: Obj72) named 
    self.drawConnections(
(self.obj96,self.obj37,[999.74561475802398, 147.65445251207876, 979.99999999999955, 160.99999999999704, 975.17749951769281, 187.024562960042],"bezier", 3) )
    # Connections for obj97 (graphObject_: Obj74) named 
    self.drawConnections(
(self.obj97,self.obj36,[1040.7309945962388, 190.74938483035629, 1088.0, 157.99999999999898, 1080.8359093978315, 120.96206296004181],"bezier", 3) )
    # Connections for obj98 (graphObject_: Obj76) named 
    self.drawConnections(
(self.obj98,self.obj36,[1053.5999999999999, 70.999999999999716, 1083.0, 75.999999999999545, 1081.1774995176929, 103.02456296004208],"bezier", 3) )
    # Connections for obj99 (graphObject_: Obj78) named 
    self.drawConnections(
(self.obj99,self.obj40,[304.1992505009996, 535.05729393399997, 329.63107437636552, 560.55907222560222, 324.3096353895337, 566.70014112861418],"bezier", 3) )
    # Connections for obj100 (graphObject_: Obj80) named 
    self.drawConnections(
(self.obj100,self.obj39,[288.57477730799985, 547.63603472700004, 263.11170343275796, 522.13425643494134, 266.18762435556636, 509.76210956200839],"bezier", 3) )
    # Connections for obj101 (graphObject_: Obj82) named 
    self.drawConnections(
(self.obj101,self.obj39,[203.177499517, 476.02456295999986, 221.17749951745685, 460.02456296024064, 265.37003539324235, 506.40331618661406],"bezier", 3) )
    # Connections for obj102 (graphObject_: Obj84) named 
    self.drawConnections(
(self.obj102,self.obj38,[441.75217560999272, 530.6981600879999, 486.31271304820507, 512.92092556098305],"bezier", 2) )
    # Connections for obj103 (graphObject_: Obj86) named 
    self.drawConnections(
(self.obj103,self.obj42,[549.00670445799994, 103.0216055468, 602.99999999999966, 109.99999999999991, 692.01149796808693, 132.07819072029437],"bezier", 3) )
    # Connections for obj104 (graphObject_: Obj88) named 
    self.drawConnections(
(self.obj104,self.obj42,[663.28301644999999, 187.943472332, 662.28301644978376, 166.94347233175583, 692.97933664102641, 136.43524907991582],"bezier", 3) )
    # Connections for obj105 (graphObject_: Obj90) named 
    self.drawConnections(
(self.obj105,self.obj42,[763.49999999999989, 113.0, 764.99999999999932, 91.999999999999972, 708.92020890121103, 127.49479166666664],"bezier", 3) )
    # Connections for obj106 (graphObject_: Obj92) named 
    self.drawConnections(
(self.obj106,self.obj42,[748.0, 178.99999999999997, 735.99999999999977, 150.99999999999991, 708.80634552792424, 136.43524907991582],"bezier", 3) )
    # Connections for obj107 (graphObject_: Obj94) named 
    self.drawConnections(
(self.obj107,self.obj41,[517.20446087400001, 131.12835995, 476.40317276396195, 127.21762453995792, 448.80634552792418, 116.43524907991583],"bezier", 3) )
    # Connections for obj108 (graphObject_: Obj96) named 
    self.drawConnections(
(self.obj108,self.obj43,[204.82849937144488, 115.51376018664565, 193.99999999999963, 204.99999999999994, 232.01149796808679, 212.07819072029434],"bezier", 3) )
    # Connections for obj109 (graphObject_: Obj98) named 
    self.drawConnections(
(self.obj109,self.obj41,[240.00670445776174, 126.99331296004149, 293.99999999999949, 113.99999999999994, 432.97933664102641, 116.43524907991581],"bezier", 3) )
    # Connections for obj110 (graphObject_: Obj100) named 
    self.drawConnections(
(self.obj110,self.obj44,[481.94977277100003, 213.96502037299999, 533.34320001431365, 227.61979166666669],"bezier", 2) )
    # Connections for obj111 (graphObject_: Obj102) named 
    self.drawConnections(
(self.obj111,self.obj41,[530.94977277099997, 206.96502037299999, 445.27658095602618, 119.88694466351211],"bezier", 2) )
    # Connections for obj112 (graphObject_: Obj104) named 
    self.drawConnections(
(self.obj112,self.obj41,[610.00670445799994, 228.99331296, 448.80634552792418, 116.43524907991583],"bezier", 2) )
    # Connections for obj113 (graphObject_: Obj106) named 
    self.drawConnections(
(self.obj113,self.obj47,[184.00670445799966, 281.99331295999997, 216.74796458621148, 344.16809608307045],"bezier", 2) )
    # Connections for obj114 (graphObject_: Obj108) named 
    self.drawConnections(
(self.obj114,self.obj41,[400.94977277111877, 171.96502037329134, 436.56603289956797, 119.8869446635121],"bezier", 2) )
    # Connections for obj115 (graphObject_: Obj110) named 
    self.drawConnections(
(self.obj115,self.obj48,[285.94977277100003, 246.96502037299996, 352.01149796808676, 232.07819072029446],"bezier", 2) )
    # Connections for obj116 (graphObject_: Obj112) named 
    self.drawConnections(
(self.obj116,self.obj47,[344.94977277111877, 263.96502037329122, 228.92020890121108, 347.49479166666663],"bezier", 2) )
    # Connections for obj117 (graphObject_: Obj114) named 
    self.drawConnections(
(self.obj117,self.obj45,[611.74312089999978, 262.69086816499993, 772.01149796808681, 292.07819072029446],"bezier", 2) )
    # Connections for obj118 (graphObject_: Obj116) named 
    self.drawConnections(
(self.obj118,self.obj46,[553.74312089999989, 285.69086816499998, 530.00191094743798, 271.96502037329128],"bezier", 2) )
    # Connections for obj119 (graphObject_: Obj118) named 
    self.drawConnections(
(self.obj119,self.obj46,[529.07477277099997, 253.02752037299999, 525.33351264266958, 264.04309608307045],"bezier", 2) )
    # Connections for obj120 (graphObject_: Obj120) named 
    self.drawConnections(
(self.obj120,self.obj49,[311.94977277100003, 301.96502037300002, 352.01149796808676, 292.0781907202944],"bezier", 2) )
    # Connections for obj121 (graphObject_: Obj122) named 
    self.drawConnections(
(self.obj121,self.obj50,[361.006704458, 321.99331296000003, 345.33351264266952, 364.04309608307045],"bezier", 2) )
    # Connections for obj122 (graphObject_: Obj124) named 
    self.drawConnections(
(self.obj122,self.obj50,[426.50095547400002, 380.98251018699989, 414.50095547371882, 395.98251018664564, 348.80634552792418, 376.43524907991565],"bezier", 3) )
    # Connections for obj123 (graphObject_: Obj126) named 
    self.drawConnections(
(self.obj123,self.obj47,[311.006704458, 342.02160554699998, 230.00191094743795, 351.96502037329128],"bezier", 2) )
    # Connections for obj124 (graphObject_: Obj128) named 
    self.drawConnections(
(self.obj124,self.obj47,[315.94977277100003, 324.96502037299996, 228.92020890121108, 347.49479166666663],"bezier", 2) )
    # Connections for obj125 (graphObject_: Obj130) named 
    self.drawConnections(
(self.obj125,self.obj51,[496.49062379399982, 331.20013472699992, 516.74796458621154, 364.16809608307045],"bezier", 2) )
    # Connections for obj126 (graphObject_: Obj132) named 
    self.drawConnections(
(self.obj126,self.obj46,[537.49062379400004, 343.20013472699986, 525.27658095602624, 279.88694466351211],"bezier", 2) )
    # Connections for obj127 (graphObject_: Obj134) named 
    self.drawConnections(
(self.obj127,self.obj52,[550.07477277099997, 376.02752037300002, 692.01149796808693, 352.0781907202944],"bezier", 2) )
    # Connections for obj128 (graphObject_: Obj136) named 
    self.drawConnections(
(self.obj128,self.obj52,[791.4601044506054, 353.24739583333326, 750.0, 363.99999999999972, 710.00191094743798, 351.96502037329128],"bezier", 3) )
    # Connections for obj129 (graphObject_: Obj138) named 
    self.drawConnections(
(self.obj129,self.obj46,[590.01227277099997, 346.02752037299996, 528.80634552792424, 276.43524907991571],"bezier", 2) )
    # Connections for obj130 (graphObject_: Obj140) named 
    self.drawConnections(
(self.obj130,self.obj41,[460.00095547371774, 77.482510186645584, 442.99999999999989, 90.0, 441.17749951769292, 103.02456296004208],"bezier", 3) )
    # Connections for obj131 (graphObject_: Obj142) named 
    self.drawConnections(
(self.obj131,self.obj28,[413.05957265999928, 514.02475694499913, 381.99999999999983, 523.0],"bezier", 2) )
    # Connections for obj132 (graphObject_: Obj144) named 
    self.drawConnections(
(self.obj132,self.obj30,[46.417954698915892, 97.981031480020405, 63.0, 342.99999999999994],"bezier", 2) )
    # Connections for obj133 (graphObject_: Obj146) named 
    self.drawConnections(
(self.obj133,self.obj32,[1351.48966832, 142.71762453999995, 1360.8359093978318, 60.962062960042068],"bezier", 2) )
    # Connections for obj134 (graphObject_: Obj148) named 
    self.drawConnections(
(self.obj134,self.obj41,[272.94977277100003, 185.96502037299999, 432.97933664102646, 116.43524907991583],"bezier", 2) )
    # Connections for obj135 (graphObject_: Obj150) named 
    self.drawConnections(
(self.obj135,self.obj41,[409.01227277111786, 273.02752037329111, 440.83590939783176, 120.96206296004208],"bezier", 2) )
    # Connections for obj136 (graphObject_: Obj152) named 
    self.drawConnections(
(self.obj136,self.obj55,[1152.7771550570678, 285.30167258149203, 1156.7479645862115, 304.16809608307045],"bezier", 2) )
    # Connections for obj137 (graphObject_: Obj154) named 
    self.drawConnections(
(self.obj137,self.obj54,[1137.3098904851695, 299.75336816508843, 1125.2765809560262, 279.88694466351211],"bezier", 2) )
    # Connections for obj138 (graphObject_: Obj156) named 
    self.drawConnections(
(self.obj138,self.obj53,[999.94977277111855, 260.96502037329105, 1001.177499517693, 303.02456296004169],"bezier", 2) )
    # Connections for obj139 (graphObject_: Obj158) named 
    self.drawConnections(
(self.obj139,self.obj53,[1071.0067044577622, 328.02160554679187, 1010.0019109474379, 311.96502037329128],"bezier", 2) )
    # Connections for obj140 (graphObject_: Obj160) named 
    self.drawConnections(
(self.obj140,self.obj54,[1060.9497727711187, 291.96502037329128, 1112.9793366410263, 276.43524907991565],"bezier", 2) )
    # Connections for obj141 (graphObject_: Obj162) named 
    self.drawConnections(
(self.obj141,self.obj58,[617.00670445799994, 523.99331295999991, 656.74796458621154, 564.1680960830704],"bezier", 2) )
    # Connections for obj142 (graphObject_: Obj164) named 
    self.drawConnections(
(self.obj142,self.obj56,[809.00670445799835, 607.02160554699981, 876.56603289956763, 539.88694466351217],"bezier", 2) )
    # Connections for obj143 (graphObject_: Obj166) named 
    self.drawConnections(
(self.obj143,self.obj58,[708.13829047799993, 629.94347233200006, 716.13829047801289, 619.94347233175563, 668.80634552792424, 576.43524907991582],"bezier", 3) )
    # Connections for obj145 (graphObject_: Obj170) named 
    self.drawConnections(
(self.obj145,self.obj57,[893.00670445799597, 470.02160554699987, 650.00191094743786, 471.96502037329111],"bezier", 2) )
    # Connections for obj1170 (graphObject_: Obj188) named 
    self.drawConnections(
(self.obj1170,self.obj57,[790.00670445776132, 487.02160554679244, 650.00191094743786, 471.96502037329111],"bezier", 2) )
    # Connections for obj1173 (graphObject_: Obj190) named 
    self.drawConnections(
(self.obj1173,self.obj57,[651.00670445776245, 521.99331296004186, 640.83590939783176, 480.96206296004186],"bezier", 2) )
    # Connections for obj1176 (graphObject_: Obj192) named 
    self.drawConnections(
(self.obj1176,self.obj57,[714.00670445776109, 564.02160554679199, 645.27658095602601, 479.88694466351194],"bezier", 2) )
    # Connections for obj1183 (graphObject_: Obj194) named 
    self.drawConnections(
(self.obj1183,self.obj57,[735.00670445776018, 539.02160554679199, 648.80634552792424, 476.43524907991565],"bezier", 2) )
    # Connections for obj1187 (graphObject_: Obj196) named 
    self.drawConnections(
(self.obj1187,self.obj57,[761.00670445776245, 502.02160554679267, 650.00191094743786, 471.96502037329111],"bezier", 2) )
    # Connections for obj146 (graphObject_: Obj172) of type orthogonality
    self.drawConnections(
(self.obj146,self.obj63,[91.999999999999986, 60.5, 113.0, 230.0],"bezier", 2) )
    # Connections for obj147 (graphObject_: Obj173) of type orthogonality
    self.drawConnections(
(self.obj147,self.obj59,[127.5, 325.49999999999994, 1008.0, 475.0],"bezier", 2) )
    # Connections for obj148 (graphObject_: Obj174) of type orthogonality
    self.drawConnections(
(self.obj148,self.obj61,[306.5, 256.0, 347.0, 432.99999999999994],"bezier", 2) )
    # Connections for obj149 (graphObject_: Obj175) of type orthogonality
    self.drawConnections(
(self.obj149,self.obj60,[238.99999999999997, 411.5, 950.99999999999989, 139.0],"bezier", 2) )
    # Connections for obj150 (graphObject_: Obj176) of type orthogonality
    self.drawConnections(
(self.obj150,self.obj62,[373.99999999999994, 384.0, 366.24999999999994, 351.25, 564.0, 545.0],"bezier", 3) )
    # Connections for obj151 (graphObject_: Obj177) of type orthogonality
    self.drawConnections(
(self.obj151,self.obj64,[89.0, 415.0, 951.99999999999989, 296.0],"bezier", 2) )
    # Connections for obj152 (graphObject_: Obj178) of type orthogonality
    self.drawConnections(
(self.obj152,self.obj64,[89.0, 415.0, 951.99999999999989, 296.0],"bezier", 2) )
    # Connections for obj153 (graphObject_: Obj179) of type orthogonality
    self.drawConnections(
(self.obj153,self.obj64,[89.0, 415.0, 951.99999999999989, 296.0],"bezier", 2) )
    # Connections for obj154 (graphObject_: Obj180) of type orthogonality
    self.drawConnections(
(self.obj154,self.obj64,[89.0, 415.0, 951.99999999999989, 296.0],"bezier", 2) )
    # Connections for obj155 (graphObject_: Obj181) of type orthogonality
    self.drawConnections(
(self.obj155,self.obj59,[126.99999999999999, 325.49999999999994, 1008.0, 475.0],"bezier", 2) )
    # Connections for obj156 (graphObject_: Obj182) of type orthogonality
    self.drawConnections(
(self.obj156,self.obj62,[373.49999999999994, 384.0, 564.0, 545.0],"bezier", 2) )
    # Connections for obj157 (graphObject_: Obj183) of type orthogonality
    self.drawConnections(
(self.obj157,self.obj62,[373.49999999999994, 384.0, 564.0, 545.0],"bezier", 2) )
    # Connections for obj630 (graphObject_: Obj184) of type orthogonality
    self.drawConnections(
(self.obj630,self.obj62,[393.49999999999994, 394.0, 564.0, 545.0],"bezier", 2) )
    # Connections for obj631 (graphObject_: Obj185) of type orthogonality
    self.drawConnections(
(self.obj631,self.obj62,[393.49999999999994, 394.0, 564.0, 545.0],"bezier", 2) )
    # Connections for obj867 (graphObject_: Obj187) of type orthogonality
    self.drawConnections(
(self.obj867,self.obj62,[393.49999999999994, 394.0, 564.0, 545.0],"bezier", 2) )

newfunction = DigitalWatchStatechart_DCharts_MDL

loadedMMName = 'DCharts'

atom3version = '0.3'
