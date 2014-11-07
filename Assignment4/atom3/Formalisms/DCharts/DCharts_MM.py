"""
__DCharts_MM.py______________________________________________________

Automatically generated AToM3 MetaModel (DO NOT MODIFY DIRECTLY)
Author: Denis Dube
Modified: Wed Nov 30 11:48:19 2005
_____________________________________________________________________
"""
from ASG_DCharts import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from StatusBar       import *
from ATOM3TypeDialog import *

from Composite       import *
from Basic       import *
from History       import *
from Orthogonal       import *
from visual_settings       import *
from Port       import *
from Server       import *
from contains       import *
from Hyperedge       import *
from orthogonality       import *
from connection       import *
def createNewASGroot(self):
   return ASG_DCharts(self, None)

def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu.add_command(label="New Composite", command=lambda x=self: x.createNewComposite(x, 100, 100) )
    modelMenu.add_command(label="New Basic", command=lambda x=self: x.createNewBasic(x, 100, 100) )
    modelMenu.add_command(label="New History", command=lambda x=self: x.createNewHistory(x, 100, 100) )
    modelMenu.add_command(label="New Orthogonal", command=lambda x=self: x.createNewOrthogonal(x, 100, 100) )
    modelMenu.add_command(label="New visual_settings", command=lambda x=self: x.createNewvisual_settings(x, 100, 100) )
    modelMenu.add_command(label="New Port", command=lambda x=self: x.createNewPort(x, 100, 100) )
    modelMenu.add_command(label="New Server", command=lambda x=self: x.createNewServer(x, 100, 100) )
    modelMenu.add_command(label="New contains", command=lambda x=self: x.createNewcontains(x, 100, 100) )
    modelMenu.add_command(label="New Hyperedge", command=lambda x=self: x.createNewHyperedge(x, 100, 100) )
    modelMenu.add_command(label="New orthogonality", command=lambda x=self: x.createNeworthogonality(x, 100, 100) )
    modelMenu.add_command(label="New connection", command=lambda x=self: x.createNewconnection(x, 100, 100) )
