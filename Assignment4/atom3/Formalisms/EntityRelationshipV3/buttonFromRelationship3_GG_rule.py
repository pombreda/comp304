# _ buttonFromRelationship3_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from Relationship3 import *
from ASG_EntityRelationshipV3 import *
from Entity3 import *
class buttonFromRelationship3_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_EntityRelationshipV3(parent)

      self.obj66=Relationship3(parent)
      self.obj66.preAction( self.LHS.CREATE )
      self.obj66.isGraphObjectVisual = True


      # name
      self.obj66.name.setValue('')
      self.obj66.name.setNone()

      # displaySelect
      self.obj66.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
      self.obj66.displaySelect.config = 0
      self.obj66.displaySelect.setNone()

      # Actions
      self.obj66.Actions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj66.Actions.setValue(lcobj2)
      self.obj66.Actions.setNone()

      # Graphical_Appearance
      self.obj66.Graphical_Appearance.linkInfo=linkEditor(self,self.obj66.Graphical_Appearance.semObject, "")
      self.obj66.Graphical_Appearance.linkInfo.FirstLink= stickylink()
      self.obj66.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
      self.obj66.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
      self.obj66.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
      self.obj66.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
      self.obj66.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
      self.obj66.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
      self.obj66.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
      self.obj66.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('_1stLink', self.obj66.Graphical_Appearance.linkInfo.FirstLink))
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('_1stSegment', self.obj66.Graphical_Appearance.linkInfo.FirstSegment))
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.obj66.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
      self.obj66.Graphical_Appearance.linkInfo.Center.setValue( ('_Center', self.obj66.Graphical_Appearance.linkInfo))
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('_2ndSegment', self.obj66.Graphical_Appearance.linkInfo.SecondSegment))
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.obj66.Graphical_Appearance.linkInfo.SecondLink= stickylink()
      self.obj66.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
      self.obj66.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
      self.obj66.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
      self.obj66.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
      self.obj66.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
      self.obj66.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
      self.obj66.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
      self.obj66.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('_2ndLink', self.obj66.Graphical_Appearance.linkInfo.SecondLink))
      self.obj66.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj66.Graphical_Appearance.semObject
      self.obj66.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj66.Graphical_Appearance.semObject
      self.obj66.Graphical_Appearance.linkInfo.Center.semObject=self.obj66.Graphical_Appearance.semObject
      self.obj66.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj66.Graphical_Appearance.semObject
      self.obj66.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj66.Graphical_Appearance.semObject
      self.obj66.Graphical_Appearance.setNone()

      # attributes
      self.obj66.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj66.attributes.setValue(lcobj2)
      self.obj66.attributes.setNone()

      # cardinality
      self.obj66.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj66.cardinality.setValue(lcobj2)
      self.obj66.cardinality.setNone()

      # display
      self.obj66.display.setValue('')
      self.obj66.display.setNone()

      # Constraints
      self.obj66.Constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj66.Constraints.setValue(lcobj2)
      self.obj66.Constraints.setNone()

      self.obj66.GGLabel.setValue(1)
      self.obj66.graphClass_= graph_Relationship3
      if parent.genGraphics:
         new_obj = graph_Relationship3(100.0,100.0,self.obj66)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj66.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj66)
      self.RHS = ASG_EntityRelationshipV3(parent)

      self.obj68=Relationship3(parent)
      self.obj68.preAction( self.RHS.CREATE )
      self.obj68.isGraphObjectVisual = True


      # name
      self.obj68.name.setValue('')
      self.obj68.name.setNone()

      # displaySelect
      self.obj68.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
      self.obj68.displaySelect.config = 0

      # Actions
      self.obj68.Actions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj68.Actions.setValue(lcobj2)
      self.obj68.Actions.setNone()

      # Graphical_Appearance
      self.obj68.Graphical_Appearance.linkInfo=linkEditor(self,self.obj68.Graphical_Appearance.semObject, "")
      self.obj68.Graphical_Appearance.linkInfo.FirstLink= stickylink()
      self.obj68.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
      self.obj68.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
      self.obj68.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
      self.obj68.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
      self.obj68.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
      self.obj68.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
      self.obj68.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
      self.obj68.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('_1stLink', self.obj68.Graphical_Appearance.linkInfo.FirstLink))
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('_1stSegment', self.obj68.Graphical_Appearance.linkInfo.FirstSegment))
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.obj68.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
      self.obj68.Graphical_Appearance.linkInfo.Center.setValue( ('_Center', self.obj68.Graphical_Appearance.linkInfo))
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('_2ndSegment', self.obj68.Graphical_Appearance.linkInfo.SecondSegment))
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.obj68.Graphical_Appearance.linkInfo.SecondLink= stickylink()
      self.obj68.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
      self.obj68.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
      self.obj68.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
      self.obj68.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
      self.obj68.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
      self.obj68.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
      self.obj68.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
      self.obj68.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('_2ndLink', self.obj68.Graphical_Appearance.linkInfo.SecondLink))
      self.obj68.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj68.Graphical_Appearance.semObject
      self.obj68.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj68.Graphical_Appearance.semObject
      self.obj68.Graphical_Appearance.linkInfo.Center.semObject=self.obj68.Graphical_Appearance.semObject
      self.obj68.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj68.Graphical_Appearance.semObject
      self.obj68.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj68.Graphical_Appearance.semObject
      self.obj68.Graphical_Appearance.setNone()

      # attributes
      self.obj68.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj68.attributes.setValue(lcobj2)
      self.obj68.attributes.setNone()

      # cardinality
      self.obj68.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj68.cardinality.setValue(lcobj2)
      self.obj68.cardinality.setNone()

      # display
      self.obj68.display.setValue('')

      # Constraints
      self.obj68.Constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj68.Constraints.setValue(lcobj2)
      self.obj68.Constraints.setNone()

      self.obj68.GGLabel.setValue(1)
      self.obj68.graphClass_= graph_Relationship3
      if parent.genGraphics:
         new_obj = graph_Relationship3(100.0,100.0,self.obj68)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj68.graphObject_ = new_obj
      self.obj680= AttrCalc()
      self.obj680.Copy=ATOM3Boolean()
      self.obj680.Copy.setValue(('Copy from LHS', 1))
      self.obj680.Copy.config = 0
      self.obj680.Specify=ATOM3Constraint()
      self.obj680.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj68.GGset2Any['name']= self.obj680
      self.obj681= AttrCalc()
      self.obj681.Copy=ATOM3Boolean()
      self.obj681.Copy.setValue(('Copy from LHS', 1))
      self.obj681.Copy.config = 0
      self.obj681.Specify=ATOM3Constraint()
      self.obj681.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj68.GGset2Any['Actions']= self.obj681
      self.obj682= AttrCalc()
      self.obj682.Copy=ATOM3Boolean()
      self.obj682.Copy.setValue(('Copy from LHS', 1))
      self.obj682.Copy.config = 0
      self.obj682.Specify=ATOM3Constraint()
      self.obj682.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj68.GGset2Any['Constraints']= self.obj682
      self.obj683= AttrCalc()
      self.obj683.Copy=ATOM3Boolean()
      self.obj683.Copy.setValue(('Copy from LHS', 1))
      self.obj683.Copy.config = 0
      self.obj683.Specify=ATOM3Constraint()
      self.obj683.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj68.GGset2Any['Graphical_Appearance']= self.obj683
      self.obj684= AttrCalc()
      self.obj684.Copy=ATOM3Boolean()
      self.obj684.Copy.setValue(('Copy from LHS', 1))
      self.obj684.Copy.config = 0
      self.obj684.Specify=ATOM3Constraint()
      self.obj684.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj68.GGset2Any['attributes']= self.obj684
      self.obj685= AttrCalc()
      self.obj685.Copy=ATOM3Boolean()
      self.obj685.Copy.setValue(('Copy from LHS', 1))
      self.obj685.Copy.config = 0
      self.obj685.Specify=ATOM3Constraint()
      self.obj685.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj68.GGset2Any['cardinality']= self.obj685
      self.obj686= AttrCalc()
      self.obj686.Copy=ATOM3Boolean()
      self.obj686.Copy.setValue(('Copy from LHS', 1))
      self.obj686.Copy.config = 0
      self.obj686.Specify=ATOM3Constraint()
      self.obj686.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj68.GGset2Any['display']= self.obj686
      self.obj687= AttrCalc()
      self.obj687.Copy=ATOM3Boolean()
      self.obj687.Copy.setValue(('Copy from LHS', 1))
      self.obj687.Copy.config = 0
      self.obj687.Specify=ATOM3Constraint()
      self.obj687.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj68.GGset2Any['displaySelect']= self.obj687

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj68)
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
      
      

