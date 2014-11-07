
import BoardStateObserver

from Tkinter import *

class GridWindow(BoardStateObserver.BoardStateObserver):
    def __init__(self, master, controller, rows, cols, rowOffset = 0, colOffset = 0, rowHeight = 40, colWidth = 40, squareColourInFocus = "LightGray", squareColourOutFocus = "White", dividerWidth = 3):
        self.rows = rows
        self.cols = cols
        self.rowHeight = rowHeight
        self.colWidth = colWidth
        self.squareColourInFocus = squareColourInFocus
        self.squareColourOutFocus = squareColourOutFocus
        self.dividerWidth = dividerWidth
        self.master = master
        self.window = Toplevel(master) # create a separate window
        self.window.title("(" + str(rowOffset) + "," + str(colOffset) + ")")
        
        # bind UI events to callback methods
        self.window.bind("<Button-1>", self.onClick)
        self.window.bind("<Key>", self.onKey)
        self.window.protocol("WM_DELETE_WINDOW", self.onClose)
        # the grid is drawn on a Tkinter Canvas
        self.canvas = Canvas(self.window, width=cols*self.colWidth+2, height=rows*self.rowHeight+2)
        self.canvas.pack()
        # containers of the GridWindow elements
        self.rectangle = {}
        self.text = {}
        # The coordinate of the square that currently has focus
        # A square's coordinate is stored as a tuple (row, col),
        # where row and col are integers in the range 0 to 9
        self.focus = None
        # These are the keyboard keys that can be used to clear a
        # square. Right now, these are space, backspace and enter.
        # self.clearkey = [13, 8, 32]
        # Updated March 2009 based on
        #  http://infohost.nmt.edu/tcc/help/pubs/tkinter/key-names.html 
        #  and a simple experiment printing out event.keycode
        #  keycode(SPACE)     = 65
        #  keycode(BACKSPACE) = 22
        #  keycode(ENTER)     = 36
        self.clearkey = [65, 22, 36]
        self.controller = controller
        for row in range(0, self.rows):
        	for col in range(0, self.cols):
        		self.rectangle[(row, col)] = \
        		self.canvas.create_rectangle(2+colWidth*col, 2+rowHeight*row, 2+colWidth*(col+1), 2+rowHeight*(row+1), fill="White")   
        		self.text[(row, col)] = \
        		self.canvas.create_text(2+colWidth*(col+0.5), 2+rowHeight*(row+0.5), text=str(""))
        		# show coordinates in cells
        		# note how on a Tkinter Canvas, (x,y) coordinate (0,0) is the top left corner
        
    def setNumber(self, location, number):
        """ Sets a number in the specified square """
        itemId = self.text[location]
        if number == None:
        	number = ""
        self.canvas.itemconfigure(itemId, text=number)
        
    def setColour(self, location, colour):
        """ Sets the colour of the specified square"""
        itemId = self.rectangle[location]
        self.canvas.itemconfigure(itemId, fill=colour)
        
    def onClick(self, event):
        """ Called when a square is clicked on
         Sets its background (fill) colour"""
        row = (event.y - 2) / self.rowHeight 
        col = (event.x - 2) / self.colWidth
                        
        if row >= 0 and row < self.rows and col >= 0 and col < self.cols:
        	if (self.focus != None):
        		self.setColour(self.focus, self.squareColourOutFocus)                
        	self.focus = (row, col)
        	self.setColour(self.focus, self.squareColourInFocus)
        
    def onKey(self, event):
        """ Called when a keyboard key is pressed
         (when this Soduko window has the focus)"""
        if self.focus != None:
        	if "123456789".find(event.char) != -1:
        		newValue = event.char
        	elif event.keycode in self.clearkey:
        		newValue = ""
        	else:
        		return
        
        	self.controller.makePlay(self.focus, newValue)
        
    def onClose(self):
        """ Called when a particular window is closed."""
        self.controller.closeGridWindow(self)
        self.window.destroy()
        
    def boardStateChanged(self, board):
        for i in range(0, self.rows):
        	for j in range(0, self.cols):
        		self.setNumber((i, j), board.getCell((i, j)))
        
    
