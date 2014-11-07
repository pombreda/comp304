"""
__ToolbarBehaviour_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Denis Dube
Modified: Mon May 29 15:54:06 2006
______________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Basic import *
from Hyperedge import *
from TextAnnotationRoundedBox import *
from TextAnnotationBox import *
from graph_Basic import *
from graph_TextAnnotationBox import *
from graph_Hyperedge import *
from graph_TextAnnotationRoundedBox import *
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

def ToolbarBehaviour_MDL(self, rootNode, DChartsRootNode=None, AnnotationRootNode=None):

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


    # --- Generating attributes code for ASG Annotation ---
    if( AnnotationRootNode ): 
        # description
        AnnotationRootNode.description.setValue('\n')
        AnnotationRootNode.description.setHeight(15)

        # author
        AnnotationRootNode.author.setValue('')
        AnnotationRootNode.author.setNone()
    # --- ASG attributes over ---


    self.obj37=Basic(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # is_default
    self.obj37.is_default.setValue((None, 1))
    self.obj37.is_default.config = 0

    # name
    self.obj37.name.setValue('Default')

    # exit_action
    self.obj37.exit_action.setValue('\n')
    self.obj37.exit_action.setHeight(15)

    # enter_action
    self.obj37.enter_action.setValue('\n')
    self.obj37.enter_action.setHeight(15)

    self.obj37.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(80.0,100.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,92.0,103.0,110.0,121.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,103.125,130.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Default')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font24457744')
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
    self.obj38.name.setValue('Idle')

    # exit_action
    self.obj38.exit_action.setValue('\n')
    self.obj38.exit_action.setHeight(15)

    # enter_action
    self.obj38.enter_action.setValue('\n')
    self.obj38.enter_action.setHeight(15)

    self.obj38.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(460.0,100.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,472.0,103.0,490.0,121.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,461.125,96.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Idle')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font24945688')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-22.0, -34.0]
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
    self.obj39.name.setValue('Do Layout*')

    # exit_action
    self.obj39.exit_action.setValue('\n')
    self.obj39.exit_action.setHeight(15)

    # enter_action
    self.obj39.enter_action.setValue('#event = eventhandler.get_event_params()\n#event._isHandled = True\n\nfrom FSB_Code.Layout import toolbarLayout\ntoolbarLayout(self)\n\neventhandler.event(\'[Done]\')\n')
    self.obj39.enter_action.setHeight(15)

    self.obj39.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(460.0,0.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,472.0,3.0,490.0,21.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,390.125,12.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Do Layout*')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font25482024')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.82
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-93.0, -18.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=Hyperedge(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # name
    self.obj40.name.setValue('')
    self.obj40.name.setNone()

    # broadcast
    self.obj40.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj40.broadcast.setHeight(15)

    # guard
    self.obj40.guard.setValue('1')

    # trigger
    self.obj40.trigger.setValue('<Any-ButtonRelease-1>')

    # action
    self.obj40.action.setValue('\n')
    self.obj40.action.setHeight(15)

    # broadcast_to
    self.obj40.broadcast_to.setValue('')
    self.obj40.broadcast_to.setNone()

    # display
    self.obj40.display.setValue('<Any-ButtonRelease-1>')

    self.obj40.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(471.006791091,62.0349382043,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.05
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-129.0, -11.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=Hyperedge(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # name
    self.obj41.name.setValue('')
    self.obj41.name.setNone()

    # broadcast
    self.obj41.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj41.broadcast.setHeight(15)

    # guard
    self.obj41.guard.setValue('1')

    # trigger
    self.obj41.trigger.setValue('[Done]')

    # action
    self.obj41.action.setValue('\n')
    self.obj41.action.setHeight(15)

    # broadcast_to
    self.obj41.broadcast_to.setValue('')
    self.obj41.broadcast_to.setNone()

    # display
    self.obj41.display.setValue('[Done]')

    self.obj41.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(491.006617824,61.9516877158,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [4.0, -11.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=Hyperedge(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # name
    self.obj42.name.setValue('')
    self.obj42.name.setNone()

    # broadcast
    self.obj42.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj42.broadcast.setHeight(2)

    # guard
    self.obj42.guard.setValue('1')

    # trigger
    self.obj42.trigger.setValue('(create)*')

    # action
    self.obj42.action.setValue('\n# self is a DChart semantic entity, subclass of ASGNode\nself = eventhandler.get_event_params()\natom3i = self.parent\ncb = atom3i.cb\n')
    self.obj42.action.setHeight(20)

    # broadcast_to
    self.obj42.broadcast_to.setValue('')
    self.obj42.broadcast_to.setNone()

    # display
    self.obj42.display.setValue('(create)*')

    self.obj42.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(291.006704458,112.021605547,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.97
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-14.0, -17.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=TextAnnotationRoundedBox(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # text
    self.obj43.text.setValue('Toolbar behaviour\n')
    self.obj43.text.setHeight(15)

    # autoOptimizeArrow
    self.obj43.autoOptimizeArrow.setValue((None, 0))
    self.obj43.autoOptimizeArrow.config = 0

    # charHeight
    self.obj43.charHeight.setValue(20.0)

    # autoResize
    self.obj43.autoResize.setValue((None, 0))
    self.obj43.autoResize.config = 0

    # charWidth
    self.obj43.charWidth.setValue(7.8)

    self.obj43.graphClass_= graph_TextAnnotationRoundedBox
    if self.genGraphics:
       new_obj = graph_TextAnnotationRoundedBox(60.0,20.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TextAnnotationRoundedBox", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.350000000000005, 1.6800000000000002]
       new_obj.layConstraints['Label Offset'] = [2.0, 8.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=TextAnnotationBox(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # text
    self.obj44.text.setValue('Legend:\n    * only these states/transitions have action code\n    + hierarchical state (ie: implemented in another statechart)\n    [...] internally generated event\n    <...> event generated by another, possibly different, behaviour statechart\n    (...) event generated by the semantic object associated with this statechart\n    {...} event generated by a semantic relation object\n    AFTER(0) means an instaneous transition\n')
    self.obj44.text.setHeight(15)

    # charWidth
    self.obj44.charWidth.setValue(7.8)

    # autoResize
    self.obj44.autoResize.setValue((None, 0))
    self.obj44.autoResize.config = 0

    # autoOptimizeArrow
    self.obj44.autoOptimizeArrow.setValue((None, 0))
    self.obj44.autoOptimizeArrow.config = 0

    # charHeight
    self.obj44.charHeight.setValue(18.0)

    self.obj44.graphClass_= graph_TextAnnotationBox
    if self.genGraphics:
       new_obj = graph_TextAnnotationBox(80.0,340.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TextAnnotationBox", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [9.199999999999994, 7.9399999999999906]
       new_obj.layConstraints['Label Offset'] = [-6.0, -4.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    # Connections for obj37 (graphObject_: Obj0) named Default
    self.drawConnections(
(self.obj37,self.obj42,[110.00191094743791, 111.96502037329125, 291.00670445799994, 112.02160554699999],"bezier", 2) )
    # Connections for obj38 (graphObject_: Obj1) named Idle
    self.drawConnections(
(self.obj38,self.obj40,[476.74796458621148, 104.16809608307044, 471.09218862115085, 82.550563204282597, 471.00679109100003, 62.034938204299998],"bezier", 3) )
    # Connections for obj39 (graphObject_: Obj2) named Do Layout*
    self.drawConnections(
(self.obj39,self.obj41,[485.27658095602618, 19.886944663512129, 490.92122029437394, 41.436062715801484, 491.00661782400005, 61.951687715799999],"bezier", 3) )
    # Connections for obj40 (graphObject_: Obj3) named 
    self.drawConnections(
(self.obj40,self.obj39,[471.00679109100003, 62.034938204299998, 470.92139356122027, 41.519313204282611, 476.56603289956797, 19.886944663512129],"bezier", 3) )
    # Connections for obj41 (graphObject_: Obj5) named 
    self.drawConnections(
(self.obj41,self.obj38,[491.00661782400005, 61.951687715799999, 491.09201535430446, 82.467312715801455, 485.33351264266952, 104.04309608307044],"bezier", 3) )
    # Connections for obj42 (graphObject_: Obj7) named 
    self.drawConnections(
(self.obj42,self.obj38,[291.00670445776228, 112.02160554679284, 472.01149796808687, 112.07819072029443],"bezier", 2) )
    # Connections for obj43 (graphObject_: Obj9) of type TextAnnotationRoundedBox
    self.drawConnections(
 )
    # Connections for obj44 (graphObject_: Obj10) of type TextAnnotationBox
    self.drawConnections(
 )

newfunction = ToolbarBehaviour_MDL

loadedMMName = ['DCharts', 'Annotation_META']

atom3version = '0.3'
