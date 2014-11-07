file = open(fileName, "r")

command = LoadCommand(self.board)
self.plays.append(command)

self.__lastFileName = fileName
lines = file.readlines()
for line in lines:
	values = line.split(" ")
	i = 0
	j = 0

	for v in values:
		if v == "0":
			v = None
		else:
			v = str(v)
		self.board.setCell((i,j), v);
		j  = j + 1
		if j == 9:
			i = i + 1
			j = 0

file.close()
self.board.notifyObservers()
self.btn_save.config(state="active")
