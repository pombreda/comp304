
import SudokuVisitor

class SudokuSaver(SudokuVisitor.SudokuVisitor):
    def __init__(self, file):
        super(SudokuSaver, self).__init__()
        self.file = file
        pass
        
    def visitBoard(self, board):
        for i in range(9):
        	for j in range(9):
        		if board.state[(i,j)] == None:
        			self.file.write("0")
        		else:
        			self.file.write(str(board.state[(i,j)]))
        		self.file.write(" ")
        
    
