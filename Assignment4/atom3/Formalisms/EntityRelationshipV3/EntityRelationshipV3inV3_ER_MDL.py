"""
__EntityRelationshipV3inV3_ER_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Denis Dube
Modified: Mon May 16 13:07:56 2005
_________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Entity3 import *
from Relationship3 import *
from graph_Entity3 import *
from graph_Relationship3 import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def EntityRelationshipV3inV3_ER_MDL(self, rootNode, EntityRelationshipV3RootNode=None):

    # --- Generating attributes code for ASG EntityRelationshipV3 ---
    if( EntityRelationshipV3RootNode ): 
        # attributes
        EntityRelationshipV3RootNode.attributes.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('')
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('Annonymous')
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Text('\n', 60,15 )
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('attributes', 'List', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Attribute,self.types )
        lcobj2=[]
        cobj2=ATOM3Attribute(self.types)
        cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
        cobj2.initialValue=ATOM3String('')
        lcobj2.append(cobj2)
        cobj2=ATOM3Attribute(self.types)
        cobj2.setValue(('author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
        cobj2.initialValue=ATOM3String('Annonymous')
        lcobj2.append(cobj2)
        cobj2=ATOM3Attribute(self.types)
        cobj2.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
        cobj2.initialValue=ATOM3Text('\n', 60,15 )
        lcobj2.append(cobj2)
        cobj1.initialValue.setValue(lcobj2)
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('constraints', 'List', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Constraint)
        lcobj2=[]
        cobj1.initialValue.setValue(lcobj2)
        lcobj1.append(cobj1)
        EntityRelationshipV3RootNode.attributes.setValue(lcobj1)

        # author
        EntityRelationshipV3RootNode.author.setValue('Denis')

        # description
        EntityRelationshipV3RootNode.description.setValue('A truly boostrapping Entity Relationship model\n\nThis model is: EntityRelationship version 3\nIt was created in formalism: EntityRelationship version 3\n\nBeautiful no? \n\nThe big advantage, of course, is that if want to make modifications to the ER formalism (like I did so that I could add a text-fitting post-action), it can be done right in this model, and then you just  code re-generate the formalism. NO MORE CODE HACKING :D\n')

        # name
        EntityRelationshipV3RootNode.name.setValue('EntityRelationshipV3')

        # constraints
        EntityRelationshipV3RootNode.constraints.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        EntityRelationshipV3RootNode.constraints.setValue(lcobj1)
    # --- ASG attributes over ---


    self.obj23=Entity3(self)
    self.obj23.isGraphObjectVisual = True


    # name
    self.obj23.name.setValue('Entity3')

    # displaySelect
    self.obj23.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj23.displaySelect.config = 0

    # Actions
    self.obj23.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('storeKeyword', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.oldKeyword = self.keyword_.toString()\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('addCardinality', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '# see if we are source or destination\ndirection = params[0]\nif direction == "SOURCE&DESTINATION":\n    at3c = ATOM3Connection(self.out_connections_[len(self.out_connections_)-1])\n    at3c.direction.setValue((None,0))                   # set value of direction\n    self.cardinality.newItem( at3c )\n    at3c = ATOM3Connection(self.in_connections_[len(self.in_connections_)-1])\n    at3c.direction.setValue((None,1))                   # set value of direction\n    self.cardinality.newItem( at3c )\nelif direction == "SOURCE":\n    at3c = ATOM3Connection(self.out_connections_[len(self.out_connections_)-1])\n    at3c.direction.setValue((None,0))                   # set value of direction\nelse:\n    at3c = ATOM3Connection(self.in_connections_[len(self.in_connections_)-1])\n    at3c.direction.setValue((None,1))                   # set value of direction\nself.cardinality.newItem( at3c )\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('updateGraphics', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.Graphical_Appearance.updateGraphicalFile(self.keyword_.toString())\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('removeFromRelationships', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 'for rel in self.in_connections_:\n  cards = rel.cardinality.getValue()				# obtain the list of relationshp\'s cardinalities\n  counter = 0							# an auxiliary counter\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.name.toString() and direction[1] == 1:		# if that\'s me\n        rel.cardinality.deleteItem(counter)\n        break\n      counter = counter + 1\nfor rel in self.out_connections_:\n  cards = rel.cardinality.getValue()				# obtain the list of relationshp\'s cardinalities\n  counter = 0							# an auxiliary counter\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.name.toString() and direction[1] == 0:		# if that\'s me\n        rel.cardinality.deleteItem(counter)\n        break\n      counter = counter + 1\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('removeConnection', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]), 'object    = params[0]\nif params[1] == "SOURCE": direct = "Source"\nelse: direct = "Destination"\n\ncards = self.cardinality.getValue()				# obtain the list of cardinalities\ncounter = 0\nfor card in cards:\n    name, direction, min, max = card.getValue()\n    if name == object.name.toString() and direction[0][direction[1]] == direct:		# if that\'s me\n      self.cardinality.deleteItem(counter)\n      break\n    counter = counter + 1\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('updateRelationships', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'for rel in self.in_connections_:\n  cards = rel.cardinality.getValue()\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.oldKeyword and direction[1] == 0:\n        card.setValue((self, None, None, None))\n        break\nfor rel in self.out_connections_:\n  cards = rel.cardinality.getValue()\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.oldKeyword and direction[1] == 1:\n        card.setValue((self, None, None, None))\n        break\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('displayList', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]), 'bullet = \'  - \'\nbulletPre = \'  < \'\nbulletPost = \'  > \' \ntext = \'\'\nd = self.displaySelect.getValueAsDict()\n\n# Add stuff to the displayable text, depending on if it is hidden or not\nif( d.has_key( \'attributes\' ) and d[ \'attributes\' ] == False and len( self.attributes.getValue() ) > 0 ):	\n	text += \'Attributes:\\n\'\n	for item in self.attributes.getValue():\n		val = item.getValue()\n		text += bullet + val[0] + \' :: \' + val[1] + \'\\n\'\n\nif( d.has_key( \'constraints\' ) and d[ \'constraints\' ] == False and len( self.Constraints.getValue() ) > 0 ):	\n	text += \'Constraints:\\n\'\n	for item in self.Constraints.getValue():\n		val = item.getValue()\n		if( val[2][1] == 0 ): text += bulletPre\n		else: text += bulletPost\n		text += val[0] + \'\\n\'\n\nif( d.has_key( \'actions\' ) and d[ \'actions\' ] == False and len( self.Actions.getValue() ) > 0 ):		\n	text += \'Actions:\\n\'\n	for item in self.Actions.getValue():\n		val = item.getValue()\n		if( val[2][1] == 0 ): text += bulletPre\n		else: text += bulletPost\n		text += val[0]  + \'\\n\'\n\nif( d.has_key( \'cardinality\' ) and d[ \'cardinality\' ] == False and len( self.cardinality.getValue() ) > 0 ):	\n	text += \'Cardinalities:\\n\'\n	for item in self.cardinality.getValue():\n		val = item.getValue()\n		if( val[1][1] == 0 ): text += bullet + \'To \'\n		else: text += bullet + \'From \'\n		text += val[0] + \': \' + val[2] + \' to \' + val[3] + \'\\n\'\n\nself.display.setValue( text )\n\nif( self.graphObject_ ): self.graphObject_.ModifyAttribute( \'display\',  text )  \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('fitText', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]), 'obj = self.graphObject_\nif( not obj ): return\n\n# Input to the fitNode2Text2 method is as follows:\n# String, GraphForm of the String attribute, GraphForm of the rectangle container, Fudge factor\n# NOTE: Fudge factor is two optional parameters: scale X and scale Y\ntextGFtupleList = []\ntextGFtupleList.append( (self.name.getValue(), obj.gf9, obj.gf8, 1.2 ) )\ntextGFtupleList.append( (self.display.getValue(), obj.gf68, obj.gf12, 1.05, 1.05 ) )\n\nobj.fitNodeToText2( textGFtupleList )\n\n\n\n\n\n\n\n\n\n\n\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('fixConnections', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '# After re-sizing, arrows may not line up unless we do this\nfrom Utilities import optimizeConnectionPorts\noptimizeConnectionPorts( self.parent )\n'))
    lcobj2.append(cobj2)
    self.obj23.Actions.setValue(lcobj2)

    # Graphical_Appearance
    self.obj23.Graphical_Appearance.setValue( ('Entity3', self.obj23))

    # attributes
    self.obj23.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Entity_')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Graphical_Appearance', 'Appearance', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Appearance()
    cobj2.initialValue.setValue( ('class0', None))
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 0, 1, 0, self.types],ATOM3Connection)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attributes', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Attribute,self.types )
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Constraints', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Constraint)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Actions', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Action)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('display', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n', 60,15 )
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('displaySelect', 'MSEnum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3MSEnum(['attributes', 'constraints', 'actions', 'cardinality'],[0,0,0,0],1,1)
    lcobj2.append(cobj2)
    self.obj23.attributes.setValue(lcobj2)

    # cardinality
    self.obj23.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Relationship3', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Relationship3', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj23.cardinality.setValue(lcobj2)

    # display
    self.obj23.display.setValue('Attributes:\n  - name :: String\n  - Graphical_Appearance :: Appearance\n  - cardinality :: List\n  - attributes :: List\n  - Constraints :: List\n  - Actions :: List\n  - display :: Text\n  - displaySelect :: MSEnum\nConstraints:\n  > checkKeywordValidity\n  > checkNameValidity\n  > classes2relationships\nActions:\n  < storeKeyword\n  > addCardinality\n  > updateGraphics\n  < removeFromRelationships\n  > removeConnection\n  > updateRelationships\n  > displayList\n  > fitText\n  > fixConnections\nCardinalities:\n  - To Relationship3: 0 to N\n  - From Relationship3: 0 to N\n')

    # Constraints
    self.obj23.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('checkKeywordValidity', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'attrs = self.attributes.getValue()\nnumKeys = 0\nfor attr in attrs:\n  name, selType, ivalue, key, dirEditing = attr.getValue()\n  if key[1] == 1:\n      numKeys = numKeys + 1\n      if numKeys > 1:\n        return ("This entity has more than one keyword", self.graphObject_)\n      if selType != "String":\n        return ("Keyword ("+name+") is not a string", self.graphObject_)\nreturn None\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('checkNameValidity', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import string\nif not self.name.isNone():\n  vname = self.name.getValue()\n  # check if we have a name\n  if (not vname) or (vname == ""):                 # the name is mandatory\n      return "Entity name must be specified"\n  # now check that the name is valid (a variable name)\n  if string.count(vname, " ") > 0:\n      return "Invalid entity name, no white spaces allowed"\n  # check first character\n  if (vname[0] >= \'0\') and (vname[0] <= \'9\'):              # a number\n      return "Invalid variable name, first character must be a letter or \'_\'"\n  if vname[0] != \'_\' and (vname[0]<\'A\' or vname[0]>\'z\'):\n      return "Invalid entity name, first character must be a letter or \'_\'"\n  # now check for the rest of not allowed characters...\n  for c in range(len(vname)-1):\n      if vname[c+1] < \'A\' or vname[c+1] > \'z\':              # not a letter\n        if vname[c+1] < \'0\' or vname[c+1] > \'9\':           # not a number\n            if vname[c+1] != \'_\':                                # not underscore\n              return ("Invalid entity name, character \'"+vname[c+1]+"\' is not allowed", self.graphObject_)\nreturn None\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('classes2relationships', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'for c in self.in_connections_:\n  if c.getClass() != \'Relationship3\':\n      return ( c.toString(), \'is not a relationship\' )\nfor c in self.out_connections_:\n  if c.getClass() != \'Relationship3\':\n      return ( c.toString(), \'is not a relationship\' )\nreturn None\n\n'))
    lcobj2.append(cobj2)
    self.obj23.Constraints.setValue(lcobj2)

    self.obj23.graphClass_= graph_Entity3
    if self.genGraphics:
       new_obj = graph_Entity3(420.0,188.0,self.obj23)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Entity3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.8101226993865032, 5.5213483146067421]
    else: new_obj = None
    self.obj23.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj23)
    self.globalAndLocalPostcondition(self.obj23, rootNode)

    self.obj24=Relationship3(self)
    self.obj24.isGraphObjectVisual = True


    # name
    self.obj24.name.setValue('Relationship3')

    # displaySelect
    self.obj24.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj24.displaySelect.config = 0

    # Actions
    self.obj24.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('storeKeyword', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.oldKeyword = self.keyword_.toString()\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('updateGraphics', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.Graphical_Appearance.updateGraphicalFile(self.keyword_.toString())\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('removeCardinalitiesFromEntities', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 'for ent in self.in_connections_:\n  cards = ent.cardinality.getValue()				# obtain the list of relationshp\'s cardinalities\n  counter = 0							# an auxiliary counter\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.name.toString() and direction[1] == 0:		# if that\'s me\n        ent.cardinality.deleteItem(counter)\n        break\n      counter = counter + 1\nfor ent in self.out_connections_:\n  cards = ent.cardinality.getValue()				# obtain the list of relationshp\'s cardinalities\n  counter = 0							# an auxiliary counter\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.name.toString() and direction[1] == 1:		# if that\'s me\n        ent.cardinality.deleteItem(counter)\n        break\n      counter = counter + 1\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('removeConnection', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]), 'object    = params[0]\nif object == None:						# that means its myself!!\n    object = self\nif params[1] == "SOURCE": direct = "Source"\nelse: direct = "Destination"\ncards = self.cardinality.getValue()				# obtain the list of cardinalities\ncounter = 0\nfor card in cards:\n    name, direction, min, max = card.getValue()\n    if name == object.name.toString() and direction[0][direction[1]] == direct:		# if that\'s me\n      self.cardinality.deleteItem(counter)\n      break\n    counter = counter + 1\nif self == object:						# have to remove the other part...\n    if direct == "Source": direct = "Destination"\n    else: direct = "Source"\n    cards = self.cardinality.getValue()				# obtain the list of cardinalities\n    counter = 0\n    for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == object.name.toString() and direction[0][direction[1]] == direct:		# if that\'s me\n          self.cardinality.deleteItem(counter)\n          break\n      counter = counter + 1\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('addCardinality', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '# see if we are source or destination\ndirection = params[0]\nif direction == "SOURCE&DESTINATION":\n    at3c = ATOM3Connection(self.out_connections_[len(self.out_connections_)-1])\n    at3c.direction.setValue((None,0))                   # set value of direction\n    self.cardinality.newItem( at3c )\n    at3c = ATOM3Connection(self.in_connections_[len(self.in_connections_)-1])\n    at3c.direction.setValue((None,1))                   # set value of direction\n    self.cardinality.newItem( at3c )\nelif direction == "SOURCE":\n    at3c = ATOM3Connection(self.out_connections_[len(self.out_connections_)-1])\n    at3c.direction.setValue((None,0))                   # set value of direction\nelse:\n    at3c = ATOM3Connection(self.in_connections_[len(self.in_connections_)-1])\n    at3c.direction.setValue((None,1))                   # set value of direction\nself.cardinality.newItem( at3c )\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('updateRelationships', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'for rel in self.in_connections_:\n  cards = rel.cardinality.getValue()\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.oldKeyword and direction[1] == 0:\n        card.setValue((self, None, None, None))\n        break\nfor rel in self.out_connections_:\n  cards = rel.cardinality.getValue()\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.oldKeyword and direction[1] == 1:\n        card.setValue((self, None, None, None))\n        break\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('displayList', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'bullet = \'  - \'\nbulletPre = \'  < \'\nbulletPost = \'  > \' \ntext = \'\'\nd = self.displaySelect.getValueAsDict()\n\n# Add stuff to the displayable text, depending on if it is hidden or not\nif( d.has_key( \'attributes\' ) and d[ \'attributes\' ] == False and len( self.attributes.getValue() ) > 0 ):	\n	text += \'Attributes:\\n\'\n	for item in self.attributes.getValue():\n		val = item.getValue()\n		text += bullet + val[0] + \' :: \' + val[1] + \'\\n\'\n\nif( d.has_key( \'constraints\' ) and d[ \'constraints\' ] == False and len( self.Constraints.getValue() ) > 0 ):	\n	text += \'Constraints:\\n\'\n	for item in self.Constraints.getValue():\n		val = item.getValue()\n		if( val[2][1] == 0 ): text += bulletPre\n		else: text += bulletPost\n		text += val[0] + \'\\n\'\n\nif( d.has_key( \'actions\' ) and d[ \'actions\' ] == False and len( self.Actions.getValue() ) > 0 ):		\n	text += \'Actions:\\n\'\n	for item in self.Actions.getValue():\n		val = item.getValue()\n		if( val[2][1] == 0 ): text += bulletPre\n		else: text += bulletPost\n		text += val[0]  + \'\\n\'\n\nif( d.has_key( \'cardinality\' ) and d[ \'cardinality\' ] == False and len( self.cardinality.getValue() ) > 0 ):	\n	text += \'Cardinalities:\\n\'\n	for item in self.cardinality.getValue():\n		val = item.getValue()\n		if( val[1][1] == 0 ): text += bullet + \'To \'\n		else: text += bullet + \'From \'\n		text += val[0] + \': \' + val[2] + \' to \' + val[3] + \'\\n\'\n\nself.display.setValue( text )\n\nif( self.graphObject_ ): self.graphObject_.ModifyAttribute( \'display\',  text )  \n\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('fitText', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'obj = self.graphObject_\nif( not obj ): return\nobj = obj.centerObject\nif( not obj ): return\n\n# String, GraphForm with string, Containing Rectangle GraphForm, Fudge factor\ntextGFtupleList = []\ntextGFtupleList.append( (self.name.getValue(), obj.gf3, obj.gf9, 1.2 ) )\ntextGFtupleList.append( (self.display.getValue(), obj.gf11, obj.gf12, 1.05, 1.05 ) )\n\nobj.fitNodeToText2( textGFtupleList )\n\n\n\n\n\n'))
    lcobj2.append(cobj2)
    self.obj24.Actions.setValue(lcobj2)

    # Graphical_Appearance
    self.obj24.Graphical_Appearance.setValue( ('Relationship3', self.obj24))
    self.obj24.Graphical_Appearance.linkInfo=linkEditor(self,self.obj24.Graphical_Appearance.semObject, "Relationship3")
    self.obj24.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('Relationship3_1stLink', self.obj24.Graphical_Appearance.linkInfo.FirstLink))
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('blue')
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('Relationship3_1stSegment', self.obj24.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj24.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj24.Graphical_Appearance.linkInfo.Center.setValue( ('Relationship3_Center', self.obj24.Graphical_Appearance.linkInfo))
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('blue')
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('Relationship3_2ndSegment', self.obj24.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj24.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(15)
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(9)
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('Relationship3_2ndLink', self.obj24.Graphical_Appearance.linkInfo.SecondLink))
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj24.Graphical_Appearance.semObject
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj24.Graphical_Appearance.semObject
    self.obj24.Graphical_Appearance.linkInfo.Center.semObject=self.obj24.Graphical_Appearance.semObject
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj24.Graphical_Appearance.semObject
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj24.Graphical_Appearance.semObject

    # attributes
    self.obj24.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Relationship_')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Graphical_Appearance', 'Link', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Link()
    cobj2.initialValue.setValue( ('None', None))
    cobj2.initialValue.linkInfo=linkEditor(self,cobj2.initialValue.semObject, "Relationship3")
    cobj2.initialValue.linkInfo.FirstLink= stickylink()
    cobj2.initialValue.linkInfo.FirstLink.arrow=ATOM3Boolean()
    cobj2.initialValue.linkInfo.FirstLink.arrow.setValue((' ', 0))
    cobj2.initialValue.linkInfo.FirstLink.arrow.config = 0
    cobj2.initialValue.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    cobj2.initialValue.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    cobj2.initialValue.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    cobj2.initialValue.linkInfo.FirstLink.decoration=ATOM3Appearance()
    cobj2.initialValue.linkInfo.FirstLink.decoration.setValue( ('Relationship3_1stLink', cobj2.initialValue.linkInfo.FirstLink))
    cobj2.initialValue.linkInfo.FirstSegment= widthXfillXdecoration()
    cobj2.initialValue.linkInfo.FirstSegment.width=ATOM3Integer(2)
    cobj2.initialValue.linkInfo.FirstSegment.fill=ATOM3String('black')
    cobj2.initialValue.linkInfo.FirstSegment.stipple=ATOM3String('')
    cobj2.initialValue.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    cobj2.initialValue.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    cobj2.initialValue.linkInfo.FirstSegment.arrow.config = 0
    cobj2.initialValue.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    cobj2.initialValue.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    cobj2.initialValue.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    cobj2.initialValue.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    cobj2.initialValue.linkInfo.FirstSegment.decoration.setValue( ('Relationship3_1stSegment', cobj2.initialValue.linkInfo.FirstSegment))
    cobj2.initialValue.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    cobj2.initialValue.linkInfo.Center=ATOM3Appearance()
    cobj2.initialValue.linkInfo.Center.setValue( ('Relationship3_Center', cobj2.initialValue.linkInfo))
    cobj2.initialValue.linkInfo.SecondSegment= widthXfillXdecoration()
    cobj2.initialValue.linkInfo.SecondSegment.width=ATOM3Integer(2)
    cobj2.initialValue.linkInfo.SecondSegment.fill=ATOM3String('black')
    cobj2.initialValue.linkInfo.SecondSegment.stipple=ATOM3String('')
    cobj2.initialValue.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    cobj2.initialValue.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    cobj2.initialValue.linkInfo.SecondSegment.arrow.config = 0
    cobj2.initialValue.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    cobj2.initialValue.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    cobj2.initialValue.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    cobj2.initialValue.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    cobj2.initialValue.linkInfo.SecondSegment.decoration.setValue( ('Relationship3_2ndSegment', cobj2.initialValue.linkInfo.SecondSegment))
    cobj2.initialValue.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    cobj2.initialValue.linkInfo.SecondLink= stickylink()
    cobj2.initialValue.linkInfo.SecondLink.arrow=ATOM3Boolean()
    cobj2.initialValue.linkInfo.SecondLink.arrow.setValue((' ', 1))
    cobj2.initialValue.linkInfo.SecondLink.arrow.config = 0
    cobj2.initialValue.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    cobj2.initialValue.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    cobj2.initialValue.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    cobj2.initialValue.linkInfo.SecondLink.decoration=ATOM3Appearance()
    cobj2.initialValue.linkInfo.SecondLink.decoration.setValue( ('Relationship3_2ndLink', cobj2.initialValue.linkInfo.SecondLink))
    cobj2.initialValue.linkInfo.FirstLink.decoration.semObject=cobj2.initialValue.semObject
    cobj2.initialValue.linkInfo.FirstSegment.decoration.semObject=cobj2.initialValue.semObject
    cobj2.initialValue.linkInfo.Center.semObject=cobj2.initialValue.semObject
    cobj2.initialValue.linkInfo.SecondSegment.decoration.semObject=cobj2.initialValue.semObject
    cobj2.initialValue.linkInfo.SecondLink.decoration.semObject=cobj2.initialValue.semObject
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 0, 1, 0, self.types],ATOM3Connection)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attributes', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Attribute,self.types )
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Constraints', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Constraint)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Actions', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Action)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('display', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n', 60,15 )
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('displaySelect', 'MSEnum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3MSEnum(['attributes', 'constraints', 'actions', 'cardinality'],[0,0,0,0],1,1)
    lcobj2.append(cobj2)
    self.obj24.attributes.setValue(lcobj2)

    # cardinality
    self.obj24.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Entity3', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Entity3', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj24.cardinality.setValue(lcobj2)

    # display
    self.obj24.display.setValue('Attributes:\n  - name :: String\n  - Graphical_Appearance :: Link\n  - cardinality :: List\n  - attributes :: List\n  - Constraints :: List\n  - Actions :: List\n  - display :: Text\n  - displaySelect :: MSEnum\nConstraints:\n  > relationships2classes\n  > checkKeywordValidity\n  > checkNameValidity\nActions:\n  < storeKeyword\n  > updateGraphics\n  > removeCardinalitiesFromEntities\n  > removeConnection\n  > addCardinality\n  > updateRelationships\n  > displayList\n  > fitText\nCardinalities:\n  - From Entity3: 1 to N\n  - To Entity3: 1 to N\n')

    # Constraints
    self.obj24.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('relationships2classes', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'for c in self.in_connections_:\n  if c.getClass() != \'Entity3\' and c.getClass() != \'Relationship3\':\n      return ( c.keyword_.toString(), \'bad object type\' )\nfor c in self.out_connections_:\n  if c.getClass() != \'Entity3\' and c.getClass() != \'Relationship3\':\n      return ( c.keyword_.toString(), \'bad object type\' )\nreturn None\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('checkKeywordValidity', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'attrs = self.attributes.getValue()\nnumKeys = 0\nfor attr in attrs:\n  name, selType, ivalue, key, dirEditing = attr.getValue()\n  if key[1] == 1:\n      numKeys = numKeys + 1\n      if numKeys > 1:\n        return ("This entity has more than one keyword", self.graphObject_)\n      if selType != "String":\n        return ("Keyword ("+name+") is not a string", self.graphObject_)\nreturn None\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('checkNameValidity', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import string\nif not self.name.isNone:\n  vname = self.name.getValue()\n  # check if we have a name\n  if (not vname) or (vname == ""):                 # the name is mandatory\n    return "Relationship name must be specified"\n  # now check that the name is valid (a variable name)\n  if string.count(vname, " ") > 0:\n    return "Invalid relationship name, no white spaces allowed"\n  # check first character\n  if (vname[0] >= \'0\') and (vname[0] <= \'9\'):              # a number\n    return "Invalid variable name, first character must be a letter or \'_\'"\n  if vname[0] != \'_\' and (vname[0]<\'A\' or vname[0]>\'z\'):\n    return "Invalid relationship name, first character must be a letter or \'_\'"\n  # now check for the rest of not allowed characters...\n  for c in range(len(vname)-1):\n    if vname[c+1] < \'A\' or vname[c+1] > \'z\':              # not a letter\n        if vname[c+1] < \'0\' or vname[c+1] > \'9\':           # not a number\n          if vname[c+1] != \'_\':                                # not underscore\n              return ("Invalid relationship name, character \'"+vname[c+1]+"\' is not allowed", self.graphObject_)\nreturn None\n'))
    lcobj2.append(cobj2)
    self.obj24.Constraints.setValue(lcobj2)

    self.obj24.graphClass_= graph_Relationship3
    if self.genGraphics:
       new_obj = graph_Relationship3(220.0,288.0,self.obj24)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Relationship3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.75, 5.080645161290323]
    else: new_obj = None
    self.obj24.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24)
    self.globalAndLocalPostcondition(self.obj24, rootNode)
    self.drawConnections((self.obj23,self.obj24,[429.0, 347.42696629213481, 220.0, 348.0, 220.0, 288.0],"bezier", 3) )
    self.drawConnections((self.obj24,self.obj23,[220.0, 288.0, 220.0, 248.0, 429.0, 237.0],"bezier", 3) )
newfunction = EntityRelationshipV3inV3_ER_MDL

loadedMMName = 'EntityRelationshipV3_META'

atom3version = '0.3'
