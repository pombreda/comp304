"""
__graph_Entity3.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Entity3(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 163, 103
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
        h = drawing.create_oval(self.translate([9.0, 49.0, 9.0, 49.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([9.0, 69.0, 9.0, 69.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([9.0, 89.0, 9.0, 89.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([169.0, 29.0, 169.0, 29.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([29.0, 109.0, 29.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([49.0, 109.0, 49.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([69.0, 109.0, 69.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([89.0, 109.0, 89.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([109.0, 109.0, 109.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([129.0, 109.0, 129.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([149.0, 109.0, 149.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([169.0, 49.0, 169.0, 49.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([169.0, 69.0, 169.0, 69.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([169.0, 89.0, 169.0, 89.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([29.0, 9.0000000000000284, 29.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([49.0, 9.0000000000000284, 49.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([69.0, 9.0000000000000284, 69.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([89.0, 9.0000000000000284, 89.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([109.0, 9.0000000000000284, 109.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([129.0, 9.0000000000000284, 129.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([149.0, 9.0000000000000284, 149.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([9.0, 29.0, 9.0, 29.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([9.0, 22.0, 169.5, 108.5]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'lightyellow')
        self.gf12 = GraphicalForm(drawing, h, "gf12")
        self.graphForms.append(self.gf12)

        h = drawing.create_rectangle(self.translate([9.0, 9.0, 169.5, 22.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'orange')
        self.gf8 = GraphicalForm(drawing, h, "gf8")
        self.graphForms.append(self.gf8)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Arial', size=12, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([88.0, 16.0, 88.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf9 = GraphicalForm(drawing, h, 'gf9', fontObject=font)
        self.graphForms.append(self.gf9)

        if self.semanticObject: drawText = self.semanticObject.display.toString()
        else: drawText = "<display>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([11.0, 68.2, 11.0, 11.0])[:2], tags = self.tag, font=font, fill = 'blue1', anchor = 'w', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["display"] = h
        self.gf68 = GraphicalForm(drawing, h, 'gf68', fontObject=font)
        self.graphForms.append(self.gf68)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Entity3
