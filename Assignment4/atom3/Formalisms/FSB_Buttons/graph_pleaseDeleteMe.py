"""
__graph_pleaseDeleteMe.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_pleaseDeleteMe(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 83, 65
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []
        self.imageDict = self.getImageDict()

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([1.0, 1.0, 71.0, 64.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'yellow')
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)

        h = drawing.create_polygon(self.translate([81.0, 21.0, 40.0, 27.0, 64.0, 51.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'black', smooth = '0', splinesteps =  '12')
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)

        h = drawing.create_oval(self.translate([21.0, 16.0, 34.0, 29.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'black')
        self.gf2 = GraphicalForm(drawing, h, "gf2")
        self.graphForms.append(self.gf2)

        h = drawing.create_oval(self.translate([39.0, 32.0, 39.0, 32.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_pleaseDeleteMe
