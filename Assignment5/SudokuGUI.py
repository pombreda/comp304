

from Tkinter import *
import tkFileDialog
import tkMessageBox
import tkFont

from collections import deque

from SudokuBoardState import SudokuBoardState
from GridWindow import GridWindow
from MainWindow import MainWindow
from RowWindow import RowWindow
from ColWindow import ColWindow
from BlockWindow import BlockWindow
from SudokuCommand import SudokuCommand
from LoadCommand import LoadCommand
from SudokuSaver import SudokuSaver

class SudokuGUI(object):
    def __init__(self, master):
        self.master = master
        self.board = SudokuBoardState()
        self.plays = []
        self.master.protocol("WM_DELETE_WINDOW", self.onQuit)
        
        frame = Frame(master)
        fileFrame = Frame(frame, borderwidth=5)
        self.btn_load = Button(fileFrame, width=15, text="Load from File", command=self.load)
        self.btn_load.config(state="active")
        self.btn_load.pack()
        self.btn_saveAs = Button(fileFrame, width=15, text="Save As", command=self.saveAs)
        self.btn_saveAs.config(state="active")
        self.btn_saveAs.pack()
        self.btn_save = Button(fileFrame, width=15, text="Save", command=self.save)
        self.btn_save.config(state="disabled") # disabled as long as no filename set (by previous "Save As")
        self.btn_save.pack()
        fileFrame.pack()
        undoFrame = Frame(frame, borderwidth=5)
        self.btn_undo = Button(undoFrame, width=15, text="Undo last", command=self.undo)
        self.btn_undo.pack()
        self.btn_undo_since_error = Button(undoFrame, width=15, text="Undo since error", command=self.undo_last_error)
        self.btn_undo_since_error.pack()
        undoFrame.pack()
        topFrame = Frame(frame, borderwidth=5)
        self.btn_open = Button(topFrame, width=15, text="Open Full Board", command=self.open_main_board)
        self.btn_open.pack()
        topFrame.pack()
                
        blockFrame = Frame(frame, borderwidth=5)
                
        frame_label = Frame(blockFrame)
        label = Label(frame_label, text="Open Block Windows")
        label.pack()
        frame_label.pack()
                
        frame_buttons = Frame(blockFrame)
        self.btn_open_block1 = Button(frame_buttons, text="(1,1)", command= lambda : self.open_block_board(0,0) )
        self.btn_open_block1.grid(row=0, column=0)
        self.btn_open_block2 = Button(frame_buttons, text="(1,2)", command= lambda : self.open_block_board(0,3) )
        self.btn_open_block2.grid(row=0, column=1)
        self.btn_open_block3 = Button(frame_buttons, text="(1,3)", command= lambda : self.open_block_board(0,6) )
        self.btn_open_block3.grid(row=0, column=2)
        self.btn_open_block4 = Button(frame_buttons, text="(2,1)", command= lambda : self.open_block_board(3,0) )
        self.btn_open_block4.grid(row=1, column=0)
        self.btn_open_block5 = Button(frame_buttons, text="(2,2)", command= lambda : self.open_block_board(3,3) )
        self.btn_open_block5.grid(row=1, column=1)
        self.btn_open_block6 = Button(frame_buttons, text="(2,3)", command= lambda : self.open_block_board(3,6) )
        self.btn_open_block6.grid(row=1, column=2)
        self.btn_open_block7 = Button(frame_buttons, text="(3,1)", command= lambda : self.open_block_board(6,0) )
        self.btn_open_block7.grid(row=2, column=0)
        self.btn_open_block8 = Button(frame_buttons, text="(3,2)", command= lambda : self.open_block_board(6,3) )
        self.btn_open_block8.grid(row=2, column=1)
        self.btn_open_block9 = Button(frame_buttons, text="(3,3)", command= lambda : self.open_block_board(6,6) )
        self.btn_open_block9.grid(row=2, column=2)
        frame_buttons.pack()
                
        blockFrame.pack()
                
        rowFrame = Frame(frame, borderwidth=5)
                
        frame_label = Frame(rowFrame)
        label = Label(frame_label, text="Open Row Windows")
        label.pack()
        frame_label.pack()
                
        frame_buttons = Frame(rowFrame)
        self.btn_open_block1 = Button(frame_buttons, text=" 1 ", command= lambda : self.open_row_board(0,0) )
        self.btn_open_block1.grid(row=0, column=0)
        self.btn_open_block2 = Button(frame_buttons, text=" 2 ", command= lambda : self.open_row_board(1,0) )
        self.btn_open_block2.grid(row=0, column=1)
        self.btn_open_block3 = Button(frame_buttons, text=" 3 ", command= lambda : self.open_row_board(2,0) )
        self.btn_open_block3.grid(row=0, column=2)
        self.btn_open_block4 = Button(frame_buttons, text=" 4 ", command= lambda : self.open_row_board(3,0) )
        self.btn_open_block4.grid(row=1, column=0)
        self.btn_open_block5 = Button(frame_buttons, text=" 5 ", command= lambda : self.open_row_board(4,0) )
        self.btn_open_block5.grid(row=1, column=1)
        self.btn_open_block6 = Button(frame_buttons, text=" 6 ", command= lambda : self.open_row_board(5,0) )
        self.btn_open_block6.grid(row=1, column=2)
        self.btn_open_block7 = Button(frame_buttons, text=" 7 ", command= lambda : self.open_row_board(6,0) )
        self.btn_open_block7.grid(row=2, column=0)
        self.btn_open_block8 = Button(frame_buttons, text=" 8 ", command= lambda : self.open_row_board(7,0) )
        self.btn_open_block8.grid(row=2, column=1)
        self.btn_open_block9 = Button(frame_buttons, text=" 9 ", command= lambda : self.open_row_board(8,0) )
        self.btn_open_block9.grid(row=2, column=2)
        frame_buttons.pack()
                
        rowFrame.pack()
                
        colFrame = Frame(frame, borderwidth=5)
                
        frame_label = Frame(colFrame)
        label = Label(frame_label, text="Open Column Windows")
        label.pack()
        frame_label.pack()
                
        frame_buttons = Frame(colFrame)
        self.btn_open_block1 = Button(frame_buttons, text=" 1 ", command= lambda : self.open_col_board(0,0) )
        self.btn_open_block1.grid(row=0, column=0)
        self.btn_open_block2 = Button(frame_buttons, text=" 2 ", command= lambda : self.open_col_board(0,1) )
        self.btn_open_block2.grid(row=0, column=1)
        self.btn_open_block3 = Button(frame_buttons, text=" 3 ", command= lambda : self.open_col_board(0,2) )
        self.btn_open_block3.grid(row=0, column=2)
        self.btn_open_block4 = Button(frame_buttons, text=" 4 ", command= lambda : self.open_col_board(0,3) )
        self.btn_open_block4.grid(row=1, column=0)
        self.btn_open_block5 = Button(frame_buttons, text=" 5 ", command= lambda : self.open_col_board(0,4) )
        self.btn_open_block5.grid(row=1, column=1)
        self.btn_open_block6 = Button(frame_buttons, text=" 6 ", command= lambda : self.open_col_board(0,5) )
        self.btn_open_block6.grid(row=1, column=2)
        self.btn_open_block7 = Button(frame_buttons, text=" 7 ", command= lambda : self.open_col_board(0,6) )
        self.btn_open_block7.grid(row=2, column=0)
        self.btn_open_block8 = Button(frame_buttons, text=" 8 ", command= lambda : self.open_col_board(0,7) )
        self.btn_open_block8.grid(row=2, column=1)
        self.btn_open_block9 = Button(frame_buttons, text=" 9 ", command= lambda : self.open_col_board(0,8) )
        self.btn_open_block9.grid(row=2, column=2)
        frame_buttons.pack()
                
        colFrame.pack()
                
        bottomFrame = Frame(frame, borderwidth=5)
        self.btn_quit = Button(bottomFrame, text="Quit", command=self.quit)
        self.btn_quit.pack()
        bottomFrame.pack()
                
        frame.pack()
        
    def open_main_board(self):
        newWindow = MainWindow(self.master, self)
        self.board.addObserver(newWindow)
        newWindow.boardStateChanged(self.board)
        
    def open_block_board(self, rowOffset, colOffset):
        newWindow = BlockWindow(self.master, self, rowOffset, colOffset)
        self.board.addObserver(newWindow)
        newWindow.boardStateChanged(self.board)
        
    def open_row_board(self, rowOffset, colOffset):
        newWindow = RowWindow(self.master, self, rowOffset, colOffset)
        self.board.addObserver(newWindow)
        newWindow.boardStateChanged(self.board)
        
    def open_col_board(self, rowOffset, colOffset):
        newWindow = ColWindow(self.master, self, rowOffset, colOffset)
        self.board.addObserver(newWindow)
        newWindow.boardStateChanged(self.board)
        
    def load(self):
        fileName = tkFileDialog.askopenfilename(defaultextension=".sdk", filetypes=[("Sudoku", "*.sdk"), ("All", "*")])
        
        try:
        	self.doLoad(fileName)
        except IOError:
        	tkMessageBox.showwarning("Load", "Unable to load the file")
        
        
    def doLoad(self, fileName):
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
        
    def saveAs(self):
        print "Saving to File"        
        fileName = tkFileDialog.asksaveasfilename(defaultextension=".sdk",filetypes=[("Sudoku", "*.sdk"),("All", "*")])
        self.__lastFileName = fileName
        self.btn_save.config(state="active")
        self.save()
        	
        
    def save(self):
        self.doSave(self.__lastFileName)
        
    def undo(self):
        try:
        	command = self.plays.pop()
        	command.undo()
        except IndexError:
        	pass
        
    def undo_last_error(self):
        try:
        	command = self.plays.pop()
        	while not command.solvable:
        		command.undo()
        		command = self.plays.pop()
        
        	self.plays.append(command)
        	self.board.notifyObservers()
        except IndexError:
        	pass
        	
        
    def quit(self):
        self.master.destroy()
        
    def onQuit(self):
        self.master.destroy()
        
    def accept(self, visitor):
        self.board.accept(visitor)
        
    def makePlay(self, location, value):
        old = self.board.getCell(location)
        command = SudokuCommand(self.board, location, old, value)
        command.do()
        command.solvable = self.board.solvable()
        self.plays.append(command)
        
    def closeGridWindow(self, window):
        self.board.removeObserver(window)
        
    def doSave(self, fileName):
        try:
        	file = open(fileName, "w+")
        	visitor = SudokuSaver(file)
        	self.accept(visitor)
        	file.close()
        except IOError:
        	self.btn_save.config(state="disabled")
        	tkMessageBox.showwarning("Save", "Unable to create the file")
        

if __name__ == '__main__':
    root = Tk()
    sudokuGui = SudokuGUI(root)
    
    root.title('Ultimate Sudoku')
    root.mainloop()  