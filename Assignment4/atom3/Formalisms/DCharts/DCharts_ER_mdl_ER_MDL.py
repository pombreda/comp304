"""
__DCharts_ER_mdl_ER_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Denis Dube
Modified: Wed Nov 30 11:48:18 2005
_______________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from ERentity import *
from ERrelationship import *
from graph_ERrelationship import *
from graph_ERentity import *
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

def DCharts_ER_mdl_ER_MDL(self, rootNode, EntityRelationshipRootNode=None):

    # --- Generating attributes code for ASG EntityRelationship ---
    if( EntityRelationshipRootNode ): 
        # attributes
        EntityRelationshipRootNode.attributes.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('variables', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Text('\n', 80,15 )
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('event_clauses', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Text('\n', 80,15 )
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('misc', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
        cobj1.initialValue=ATOM3Text('\n', 80,15 )
        lcobj1.append(cobj1)
        EntityRelationshipRootNode.attributes.setValue(lcobj1)

        # name
        EntityRelationshipRootNode.name.setValue('DCharts')

        # constraints
        EntityRelationshipRootNode.constraints.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        EntityRelationshipRootNode.constraints.setValue(lcobj1)
    # --- ASG attributes over ---


    self.obj50=ERentity(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # attributes
    self.obj50.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Composite')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('is_default', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('visible', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('auto_adjust', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('enter_action', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('', 60,15 )
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('exit_action', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('', 60,15 )
    lcobj2.append(cobj2)
    self.obj50.attributes.setValue(lcobj2)

    # cardinality
    self.obj50.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Hyperedge', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Hyperedge', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('orthogonality', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('contains', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj50.cardinality.setValue(lcobj2)

    # appearance
    self.obj50.appearance.setValue( ('Composite', self.obj50))

    # name
    self.obj50.name.setValue('Composite')

    # constraints
    self.obj50.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Composite_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Composite_CREATE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Composite_DRAG', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), 'import DCharts_utils\nDCharts_utils.Composite_DRAG(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Composite_MOVE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 'import DCharts_utils\nDCharts_utils.Composite_MOVE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Composite_DROP', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), 'import DCharts_utils\nDCharts_utils.Composite_DROP(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Composite_EDIT', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Composite_EDIT(self)\n'))
    lcobj2.append(cobj2)
    self.obj50.constraints.setValue(lcobj2)

    self.obj50.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(47.0,149.7,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.8199999999999998, 1.4800000000000002]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)

    self.obj51=ERentity(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # attributes
    self.obj51.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Basic')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('is_default', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('enter_action', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 60,15 )
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('exit_action', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 60,15 )
    lcobj2.append(cobj2)
    self.obj51.attributes.setValue(lcobj2)

    # cardinality
    self.obj51.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('contains', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Hyperedge', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Hyperedge', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj51.cardinality.setValue(lcobj2)

    # appearance
    self.obj51.appearance.setValue( ('Basic', self.obj51))

    # name
    self.obj51.name.setValue('Basic')

    # constraints
    self.obj51.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Basic_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Basic_CREATE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Basic_DRAG', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), 'import DCharts_utils\nDCharts_utils.Basic_DRAG(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Basic_DROP', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), 'import DCharts_utils\nDCharts_utils.Basic_DROP(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Basic_MOVE', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 'import DCharts_utils\nDCharts_utils.Basic_MOVE(self)\n'))
    lcobj2.append(cobj2)
    self.obj51.constraints.setValue(lcobj2)

    self.obj51.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(456.0,170.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.7800000000000002, 1.2100000000000002]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)

    self.obj52=ERentity(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # attributes
    self.obj52.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('is_default', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('History')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('star', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    self.obj52.attributes.setValue(lcobj2)

    # cardinality
    self.obj52.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('contains', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Hyperedge', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Hyperedge', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj52.cardinality.setValue(lcobj2)

    # appearance
    self.obj52.appearance.setValue( ('History', self.obj52))

    # name
    self.obj52.name.setValue('History')

    # constraints
    self.obj52.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('History_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.History_CREATE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('History_DRAG', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), 'import DCharts_utils\nDCharts_utils.History_DRAG(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('History_DROP', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), 'import DCharts_utils\nDCharts_utils.History_DROP(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('History_MOVE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 'import DCharts_utils\nDCharts_utils.History_MOVE(self)\n'))
    lcobj2.append(cobj2)
    self.obj52.constraints.setValue(lcobj2)

    self.obj52.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(456.0,290.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.8400000000000001, 1.02]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)

    self.obj53=ERentity(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # attributes
    self.obj53.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Orthogonal')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('visible', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('auto_adjust', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    self.obj53.attributes.setValue(lcobj2)

    # cardinality
    self.obj53.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('orthogonality', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj53.cardinality.setValue(lcobj2)

    # appearance
    self.obj53.appearance.setValue( ('Orthogonal', self.obj53))

    # name
    self.obj53.name.setValue('Orthogonal')

    # constraints
    self.obj53.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Orthogonal_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Orthogonal_CREATE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Orthogonal_DRAG', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), 'import DCharts_utils\nDCharts_utils.Orthogonal_DRAG(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Orthogonal_MOVE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 'import DCharts_utils\nDCharts_utils.Orthogonal_MOVE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Orthogonal_DROP', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), 'import DCharts_utils\nDCharts_utils.Orthogonal_DROP(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Orthogonal_EDIT', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Orthogonal_EDIT(self)\n'))
    lcobj2.append(cobj2)
    self.obj53.constraints.setValue(lcobj2)

    self.obj53.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(456.0,410.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.8300000000000007, 1.1000000000000001]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)

    self.obj54=ERentity(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # attributes
    self.obj54.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('contains_links_visible', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Composite_default_height', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(50.0)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Composite_default_width', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Float(50.0)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('contains_color', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('pink')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('orthogonality_links_visible', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('orthogonality_color', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('lightblue')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Hyperedge_links_visible', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Hyperedge_color', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('darkblue')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Composite_color', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('darkblue')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Orthogonal_color', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('darkgray')
    lcobj2.append(cobj2)
    self.obj54.attributes.setValue(lcobj2)

    # cardinality
    self.obj54.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj54.cardinality.setValue(lcobj2)

    # appearance
    self.obj54.appearance.setValue( ('visual_settings', self.obj54))

    # name
    self.obj54.name.setValue('visual_settings')

    # constraints
    self.obj54.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('apply_settings', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.visual_settings_EDIT_CREATE(self)\n'))
    lcobj2.append(cobj2)
    self.obj54.constraints.setValue(lcobj2)

    self.obj54.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(20.0,620.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.6100000000000017, 2.5299999999999976]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)

    self.obj55=ERentity(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # attributes
    self.obj55.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Port')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('is_in', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('is_out', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    self.obj55.attributes.setValue(lcobj2)

    # cardinality
    self.obj55.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('connection', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj55.cardinality.setValue(lcobj2)

    # appearance
    self.obj55.appearance.setValue( ('Port', self.obj55))

    # name
    self.obj55.name.setValue('Port')

    # constraints
    self.obj55.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj55.constraints.setValue(lcobj2)

    self.obj55.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(779.0,30.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.6000000000000005, 0.97999999999999998]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)

    self.obj56=ERentity(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # attributes
    self.obj56.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('id', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Server')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name_pattern', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    self.obj56.attributes.setValue(lcobj2)

    # cardinality
    self.obj56.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('connection', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj56.cardinality.setValue(lcobj2)

    # appearance
    self.obj56.appearance.setValue( ('Server', self.obj56))

    # name
    self.obj56.name.setValue('Server')

    # constraints
    self.obj56.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj56.constraints.setValue(lcobj2)

    self.obj56.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(779.0,270.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.6700000000000006, 0.86999999999999988]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)

    self.obj57=ERrelationship(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # attributes
    self.obj57.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj57.attributes.setValue(lcobj2)

    # cardinality
    self.obj57.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Composite', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Basic', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('History', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Orthogonal', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Composite', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj57.cardinality.setValue(lcobj2)

    # appearance
    self.obj57.appearance.setValue( ('contains', self.obj57))
    self.obj57.appearance.linkInfo=linkEditor(self,self.obj57.appearance.semObject, "contains")
    self.obj57.appearance.linkInfo.FirstLink= stickylink()
    self.obj57.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj57.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj57.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj57.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj57.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj57.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj57.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj57.appearance.linkInfo.FirstLink.decoration.setValue( ('contains_1stLink', self.obj57.appearance.linkInfo.FirstLink))
    self.obj57.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj57.appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj57.appearance.linkInfo.FirstSegment.fill=ATOM3String('orange')
    self.obj57.appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj57.appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj57.appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj57.appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj57.appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj57.appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj57.appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj57.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj57.appearance.linkInfo.FirstSegment.decoration.setValue( ('contains_1stSegment', self.obj57.appearance.linkInfo.FirstSegment))
    self.obj57.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj57.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj57.appearance.linkInfo.Center.setValue( ('contains_Center', self.obj57.appearance.linkInfo))
    self.obj57.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj57.appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj57.appearance.linkInfo.SecondSegment.fill=ATOM3String('orange')
    self.obj57.appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj57.appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj57.appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj57.appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj57.appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj57.appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj57.appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj57.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj57.appearance.linkInfo.SecondSegment.decoration.setValue( ('contains_2ndSegment', self.obj57.appearance.linkInfo.SecondSegment))
    self.obj57.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj57.appearance.linkInfo.SecondLink= stickylink()
    self.obj57.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj57.appearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
    self.obj57.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj57.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
    self.obj57.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
    self.obj57.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
    self.obj57.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj57.appearance.linkInfo.SecondLink.decoration.setValue( ('contains_2ndLink', self.obj57.appearance.linkInfo.SecondLink))
    self.obj57.appearance.linkInfo.FirstLink.decoration.semObject=self.obj57.appearance.semObject
    self.obj57.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj57.appearance.semObject
    self.obj57.appearance.linkInfo.Center.semObject=self.obj57.appearance.semObject
    self.obj57.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj57.appearance.semObject
    self.obj57.appearance.linkInfo.SecondLink.decoration.semObject=self.obj57.appearance.semObject

    # name
    self.obj57.name.setValue('contains')

    # constraints
    self.obj57.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('contains_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.contains_CREATE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('contains_CONNECT', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.contains_CONNECT(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('contains_DELETE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.contains_DELETE(self)\n\n'))
    lcobj2.append(cobj2)
    self.obj57.constraints.setValue(lcobj2)

    self.obj57.graphClass_= graph_ERrelationship
    if self.genGraphics:
       new_obj = graph_ERrelationship(320.0,340.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)

    self.obj58=ERrelationship(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # attributes
    self.obj58.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('trigger', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('guard', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('1')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('action', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('', 60,15 )
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('broadcast', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('# return an instance of DEVSevent or None\nreturn None\n', 60,15 )
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('broadcast_to', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('display', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    self.obj58.attributes.setValue(lcobj2)

    # cardinality
    self.obj58.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Composite', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Composite', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Basic', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('History', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Basic', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('History', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    self.obj58.cardinality.setValue(lcobj2)

    # appearance
    self.obj58.appearance.setValue( ('Hyperedge', self.obj58))
    self.obj58.appearance.linkInfo=linkEditor(self,self.obj58.appearance.semObject, "Hyperedge")
    self.obj58.appearance.linkInfo.FirstLink= stickylink()
    self.obj58.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj58.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj58.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj58.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(3)
    self.obj58.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(6)
    self.obj58.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj58.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj58.appearance.linkInfo.FirstLink.decoration.setValue( ('Hyperedge_1stLink', self.obj58.appearance.linkInfo.FirstLink))
    self.obj58.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj58.appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj58.appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
    self.obj58.appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj58.appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj58.appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj58.appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj58.appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj58.appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj58.appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj58.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj58.appearance.linkInfo.FirstSegment.decoration.setValue( ('Hyperedge_1stSegment', self.obj58.appearance.linkInfo.FirstSegment))
    self.obj58.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj58.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj58.appearance.linkInfo.Center.setValue( ('Hyperedge_Center', self.obj58.appearance.linkInfo))
    self.obj58.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj58.appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj58.appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
    self.obj58.appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj58.appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj58.appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj58.appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj58.appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj58.appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj58.appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj58.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj58.appearance.linkInfo.SecondSegment.decoration.setValue( ('Hyperedge_2ndSegment', self.obj58.appearance.linkInfo.SecondSegment))
    self.obj58.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj58.appearance.linkInfo.SecondLink= stickylink()
    self.obj58.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj58.appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj58.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj58.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(6)
    self.obj58.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(9)
    self.obj58.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(6)
    self.obj58.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj58.appearance.linkInfo.SecondLink.decoration.setValue( ('Hyperedge_2ndLink', self.obj58.appearance.linkInfo.SecondLink))
    self.obj58.appearance.linkInfo.FirstLink.decoration.semObject=self.obj58.appearance.semObject
    self.obj58.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj58.appearance.semObject
    self.obj58.appearance.linkInfo.Center.semObject=self.obj58.appearance.semObject
    self.obj58.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj58.appearance.semObject
    self.obj58.appearance.linkInfo.SecondLink.decoration.semObject=self.obj58.appearance.semObject

    # name
    self.obj58.name.setValue('Hyperedge')

    # constraints
    self.obj58.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Hyperedge_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Hyperedge_CREATE(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Hyperedge_CONNECT', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Hyperedge_CONNECT(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Hyperedge_DELETE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Hyperedge_DELETE(self)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Hyperedge_DROP', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), 'import DCharts_utils\nDCharts_utils.Hyperedge_DROP(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('Hyperedge_MOVE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 'import DCharts_utils\nDCharts_utils.Hyperedge_MOVE(self)\n'))
    lcobj2.append(cobj2)
    self.obj58.constraints.setValue(lcobj2)

    self.obj58.graphClass_= graph_ERrelationship
    if self.genGraphics:
       new_obj = graph_ERrelationship(130.0,360.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)

    self.obj59=ERrelationship(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # attributes
    self.obj59.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj59.attributes.setValue(lcobj2)

    # cardinality
    self.obj59.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Composite', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Orthogonal', (('Source', 'Destination'), 0), '1', '1'))
    lcobj2.append(cobj2)
    self.obj59.cardinality.setValue(lcobj2)

    # appearance
    self.obj59.appearance.setValue( ('orthogonality', self.obj59))
    self.obj59.appearance.linkInfo=linkEditor(self,self.obj59.appearance.semObject, "orthogonality")
    self.obj59.appearance.linkInfo.FirstLink= stickylink()
    self.obj59.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj59.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj59.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj59.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj59.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj59.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj59.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj59.appearance.linkInfo.FirstLink.decoration.setValue( ('orthogonality_1stLink', self.obj59.appearance.linkInfo.FirstLink))
    self.obj59.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj59.appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj59.appearance.linkInfo.FirstSegment.fill=ATOM3String('red')
    self.obj59.appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj59.appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj59.appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj59.appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj59.appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj59.appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj59.appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj59.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj59.appearance.linkInfo.FirstSegment.decoration.setValue( ('orthogonality_1stSegment', self.obj59.appearance.linkInfo.FirstSegment))
    self.obj59.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj59.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj59.appearance.linkInfo.Center.setValue( ('orthogonality_Center', self.obj59.appearance.linkInfo))
    self.obj59.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj59.appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj59.appearance.linkInfo.SecondSegment.fill=ATOM3String('red')
    self.obj59.appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj59.appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj59.appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj59.appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj59.appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj59.appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj59.appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj59.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj59.appearance.linkInfo.SecondSegment.decoration.setValue( ('orthogonality_2ndSegment', self.obj59.appearance.linkInfo.SecondSegment))
    self.obj59.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj59.appearance.linkInfo.SecondLink= stickylink()
    self.obj59.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj59.appearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
    self.obj59.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj59.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
    self.obj59.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
    self.obj59.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
    self.obj59.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj59.appearance.linkInfo.SecondLink.decoration.setValue( ('orthogonality_2ndLink', self.obj59.appearance.linkInfo.SecondLink))
    self.obj59.appearance.linkInfo.FirstLink.decoration.semObject=self.obj59.appearance.semObject
    self.obj59.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj59.appearance.semObject
    self.obj59.appearance.linkInfo.Center.semObject=self.obj59.appearance.semObject
    self.obj59.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj59.appearance.semObject
    self.obj59.appearance.linkInfo.SecondLink.decoration.semObject=self.obj59.appearance.semObject

    # name
    self.obj59.name.setValue('orthogonality')

    # constraints
    self.obj59.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('orthogonality_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.orthogonality_CREATE(self)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('orthogonality_CONNECT', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.orthogonality_CONNECT(self)\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('orthogonality_DELETE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.orthogonality_DELETE(self)\n'))
    lcobj2.append(cobj2)
    self.obj59.constraints.setValue(lcobj2)

    self.obj59.graphClass_= graph_ERrelationship
    if self.genGraphics:
       new_obj = graph_ERrelationship(202.0,481.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)

    self.obj60=ERrelationship(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # attributes
    self.obj60.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('server_port', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('port')
    lcobj2.append(cobj2)
    self.obj60.attributes.setValue(lcobj2)

    # cardinality
    self.obj60.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Port', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Server', (('Source', 'Destination'), 0), '1', '1'))
    lcobj2.append(cobj2)
    self.obj60.cardinality.setValue(lcobj2)

    # appearance
    self.obj60.appearance.setValue( ('connection', self.obj60))
    self.obj60.appearance.linkInfo=linkEditor(self,self.obj60.appearance.semObject, "connection")
    self.obj60.appearance.linkInfo.FirstLink= stickylink()
    self.obj60.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj60.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj60.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj60.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj60.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj60.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj60.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj60.appearance.linkInfo.FirstLink.decoration.setValue( ('connection_1stLink', self.obj60.appearance.linkInfo.FirstLink))
    self.obj60.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj60.appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj60.appearance.linkInfo.FirstSegment.fill=ATOM3String('blue')
    self.obj60.appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj60.appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj60.appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj60.appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj60.appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj60.appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj60.appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj60.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj60.appearance.linkInfo.FirstSegment.decoration.setValue( ('connection_1stSegment', self.obj60.appearance.linkInfo.FirstSegment))
    self.obj60.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj60.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj60.appearance.linkInfo.Center.setValue( ('connection_Center', self.obj60.appearance.linkInfo))
    self.obj60.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj60.appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj60.appearance.linkInfo.SecondSegment.fill=ATOM3String('blue')
    self.obj60.appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj60.appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj60.appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj60.appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj60.appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj60.appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj60.appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj60.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj60.appearance.linkInfo.SecondSegment.decoration.setValue( ('connection_2ndSegment', self.obj60.appearance.linkInfo.SecondSegment))
    self.obj60.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj60.appearance.linkInfo.SecondLink= stickylink()
    self.obj60.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj60.appearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
    self.obj60.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj60.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
    self.obj60.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
    self.obj60.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
    self.obj60.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj60.appearance.linkInfo.SecondLink.decoration.setValue( ('connection_2ndLink', self.obj60.appearance.linkInfo.SecondLink))
    self.obj60.appearance.linkInfo.FirstLink.decoration.semObject=self.obj60.appearance.semObject
    self.obj60.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj60.appearance.semObject
    self.obj60.appearance.linkInfo.Center.semObject=self.obj60.appearance.semObject
    self.obj60.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj60.appearance.semObject
    self.obj60.appearance.linkInfo.SecondLink.decoration.semObject=self.obj60.appearance.semObject

    # name
    self.obj60.name.setValue('connection')

    # constraints
    self.obj60.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj60.constraints.setValue(lcobj2)

    self.obj60.graphClass_= graph_ERrelationship
    if self.genGraphics:
       new_obj = graph_ERrelationship(880.0,200.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)

    # Connections for obj50 (graphObject_: Obj0) named Composite
    self.drawConnections(
(self.obj50,self.obj57,[274.39999999999998, 287.5, 260.0, 320.0, 260.0, 340.0, 320.0, 340.0], 0, 4),
(self.obj50,self.obj58,[165.19999999999999, 287.5, 165.0, 361.0, 130.0, 360.0], 0, 3),
(self.obj50,self.obj59,[201.59999999999999, 287.5, 202.0, 481.0], 0, 2) )
    # Connections for obj51 (graphObject_: Obj1) named Basic
    self.drawConnections(
(self.obj51,self.obj58,[465.0, 267.39999999999998, 780.0, 267.0, 780.0, 560.0, 110.0, 560.0, 110.0, 360.0, 130.0, 360.0], 0, 6) )
    # Connections for obj52 (graphObject_: Obj2) named History
    self.drawConnections(
(self.obj52,self.obj58,[465.0, 359.39999999999998, 800.0, 380.0, 800.0, 540.0, 150.0, 540.0, 150.0, 360.0, 130.0, 360.0], 0, 6) )
    # Connections for obj53 (graphObject_: Obj3) named Orthogonal
    self.drawConnections(
(self.obj53,self.obj57,[465.0, 459.0, 320.0, 460.0, 320.0, 340.0], 0, 3) )
    # Connections for obj54 (graphObject_: Obj4) named visual_settings
    self.drawConnections(
 )
    # Connections for obj55 (graphObject_: Obj5) named Port
    self.drawConnections(
(self.obj55,self.obj60,[884.0, 137.80000000000001, 880.0, 200.0], 0, 2) )
    # Connections for obj56 (graphObject_: Obj6) named Server
    self.drawConnections(
 )
    # Connections for obj57 (graphObject_: Obj7) named contains
    self.drawConnections(
(self.obj57,self.obj51,[320.0, 340.0, 400.0, 340.0, 400.0, 220.0, 465.0, 267.39999999999998], 0, 4),
(self.obj57,self.obj52,[320.0, 340.0, 400.0, 260.0, 400.0, 360.0, 465.0, 318.60000000000002], 0, 4),
(self.obj57,self.obj50,[320.0, 340.0, 380.0, 220.0, 380.0, 201.0, 347.19999999999999, 228.29999999999998], 0, 4) )
    # Connections for obj58 (graphObject_: Obj9) named Hyperedge
    self.drawConnections(
(self.obj58,self.obj50,[130.0, 360.0, 92.0, 360.0, 92.400000000000006, 287.5], 0, 3),
(self.obj58,self.obj51,[130.0, 360.0, 130.0, 380.0, 30.0, 380.0, 30.0, 40.0, 450.0, 40.0, 450.0, 200.0, 465.0, 267.39999999999998], 0, 7),
(self.obj58,self.obj52,[130.0, 360.0, 50.0, 360.0, 50.0, 60.0, 430.0, 60.0, 430.0, 340.0, 465.0, 359.39999999999998], 0, 6) )
    # Connections for obj59 (graphObject_: Obj11) named orthogonality
    self.drawConnections(
(self.obj59,self.obj53,[202.0, 481.0, 465.0, 481.0], 0, 2) )
    # Connections for obj60 (graphObject_: Obj13) named connection
    self.drawConnections(
(self.obj60,self.obj56,[880.0, 200.0, 888.20000000000005, 284.19999999999999], 0, 2) )

newfunction = DCharts_ER_mdl_ER_MDL

loadedMMName = 'EntityRelationship'

atom3version = '0.3'
