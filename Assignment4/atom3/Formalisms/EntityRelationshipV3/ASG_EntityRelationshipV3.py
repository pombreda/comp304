"""
__ASG_EntityRelationshipV3.py_____________________________________________________

Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)
Author: Denis Dube
Modified: Mon May 16 13:07:59 2005
__________________________________________________________________________________
"""
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Text import *
from ATOM3List import *
from ATOM3Attribute import *
from ATOM3Enum import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Float import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *
class ASG_EntityRelationshipV3(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'EntityRelationshipV3', ASGroot, ['ASG_EntityRelationshipV3' ,'Entity3' ,'Relationship3'])

      ATOM3Type.__init__(self)
      self.parent = parent
      self.name=ATOM3String('')
      self.keyword_= self.name
      self.author=ATOM3String('Annonymous')
      self.description=ATOM3Text('\n', 60,15 )
      self.attributes=ATOM3List([ 1, 1, 1, 0],ATOM3Attribute,parent.types )
      lcobj0=[]
      cobj0=ATOM3Attribute(parent.types)
      cobj0.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
      cobj0.initialValue=ATOM3String('')
      lcobj0.append(cobj0)
      cobj0=ATOM3Attribute(parent.types)
      cobj0.setValue(('author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
      cobj0.initialValue=ATOM3String('Annonymous')
      lcobj0.append(cobj0)
      cobj0=ATOM3Attribute(parent.types)
      cobj0.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
      cobj0.initialValue=ATOM3Text('\n', 60,15 )
      lcobj0.append(cobj0)
      self.attributes.setValue(lcobj0)
      self.constraints=ATOM3List([ 1, 1, 1, 0],ATOM3Constraint)
      lcobj0=[]
      self.constraints.setValue(lcobj0)
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'author': ('ATOM3String', ),
                                  'description': ('ATOM3Text', ),
                                  'attributes': ('ATOM3List', 'ATOM3Attribute'),
                                  'constraints': ('ATOM3List', 'ATOM3Constraint')      }
      self.realOrder = ['name','author','description','attributes','constraints']
      self.directEditing = [1,1,1,1,1]
   def clone(self):
      return self
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.name
   def open(self, parent, topWindowParent):
       from ATOM3 import *
       a = ATOM3(topWindowParent, 'EntityRelationshipV3', 0, 1, self)
       #self.writeContents(a)
       return a
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def preAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None


