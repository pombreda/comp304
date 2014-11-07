class SudokuSaver
!!!147297.python!!!	visitBoard(in self : , in board : )
for value in board.state:
	if board.state[value] == None:
		self.file.write("0")
	else:
		self.file.write(str(board.state[value]))
	self.file.write(" ")
!!!147297.python!!!	visitBoard(in self : , in board : )
for i in range(10):
	for j in range(10):
		if board.state[(i,j)] == None:
			self.file.write("0")
		else:
			self.file.write(str(board.state[(i,j)]))
		self.file.write(" ")
!!!147297.python!!!	visitBoard(in self : , in board : )
for i in range(9):
	for j in range(9):
		if board.state[(i,j)] == None:
			self.file.write("0")
		else:
			self.file.write(str(board.state[(i,j)]))
		self.file.write(" ")
