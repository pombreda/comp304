# _ buttonFromRelationship3b_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Relationship3 import *
from ASG_EntityRelationshipV3 import *
from Entity3 import *
class buttonFromRelationship3b_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 3)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_EntityRelationshipV3(parent)

      self.obj56=Relationship3(parent)


      # name
      self.obj56.name.setValue('')
      self.obj56.name.setNone()

      # displaySelect
      self.obj56.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
      self.obj56.displaySelect.config = 0
      self.obj56.displaySelect.setNone()

      # Actions
      self.obj56.Actions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj56.Actions.setValue(lcobj2)
      self.obj56.Actions.setNone()

      # Graphical_Appearance
      self.obj56.Graphical_Appearance.setNone()

      # attributes
      self.obj56.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj56.attributes.setValue(lcobj2)
      self.obj56.attributes.setNone()

      # cardinality
      self.obj56.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj56.cardinality.setValue(lcobj2)
      self.obj56.cardinality.setNone()

      # display
      self.obj56.display.setValue('')
      self.obj56.display.setNone()

      # Constraints
      self.obj56.Constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj56.Constraints.setValue(lcobj2)
      self.obj56.Constraints.setNone()
      self.obj56.GGLabel.setValue(1)
      self.obj56.graphClass_= graph_Relationship3
      if parent.genGraphics:
         new_obj = graph_Relationship3(227.0,100.0,self.obj56)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj56.graphObject_ = new_obj
      self.LHS.addNode(self.obj56)
      self.RHS = ASG_EntityRelationshipV3(parent)

      self.obj58=Relationship3(parent)


      # name
      self.obj58.name.setValue('')
      self.obj58.name.setNone()

      # displaySelect
      self.obj58.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
      self.obj58.displaySelect.config = 0

      # Actions
      self.obj58.Actions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj58.Actions.setValue(lcobj2)
      self.obj58.Actions.setNone()

      # Graphical_Appearance
      self.obj58.Graphical_Appearance.setNone()

      # attributes
      self.obj58.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj58.attributes.setValue(lcobj2)
      self.obj58.attributes.setNone()

      # cardinality
      self.obj58.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj58.cardinality.setValue(lcobj2)
      self.obj58.cardinality.setNone()

      # display
      self.obj58.display.setValue('')

      # Constraints
      self.obj58.Constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj58.Constraints.setValue(lcobj2)
      self.obj58.Constraints.setNone()
      self.obj58.GGLabel.setValue(1)
      self.obj58.graphClass_= graph_Relationship3
      if parent.genGraphics:
         new_obj = graph_Relationship3(227.0,100.0,self.obj58)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj58.graphObject_ = new_obj
      self.obj580= AttrCalc()
      self.obj580.Copy=ATOM3Boolean()
      self.obj580.Copy.setValue(('Copy from LHS', 1))
      self.obj580.Copy.config = 0
      self.obj580.Specify=ATOM3Constraint()
      self.obj580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj58.GGset2Any['name']= self.obj580
      self.obj581= AttrCalc()
      self.obj581.Copy=ATOM3Boolean()
      self.obj581.Copy.setValue(('Copy from LHS', 1))
      self.obj581.Copy.config = 0
      self.obj581.Specify=ATOM3Constraint()
      self.obj581.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj58.GGset2Any['Actions']= self.obj581
      self.obj582= AttrCalc()
      self.obj582.Copy=ATOM3Boolean()
      self.obj582.Copy.setValue(('Copy from LHS', 1))
      self.obj582.Copy.config = 0
      self.obj582.Specify=ATOM3Constraint()
      self.obj582.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj58.GGset2Any['Constraints']= self.obj582
      self.obj583= AttrCalc()
      self.obj583.Copy=ATOM3Boolean()
      self.obj583.Copy.setValue(('Copy from LHS', 1))
      self.obj583.Copy.config = 0
      self.obj583.Specify=ATOM3Constraint()
      self.obj583.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj58.GGset2Any['Graphical_Appearance']= self.obj583
      self.obj584= AttrCalc()
      self.obj584.Copy=ATOM3Boolean()
      self.obj584.Copy.setValue(('Copy from LHS', 1))
      self.obj584.Copy.config = 0
      self.obj584.Specify=ATOM3Constraint()
      self.obj584.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj58.GGset2Any['attributes']= self.obj584
      self.obj585= AttrCalc()
      self.obj585.Copy=ATOM3Boolean()
      self.obj585.Copy.setValue(('Copy from LHS', 1))
      self.obj585.Copy.config = 0
      self.obj585.Specify=ATOM3Constraint()
      self.obj585.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj58.GGset2Any['cardinality']= self.obj585
      self.obj586= AttrCalc()
      self.obj586.Copy=ATOM3Boolean()
      self.obj586.Copy.setValue(('Copy from LHS', 1))
      self.obj586.Copy.config = 0
      self.obj586.Specify=ATOM3Constraint()
      self.obj586.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj58.GGset2Any['display']= self.obj586
      self.obj587= AttrCalc()
      self.obj587.Copy=ATOM3Boolean()
      self.obj587.Copy.setValue(('Copy from LHS', 1))
      self.obj587.Copy.config = 0
      self.obj587.Specify=ATOM3Constraint()
      self.obj587.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj58.GGset2Any['displaySelect']= self.obj587
      self.RHS.addNode(self.obj58)
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
      
      

