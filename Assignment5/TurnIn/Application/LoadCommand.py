
import Command

class LoadCommand(Command.Command):
    def undo(self):
        self.board.state = self.state
        self.board.notifyObservers()
        
    def do(self):
        pass
        
    def __init__(self, board):
        super(LoadCommand, self).__init__()
        self.state = {}
        self.board = board
        for val in board.state:
        	self.state[val] = board.state[val]
        
    
