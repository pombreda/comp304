"""Unit test for Sudoku application"""

from Tkinter import *
from BlockWindow import BlockWindow
from BoardStateObserver import BoardStateObserver
from ColWindow import ColWindow
from SudokuCommand import SudokuCommand
from GridWindow import GridWindow
from LoadCommand import LoadCommand
from MainWindow import MainWindow
from RowWindow import RowWindow
from SudokuBoardState import SudokuBoardState
from SudokuCommand import SudokuCommand
from SudokuGUI import SudokuGUI
from SudokuSaver import SudokuSaver
from SudokuVisitor import SudokuVisitor
import unittest

class ObserverTests(unittest.TestCase):

    def testSubscribeSuccess(self):
        """test that if an observer subscribes to a subject,
	   the observer is added to the subject's subscriptions"""
        state = SudokuBoardState()
	obs = BoardStateObserver()
	count1 = state.observers.count(obs)
	state.addObserver(obs)
	count2 = state.observers.count(obs)
        self.assertEqual(count2, count1 + 1)

    def testUnsubscribeSuccess(self):
        """test that if an observer unsubscribe to a subject,
	   the observer is removed to the subject's subscriptions"""
        state = SudokuBoardState()
	obs = BoardStateObserver()
	state.addObserver(obs)
	count1 = state.observers.count(obs)
	state.removeObserver(obs)
	count2 = state.observers.count(obs)
	if count1 == 0:
        	self.assertEqual(count2, 0)
	else:
		self.assertEqual(count2, count1 - 1)

    def testSubscriptionSanity(self):
        """test that if an observer is not subscribed to a subject,
	   and then it subscribes to then subjct,
	   and then unsubscribes from it,
	   the observer is not on the subject's subscription list"""
        state = SudokuBoardState()
	obs = BoardStateObserver()
	count1 = state.observers.count(obs)
	state.addObserver(obs)
	state.removeObserver(obs)
	count2 = state.observers.count(obs)
        self.assertEqual(count2, count1)

    def testObserveSuccess(self):
        """test that if the observer subscribes to a subject,
	   and we modify the state of the subject,
	   then the observer receives the updated state.

           In other words, test that if an observer is subscribed to a subject,
	   then if we change the subject's state,
	   it then sends a notify() call to the observer,
	   which then calls the subject with getState()
	   to retrieve the updated state, and then displays it."""
        state = SudokuBoardState()
	obs = BoardStateObserver()
	obs.boardStateChanged = lambda board: self.assertEqual(board.state[(0,0)], 1)
	state.addObserver(obs)
	
	state.setCell((0,0), 1)
        return True;

class CommandTests(unittest.TestCase):

    def testCommandSuccess(self):
        """test that if we modify a cell from the GUI window with a valid value,
	   the internal state of the sudoku board is also modified properly.

	   In other words, test that if an Invoker calls a Command/ConcreteCommand,
 	   the Command/ConcreteCommand calls the Receiver and modifies the state appropriately."""
        state = SudokuBoardState()
	state.setCell((0,0),None)
	command = SudokuCommand(state, (0, 0), 0, 5)
	self.assertEqual(state.getCell((0,0)), None)
	command.do()
	self.assertEqual(state.getCell((0,0)), 5)

    def testCommandFail(self):
        """test that if we modify a cell from the GUI window with an invalid value,
	   the internal state of the sudoku board is not changed."""
        state = SudokuBoardState()
	state.setCell((0,0),0)
	command = SudokuCommand(state, (0, 0), 0, 'a')
	self.assertEqual(state.getCell((0,0)), None)
	command.do()
	self.assertEqual(state.getCell((0,0)), None)

    def testUndoSuccess(self):
        """test that if we modify a cell value, and then call the undo() function,
	   then the initial and final states are identical"""
        state = SudokuBoardState()
	state.setCell((0,0),None)
	command = SudokuCommand(state, (0, 0), 0, 5)
	self.assertEqual(state.getCell((0,0)), None)
	command.do()
	self.assertEqual(state.getCell((0,0)), 5)
	command.undo()
	self.assertEqual(state.getCell((0,0)), None)


class VisitorTests(unittest.TestCase):

    def testVisitorSuccess(self):
        """test that if we save a sudoku board to a file,
	   and then load it from the same file,
	   the initial and final states of the board are identical.

	   In other words, test that our visitor interface
	   has all the calls needed to retrieve all the needed states it needs to visit,
	   and that it calls them successfully so that they are all saved in a file appropriately."""
	root = Tk()
	sudokuGui = SudokuGUI(root)
	#board = {}
	#for v in sudokuGui.board.state:
	#	board[v] = sudokuGui.board.state[v]
	board1 = [None] * 81
	board1 = sudokuGui.board.toBoard()
		
	sudokuGui.doSave("testSaveFile.sdk")
	sudokuGui.doLoad("testSaveFile.sdk")
	#for v in sudokuGui.board.state:
	#	self.assertEqual(board[v], sudokuGui.board.state[v])
	board2 = [None] * 81
	board2 = sudokuGui.board.toBoard()

	for v in range(0,81):
		self.assertEqual(board1[v], board2[v])



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
                          
