"""
__copyBuffer.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Unamed
Modified: Mon Mar 15 19:27:16 2010
____________________________________________________________________
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

def copyBuffer(self, rootNode):

    # variables
    rootNode.variables.setValue('\n')
    rootNode.variables.setHeight(15)

    # misc
    rootNode.misc.setValue('\n')
    rootNode.misc.setHeight(15)

    # event_clauses
    rootNode.event_clauses.setValue('\n')
    rootNode.event_clauses.setHeight(15)

    rootNode.postAction( rootNode.CREATE )

    self.obj28=Composite(self)
    self.obj28.isGraphObjectVisual = True

    if(hasattr(self.obj28, '_setHierarchicalLink')):
      self.obj28._setHierarchicalLink(False)

    # auto_adjust
    self.obj28.auto_adjust.setValue((None, 1))
    self.obj28.auto_adjust.config = 0

    # name
    self.obj28.name.setValue('ON')

    # is_default
    self.obj28.is_default.setValue((None, 1))
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
       new_obj = graph_Composite(68.0,175.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,94.0,77.0,554.0,647.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,94.0,70.0)
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
    self.obj29.name.setValue('NORMAL')

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
       new_obj = graph_Composite(272.0,124.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,158.0,95.0,422.0,449.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,158.0,88.0)
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
    self.obj30.name.setValue('FLASHING')

    # is_default
    self.obj30.is_default.setValue((None, 0))
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
       new_obj = graph_Composite(272.0,407.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,171.0,530.0,414.0,640.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,171.0,523.0)
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
    self.obj30.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)
    self.obj30.postAction( rootNode.CREATE )

    self.obj31=Composite(self)
    self.obj31.isGraphObjectVisual = True

    if(hasattr(self.obj31, '_setHierarchicalLink')):
      self.obj31._setHierarchicalLink(False)

    # auto_adjust
    self.obj31.auto_adjust.setValue((None, 1))
    self.obj31.auto_adjust.config = 0

    # name
    self.obj31.name.setValue('RED')

    # is_default
    self.obj31.is_default.setValue((None, 1))
    self.obj31.is_default.config = 0

    # visible
    self.obj31.visible.setValue((None, 1))
    self.obj31.visible.config = 0

    # exit_action
    self.obj31.exit_action.setValue('\n')
    self.obj31.exit_action.setHeight(15)

    # enter_action
    self.obj31.enter_action.setValue('\n')
    self.obj31.enter_action.setHeight(15)

    self.obj31.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(223.0,47.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,177.0,113.0,415.0,188.0)
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
    self.obj32.name.setValue('GREEN')

    # exit_action
    self.obj32.exit_action.setValue('\n')
    self.obj32.exit_action.setHeight(15)

    # enter_action
    self.obj32.enter_action.setValue('\n')
    self.obj32.enter_action.setHeight(15)

    self.obj32.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(274.0,408.0,self.obj32)
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
    self.obj33.name.setValue('YELLOW')

    # exit_action
    self.obj33.exit_action.setValue('\n')
    self.obj33.exit_action.setHeight(15)

    # enter_action
    self.obj33.enter_action.setValue('\n')
    self.obj33.enter_action.setHeight(15)

    self.obj33.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(274.0,319.0,self.obj33)
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
    self.obj34.is_default.setValue((None, 1))
    self.obj34.is_default.config = 0

    # name
    self.obj34.name.setValue('RED_WAIT')

    # exit_action
    self.obj34.exit_action.setValue('\n')
    self.obj34.exit_action.setHeight(15)

    # enter_action
    self.obj34.enter_action.setValue('\n')
    self.obj34.enter_action.setHeight(15)

    self.obj34.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(355.0,147.0,self.obj34)
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
    self.obj35.name.setValue('GREEN_SOON')

    # exit_action
    self.obj35.exit_action.setValue('\n')
    self.obj35.exit_action.setHeight(15)

    # enter_action
    self.obj35.enter_action.setValue('\n')
    self.obj35.enter_action.setHeight(15)

    self.obj35.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(202.0,146.0,self.obj35)
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
    self.obj36.name.setValue('YELLOW_ON')

    # exit_action
    self.obj36.exit_action.setValue('\n')
    self.obj36.exit_action.setHeight(15)

    # enter_action
    self.obj36.enter_action.setValue('\n')
    self.obj36.enter_action.setHeight(15)

    self.obj36.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(263.0,533.0,self.obj36)
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
    self.obj37.name.setValue('YELLOW_OFF')

    # exit_action
    self.obj37.exit_action.setValue('\n')
    self.obj37.exit_action.setHeight(15)

    # enter_action
    self.obj37.enter_action.setValue('\n')
    self.obj37.enter_action.setHeight(15)

    self.obj37.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(269.0,599.0,self.obj37)
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
    self.obj38.name.setValue('OFF')

    # exit_action
    self.obj38.exit_action.setValue('\n')
    self.obj38.exit_action.setHeight(15)

    # enter_action
    self.obj38.enter_action.setValue('\n')
    self.obj38.enter_action.setHeight(15)

    self.obj38.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(400.0,13.0,self.obj38)
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
    self.obj39.name.setValue('DEAD')

    # exit_action
    self.obj39.exit_action.setValue('\n')
    self.obj39.exit_action.setHeight(15)

    # enter_action
    self.obj39.enter_action.setValue('\n')
    self.obj39.enter_action.setHeight(15)

    self.obj39.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(624.0,349.0,self.obj39)
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
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=History(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # is_default
    self.obj40.is_default.setValue((None, 0))
    self.obj40.is_default.config = 0

    # star
    self.obj40.star.setValue((None, 1))
    self.obj40.star.config = 0

    # name
    self.obj40.name.setValue('')
    self.obj40.name.setNone()

    self.obj40.graphClass_= graph_History
    if self.genGraphics:
       new_obj = graph_History(477.0,180.0,self.obj40)
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
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=contains(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    self.obj41.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(217.5,242.5,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=contains(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    self.obj42.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(318.0,250.5,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=contains(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    self.obj43.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(275.0,352.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=contains(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    self.obj44.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(303.0,260.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=contains(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    self.obj45.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(282.0,263.5,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=contains(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    self.obj46.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(352.0,-327.5,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=contains(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    self.obj47.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(290.0,-327.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=contains(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    self.obj48.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(303.5,248.5,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=contains(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    self.obj49.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(165.0,504.5,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=contains(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    self.obj50.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(167.0,544.5,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
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
    self.obj51.trigger.setValue('AFTER(6)')

    # action
    self.obj51.action.setValue('\n')
    self.obj51.action.setHeight(15)

    # broadcast_to
    self.obj51.broadcast_to.setValue('')
    self.obj51.broadcast_to.setNone()

    # display
    self.obj51.display.setValue('AFTER(6)')

    self.obj51.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(274.0,158.5,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
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
    self.obj52.trigger.setValue('CROSSWALK')

    # action
    self.obj52.action.setValue('\n')
    self.obj52.action.setHeight(15)

    # broadcast_to
    self.obj52.broadcast_to.setValue('')
    self.obj52.broadcast_to.setNone()

    # display
    self.obj52.display.setValue('CROSSWALK')

    self.obj52.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(271.0,121.5,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
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
    self.obj53.trigger.setValue('AFTER(5)')

    # action
    self.obj53.action.setValue('\n')
    self.obj53.action.setHeight(15)

    # broadcast_to
    self.obj53.broadcast_to.setValue('')
    self.obj53.broadcast_to.setNone()

    # display
    self.obj53.display.setValue('AFTER(5)')

    self.obj53.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(296.0,374.5,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
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
    self.obj54.trigger.setValue('AFTER(2)')

    # action
    self.obj54.action.setValue('\n')
    self.obj54.action.setHeight(15)

    # broadcast_to
    self.obj54.broadcast_to.setValue('')
    self.obj54.broadcast_to.setNone()

    # display
    self.obj54.display.setValue('AFTER(2)')

    self.obj54.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(294.5,259.5,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.6785714285714286, 2.5714285714285716]
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
    self.obj55.trigger.setValue('AFTER(2)')

    # action
    self.obj55.action.setValue('\n')
    self.obj55.action.setHeight(15)

    # broadcast_to
    self.obj55.broadcast_to.setValue('')
    self.obj55.broadcast_to.setNone()

    # display
    self.obj55.display.setValue('AFTER(2)')

    self.obj55.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(223.0,225.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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
    self.obj56.trigger.setValue('AFTER(0.5)')

    # action
    self.obj56.action.setValue('\n')
    self.obj56.action.setHeight(15)

    # broadcast_to
    self.obj56.broadcast_to.setValue('')
    self.obj56.broadcast_to.setNone()

    # display
    self.obj56.display.setValue('AFTER(0.5)')

    self.obj56.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(348.0,584.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=Hyperedge(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # name
    self.obj57.name.setValue('')
    self.obj57.name.setNone()

    # broadcast
    self.obj57.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj57.broadcast.setHeight(15)

    # guard
    self.obj57.guard.setValue('1')

    # trigger
    self.obj57.trigger.setValue('ON-OFF')

    # action
    self.obj57.action.setValue('\n')
    self.obj57.action.setHeight(15)

    # broadcast_to
    self.obj57.broadcast_to.setValue('')
    self.obj57.broadcast_to.setNone()

    # display
    self.obj57.display.setValue('ON-OFF')

    self.obj57.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(497.0,144.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

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
    self.obj58.trigger.setValue('ON-OFF')

    # action
    self.obj58.action.setValue('\n')
    self.obj58.action.setHeight(15)

    # broadcast_to
    self.obj58.broadcast_to.setValue('')
    self.obj58.broadcast_to.setNone()

    # display
    self.obj58.display.setValue('ON-OFF')

    self.obj58.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(325.0,25.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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
    self.obj59.trigger.setValue('POLICE')

    # action
    self.obj59.action.setValue('\n')
    self.obj59.action.setHeight(15)

    # broadcast_to
    self.obj59.broadcast_to.setValue('')
    self.obj59.broadcast_to.setNone()

    # display
    self.obj59.display.setValue('POLICE')

    self.obj59.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(466.0,464.5,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
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
    self.obj60.trigger.setValue('POLICE')

    # action
    self.obj60.action.setValue('\n')
    self.obj60.action.setHeight(15)

    # broadcast_to
    self.obj60.broadcast_to.setValue('')
    self.obj60.broadcast_to.setNone()

    # display
    self.obj60.display.setValue('POLICE')

    self.obj60.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(102.0,466.5,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
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
    self.obj61.trigger.setValue('QUIT')

    # action
    self.obj61.action.setValue('\n')
    self.obj61.action.setHeight(15)

    # broadcast_to
    self.obj61.broadcast_to.setValue('')
    self.obj61.broadcast_to.setNone()

    # display
    self.obj61.display.setValue('QUIT')

    self.obj61.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(565.5,360.5,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
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
    self.obj62.trigger.setValue('AFTER(0.5)')

    # action
    self.obj62.action.setValue('\n')
    self.obj62.action.setHeight(15)

    # broadcast_to
    self.obj62.broadcast_to.setValue('')
    self.obj62.broadcast_to.setNone()

    # display
    self.obj62.display.setValue('AFTER(0.5)')

    self.obj62.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(181.0,579.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    # Connections for obj28 (graphObject_: Obj0) named ON
    self.drawConnections(
(self.obj28,self.obj41,[121.00000000000001, 200.99999999999997, 217.49999999999997, 242.49999999999994], 0, 2),
(self.obj28,self.obj42,[325.0, 75.0, 317.99999999999994, 250.49999999999994], 0, 2),
(self.obj28,self.obj43,[195.99999999999994, 267.99999999999994, 275.0, 352.0], 0, 2),
(self.obj28,self.obj58,[325.0, 75.0, 325.0, 25.0], 0, 2),
(self.obj28,self.obj61,[556.0, 360.99999999999994, 565.5, 360.5], 0, 2) )
    # Connections for obj29 (graphObject_: Obj1) named NORMAL
    self.drawConnections(
(self.obj29,self.obj44,[290.0, 450.0, 303.0, 259.99999999999994], 0, 2),
(self.obj29,self.obj45,[290.0, 450.0, 282.0, 263.49999999999994], 0, 2),
(self.obj29,self.obj48,[158.0, 271.99999999999994, 303.5, 248.49999999999994], 0, 2),
(self.obj29,self.obj60,[158.0, 271.99999999999994, 102.99999999999999, 272.99999999999994, 102.0, 466.49999999999989], 0, 3) )
    # Connections for obj30 (graphObject_: Obj2) named FLASHING
    self.drawConnections(
(self.obj30,self.obj49,[170.99999999999997, 585.0, 164.99999999999997, 504.49999999999989], 0, 2),
(self.obj30,self.obj50,[292.99999999999994, 530.0, 166.99999999999997, 544.5], 0, 2),
(self.obj30,self.obj59,[415.00000000000006, 585.0, 465.99999999999989, 583.99999999999989, 465.99999999999989, 464.5], 0, 3) )
    # Connections for obj31 (graphObject_: Obj3) named RED
    self.drawConnections(
(self.obj31,self.obj46,[415.00000000000006, 178.0, 352.0, -327.49999999999994], 0, 2),
(self.obj31,self.obj47,[176.0, 178.0, 290.0, -327.0], 0, 2) )
    # Connections for obj32 (graphObject_: Obj4) named GREEN
    self.drawConnections(
(self.obj32,self.obj53,[295.0, 410.99999999999994, 295.99999999999994, 374.5], 0, 2) )
    # Connections for obj33 (graphObject_: Obj5) named YELLOW
    self.drawConnections(
(self.obj33,self.obj54,[295.17749951769309, 322.02456296004203, 294.49999999999994, 259.5], 0, 2) )
    # Connections for obj34 (graphObject_: Obj6) named RED_WAIT
    self.drawConnections(
(self.obj34,self.obj51,[368.0, 158.99999999999997, 274.0, 158.49999999999997], 0, 2),
(self.obj34,self.obj52,[376.0, 150.0, 376.0, 121.00000000000001, 271.0, 121.5], 0, 3) )
    # Connections for obj35 (graphObject_: Obj7) named GREEN_SOON
    self.drawConnections(
(self.obj35,self.obj55,[223.0, 166.99999999999997, 223.0, 225.0], 0, 2) )
    # Connections for obj36 (graphObject_: Obj8) named YELLOW_ON
    self.drawConnections(
(self.obj36,self.obj62,[276.0, 545.0, 181.00000000000003, 545.0, 181.00000000000003, 578.99999999999989], 0, 3) )
    # Connections for obj37 (graphObject_: Obj9) named YELLOW_OFF
    self.drawConnections(
(self.obj37,self.obj56,[299.0, 611.0, 348.0, 612.0, 348.0, 583.99999999999989], 0, 3) )
    # Connections for obj38 (graphObject_: Obj10) named OFF
    self.drawConnections(
(self.obj38,self.obj57,[429.99999999999983, 25.0, 497.99999999999983, 25.0, 496.99999999999989, 144.5], 0, 3) )
    # Connections for obj39 (graphObject_: Obj11) named DEAD
    self.drawConnections(
 )
    # Connections for obj40 (graphObject_: Obj12) named 
    self.drawConnections(
 )
    # Connections for obj41 (graphObject_: Obj13) of type contains
    self.drawConnections(
(self.obj41,self.obj29,[217.49999999999997, 242.49999999999989, 158.0, 271.99999999999994], 0, 2) )
    # Connections for obj42 (graphObject_: Obj14) of type contains
    self.drawConnections(
(self.obj42,self.obj30,[317.99999999999994, 250.49999999999994, 253.99999999999997, 538.0], 0, 2) )
    # Connections for obj43 (graphObject_: Obj15) of type contains
    self.drawConnections(
(self.obj43,self.obj40,[275.0, 352.0, 479.99999999999994, 201.99999999999997], 0, 2) )
    # Connections for obj44 (graphObject_: Obj16) of type contains
    self.drawConnections(
(self.obj44,self.obj32,[303.0, 259.99999999999994, 295.0, 410.99999999999994], 0, 2) )
    # Connections for obj45 (graphObject_: Obj17) of type contains
    self.drawConnections(
(self.obj45,self.obj33,[282.0, 263.49999999999994, 295.0, 322.0], 0, 2) )
    # Connections for obj46 (graphObject_: Obj18) of type contains
    self.drawConnections(
(self.obj46,self.obj34,[352.0, -327.49999999999994, 368.0, 158.99999999999997], 0, 2) )
    # Connections for obj47 (graphObject_: Obj19) of type contains
    self.drawConnections(
(self.obj47,self.obj35,[290.0, -327.0, 223.0, 148.99999999999997], 0, 2) )
    # Connections for obj48 (graphObject_: Obj20) of type contains
    self.drawConnections(
(self.obj48,self.obj31,[303.5, 248.49999999999994, 295.0, 112.99999999999997], 0, 2) )
    # Connections for obj49 (graphObject_: Obj21) of type contains
    self.drawConnections(
(self.obj49,self.obj36,[164.99999999999997, 504.49999999999989, 292.99999999999994, 545.0], 0, 2) )
    # Connections for obj50 (graphObject_: Obj22) of type contains
    self.drawConnections(
(self.obj50,self.obj37,[166.99999999999997, 544.5, 299.0, 611.0], 0, 2) )
    # Connections for obj51 (graphObject_: Obj23) named 
    self.drawConnections(
(self.obj51,self.obj35,[274.0, 158.49999999999997, 232.0, 158.0], 0, 2) )
    # Connections for obj52 (graphObject_: Obj25) named 
    self.drawConnections(
(self.obj52,self.obj35,[271.0, 121.5, 223.0, 122.0, 223.0, 148.99999999999997], 0, 3) )
    # Connections for obj53 (graphObject_: Obj27) named 
    self.drawConnections(
(self.obj53,self.obj33,[295.99999999999994, 374.5, 295.0, 340.0], 0, 2) )
    # Connections for obj54 (graphObject_: Obj29) named 
    self.drawConnections(
(self.obj54,self.obj31,[294.49999999999994, 259.5, 295.99999999999994, 190.0], 0, 2) )
    # Connections for obj55 (graphObject_: Obj31) named 
    self.drawConnections(
(self.obj55,self.obj32,[223.0, 225.0, 222.00000000000003, 353.99999999999994, 223.0, 420.00000000000006, 287.0, 420.00000000000006], 0, 4) )
    # Connections for obj56 (graphObject_: Obj33) named 
    self.drawConnections(
(self.obj56,self.obj36,[348.0, 583.99999999999989, 346.99999999999989, 545.0, 292.99999999999994, 545.0], 0, 3) )
    # Connections for obj57 (graphObject_: Obj35) named 
    self.drawConnections(
(self.obj57,self.obj40,[496.99999999999989, 144.5, 497.99999999999983, 182.99999999999997], 0, 2) )
    # Connections for obj58 (graphObject_: Obj37) named 
    self.drawConnections(
(self.obj58,self.obj38,[325.0, 25.0, 413.0, 25.0], 0, 2) )
    # Connections for obj59 (graphObject_: Obj39) named 
    self.drawConnections(
(self.obj59,self.obj29,[465.99999999999989, 464.5, 465.00000000000006, 271.99999999999994, 421.99999999999983, 271.99999999999994], 0, 3) )
    # Connections for obj60 (graphObject_: Obj41) named 
    self.drawConnections(
(self.obj60,self.obj30,[102.0, 466.49999999999989, 102.99999999999999, 581.0, 170.99999999999997, 581.0], 0, 3) )
    # Connections for obj61 (graphObject_: Obj43) named 
    self.drawConnections(
(self.obj61,self.obj39,[565.5, 360.5, 636.99999999999989, 360.99999999999994], 0, 2) )
    # Connections for obj62 (graphObject_: Obj45) named 
    self.drawConnections(
(self.obj62,self.obj37,[181.00000000000003, 578.99999999999989, 181.00000000000003, 612.0, 282.0, 611.0], 0, 3) )

newfunction = copyBuffer

loadedMMName = 'DCharts'