def setConnectivity(self):
    self.ConnectivityMap['Hyperedge']={
           'Hyperedge': [( 'Composite', self.createNewComposite), ( 'Basic', self.createNewBasic), ( 'History', self.createNewHistory)]
          ,'Orthogonal': []
          ,'Composite': []
          ,'contains': [( 'Composite', self.createNewComposite)]
          ,'orthogonality': [( 'Composite', self.createNewComposite)]
          ,'Server': []
          ,'connection': []
          ,'visual_settings': []
          ,'Basic': []
          ,'Port': []
          ,'History': [] }
    self.ConnectivityMap['Orthogonal']={
           'Hyperedge': []
          ,'Orthogonal': []
          ,'Composite': [( 'contains', self.createNewcontains)]
          ,'contains': []
          ,'orthogonality': []
          ,'Server': []
          ,'connection': []
          ,'visual_settings': []
          ,'Basic': [( 'contains', self.createNewcontains)]
          ,'Port': []
          ,'History': [( 'contains', self.createNewcontains)] }
    self.ConnectivityMap['Composite']={
           'Hyperedge': []
          ,'Orthogonal': [( 'orthogonality', self.createNeworthogonality)]
          ,'Composite': [( 'contains', self.createNewcontains), ( 'Hyperedge', self.createNewHyperedge)]
          ,'contains': []
          ,'orthogonality': []
          ,'Server': []
          ,'connection': []
          ,'visual_settings': []
          ,'Basic': [( 'contains', self.createNewcontains), ( 'Hyperedge', self.createNewHyperedge)]
          ,'Port': []
          ,'History': [( 'contains', self.createNewcontains), ( 'Hyperedge', self.createNewHyperedge)] }
    self.ConnectivityMap['contains']={
           'Hyperedge': [( 'Composite', self.createNewComposite), ( 'Basic', self.createNewBasic), ( 'History', self.createNewHistory)]
          ,'Orthogonal': []
          ,'Composite': []
          ,'contains': [( 'Composite', self.createNewComposite)]
          ,'orthogonality': [( 'Composite', self.createNewComposite)]
          ,'Server': []
          ,'connection': []
          ,'visual_settings': []
          ,'Basic': []
          ,'Port': []
          ,'History': [] }
    self.ConnectivityMap['orthogonality']={
           'Hyperedge': []
          ,'Orthogonal': []
          ,'Composite': []
          ,'contains': [( 'Orthogonal', self.createNewOrthogonal)]
          ,'orthogonality': []
          ,'Server': []
          ,'connection': []
          ,'visual_settings': []
          ,'Basic': []
          ,'Port': []
          ,'History': [] }
    self.ConnectivityMap['Server']={
           'Hyperedge': []
          ,'Orthogonal': []
          ,'Composite': []
          ,'contains': []
          ,'orthogonality': []
          ,'Server': []
          ,'connection': []
          ,'visual_settings': []
          ,'Basic': []
          ,'Port': []
          ,'History': [] }
    self.ConnectivityMap['connection']={
           'Hyperedge': []
          ,'Orthogonal': []
          ,'Composite': []
          ,'contains': []
          ,'orthogonality': []
          ,'Server': []
          ,'connection': []
          ,'visual_settings': []
          ,'Basic': []
          ,'Port': []
          ,'History': [] }
    self.ConnectivityMap['visual_settings']={
           'Hyperedge': []
          ,'Orthogonal': []
          ,'Composite': []
          ,'contains': []
          ,'orthogonality': []
          ,'Server': []
          ,'connection': []
          ,'visual_settings': []
          ,'Basic': []
          ,'Port': []
          ,'History': [] }
    self.ConnectivityMap['Basic']={
           'Hyperedge': []
          ,'Orthogonal': []
          ,'Composite': [( 'Hyperedge', self.createNewHyperedge)]
          ,'contains': []
          ,'orthogonality': []
          ,'Server': []
          ,'connection': []
          ,'visual_settings': []
          ,'Basic': [( 'Hyperedge', self.createNewHyperedge)]
          ,'Port': []
          ,'History': [( 'Hyperedge', self.createNewHyperedge)] }
    self.ConnectivityMap['Port']={
           'Hyperedge': []
          ,'Orthogonal': []
          ,'Composite': []
          ,'contains': []
          ,'orthogonality': []
          ,'Server': [( 'connection', self.createNewconnection)]
          ,'connection': []
          ,'visual_settings': []
          ,'Basic': []
          ,'Port': []
          ,'History': [] }
    self.ConnectivityMap['History']={
           'Hyperedge': []
          ,'Orthogonal': []
          ,'Composite': [( 'Hyperedge', self.createNewHyperedge)]
          ,'contains': []
          ,'orthogonality': []
          ,'Server': []
          ,'connection': []
          ,'visual_settings': []
          ,'Basic': [( 'Hyperedge', self.createNewHyperedge)]
          ,'Port': []
          ,'History': [( 'Hyperedge', self.createNewHyperedge)] }
    
    self.CardinalityTable['Composite']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'Port': []
          ,'Server': []
          ,'contains': [('0', 'N', 'Source'), ('0', '1', 'Destination')]
          ,'Hyperedge': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'orthogonality': [('0', 'N', 'Source')]
          ,'connection': [] }
    self.CardinalityTable['Basic']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'Port': []
          ,'Server': []
          ,'contains': [('0', '1', 'Destination')]
          ,'Hyperedge': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'orthogonality': []
          ,'connection': [] }
    self.CardinalityTable['History']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'Port': []
          ,'Server': []
          ,'contains': [('0', '1', 'Destination')]
          ,'Hyperedge': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'orthogonality': []
          ,'connection': [] }
    self.CardinalityTable['Orthogonal']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'Port': []
          ,'Server': []
          ,'contains': [('0', 'N', 'Source')]
          ,'Hyperedge': []
          ,'orthogonality': [('0', 'N', 'Destination')]
          ,'connection': [] }
    self.CardinalityTable['visual_settings']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'Port': []
          ,'Server': []
          ,'contains': []
          ,'Hyperedge': []
          ,'orthogonality': []
          ,'connection': [] }
    self.CardinalityTable['Port']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'Port': []
          ,'Server': []
          ,'contains': []
          ,'Hyperedge': []
          ,'orthogonality': []
          ,'connection': [('0', 'N', 'Source')] }
    self.CardinalityTable['Server']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'Port': []
          ,'Server': []
          ,'contains': []
          ,'Hyperedge': []
          ,'orthogonality': []
          ,'connection': [('0', 'N', 'Destination')] }
    self.CardinalityTable['contains']={
          'Composite': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'Basic': [('0', 'N', 'Source')]
          ,'History': [('0', 'N', 'Source')]
          ,'Orthogonal': [('0', 'N', 'Destination')]
          ,'visual_settings': []
          ,'Port': []
          ,'Server': []
          ,'contains': []
          ,'Hyperedge': []
          ,'orthogonality': []
          ,'connection': [] }
    self.CardinalityTable['Hyperedge']={
          'Composite': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Basic': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'History': [('0', 'N', 'Destination'), ('0', '1', 'Source')]
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'Port': []
          ,'Server': []
          ,'contains': []
          ,'Hyperedge': []
          ,'orthogonality': []
          ,'connection': [] }
    self.CardinalityTable['orthogonality']={
          'Composite': [('1', '1', 'Destination')]
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': [('1', '1', 'Source')]
          ,'visual_settings': []
          ,'Port': []
          ,'Server': []
          ,'contains': []
          ,'Hyperedge': []
          ,'orthogonality': []
          ,'connection': [] }
    self.CardinalityTable['connection']={
          'Composite': []
          ,'Basic': []
          ,'History': []
          ,'Orthogonal': []
          ,'visual_settings': []
          ,'Port': [('1', '1', 'Destination')]
          ,'Server': [('1', '1', 'Source')]
          ,'contains': []
          ,'Hyperedge': []
          ,'orthogonality': []
          ,'connection': [] }
    
    self.entitiesInMetaModel['DCharts']=["Composite", "Basic", "History", "Orthogonal", "visual_settings", "Port", "Server", "contains", "Hyperedge", "orthogonality", "connection"]

    
