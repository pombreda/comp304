from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_TTPN_Place_Transition_Rel_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 52, 22
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        constObj = ATOM3Constraint(atribs,"hideWeight","self.semanticObject.", [], [])
        constObj.setValue(('hideWeight', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'if self.semanticObject.weight.getValue() == 1 : self.gf0.setVisible(0)\012else: self.gf0.setVisible(1)\012\012\012\012\012'))
        self.constraintList.append(constObj)

        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([26.0, 19.0, 26.0, 19.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        if self.semanticObject: drawText = self.semanticObject.weight.toString(25,5)
        else: drawText = "<weight>"
        h = drawing.create_text(self.translate([26.0, 7.0]), tags = self.tag, text = drawText, fill= 'blue', anchor= 'center', font= 'Helvetica -12', justify= 'left', width= '0', stipple= '')
        self.attr_display["weight"] = h
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)

    def hideWeight(self):
       if self.semanticObject.weight.getValue() == 1 : self.gf0.setVisible(0)
       else: self.gf0.setVisible(1)
       
       
       
       
       

    def postCondition (self, actionID, * params):
       if actionID ==  self.EDIT or actionID == self.CREATE:
         res = self.hideWeight()
         if res: return res
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_TTPN_Place_Transition_Rel_Center
