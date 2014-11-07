
import Command

class SudokuCommand(Command.Command):
    def __init__(self, board, position, oldValue, newValue):
        self.position = position
        self.oldValue = oldValue
        self.newValue = newValue
        self.solvable = False
        self.board = board
        pass
        
    def do(self):
        self.board.setCell(self.position, self.newValue)
        
    def undo(self):
        self.board.setCell(self.position, self.oldValue)
        
    
