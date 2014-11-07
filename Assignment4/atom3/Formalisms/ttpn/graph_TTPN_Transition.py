from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_TTPN_Transition(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 97, 85
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        constObj = ATOM3Constraint(atribs,"changeAtomic","self.semanticObject.", [], [])
        constObj.setValue(('changeAtomic', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'if self.semanticObject.atomic.getValue()[1]:\012   self.gf5.setVisible(1)\012else:\012   self.gf5.setVisible(0)\012if self.semanticObject.processes.getValue() == 1:\012   self.gf6.setVisible(0)\012else:\012   self.gf6.setVisible(1)\012\012'))
        self.constraintList.append(constObj)

        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_line(self.translate([51.0, 19.0, 51.0, 58.0]), tags = self.tag, fill= 'black', joinstyle= 'round', smooth= 0, capstyle= 'butt', arrow= 'none', arrowshape= '8 10 3', splinesteps= '12', width= '5.0', stipple= '')
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)
        h = drawing.create_oval(self.translate([51.0, 38.0, 51.0, 38.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_text(self.translate([53.0, 7.0]), tags = self.tag, fill= 'black', anchor= 'center', font= 'Helvetica -12', text= ', ', justify= 'left', width= '0', stipple= '')
        self.gf2 = GraphicalForm(drawing, h, "gf2")
        self.graphForms.append(self.gf2)
        h = drawing.create_text(self.translate([51.0, 78.0]), tags = self.tag, fill= 'black', anchor= 'center', font= '{MS Sans Serif} 8', text= 'atomic', justify= 'left', width= '0', stipple= '')
        self.gf5 = GraphicalForm(drawing, h, "gf5")
        self.graphForms.append(self.gf5)
        if self.semanticObject: drawText = self.semanticObject.time.toString(25,5)
        else: drawText = "<time>"
        h = drawing.create_text(self.translate([56.0, 8.0]), tags = self.tag, text = drawText, fill= 'blue', anchor= 'w', font= 'Helvetica -12', justify= 'left', width= '0', stipple= '')
        self.attr_display["time"] = h
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)
        if self.semanticObject: drawText = self.semanticObject.processes.toString(25,5)
        else: drawText = "<processes>"
        h = drawing.create_text(self.translate([51.0, 65.0]), tags = self.tag, text = drawText, fill= 'blue', anchor= 'center', font= 'Helvetica -12', justify= 'left', width= '0', stipple= '')
        self.attr_display["processes"] = h
        self.gf6 = GraphicalForm(drawing, h, "gf6")
        self.graphForms.append(self.gf6)
        if self.semanticObject: drawText = self.semanticObject.name.toString(25,5)
        else: drawText = "<name>"
        h = drawing.create_text(self.translate([47.0, 8.0]), tags = self.tag, text = drawText, fill= 'blue', anchor= 'e', font= 'Helvetica -12', justify= 'right', width= '0', stipple= '')
        self.attr_display["name"] = h
        self.gf4 = GraphicalForm(drawing, h, "gf4")
        self.graphForms.append(self.gf4)

    def changeAtomic(self):
       if self.semanticObject.atomic.getValue()[1]:
          self.gf5.setVisible(1)
       else:
          self.gf5.setVisible(0)
       if self.semanticObject.processes.getValue() == 1:
          self.gf6.setVisible(0)
       else:
          self.gf6.setVisible(1)
       
       

    def postCondition (self, actionID, * params):
       if actionID ==  self.EDIT or actionID == self.CREATE:
         res = self.changeAtomic()
         if res: return res
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_TTPN_Transition
