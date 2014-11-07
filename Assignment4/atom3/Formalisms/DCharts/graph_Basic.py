import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Basic(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 1083, 591
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 1
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None

        constObj = ATOM3Constraint(atribs,"Basic_Visual_EDIT_CREATE","self.semanticObject.", [], [])
        constObj.setValue(('Basic_Visual_EDIT_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Basic_Visual_EDIT_CREATE(self)\n'))
        self.constraintList.append(constObj)
        self.graphForms = []
        self.imageDict = self.getImageDict()

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([12.0, 3.0, 30.0, 21.0]), tags = self.tag, stipple = '', width = 2, outline = 'darkblue', fill = 'lightgray')
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)

        h = drawing.create_oval(self.translate([21.228501549606143, 2.8749999999999929, 21.228501549606143, 2.8749999999999929]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([20.886911429744945, 20.8125, 20.886911429744945, 20.8125]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([30.052912979351049, 11.815457413249247, 30.052912979351049, 11.815457413249247]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([12.0625, 11.928627760252381, 12.0625, 11.928627760252381]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([13.394202046226825, 7.4702287066246047, 13.394202046226825, 7.4702287066246047]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([16.798966618124592, 4.0185331230283943, 16.798966618124592, 4.0185331230283943]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([25.38451467458264, 3.8935331230283938, 25.38451467458264, 3.8935331230283938]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([28.971210933124187, 7.3452287066246047, 28.971210933124187, 7.3452287066246047]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([13.030338672939617, 16.285686119873795, 13.030338672939617, 16.285686119873795]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([28.857347559837297, 16.285686119873795, 28.857347559837297, 16.285686119873795]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([25.327582987939337, 19.737381703470074, 25.327582987939337, 19.737381703470074]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([16.61703493148115, 19.737381703470074, 16.61703493148115, 19.737381703470074]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        if self.semanticObject: drawText = self.semanticObject.name.toString(25,5)
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([23.125, 30.0]), tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, justify= 'left', width='0', stipple='' )
        self.attr_display["name"] = h
        self.gf1 = GraphicalForm(drawing, h, 'gf1', fontObject=font)
        self.graphForms.append(self.gf1)


    def Basic_Visual_EDIT_CREATE(self,params):
        import DCharts_utils
        DCharts_utils.Basic_Visual_EDIT_CREATE(self)
        

    def postCondition( self, actionID, * params):
        if actionID ==  self.EDIT or actionID == self.CREATE:
             res = self.Basic_Visual_EDIT_CREATE(params)
             if res: return res
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Basic
