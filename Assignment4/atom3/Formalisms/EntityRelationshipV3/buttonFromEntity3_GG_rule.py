# _ buttonFromEntity3_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Relationship3 import *
from ASG_EntityRelationshipV3 import *
from Entity3 import *
class buttonFromEntity3_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 2)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_EntityRelationshipV3(parent)

      self.obj59=Entity3(parent)
      self.obj59.preAction( self.LHS.CREATE )
      self.obj59.isGraphObjectVisual = True


      # name
      self.obj59.name.setValue('')
      self.obj59.name.setNone()

      # displaySelect
      self.obj59.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
      self.obj59.displaySelect.config = 0
      self.obj59.displaySelect.setNone()

      # Actions
      self.obj59.Actions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj59.Actions.setValue(lcobj2)
      self.obj59.Actions.setNone()

      # Graphical_Appearance
      self.obj59.Graphical_Appearance.setValue( ('Entity_', self.obj59))
      self.obj59.Graphical_Appearance.setNone()

      # attributes
      self.obj59.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj59.attributes.setValue(lcobj2)
      self.obj59.attributes.setNone()

      # cardinality
      self.obj59.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj59.cardinality.setValue(lcobj2)
      self.obj59.cardinality.setNone()

      # display
      self.obj59.display.setValue('')
      self.obj59.display.setNone()

      # Constraints
      self.obj59.Constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj59.Constraints.setValue(lcobj2)
      self.obj59.Constraints.setNone()

      self.obj59.GGLabel.setValue(1)
      self.obj59.graphClass_= graph_Entity3
      if parent.genGraphics:
         new_obj = graph_Entity3(200.0,120.0,self.obj59)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 2.375]
      else: new_obj = None
      self.obj59.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj59)
      self.RHS = ASG_EntityRelationshipV3(parent)

      self.obj61=Entity3(parent)
      self.obj61.preAction( self.RHS.CREATE )
      self.obj61.isGraphObjectVisual = True


      # name
      self.obj61.name.setValue('')
      self.obj61.name.setNone()

      # displaySelect
      self.obj61.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
      self.obj61.displaySelect.config = 0

      # Actions
      self.obj61.Actions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj61.Actions.setValue(lcobj2)
      self.obj61.Actions.setNone()

      # Graphical_Appearance
      self.obj61.Graphical_Appearance.setValue( ('Entity_', self.obj61))
      self.obj61.Graphical_Appearance.setNone()

      # attributes
      self.obj61.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj61.attributes.setValue(lcobj2)
      self.obj61.attributes.setNone()

      # cardinality
      self.obj61.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj61.cardinality.setValue(lcobj2)
      self.obj61.cardinality.setNone()

      # display
      self.obj61.display.setValue('')

      # Constraints
      self.obj61.Constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj61.Constraints.setValue(lcobj2)
      self.obj61.Constraints.setNone()

      self.obj61.GGLabel.setValue(1)
      self.obj61.graphClass_= graph_Entity3
      if parent.genGraphics:
         new_obj = graph_Entity3(200.0,120.0,self.obj61)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.7272727272727273]
      else: new_obj = None
      self.obj61.graphObject_ = new_obj
      self.obj610= AttrCalc()
      self.obj610.Copy=ATOM3Boolean()
      self.obj610.Copy.setValue(('Copy from LHS', 1))
      self.obj610.Copy.config = 0
      self.obj610.Specify=ATOM3Constraint()
      self.obj610.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj61.GGset2Any['name']= self.obj610
      self.obj611= AttrCalc()
      self.obj611.Copy=ATOM3Boolean()
      self.obj611.Copy.setValue(('Copy from LHS', 1))
      self.obj611.Copy.config = 0
      self.obj611.Specify=ATOM3Constraint()
      self.obj611.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj61.GGset2Any['Actions']= self.obj611
      self.obj612= AttrCalc()
      self.obj612.Copy=ATOM3Boolean()
      self.obj612.Copy.setValue(('Copy from LHS', 1))
      self.obj612.Copy.config = 0
      self.obj612.Specify=ATOM3Constraint()
      self.obj612.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj61.GGset2Any['Constraints']= self.obj612
      self.obj613= AttrCalc()
      self.obj613.Copy=ATOM3Boolean()
      self.obj613.Copy.setValue(('Copy from LHS', 1))
      self.obj613.Copy.config = 0
      self.obj613.Specify=ATOM3Constraint()
      self.obj613.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj61.GGset2Any['Graphical_Appearance']= self.obj613
      self.obj614= AttrCalc()
      self.obj614.Copy=ATOM3Boolean()
      self.obj614.Copy.setValue(('Copy from LHS', 1))
      self.obj614.Copy.config = 0
      self.obj614.Specify=ATOM3Constraint()
      self.obj614.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj61.GGset2Any['attributes']= self.obj614
      self.obj615= AttrCalc()
      self.obj615.Copy=ATOM3Boolean()
      self.obj615.Copy.setValue(('Copy from LHS', 1))
      self.obj615.Copy.config = 0
      self.obj615.Specify=ATOM3Constraint()
      self.obj615.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj61.GGset2Any['cardinality']= self.obj615
      self.obj616= AttrCalc()
      self.obj616.Copy=ATOM3Boolean()
      self.obj616.Copy.setValue(('Copy from LHS', 1))
      self.obj616.Copy.config = 0
      self.obj616.Specify=ATOM3Constraint()
      self.obj616.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj61.GGset2Any['display']= self.obj616
      self.obj617= AttrCalc()
      self.obj617.Copy=ATOM3Boolean()
      self.obj617.Copy.setValue(('Copy from LHS', 1))
      self.obj617.Copy.config = 0
      self.obj617.Specify=ATOM3Constraint()
      self.obj617.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj61.GGset2Any['displaySelect']= self.obj617

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj61)
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
      
      

