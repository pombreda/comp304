"""
Constructor.py

2006 by Denis Dube
"""

from FSB_Code.ButtonBehaviour_MDL_Compiled import ButtonBehaviour_MDL
from FSB_Code.ToolbarBehaviour_MDL_Compiled import ToolbarBehaviour_MDL



def toolbarCreate(self):
  """
  Called when a toolbar is created on the canvas
  Parameter:
    self = Toolbar semantic object
  """
  atom3i = self.parent
  TkInstance = atom3i.parent
  
  self.UI_Statechart = ToolbarBehaviour_MDL()
  self.UI_Statechart.initModel(TkInstance=TkInstance)
  self.UI_Statechart.event("(create)*", self) 
    
    


def buttonCreate(self):
  """
  Called when a button is created on the canvas
  Parameter:
    self = Button semantic object
  """
  atom3i = self.parent
  TkInstance = atom3i.parent
  
  self.UI_Statechart = ButtonBehaviour_MDL()
  self.UI_Statechart.initModel(TkInstance=TkInstance)
  self.UI_Statechart.event("(create)*", self) 
    
  
def buttonActivation(self):
  """
  Intention in context:
    Button has been pushed, load the relevent button action into memory. This
    is called by the UI_Statechart of the Button semantic object.
    Action will be executed when triggered on the canvas
  """
  #print 'BUTTON ACTIVATION', __file__
  atom3i = self.parent
  
  # Setup the button action. Will be triggered by canvas button press
  methodName, method = self.info.getActionMethod()
  if(self.info.isActionImmediate()):
    method(atom3i, 0, 0)
  else:
    atom3i.mode = methodName
    atom3i.cb.setATOM3action(atom3i.mode)
    atom3i.userActionsMap[methodName] = method
  
  # Show which button is active
  obj = self.graphObject_
  bbox = obj.getbbox()
  color = 'chartreuse'
  #boxHandler = obj.dc.create_rectangle(bbox, width=4, outline=color, dash=(8,8))
  boxHandler2 = obj.dc.create_rectangle(bbox, width=6, outline=color, 
                                        fill='yellow', stipple='gray25')
                                        #outlinestipple='gray25')
  highlightTime = 3000 # milliseconds
  #atom3i.parent.after(highlightTime, lambda c=obj.dc, h=boxHandler: c.delete(h))
  atom3i.parent.after(highlightTime, lambda c=obj.dc, h=boxHandler2: c.delete(h))
  
  # Stop the selection mechanism from messing around 
  atom3i.parent.after(100, lambda h=atom3i.cb.highlighter: h(0))
    
    
    
  