"""
__graph_FBS_BLink.py___________________________________________________________

Automatically generated LINK for entity FBS_BLink
DO NOT MODIFY DIRECTLY
_______________________________________________________________________________
"""
from graphLink import *
from stickylink import *
from widthXfillXdecoration import *
class graph_FBS_BLink(graphLink):

   def __init__(self, xc, yc, semObject = None ):
      self.semObject = semObject
      self.semanticObject = semObject
      from linkEditor import *
      self.le=linkEditor(self,self.semObject, "FBS_BLink")
      # This is a non-visual link
      graphLink.__init__(self, xc, yc, self.le,semObject)
