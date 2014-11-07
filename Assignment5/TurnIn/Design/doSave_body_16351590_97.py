try:
	file = open(fileName, "w+")
	visitor = SudokuSaver(file)
	self.accept(visitor)
	file.close()
except IOError:
	self.btn_save.config(state="disabled")
	tkMessageBox.showwarning("Save", "Unable to create the file")
