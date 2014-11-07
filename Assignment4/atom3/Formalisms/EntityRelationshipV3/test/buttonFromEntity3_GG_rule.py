# _ buttonFromEntity3_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Relationship3 import *
from ASG_EntityRelationshipV3 import *
from Entity3 import *
class buttonFromEntity3_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_EntityRelationshipV3(parent)

      self.obj42=Entity3(parent)


      # name
      self.obj42.name.setValue('')
      self.obj42.name.setNone()

      # displaySelect
      self.obj42.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
      self.obj42.displaySelect.config = 0
      self.obj42.displaySelect.setNone()

      # Actions
      self.obj42.Actions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj42.Actions.setValue(lcobj2)
      self.obj42.Actions.setNone()

      # Graphical_Appearance
      self.obj42.Graphical_Appearance.setValue( ('Entity_', self.obj42))
      self.obj42.Graphical_Appearance.setNone()

      # attributes
      self.obj42.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj42.attributes.setValue(lcobj2)
      self.obj42.attributes.setNone()

      # cardinality
      self.obj42.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj42.cardinality.setValue(lcobj2)
      self.obj42.cardinality.setNone()

      # display
      self.obj42.display.setValue('')
      self.obj42.display.setNone()

      # Constraints
      self.obj42.Constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj42.Constraints.setValue(lcobj2)
      self.obj42.Constraints.setNone()
      self.obj42.GGLabel.setValue(1)
      self.obj42.graphClass_= graph_Entity3
      if parent.genGraphics:
         new_obj = graph_Entity3(200.0,120.0,self.obj42)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 2.1111111111111112]
      else: new_obj = None
      self.obj42.graphObject_ = new_obj
      self.LHS.addNode(self.obj42)
      self.RHS = ASG_EntityRelationshipV3(parent)

      self.obj44=Entity3(parent)


      # name
      self.obj44.name.setValue('')
      self.obj44.name.setNone()

      # displaySelect
      self.obj44.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
      self.obj44.displaySelect.config = 0

      # Actions
      self.obj44.Actions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj44.Actions.setValue(lcobj2)
      self.obj44.Actions.setNone()

      # Graphical_Appearance
      self.obj44.Graphical_Appearance.setValue( ('Entity_', self.obj44))
      self.obj44.Graphical_Appearance.setNone()

      # attributes
      self.obj44.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj44.attributes.setValue(lcobj2)
      self.obj44.attributes.setNone()

      # cardinality
      self.obj44.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj44.cardinality.setValue(lcobj2)
      self.obj44.cardinality.setNone()

      # display
      self.obj44.display.setValue('')

      # Constraints
      self.obj44.Constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj44.Constraints.setValue(lcobj2)
      self.obj44.Constraints.setNone()
      self.obj44.GGLabel.setValue(1)
      self.obj44.graphClass_= graph_Entity3
      if parent.genGraphics:
         new_obj = graph_Entity3(200.0,120.0,self.obj44)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.4615384615384615]
      else: new_obj = None
      self.obj44.graphObject_ = new_obj
      self.obj440= AttrCalc()
      self.obj440.Copy=ATOM3Boolean()
      self.obj440.Copy.setValue(('Copy from LHS', 1))
      self.obj440.Copy.config = 0
      self.obj440.Specify=ATOM3Constraint()
      self.obj440.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['name']= self.obj440
      self.obj441= AttrCalc()
      self.obj441.Copy=ATOM3Boolean()
      self.obj441.Copy.setValue(('Copy from LHS', 1))
      self.obj441.Copy.config = 0
      self.obj441.Specify=ATOM3Constraint()
      self.obj441.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['Actions']= self.obj441
      self.obj442= AttrCalc()
      self.obj442.Copy=ATOM3Boolean()
      self.obj442.Copy.setValue(('Copy from LHS', 1))
      self.obj442.Copy.config = 0
      self.obj442.Specify=ATOM3Constraint()
      self.obj442.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['Constraints']= self.obj442
      self.obj443= AttrCalc()
      self.obj443.Copy=ATOM3Boolean()
      self.obj443.Copy.setValue(('Copy from LHS', 1))
      self.obj443.Copy.config = 0
      self.obj443.Specify=ATOM3Constraint()
      self.obj443.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['Graphical_Appearance']= self.obj443
      self.obj444= AttrCalc()
      self.obj444.Copy=ATOM3Boolean()
      self.obj444.Copy.setValue(('Copy from LHS', 1))
      self.obj444.Copy.config = 0
      self.obj444.Specify=ATOM3Constraint()
      self.obj444.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['attributes']= self.obj444
      self.obj445= AttrCalc()
      self.obj445.Copy=ATOM3Boolean()
      self.obj445.Copy.setValue(('Copy from LHS', 1))
      self.obj445.Copy.config = 0
      self.obj445.Specify=ATOM3Constraint()
      self.obj445.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['cardinality']= self.obj445
      self.obj446= AttrCalc()
      self.obj446.Copy=ATOM3Boolean()
      self.obj446.Copy.setValue(('Copy from LHS', 1))
      self.obj446.Copy.config = 0
      self.obj446.Specify=ATOM3Constraint()
      self.obj446.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['display']= self.obj446
      self.obj447= AttrCalc()
      self.obj447.Copy=ATOM3Boolean()
      self.obj447.Copy.setValue(('Copy from LHS', 1))
      self.obj447.Copy.config = 0
      self.obj447.Specify=ATOM3Constraint()
      self.obj447.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['displaySelect']= self.obj447
      self.RHS.addNode(self.obj44)
   def condition(self, graphID, isograph, atom3i):
      entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return entity.visited == 0
      
      

   def action(self, graphID, isograph, atom3i):
      entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      entity.visited = 1
      posx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)
      self.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1
      ename = entity.name.toString()
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
      
      

