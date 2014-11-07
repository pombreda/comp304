"""
__graph_FSB_Link.py___________________________________________________________

Automatically generated LINK for entity FSB_Link
DO NOT MODIFY DIRECTLY
______________________________________________________________________________
"""
from graphLink import *
from stickylink import *
from widthXfillXdecoration import *
class graph_FSB_Link(graphLink):

   def __init__(self, xc, yc, semObject = None ):
      self.semObject = semObject
      self.semanticObject = semObject
      from linkEditor import *
      self.le=linkEditor(self,self.semObject, "FSB_Link")
      # This is a non-visual link
      graphLink.__init__(self, xc, yc, self.le,semObject)
