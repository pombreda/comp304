"""
__Entity3.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: Denis Dube
Modified: Mon May 16 13:07:59 2005
_________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Appearance import *
from ATOM3List import *
from ATOM3Connection import *
from ATOM3Attribute import *
from ATOM3Enum import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Float import *
from ATOM3Link import *
from ATOM3Boolean import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *
from graph_Entity3 import *
class Entity3(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_Entity3
      self.isGraphObjectVisual = True
      self.parent = parent
      self.name=ATOM3String('Entity_')
      self.keyword_= self.name
      self.Graphical_Appearance=ATOM3Appearance()
      self.Graphical_Appearance.setValue( (self.keyword_.toString(), self))
      self.cardinality=ATOM3List([ 0, 1, 0, 0],ATOM3Connection)
      lcobj0=[]
      self.cardinality.setValue(lcobj0)
      self.attributes=ATOM3List([ 1, 1, 1, 0],ATOM3Attribute,parent.types )
      lcobj0=[]
      self.attributes.setValue(lcobj0)
      self.Constraints=ATOM3List([ 1, 1, 1, 0],ATOM3Constraint)
      lcobj0=[]
      self.Constraints.setValue(lcobj0)
      self.Actions=ATOM3List([ 1, 1, 1, 0],ATOM3Action)
      lcobj0=[]
      self.Actions.setValue(lcobj0)
      self.display=ATOM3Text('\n', 60,15 )
      self.displaySelect=ATOM3MSEnum(['attributes', 'constraints', 'actions', 'cardinality'], [0,0,0,0], 0, 1)
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'Graphical_Appearance': ('ATOM3Appearance', ),
                                  'cardinality': ('ATOM3List', 'ATOM3Connection'),
                                  'attributes': ('ATOM3List', 'ATOM3Attribute'),
                                  'Constraints': ('ATOM3List', 'ATOM3Constraint'),
                                  'Actions': ('ATOM3List', 'ATOM3Action'),
                                  'display': ('ATOM3Text', ),
                                  'displaySelect': ('ATOM3MSEnum', )      }
      self.realOrder = ['name','Graphical_Appearance','cardinality','attributes','Constraints','Actions','display','displaySelect']
      self.directEditing = [1,1,1,1,1,1,0,1]
   def clone(self):
      cloneObject = Entity3( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      cloneObject.keyword_ = cloneObject.name
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.name
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if actionID == self.EDIT:
         res = self.checkKeywordValidity(params)
         if res: return res
      if actionID == self.EDIT:
         res = self.checkNameValidity(params)
         if res: return res
      if actionID == self.CONNECT:
         res = self.classes2relationships(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def checkKeywordValidity(self, params):
      attrs = self.attributes.getValue()
      numKeys = 0
      for attr in attrs:
        name, selType, ivalue, key, dirEditing = attr.getValue()
        if key[1] == 1:
            numKeys = numKeys + 1
            if numKeys > 1:
              return ("This entity has more than one keyword", self.graphObject_)
            if selType != "String":
              return ("Keyword ("+name+") is not a string", self.graphObject_)
      return None
      

   def checkNameValidity(self, params):
      import string
      if not self.name.isNone():
        vname = self.name.getValue()
        # check if we have a name
        if (not vname) or (vname == ""):                 # the name is mandatory
            return "Entity name must be specified"
        # now check that the name is valid (a variable name)
        if string.count(vname, " ") > 0:
            return "Invalid entity name, no white spaces allowed"
        # check first character
        if (vname[0] >= '0') and (vname[0] <= '9'):              # a number
            return "Invalid variable name, first character must be a letter or '_'"
        if vname[0] != '_' and (vname[0]<'A' or vname[0]>'z'):
            return "Invalid entity name, first character must be a letter or '_'"
        # now check for the rest of not allowed characters...
        for c in range(len(vname)-1):
            if vname[c+1] < 'A' or vname[c+1] > 'z':              # not a letter
              if vname[c+1] < '0' or vname[c+1] > '9':           # not a number
                  if vname[c+1] != '_':                                # not underscore
                    return ("Invalid entity name, character '"+vname[c+1]+"' is not allowed", self.graphObject_)
      return None
      
      

   def classes2relationships(self, params):
      for c in self.in_connections_:
        if c.getClass() != 'Relationship3':
            return ( c.toString(), 'is not a relationship' )
      for c in self.out_connections_:
        if c.getClass() != 'Relationship3':
            return ( c.toString(), 'is not a relationship' )
      return None
      
      

   def preAction (self, actionID, * params):
      if actionID == self.EDIT:
         self.storeKeyword(params)
      if actionID == self.DELETE:
         self.removeFromRelationships(params)
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if actionID == self.CONNECT:
         self.addCardinality(params)
      if actionID == self.EDIT:
         self.updateGraphics(params)
      if actionID == self.DISCONNECT:
         self.removeConnection(params)
      if actionID == self.EDIT:
         self.updateRelationships(params)
      if actionID == self.EDIT or actionID == self.CONNECT or actionID == self.DISCONNECT:
         self.displayList(params)
      if actionID == self.EDIT or actionID == self.CREATE or actionID == self.CONNECT or actionID == self.DISCONNECT:
         self.fitText(params)
      if actionID == self.EDIT or actionID == self.CONNECT:
         self.fixConnections(params)
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None
   def storeKeyword(self, params):
      self.oldKeyword = self.keyword_.toString()
      

   def addCardinality(self, params):
      # see if we are source or destination
      direction = params[0]
      if direction == "SOURCE&DESTINATION":
          at3c = ATOM3Connection(self.out_connections_[len(self.out_connections_)-1])
          at3c.direction.setValue((None,0))                   # set value of direction
          self.cardinality.newItem( at3c )
          at3c = ATOM3Connection(self.in_connections_[len(self.in_connections_)-1])
          at3c.direction.setValue((None,1))                   # set value of direction
          self.cardinality.newItem( at3c )
      elif direction == "SOURCE":
          at3c = ATOM3Connection(self.out_connections_[len(self.out_connections_)-1])
          at3c.direction.setValue((None,0))                   # set value of direction
      else:
          at3c = ATOM3Connection(self.in_connections_[len(self.in_connections_)-1])
          at3c.direction.setValue((None,1))                   # set value of direction
      self.cardinality.newItem( at3c )
      

   def updateGraphics(self, params):
      self.Graphical_Appearance.updateGraphicalFile(self.keyword_.toString())
      
      

   def removeFromRelationships(self, params):
      for rel in self.in_connections_:
        cards = rel.cardinality.getValue()				# obtain the list of relationshp's cardinalities
        counter = 0							# an auxiliary counter
        for card in cards:
            name, direction, min, max = card.getValue()
            if name == self.name.toString() and direction[1] == 1:		# if that's me
              rel.cardinality.deleteItem(counter)
              break
            counter = counter + 1
      for rel in self.out_connections_:
        cards = rel.cardinality.getValue()				# obtain the list of relationshp's cardinalities
        counter = 0							# an auxiliary counter
        for card in cards:
            name, direction, min, max = card.getValue()
            if name == self.name.toString() and direction[1] == 0:		# if that's me
              rel.cardinality.deleteItem(counter)
              break
            counter = counter + 1
      

   def removeConnection(self, params):
      object    = params[0]
      if params[1] == "SOURCE": direct = "Source"
      else: direct = "Destination"
      
      cards = self.cardinality.getValue()				# obtain the list of cardinalities
      counter = 0
      for card in cards:
          name, direction, min, max = card.getValue()
          if name == object.name.toString() and direction[0][direction[1]] == direct:		# if that's me
            self.cardinality.deleteItem(counter)
            break
          counter = counter + 1
      

   def updateRelationships(self, params):
      for rel in self.in_connections_:
        cards = rel.cardinality.getValue()
        for card in cards:
            name, direction, min, max = card.getValue()
            if name == self.oldKeyword and direction[1] == 0:
              card.setValue((self, None, None, None))
              break
      for rel in self.out_connections_:
        cards = rel.cardinality.getValue()
        for card in cards:
            name, direction, min, max = card.getValue()
            if name == self.oldKeyword and direction[1] == 1:
              card.setValue((self, None, None, None))
              break
      

   def displayList(self, params):
      bullet = '  - '
      bulletPre = '  < '
      bulletPost = '  > ' 
      text = ''
      d = self.displaySelect.getValueAsDict()
      
      # Add stuff to the displayable text, depending on if it is hidden or not
      if( d.has_key( 'attributes' ) and d[ 'attributes' ] == False and len( self.attributes.getValue() ) > 0 ):	
      	text += 'Attributes:\n'
      	for item in self.attributes.getValue():
      		val = item.getValue()
      		text += bullet + val[0] + ' :: ' + val[1] + '\n'
      
      if( d.has_key( 'constraints' ) and d[ 'constraints' ] == False and len( self.Constraints.getValue() ) > 0 ):	
      	text += 'Constraints:\n'
      	for item in self.Constraints.getValue():
      		val = item.getValue()
      		if( val[2][1] == 0 ): text += bulletPre
      		else: text += bulletPost
      		text += val[0] + '\n'
      
      if( d.has_key( 'actions' ) and d[ 'actions' ] == False and len( self.Actions.getValue() ) > 0 ):		
      	text += 'Actions:\n'
      	for item in self.Actions.getValue():
      		val = item.getValue()
      		if( val[2][1] == 0 ): text += bulletPre
      		else: text += bulletPost
      		text += val[0]  + '\n'
      
      if( d.has_key( 'cardinality' ) and d[ 'cardinality' ] == False and len( self.cardinality.getValue() ) > 0 ):	
      	text += 'Cardinalities:\n'
      	for item in self.cardinality.getValue():
      		val = item.getValue()
      		if( val[1][1] == 0 ): text += bullet + 'To '
      		else: text += bullet + 'From '
      		text += val[0] + ': ' + val[2] + ' to ' + val[3] + '\n'
      
      self.display.setValue( text )
      
      if( self.graphObject_ ): self.graphObject_.ModifyAttribute( 'display',  text )  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      

   def fitText(self, params):
      obj = self.graphObject_
      if( not obj ): return
      
      # Input to the fitNode2Text2 method is as follows:
      # String, GraphForm of the String attribute, GraphForm of the rectangle container, Fudge factor
      # NOTE: Fudge factor is two optional parameters: scale X and scale Y
      textGFtupleList = []
      textGFtupleList.append( (self.name.getValue(), obj.gf9, obj.gf8, 1.2 ) )
      textGFtupleList.append( (self.display.getValue(), obj.gf68, obj.gf12, 1.05, 1.05 ) )
      
      obj.fitNodeToText2( textGFtupleList )
      
      
      
      
      
      
      
      
      
      
      
      
      

   def fixConnections(self, params):
      # After re-sizing, arrows may not line up unless we do this
      from Utilities import optimizeConnectionPorts
      optimizeConnectionPorts( self.parent )
      