def createNewComposite(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Composite(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Composite"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Composite(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Composite(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewBasic(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Basic(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Basic"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Basic(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Basic(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewHistory(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = History(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["History"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_History(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_History(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("History", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewOrthogonal(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Orthogonal(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Orthogonal"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Orthogonal(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Orthogonal(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Orthogonal", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewvisual_settings(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = visual_settings(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["visual_settings"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_visual_settings(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_visual_settings(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("visual_settings", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewPort(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Port(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Port"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Port(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Port(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Port", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewServer(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Server(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Server"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Server(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Server(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Server", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewcontains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("contains", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewHyperedge(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Hyperedge(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Hyperedge"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Hyperedge(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Hyperedge(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNeworthogonality(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = orthogonality(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["orthogonality"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_orthogonality(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_orthogonality(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("orthogonality", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewconnection(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = connection(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["connection"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_connection(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_connection(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("connection", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNew_Model(self, wherex, wherey, screenCoordinates = 1):
   self.toClass = None
   self.fromClass = None
   new_semantic_obj = ASG_DCharts(self)
   ne = len(self.ASGroot.listNodes["ASG_DCharts"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ASG_ERmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ASG_ERmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ASG_DCharts", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def fillTypesInformation(self):
    objs = []
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("String", "ATOM3String", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Boolean", "ATOM3Boolean", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Integer", "ATOM3Integer", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Float", "ATOM3Float", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("Attribute", "ATOM3Attribute", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("[1,1,1,self.types]")
    params.append(param)
    param = ATOM3String("ATOM3Attribute")
    params.append(param)
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("List", "ATOM3List", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("[]")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Enum", "ATOM3Enum", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Constraint", "ATOM3Constraint", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("'class0'")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    obj.setValue(("Appearance", "ATOM3Appearance", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("BottomType", "ATOM3BottomType", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Link", "ATOM3Link", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Port", "ATOM3Port", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Connection", "ATOM3Connection", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("MSEnum", "ATOM3MSEnum", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Text", "ATOM3Text", params, (None, 0) ))
    objs.append(obj)
    self.typeList.setValue(objs)

