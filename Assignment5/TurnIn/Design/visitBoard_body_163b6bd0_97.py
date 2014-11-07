for i in range(9):
	for j in range(9):
		if board.state[(i,j)] == None:
			self.file.write("0")
		else:
			self.file.write(str(board.state[(i,j)]))
		self.file.write(" ")
