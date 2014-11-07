
import GridWindow

class ColWindow(GridWindow.GridWindow):
    def __init__(self, master, controller, rowOffset, colOffset):
        super(ColWindow, self).__init__(master, controller, 9, 1, rowOffset, colOffset)
        pass
        
    
