# _ buttonFromRelationship3_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Relationship3 import *
from ASG_EntityRelationshipV3 import *
from Entity3 import *
class buttonFromRelationship3_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 2)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_EntityRelationshipV3(parent)

      self.obj49=Relationship3(parent)


      # name
      self.obj49.name.setValue('')
      self.obj49.name.setNone()

      # displaySelect
      self.obj49.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
      self.obj49.displaySelect.config = 0

      # Actions
      self.obj49.Actions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj49.Actions.setValue(lcobj2)
      self.obj49.Actions.setNone()

      # Graphical_Appearance
      self.obj49.Graphical_Appearance.setNone()

      # attributes
      self.obj49.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj49.attributes.setValue(lcobj2)
      self.obj49.attributes.setNone()

      # cardinality
      self.obj49.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj49.cardinality.setValue(lcobj2)
      self.obj49.cardinality.setNone()

      # display
      self.obj49.display.setValue('')

      # Constraints
      self.obj49.Constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj49.Constraints.setValue(lcobj2)
      self.obj49.Constraints.setNone()
      self.obj49.GGLabel.setValue(1)
      self.obj49.graphClass_= graph_Relationship3
      if parent.genGraphics:
         new_obj = graph_Relationship3(100.0,100.0,self.obj49)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj49.graphObject_ = new_obj
      self.LHS.addNode(self.obj49)
      self.RHS = ASG_EntityRelationshipV3(parent)

      self.obj51=Relationship3(parent)


      # name
      self.obj51.name.setValue('')
      self.obj51.name.setNone()

      # displaySelect
      self.obj51.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
      self.obj51.displaySelect.config = 0

      # Actions
      self.obj51.Actions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj51.Actions.setValue(lcobj2)
      self.obj51.Actions.setNone()

      # Graphical_Appearance
      self.obj51.Graphical_Appearance.setNone()

      # attributes
      self.obj51.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj51.attributes.setValue(lcobj2)
      self.obj51.attributes.setNone()

      # cardinality
      self.obj51.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj51.cardinality.setValue(lcobj2)
      self.obj51.cardinality.setNone()

      # display
      self.obj51.display.setValue('')

      # Constraints
      self.obj51.Constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj51.Constraints.setValue(lcobj2)
      self.obj51.Constraints.setNone()
      self.obj51.GGLabel.setValue(1)
      self.obj51.graphClass_= graph_Relationship3
      if parent.genGraphics:
         new_obj = graph_Relationship3(100.0,100.0,self.obj51)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj51.graphObject_ = new_obj
      self.obj510= AttrCalc()
      self.obj510.Copy=ATOM3Boolean()
      self.obj510.Copy.setValue(('Copy from LHS', 1))
      self.obj510.Copy.config = 0
      self.obj510.Specify=ATOM3Constraint()
      self.obj510.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj51.GGset2Any['name']= self.obj510
      self.obj511= AttrCalc()
      self.obj511.Copy=ATOM3Boolean()
      self.obj511.Copy.setValue(('Copy from LHS', 1))
      self.obj511.Copy.config = 0
      self.obj511.Specify=ATOM3Constraint()
      self.obj511.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj51.GGset2Any['Actions']= self.obj511
      self.obj512= AttrCalc()
      self.obj512.Copy=ATOM3Boolean()
      self.obj512.Copy.setValue(('Copy from LHS', 1))
      self.obj512.Copy.config = 0
      self.obj512.Specify=ATOM3Constraint()
      self.obj512.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj51.GGset2Any['Constraints']= self.obj512
      self.obj513= AttrCalc()
      self.obj513.Copy=ATOM3Boolean()
      self.obj513.Copy.setValue(('Copy from LHS', 1))
      self.obj513.Copy.config = 0
      self.obj513.Specify=ATOM3Constraint()
      self.obj513.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj51.GGset2Any['Graphical_Appearance']= self.obj513
      self.obj514= AttrCalc()
      self.obj514.Copy=ATOM3Boolean()
      self.obj514.Copy.setValue(('Copy from LHS', 1))
      self.obj514.Copy.config = 0
      self.obj514.Specify=ATOM3Constraint()
      self.obj514.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj51.GGset2Any['attributes']= self.obj514
      self.obj515= AttrCalc()
      self.obj515.Copy=ATOM3Boolean()
      self.obj515.Copy.setValue(('Copy from LHS', 1))
      self.obj515.Copy.config = 0
      self.obj515.Specify=ATOM3Constraint()
      self.obj515.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj51.GGset2Any['cardinality']= self.obj515
      self.obj516= AttrCalc()
      self.obj516.Copy=ATOM3Boolean()
      self.obj516.Copy.setValue(('Copy from LHS', 1))
      self.obj516.Copy.config = 0
      self.obj516.Specify=ATOM3Constraint()
      self.obj516.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj51.GGset2Any['display']= self.obj516
      self.obj517= AttrCalc()
      self.obj517.Copy=ATOM3Boolean()
      self.obj517.Copy.setValue(('Copy from LHS', 1))
      self.obj517.Copy.config = 0
      self.obj517.Specify=ATOM3Constraint()
      self.obj517.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj51.GGset2Any['displaySelect']= self.obj517
      self.RHS.addNode(self.obj51)
   def condition(self, graphID, isograph, atom3i):
      entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return entity.visited == 0
      
      

   def action(self, graphID, isograph, atom3i):
      entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      entity.visited = 1
      ename = entity.name.toString()
      posx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)
      self.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1
      file = self.graphRewritingSystem.file
      file.write("   self.globalPrecondition(rootNode)\n\n")
      file.write("   self.obj"+ename+"=ButtonConfig(self)\n")
      file.write("   self.obj"+ename+".Contents.Text.setValue('New "+ename+"')\n")
      file.write("   self.obj"+ename+".Contents.Image.setValue('')\n")
      file.write("   self.obj"+ename+".Contents.lastSelected= 'Text'\n")
      file.write("   self.obj"+ename+".Drawing_Mode.setValue(1)\n")
      file.write("   self.obj"+ename+".Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), ")
      file.write("(['PREcondition', 'POSTcondition'], 1),")
      file.write("(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], ")
      file.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")
      file.write("'# This method has as parameters:\\n")
      file.write("#   - wherex : X Position in window coordinates where the user clicked.\\n")
      file.write("#   - wherey : Y Position in window coordinates where the user clicked.\\n")
      file.write("newPlace = self.createNew"+ename+" (self, wherex, wherey)\\n'))\n")
      file.write("   self.obj"+ename+".graphClass_= graph_ButtonConfig\n")
      file.write("   if self.genGraphics:\n")
      file.write("      from graph_ButtonConfig import *\n")
      file.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self.obj"+ename+")\n")
      file.write("      new_obj.DrawObject(self.UMLmodel)\n")
      file.write("      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)\n")
      file.write("   else: new_obj = None\n")
      file.write("   self.obj"+ename+".graphObject_ = new_obj\n")
      file.write("   rootNode.addNode(self.obj"+ename+")\n")
      file.write("   self.globalAndLocalPostcondition(self.obj"+ename+", rootNode)\n")
      
      
      
      
      

