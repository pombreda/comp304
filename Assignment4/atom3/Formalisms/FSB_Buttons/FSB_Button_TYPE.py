from Tkinter             import *
from ATOM3Type           import *
from Operator            import *
from LeafType             import *
from TypeName            import *
from ModelType           import *
from ASG_TypesMetaModel import *
from ATOM3Text import ATOM3Text
from iconPathXaction import iconPathXaction

class FSB_Button_TYPE (iconPathXaction):
  def createTypeGraph(self, atom3i, rootNode):
    self.types = atom3i.types

    self.obj203=TypeName(atom3i)
    self.obj203.preAction( rootNode.CREATE )
    self.obj203.isGraphObjectVisual = True

    if(hasattr(self.obj203, '_setHierarchicalLink')):
      self.obj203._setHierarchicalLink(False)

    # Name
    self.obj203.Name.setValue('FSB_Button_TYPE')

    self.obj203.graphClass_= graph_TypeName
    if atom3i.genGraphics:
       new_obj = graph_TypeName(60.0,80.0,self.obj203)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj203.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj203)
    self.obj203.postAction( rootNode.CREATE )

    self.obj204=LeafType(atom3i)
    self.obj204.preAction( rootNode.CREATE )
    self.obj204.isGraphObjectVisual = True

    if(hasattr(self.obj204, '_setHierarchicalLink')):
      self.obj204._setHierarchicalLink(False)

    # TypeConstraint
    self.obj204.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))

    # Type
    self.obj204.Type.setValue(('iconPath', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj204.Type.initialValue=ATOM3String('', 20)
    self.obj204.Type.isDerivedAttribute = False

    self.obj204.graphClass_= graph_LeafType
    if atom3i.genGraphics:
       new_obj = graph_LeafType(220.0,100.0,self.obj204)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj204.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj204)
    self.obj204.postAction( rootNode.CREATE )

    self.obj205=LeafType(atom3i)
    self.obj205.preAction( rootNode.CREATE )
    self.obj205.isGraphObjectVisual = True

    if(hasattr(self.obj205, '_setHierarchicalLink')):
      self.obj205._setHierarchicalLink(False)

    # TypeConstraint
    self.obj205.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))

    # Type
    self.obj205.Type.setValue(('action', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj205.Type.initialValue=ATOM3Text('# Button action code\n# The following is generated for you: \n# def action(self): # self = ATOM3 instance\n# Typical contents of action:\n# newPlace = self.createNew<CLASS NAME IN META-MODEL>(self, wherex, wherey)\n# Action that shows dialog to edit ASG attributes:\n# self.modelAttributes(self.ASGroot.getASGbyName("<META-MODEL NAME>_META")) \n', 80,15 )
    self.obj205.Type.isDerivedAttribute = False

    self.obj205.graphClass_= graph_LeafType
    if atom3i.genGraphics:
       new_obj = graph_LeafType(220.0,180.0,self.obj205)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj205.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj205)
    self.obj205.postAction( rootNode.CREATE )

    self.obj206=Operator(atom3i)
    self.obj206.preAction( rootNode.CREATE )
    self.obj206.isGraphObjectVisual = True

    if(hasattr(self.obj206, '_setHierarchicalLink')):
      self.obj206._setHierarchicalLink(False)
      
      
    self.obj40=LeafType(atom3i)
    self.obj40.preAction( rootNode.CREATE )
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # TypeConstraint
    self.obj40.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))

    # Type
    self.obj40.Type.setValue(('takesActionImmediately', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj40.Type.initialValue=ATOM3Boolean()
    self.obj40.Type.initialValue.setValue(('', 0))
    self.obj40.Type.initialValue.config = 1
    self.obj40.Type.isDerivedAttribute = False

    self.obj40.graphClass_= graph_LeafType
    if atom3i.genGraphics:
       new_obj = graph_LeafType(220.0,240.0,self.obj40)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.obj40.postAction( rootNode.CREATE )
    

    # type
    self.obj206.type.setValue( (['X', 'U', '->'], 0) )
    self.obj206.type.config = 0

    self.obj206.graphClass_= graph_Operator
    if atom3i.genGraphics:
       new_obj = graph_Operator(188.0,107.5,self.obj206)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj206.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj206)
    self.obj206.postAction( rootNode.CREATE )

    self.obj203.out_connections_.append(self.obj206)
    self.obj206.in_connections_.append(self.obj203)
    self.obj203.graphObject_.pendingConnections.append((self.obj203.graphObject_.tag, self.obj206.graphObject_.tag, [136.0, 96.0, 188.0, 107.5], 2, 1))
    self.obj206.out_connections_.append(self.obj204)
    self.obj204.in_connections_.append(self.obj206)
    self.obj206.graphObject_.pendingConnections.append((self.obj206.graphObject_.tag, self.obj204.graphObject_.tag, [240.0, 119.0, 188.0, 107.5], 2, 1))
    self.obj206.out_connections_.append(self.obj205)
    self.obj205.in_connections_.append(self.obj206)
    self.obj206.graphObject_.pendingConnections.append((self.obj206.graphObject_.tag, self.obj205.graphObject_.tag, [240.0, 199.0, 188.0, 107.5], 2, 1))


