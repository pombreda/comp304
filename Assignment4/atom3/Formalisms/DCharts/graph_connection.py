"""
__graph_connection.py___________________________________________________________

Automatically generated LINK for entity connection
DO NOT MODIFY DIRECTLY
________________________________________________________________________________
"""
from graphLink import *
from stickylink import *
from widthXfillXdecoration import *
class graph_connection(graphLink):

   def __init__(self, xc, yc, semObject = None ):
      self.semObject = semObject
      self.semanticObject = semObject
      from linkEditor import *
      self.le=linkEditor(self,self.semObject, "connection")
      self.le.FirstLink= stickylink()
      self.le.FirstLink.arrow=ATOM3Boolean()
      self.le.FirstLink.arrow.setValue((' ', 0))
      self.le.FirstLink.arrow.config = 0
      self.le.FirstLink.arrowShape1=ATOM3Integer(0)
      self.le.FirstLink.arrowShape2=ATOM3Integer(0)
      self.le.FirstLink.arrowShape3=ATOM3Integer(0)
      self.le.FirstLink.decoration=ATOM3Appearance()
      self.le.FirstLink.decoration.setValue( ('connection_1stLink', self.le.FirstLink))
      self.le.FirstSegment= widthXfillXdecoration()
      self.le.FirstSegment.width=ATOM3Integer(2)
      self.le.FirstSegment.fill=ATOM3String('blue')
      self.le.FirstSegment.stipple=ATOM3String('')
      self.le.FirstSegment.arrow=ATOM3Boolean()
      self.le.FirstSegment.arrow.setValue((' ', 0))
      self.le.FirstSegment.arrow.config = 0
      self.le.FirstSegment.arrowShape1=ATOM3Integer(0)
      self.le.FirstSegment.arrowShape2=ATOM3Integer(0)
      self.le.FirstSegment.arrowShape3=ATOM3Integer(0)
      self.le.FirstSegment.decoration=ATOM3Appearance()
      self.le.FirstSegment.decoration.setValue( ('connection_1stSegment', self.le.FirstSegment))
      self.le.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.le.Center=ATOM3Appearance()
      self.le.Center.setValue( ('connection_Center', self.le))
      self.le.SecondSegment= widthXfillXdecoration()
      self.le.SecondSegment.width=ATOM3Integer(2)
      self.le.SecondSegment.fill=ATOM3String('blue')
      self.le.SecondSegment.stipple=ATOM3String('')
      self.le.SecondSegment.arrow=ATOM3Boolean()
      self.le.SecondSegment.arrow.setValue((' ', 0))
      self.le.SecondSegment.arrow.config = 0
      self.le.SecondSegment.arrowShape1=ATOM3Integer(0)
      self.le.SecondSegment.arrowShape2=ATOM3Integer(0)
      self.le.SecondSegment.arrowShape3=ATOM3Integer(0)
      self.le.SecondSegment.decoration=ATOM3Appearance()
      self.le.SecondSegment.decoration.setValue( ('connection_2ndSegment', self.le.SecondSegment))
      self.le.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.le.SecondLink= stickylink()
      self.le.SecondLink.arrow=ATOM3Boolean()
      self.le.SecondLink.arrow.setValue((' ', 0))
      self.le.SecondLink.arrow.config = 0
      self.le.SecondLink.arrowShape1=ATOM3Integer(0)
      self.le.SecondLink.arrowShape2=ATOM3Integer(0)
      self.le.SecondLink.arrowShape3=ATOM3Integer(0)
      self.le.SecondLink.decoration=ATOM3Appearance()
      self.le.SecondLink.decoration.setValue( ('connection_2ndLink', self.le.SecondLink))
      self.le.FirstLink.decoration.semObject=self.semObject
      self.le.FirstSegment.decoration.semObject=self.semObject
      self.le.Center.semObject=self.semObject
      self.le.SecondSegment.decoration.semObject=self.semObject
      self.le.SecondLink.decoration.semObject=self.semObject
      graphLink.__init__(self, xc, yc, self.le,semObject)
