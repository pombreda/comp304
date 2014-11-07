

import random

class SudokuBoardState(object):
    def __init__(self):
        self.state = {}
        self.observers = []
        for row in range(9):
        	for col in range(9):
        		self.state[(row, col)] = 0
        self.generate()
        
    def addObserver(self, observer):
        self.observers.append(observer)
        
    def removeObserver(self, observer):
        self.observers.remove(observer)
        
    def notifyObservers(self):
        for o in self.observers:
        	o.boardStateChanged(self)
        
    def setCell(self, position, value):
        if value != None:
        	try:
        		if int(value) not in range(1,10):
        			value = None
        	except ValueError:
        		value = None
        
        self.state[position] = value
        self.notifyObservers()
        
    def getCell(self, position):
        return self.state[position]
        
    def accept(self, visitor):
        visitor.visitBoard(self)
        
    def generate(self):
        puzzle = self.makepuzzle(self.solution([None] * 81))
        self.setBoard(puzzle)
        
    def solvable(self):
        if self.checkpuzzle(self.toBoard()) == -1:
        	return False
        else:
        	return True
        
    def solve(self):
            if(self.solvable() == False):
              return False
            state, answer = self.solveboard(self.toBoard())
            self.setBoard(answer)
            return True
        
    
    
    def setBoard(self, board):
    
    	for pos in range(81):
          if board[pos] != None:
            board[pos] = int(board[pos]) + 1
    
        for row in range(9):
          for col in range(9):
            self.setCell((row, col), board[9*row + col])
    
    def toBoard(self):
        board = [None] * 81
        for row in range(9):
          for col in range(9):
            board[9*row + col] = self.getCell((row, col))
        for pos in range(81):
          if board[pos] != None:
            board[pos] = int(board[pos]) - 1
        return board
    
    # Functions taken from http://davidbau.com/archives/2006/09/04/sudoku_generator.html (David Bau's Sudoku generator)
    
    def makepuzzle(self, board):
      puzzle = []; deduced = [None] * 81
      order = random.sample(xrange(81), 81)
      for pos in order:
        if deduced[pos] is None:
          puzzle.append((pos, board[pos]))
          deduced[pos] = board[pos]
          self.deduce(deduced)
      random.shuffle(puzzle)
      for i in xrange(len(puzzle) - 1, -1, -1):
        e = puzzle[i]; del puzzle[i]
        rating = self.checkpuzzle(self.boardforentries(puzzle), board)
        if rating == -1: puzzle.append(e)
      return self.boardforentries(puzzle)
    
    def ratepuzzle(self, puzzle, samples):
      total = 0
      for i in xrange(samples):
        state, answer = self.solveboard(puzzle)
        if answer is None: return -1
        total += len(state)
      return float(total) / samples
    
    def checkpuzzle(self, puzzle, board = None):
      state, answer = self.solveboard(puzzle)
      if answer is None: return -1
      if board is not None and not self.boardmatches(board, answer): return -1
      difficulty = len(state)
      state, second = self.solvenext(state)
      if second is not None: return -1
      return difficulty
    
    def solution(self, board):
      return self.solveboard(board)[1]
    
    def solveboard(self, original):
      board = list(original)
      guesses = self.deduce(board)
      if guesses is None: return ([], board)
      track = [(guesses, 0, board)]
      return self.solvenext(track)
    
    def solvenext(self, remembered):
      while len(remembered) > 0:
        guesses, c, board = remembered.pop()
        if c >= len(guesses): continue
        remembered.append((guesses, c + 1, board))
        workspace = list(board)
        pos, n = guesses[c]
        workspace[pos] = n
        guesses = self.deduce(workspace)
        if guesses is None: return (remembered, workspace)
        remembered.append((guesses, 0, workspace))
      return ([], None)
    
    def deduce(self, board):
      while True:
        stuck, guess, count = True, None, 0
        # fill in any spots determined by direct conflicts
        allowed, needed = self.figurebits(board)
        for pos in xrange(81):
          if None == board[pos]:
            numbers = self.listbits(allowed[pos])
            if len(numbers) == 0: return []
            elif len(numbers) == 1: board[pos] = numbers[0]; stuck = False
            elif stuck:
              guess, count = self.pickbetter(guess, count, [(pos, n) for n in numbers])
        if not stuck: allowed, needed = self.figurebits(board)
        # fill in any spots determined by elimination of other locations
        for axis in xrange(3):
          for x in xrange(9):
            numbers = self.listbits(needed[axis * 9 + x])
            for n in numbers:
              bit = 1 << n
              spots = []
              for y in xrange(9):
                pos = self.posfor(x, y, axis)
                if allowed[pos] & bit: spots.append(pos)
              if len(spots) == 0: return []
              elif len(spots) == 1: board[spots[0]] = n; stuck = False
              elif stuck:
                guess, count = self.pickbetter(guess, count, [(pos, n) for pos in spots])
        if stuck:
          if guess is not None: random.shuffle(guess)
          return guess
    
    def figurebits(self, board):
      allowed, needed = [e is None and 511 or 0 for e in board], []
      for axis in xrange(3):
        for x in xrange(9):
          bits = self.axismissing(board, x, axis)
          needed.append(bits)
          for y in xrange(9):
            allowed[self.posfor(x, y, axis)] &= bits
      return allowed, needed
    
    def posfor(self, x, y, axis = 0):
      if axis == 0: return x * 9 + y
      elif axis == 1: return y * 9 + x
      else: return ((0,3,6,27,30,33,54,57,60)[x] + (0,1,2,9,10,11,18,19,20)[y])
    
    def axisfor(self, pos, axis):
      if axis == 0: return pos / 9
      elif axis == 1: return pos % 9
      else: return (pos / 27) * 3 + (pos / 3) % 3
    
    def axismissing(self, board, x, axis):
      bits = 0
      for y in xrange(9):
        e = board[self.posfor(x, y, axis)]
        if e is not None: bits |= 1 << e
      return 511 ^ bits
      
    def listbits(self, bits):
      return [y for y in xrange(9) if 0 != bits & 1 << y]
    
    def allowed(self, board, pos):
      bits = 511
      for axis in xrange(3):
        x = self.axisfor(pos, axis)
        bits &= self.axismissing(board, x, axis)
      return bits
    
    def pickbetter(self, b, c, t):
      if b is None or len(t) < len(b): return (t, 1)
      if len(t) > len(b): return (b, c)
      if random.randint(0, c) == 0: return (t, c + 1)
      else: return (b, c + 1)
    
    def entriesforboard(self, board):
      return [(pos, board[pos]) for pos in xrange(81) if board[pos] is not None]
    
    def boardforentries(self, entries):
      board = [None] * 81
      for pos, n in entries: board[pos] = n
      return board
    
    def boardmatches(self, b1, b2):
      for i in xrange(81):
        if b1[i] != b2[i]: return False
      return True
    
    def printcode(self, n):
      if n is None: return '_'
      return str(n + 1)
    
    def printboard(self, board):
      out = ""
      for row in xrange(9):
        for col in xrange(9):
          out += (""," "," ","  "," "," ","  "," "," ")[col]
          out += self.printcode(board[posfor(row, col)])
        out += ('\n','\n','\n\n','\n','\n','\n\n','\n','\n','\n')[row]
      return out
    
    def parseboard(self, str):
      result = []
      for w in str.split():
        for x in w:
          if x in '|-=+': continue
          if x in '123456789': result.append(int(x) - 1)
          else: result.append(None)
          if len(result) == 81: return result
