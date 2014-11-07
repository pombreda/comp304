
import GridWindow

class MainWindow(GridWindow.GridWindow):
    def __init__(self, master, controller):
        super(MainWindow, self).__init__(master, controller, 9, 9)
        for i in range(0,2):
        	# thick vertical dividing line every three squares
        	self.canvas.create_line(2+3*self.colWidth*(i+1), 2, 2+3*self.colWidth*(i+1), 2+9*self.rowHeight, width=self.dividerWidth)  
        	# thick horizontal dividing line every three squares
        	self.canvas.create_line(2, 2+3*self.rowHeight*(i+1), 2+9*self.colWidth, 2+3*self.rowHeight*(i+1), width=self.dividerWidth)
        
    
