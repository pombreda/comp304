from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('EntityRelationshipV3_Buttons')
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('buttonFromEntity3')
   cobj0.Order=ATOM3Integer(2)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Relationship3 import *
   from ASG_EntityRelationshipV3 import *
   from Entity3 import *

   cobj0.LHS = ASG_EntityRelationshipV3(self)

   self.obj59=Entity3(self)
   self.obj59.preAction( cobj0.LHS.CREATE )
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
   if self.genGraphics:
      new_obj = graph_Entity3(200.0,120.0,self.obj59)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 2.375]
   else: new_obj = None
   self.obj59.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj59)
   cobj0.RHS = ASG_EntityRelationshipV3(self)

   self.obj61=Entity3(self)
   self.obj61.preAction( cobj0.RHS.CREATE )
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
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj61)
   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn entity.visited == 0\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nentity.visited = 1\nposx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)\nself.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1\nename = entity.name.toString()\nfile = self.graphRewritingSystem.file\nfile.write("   self.globalPrecondition(rootNode)\\n\\n")\nfile.write("   self.obj"+ename+"=ButtonConfig(self)\\n")\nfile.write("   self.obj"+ename+".Contents.Text.setValue(\'New "+ename+"\')\\n")\nfile.write("   self.obj"+ename+".Contents.Image.setValue(\'\')\\n")\nfile.write("   self.obj"+ename+".Contents.lastSelected= \'Text\'\\n")\nfile.write("   self.obj"+ename+".Drawing_Mode.setValue(1)\\n")\nfile.write("   self.obj"+ename+".Action.setValue((\'ActionButton1\', ([\'Python\', \'OCL\'], 1), ")\nfile.write("([\'PREcondition\', \'POSTcondition\'], 1),")\nfile.write("([\'EDIT\', \'SAVE\', \'CREATE\', \'CONNECT\', \'DELETE\', \'DISCONNECT\', \'TRANSFORM\', \'SELECT\', \'DRAG\', \'DROP\', \'MOVE OBJECT\'], ")\nfile.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")\nfile.write("\'# This method has as parameters:\\\\n")\nfile.write("#   - wherex : X Position in window coordinates where the user clicked.\\\\n")\nfile.write("#   - wherey : Y Position in window coordinates where the user clicked.\\\\n")\nfile.write("newPlace = self.createNew"+ename+" (self, wherex, wherey)\\\\n\'))\\n")\nfile.write("   self.obj"+ename+".graphClass_= graph_ButtonConfig\\n")\nfile.write("   if self.genGraphics:\\n")\nfile.write("      from graph_ButtonConfig import *\\n")\nfile.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self.obj"+ename+")\\n")\nfile.write("      new_obj.DrawObject(self.UMLmodel)\\n")\nfile.write("      self.UMLmodel.addtag_withtag(\'ButtonConfig\', new_obj.tag)\\n")\nfile.write("   else: new_obj = None\\n")\nfile.write("   self.obj"+ename+".graphObject_ = new_obj\\n")\nfile.write("   rootNode.addNode(self.obj"+ename+")\\n")\nfile.write("   self.globalAndLocalPostcondition(self.obj"+ename+", rootNode)\\n")\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('buttonFromRelationship3')
   cobj0.Order=ATOM3Integer(1)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Relationship3 import *
   from ASG_EntityRelationshipV3 import *
   from Entity3 import *

   cobj0.LHS = ASG_EntityRelationshipV3(self)

   self.obj66=Relationship3(self)
   self.obj66.preAction( cobj0.LHS.CREATE )
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
   if self.genGraphics:
      new_obj = graph_Relationship3(100.0,100.0,self.obj66)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj66.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj66)
   cobj0.RHS = ASG_EntityRelationshipV3(self)

   self.obj68=Relationship3(self)
   self.obj68.preAction( cobj0.RHS.CREATE )
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
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj68)
   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn entity.visited == 0\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nentity.visited = 1\nename = entity.name.toString()\nposx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)\nself.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1\nfile = self.graphRewritingSystem.file\nfile.write("   self.globalPrecondition(rootNode)\\n\\n")\nfile.write("   self.obj"+ename+"=ButtonConfig(self)\\n")\nfile.write("   self.obj"+ename+".Contents.Text.setValue(\'New "+ename+"\')\\n")\nfile.write("   self.obj"+ename+".Contents.Image.setValue(\'\')\\n")\nfile.write("   self.obj"+ename+".Contents.lastSelected= \'Text\'\\n")\nfile.write("   self.obj"+ename+".Drawing_Mode.setValue(1)\\n")\nfile.write("   self.obj"+ename+".Action.setValue((\'ActionButton1\', ([\'Python\', \'OCL\'], 1), ")\nfile.write("([\'PREcondition\', \'POSTcondition\'], 1),")\nfile.write("([\'EDIT\', \'SAVE\', \'CREATE\', \'CONNECT\', \'DELETE\', \'DISCONNECT\', \'TRANSFORM\', \'SELECT\', \'DRAG\', \'DROP\', \'MOVE OBJECT\'], ")\nfile.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")\nfile.write("\'# This method has as parameters:\\\\n")\nfile.write("#   - wherex : X Position in window coordinates where the user clicked.\\\\n")\nfile.write("#   - wherey : Y Position in window coordinates where the user clicked.\\\\n")\nfile.write("newPlace = self.createNew"+ename+" (self, wherex, wherey)\\\\n\'))\\n")\nfile.write("   self.obj"+ename+".graphClass_= graph_ButtonConfig\\n")\nfile.write("   if self.genGraphics:\\n")\nfile.write("      from graph_ButtonConfig import *\\n")\nfile.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self.obj"+ename+")\\n")\nfile.write("      new_obj.DrawObject(self.UMLmodel)\\n")\nfile.write("      self.UMLmodel.addtag_withtag(\'ButtonConfig\', new_obj.tag)\\n")\nfile.write("   else: new_obj = None\\n")\nfile.write("   self.obj"+ename+".graphObject_ = new_obj\\n")\nfile.write("   rootNode.addNode(self.obj"+ename+")\\n")\nfile.write("   self.globalAndLocalPostcondition(self.obj"+ename+", rootNode)\\n")\n\n'))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.rewritingSystem.name = \\\n                        self.rewritingSystem.parent.ASGroot.keyword_.toString()\nself.rewritingSystem.NButtons = 0\nfileName = self.rewritingSystem.name+".py"\ncgd = self.rewritingSystem.parent.codeGenDir\nself.rewritingSystem.file = open(cgd+"/"+fileName,"w+t")\nfile = self.rewritingSystem.file\nfile.write("from ASG_Buttons import *\\n")\nfile.write("from ButtonConfig import *\\n")\nfile.write("from ATOM3Enum import *\\n")\nfile.write("from ATOM3List import *\\n")\nfile.write("from ATOM3Float import *\\n")\nfile.write("from ATOM3Integer import *\\n")\nfile.write("from ATOM3Attribute import *\\n")\nfile.write("from ATOM3Constraint import *\\n")\nfile.write("from ATOM3Action import *\\n")\nfile.write("from ATOM3String import *\\n")\nfile.write("from ATOM3BottomType import *\\n")\nfile.write("from ATOM3Boolean import *\\n")\nfile.write("from ATOM3Appearance import *\\n")\nfile.write("from ATOM3Link import *\\n")\nfile.write("def "+self.rewritingSystem.name+"(self, rootNode, ButtonsRootNode):\\n")\nfile.write("   ButtonsRootNode.Formalism_Name.setValue(\'"\n                                            +self.rewritingSystem.name+"\')\\n")\nfile.write("   ButtonsRootNode.RowSize.setValue(4)\\n")\n\nimport os\nformFile = self.rewritingSystem.name + "_MM.py" \nfile.write("   ButtonsRootNode.Formalism_File.setValue( \'" + formFile + "\' )\\n" )\nfor nt in graph.listNodes.keys():\n for node in graph.listNodes[nt]:\n    node.visited = 0  \n\n\n"""\nAutomatically insert a \'Edit\' button\n"""\nfile.write("\\n\\n")\nposx, posy = 10+125*(self.rewritingSystem.NButtons%3), 10+70*(self.rewritingSystem.NButtons/3)\nself.rewritingSystem.NButtons = self.rewritingSystem.NButtons + 1\nename = \'Edit\'\nfile.write("   self.globalPrecondition(rootNode)\\n\\n")\nfile.write("   self.obj"+ename+"=ButtonConfig(self)\\n")\nfile.write("   self.obj"+ename+".Contents.Text.setValue(\'New "+ename+"\')\\n")\nfile.write("   self.obj"+ename+".Contents.Image.setValue(\'\')\\n")\nfile.write("   self.obj"+ename+".Contents.lastSelected= \'Text\'\\n")\nfile.write("   self.obj"+ename+".Drawing_Mode.setValue(0)\\n")\nfile.write("   self.obj"+ename+".Action.setValue((\'ActionButton1\', ([\'Python\', \'OCL\'], 1), ")\nfile.write("([\'PREcondition\', \'POSTcondition\'], 1),")\nfile.write("([\'EDIT\', \'SAVE\', \'CREATE\', \'CONNECT\', \'DELETE\', \'DISCONNECT\', \'TRANSFORM\', \'SELECT\', \'DRAG\', \'DROP\', \'MOVE OBJECT\'], ")\nfile.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")\nfile.write("\'# This method has as parameters:\\\\n")\nfile.write("#   - wherex : X Position in window coordinates where the user clicked.\\\\n")\nfile.write("#   - wherey : Y Position in window coordinates where the user clicked.\\\\n")\nfile.write("self.modelAttributes(self.ASGroot.getASGbyName(\\"%s\\")) \') )\\n" % \n                                        (self.rewritingSystem.name+\'_META\') )\nename = \'obj\' + ename\nfile.write("   self."+ename+".graphClass_= graph_ButtonConfig\\n")\nfile.write("   if self.genGraphics:\\n")\nfile.write("      from graph_ButtonConfig import *\\n")\nfile.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self."+ename+")\\n")\nfile.write("      new_obj.DrawObject(self.UMLmodel)\\n")\nfile.write("      self.UMLmodel.addtag_withtag(\'ButtonConfig\', new_obj.tag)\\n")\nfile.write("   else: new_obj = None\\n")\nfile.write("   self."+ename+".graphObject_ = new_obj\\n")\nfile.write("   rootNode.addNode(self."+ename+")\\n")\nfile.write("   self.globalAndLocalPostcondition(self."+ename+", rootNode)\\n\\n")\n\n"""\nAutomatically insert a \'Help\' button\n"""\nfile.write("\\n\\n")\nposx, posy = 10+125*(self.rewritingSystem.NButtons%3), 10+70*(self.rewritingSystem.NButtons/3)\nself.rewritingSystem.NButtons = self.rewritingSystem.NButtons + 1\nename = \'Help\'\nfile.write("   self.globalPrecondition(rootNode)\\n\\n")\nfile.write("   self.obj"+ename+"=ButtonConfig(self)\\n")\nfile.write("   self.obj"+ename+".Contents.Text.setValue(\'New "+ename+"\')\\n")\nfile.write("   self.obj"+ename+".Contents.Image.setValue(\'\')\\n")\nfile.write("   self.obj"+ename+".Contents.lastSelected= \'Text\'\\n")\nfile.write("   self.obj"+ename+".Drawing_Mode.setValue(0)\\n")\nfile.write("   self.obj"+ename+".Action.setValue((\'ActionButton1\', ([\'Python\', \'OCL\'], 1), ")\nfile.write("([\'PREcondition\', \'POSTcondition\'], 1),")\nfile.write("([\'EDIT\', \'SAVE\', \'CREATE\', \'CONNECT\', \'DELETE\', \'DISCONNECT\', \'TRANSFORM\', \'SELECT\', \'DRAG\', \'DROP\', \'MOVE OBJECT\'], ")\nfile.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")\n\nfile.write("\'# This method has as parameters:\\\\n")\nfile.write("#   - wherex : X Position in window coordinates where the user clicked.\\\\n")\nfile.write("#   - wherey : Y Position in window coordinates where the user clicked.\\\\n")\nfile.write("from HelpDialog import HelpDialog\\\\n")\nfile.write("HelpDialog([\\"%s\\"])\\\\n" % (self.rewritingSystem.name+\'Help.txt\') ) \nfile.write(" \') )\\n" )\n\nename = \'obj\' + ename\nfile.write("   self."+ename+".graphClass_= graph_ButtonConfig\\n")\nfile.write("   if self.genGraphics:\\n")\nfile.write("      from graph_ButtonConfig import *\\n")\nfile.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self."+ename+")\\n")\nfile.write("      new_obj.DrawObject(self.UMLmodel)\\n")\nfile.write("      self.UMLmodel.addtag_withtag(\'ButtonConfig\', new_obj.tag)\\n")\nfile.write("   else: new_obj = None\\n")\nfile.write("   self."+ename+".graphObject_ = new_obj\\n")\nfile.write("   rootNode.addNode(self."+ename+")\\n")\nfile.write("   self.globalAndLocalPostcondition(self."+ename+", rootNode)\\n\\n")\n\n'))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'file = self.rewritingSystem.file\n\nfile.write("\\nnewfunction = "+self.rewritingSystem.name+"\\n")\nfile.write("\\nloadedMMName = \'Buttons\'\\n")\nfile.write( \'\\natom3version = \\\'0.3\\\'\\n\' )\n\nfor nt in graph.listNodes.keys():\n for node in graph.listNodes[nt]:\n    del node.visited     \n\ndel self.rewritingSystem.file\ndel self.rewritingSystem.NButtons\n\n'))


