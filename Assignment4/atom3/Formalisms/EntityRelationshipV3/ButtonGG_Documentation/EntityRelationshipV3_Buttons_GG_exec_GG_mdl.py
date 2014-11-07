from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('EntityRelationshipV3_Buttons')
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('buttonFromEntity3')
   cobj0.Order=ATOM3Integer(1)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Relationship3 import *
   from ASG_EntityRelationshipV3 import *
   from Entity3 import *

   cobj0.LHS = ASG_EntityRelationshipV3(self)

   self.obj42=Entity3(self)

   self.obj42.name.setValue('')
   self.obj42.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
   self.obj42.displaySelect.config = 0
   self.obj42.Actions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj42.Actions.setValue(lcobj2)
   self.obj42.Actions.setNone()
   self.obj42.Graphical_Appearance.setValue( ('Entity_', self.obj42))
   self.obj42.Graphical_Appearance.setNone()
   self.obj42.attributes.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj42.attributes.setValue(lcobj2)
   self.obj42.attributes.setNone()
   self.obj42.cardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj2 =[]
   self.obj42.cardinality.setValue(lcobj2)
   self.obj42.cardinality.setNone()
   self.obj42.display.setValue('')
   self.obj42.Constraints.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj42.Constraints.setValue(lcobj2)
   self.obj42.Constraints.setNone()
   self.obj42.GGLabel.setValue(1)
   self.obj42.graphClass_= graph_Entity3
   if self.genGraphics:
      new_obj = graph_Entity3(200.0,120.0,self.obj42)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.7272727272727273]
   else: new_obj = None
   self.obj42.graphObject_ = new_obj
   cobj0.LHS.addNode(self.obj42)
   cobj0.RHS = ASG_EntityRelationshipV3(self)

   self.obj44=Entity3(self)

   self.obj44.name.setValue('')
   self.obj44.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
   self.obj44.displaySelect.config = 0
   self.obj44.Actions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj44.Actions.setValue(lcobj2)
   self.obj44.Actions.setNone()
   self.obj44.Graphical_Appearance.setValue( ('Entity_', self.obj44))
   self.obj44.Graphical_Appearance.setNone()
   self.obj44.attributes.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj44.attributes.setValue(lcobj2)
   self.obj44.attributes.setNone()
   self.obj44.cardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj2 =[]
   self.obj44.cardinality.setValue(lcobj2)
   self.obj44.cardinality.setNone()
   self.obj44.display.setValue('')
   self.obj44.Constraints.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj44.Constraints.setValue(lcobj2)
   self.obj44.Constraints.setNone()
   self.obj44.GGLabel.setValue(1)
   self.obj44.graphClass_= graph_Entity3
   if self.genGraphics:
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
   cobj0.RHS.addNode(self.obj44)
   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn entity.visited == 0\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nentity.visited = 1\nposx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)\nself.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1\nename = entity.name.toString()\nfile = self.graphRewritingSystem.file\nfile.write("   self.globalPrecondition(rootNode)\\n\\n")\nfile.write("   self.obj"+ename+"=ButtonConfig(self)\\n")\nfile.write("   self.obj"+ename+".Contents.Text.setValue(\'New "+ename+"\')\\n")\nfile.write("   self.obj"+ename+".Contents.Image.setValue(\'\')\\n")\nfile.write("   self.obj"+ename+".Contents.lastSelected= \'Text\'\\n")\nfile.write("   self.obj"+ename+".Drawing_Mode.setValue(1)\\n")\nfile.write("   self.obj"+ename+".Action.setValue((\'ActionButton1\', ([\'Python\', \'OCL\'], 1), ")\nfile.write("([\'PREcondition\', \'POSTcondition\'], 1),")\nfile.write("([\'EDIT\', \'SAVE\', \'CREATE\', \'CONNECT\', \'DELETE\', \'DISCONNECT\', \'TRANSFORM\', \'SELECT\', \'DRAG\', \'DROP\', \'MOVE OBJECT\'], ")\nfile.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")\nfile.write("\'# This method has as parameters:\\\\n")\nfile.write("#   - wherex : X Position in window coordinates where the user clicked.\\\\n")\nfile.write("#   - wherey : Y Position in window coordinates where the user clicked.\\\\n")\nfile.write("newPlace = self.createNew"+ename+" (self, wherex, wherey)\\\\n\'))\\n")\nfile.write("   self.obj"+ename+".graphClass_= graph_ButtonConfig\\n")\nfile.write("   if self.genGraphics:\\n")\nfile.write("      from graph_ButtonConfig import *\\n")\nfile.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self.obj"+ename+")\\n")\nfile.write("      new_obj.DrawObject(self.UMLmodel)\\n")\nfile.write("      self.UMLmodel.addtag_withtag(\'ButtonConfig\', new_obj.tag)\\n")\nfile.write("   else: new_obj = None\\n")\nfile.write("   self.obj"+ename+".graphObject_ = new_obj\\n")\nfile.write("   rootNode.addNode(self.obj"+ename+")\\n")\nfile.write("   self.globalAndLocalPostcondition(self.obj"+ename+", rootNode)\\n")\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('buttonFromRelationship3')
   cobj0.Order=ATOM3Integer(2)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

   from Relationship3 import *
   from ASG_EntityRelationshipV3 import *
   from Entity3 import *

   cobj0.LHS = ASG_EntityRelationshipV3(self)

   self.obj49=Relationship3(self)

   self.obj49.name.setValue('')
   self.obj49.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
   self.obj49.displaySelect.config = 0
   self.obj49.Actions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj49.Actions.setValue(lcobj2)
   self.obj49.Actions.setNone()
   self.obj49.Graphical_Appearance.setNone()
   self.obj49.Graphical_Appearance.linkInfo=linkEditor(self,self.obj49.Graphical_Appearance.semObject, "")
   self.obj49.Graphical_Appearance.linkInfo.FirstLink= stickylink()
   self.obj49.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
   self.obj49.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
   self.obj49.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
   self.obj49.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
   self.obj49.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
   self.obj49.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
   self.obj49.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
   self.obj49.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('_1stLink', self.obj49.Graphical_Appearance.linkInfo.FirstLink))
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('_1stSegment', self.obj49.Graphical_Appearance.linkInfo.FirstSegment))
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
   self.obj49.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
   self.obj49.Graphical_Appearance.linkInfo.Center.setValue( ('_Center', self.obj49.Graphical_Appearance.linkInfo))
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('_2ndSegment', self.obj49.Graphical_Appearance.linkInfo.SecondSegment))
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
   self.obj49.Graphical_Appearance.linkInfo.SecondLink= stickylink()
   self.obj49.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
   self.obj49.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
   self.obj49.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
   self.obj49.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
   self.obj49.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
   self.obj49.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
   self.obj49.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
   self.obj49.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('_2ndLink', self.obj49.Graphical_Appearance.linkInfo.SecondLink))
   self.obj49.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj49.Graphical_Appearance.semObject
   self.obj49.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj49.Graphical_Appearance.semObject
   self.obj49.Graphical_Appearance.linkInfo.Center.semObject=self.obj49.Graphical_Appearance.semObject
   self.obj49.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj49.Graphical_Appearance.semObject
   self.obj49.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj49.Graphical_Appearance.semObject
   self.obj49.attributes.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj49.attributes.setValue(lcobj2)
   self.obj49.attributes.setNone()
   self.obj49.cardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj2 =[]
   self.obj49.cardinality.setValue(lcobj2)
   self.obj49.cardinality.setNone()
   self.obj49.display.setValue('')
   self.obj49.Constraints.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj49.Constraints.setValue(lcobj2)
   self.obj49.Constraints.setNone()
   self.obj49.GGLabel.setValue(1)
   self.obj49.graphClass_= graph_Relationship3
   if self.genGraphics:
      new_obj = graph_Relationship3(100.0,100.0,self.obj49)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj49.graphObject_ = new_obj
   cobj0.LHS.addNode(self.obj49)
   cobj0.RHS = ASG_EntityRelationshipV3(self)

   self.obj51=Relationship3(self)

   self.obj51.name.setValue('')
   self.obj51.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
   self.obj51.displaySelect.config = 0
   self.obj51.Actions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj51.Actions.setValue(lcobj2)
   self.obj51.Actions.setNone()
   self.obj51.Graphical_Appearance.setNone()
   self.obj51.Graphical_Appearance.linkInfo=linkEditor(self,self.obj51.Graphical_Appearance.semObject, "")
   self.obj51.Graphical_Appearance.linkInfo.FirstLink= stickylink()
   self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
   self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
   self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
   self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
   self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
   self.obj51.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
   self.obj51.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
   self.obj51.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('_1stLink', self.obj51.Graphical_Appearance.linkInfo.FirstLink))
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('_1stSegment', self.obj51.Graphical_Appearance.linkInfo.FirstSegment))
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
   self.obj51.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
   self.obj51.Graphical_Appearance.linkInfo.Center.setValue( ('_Center', self.obj51.Graphical_Appearance.linkInfo))
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('_2ndSegment', self.obj51.Graphical_Appearance.linkInfo.SecondSegment))
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
   self.obj51.Graphical_Appearance.linkInfo.SecondLink= stickylink()
   self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
   self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
   self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
   self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
   self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
   self.obj51.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
   self.obj51.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
   self.obj51.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('_2ndLink', self.obj51.Graphical_Appearance.linkInfo.SecondLink))
   self.obj51.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj51.Graphical_Appearance.semObject
   self.obj51.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj51.Graphical_Appearance.semObject
   self.obj51.Graphical_Appearance.linkInfo.Center.semObject=self.obj51.Graphical_Appearance.semObject
   self.obj51.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj51.Graphical_Appearance.semObject
   self.obj51.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj51.Graphical_Appearance.semObject
   self.obj51.attributes.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj51.attributes.setValue(lcobj2)
   self.obj51.attributes.setNone()
   self.obj51.cardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj2 =[]
   self.obj51.cardinality.setValue(lcobj2)
   self.obj51.cardinality.setNone()
   self.obj51.display.setValue('')
   self.obj51.Constraints.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj51.Constraints.setValue(lcobj2)
   self.obj51.Constraints.setNone()
   self.obj51.GGLabel.setValue(1)
   self.obj51.graphClass_= graph_Relationship3
   if self.genGraphics:
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
   cobj0.RHS.addNode(self.obj51)
   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn entity.visited == 0\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nentity.visited = 1\nename = entity.name.toString()\nposx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)\nself.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1\nfile = self.graphRewritingSystem.file\nfile.write("   self.globalPrecondition(rootNode)\\n\\n")\nfile.write("   self.obj"+ename+"=ButtonConfig(self)\\n")\nfile.write("   self.obj"+ename+".Contents.Text.setValue(\'New "+ename+"\')\\n")\nfile.write("   self.obj"+ename+".Contents.Image.setValue(\'\')\\n")\nfile.write("   self.obj"+ename+".Contents.lastSelected= \'Text\'\\n")\nfile.write("   self.obj"+ename+".Drawing_Mode.setValue(1)\\n")\nfile.write("   self.obj"+ename+".Action.setValue((\'ActionButton1\', ([\'Python\', \'OCL\'], 1), ")\nfile.write("([\'PREcondition\', \'POSTcondition\'], 1),")\nfile.write("([\'EDIT\', \'SAVE\', \'CREATE\', \'CONNECT\', \'DELETE\', \'DISCONNECT\', \'TRANSFORM\', \'SELECT\', \'DRAG\', \'DROP\', \'MOVE OBJECT\'], ")\nfile.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")\nfile.write("\'# This method has as parameters:\\\\n")\nfile.write("#   - wherex : X Position in window coordinates where the user clicked.\\\\n")\nfile.write("#   - wherey : Y Position in window coordinates where the user clicked.\\\\n")\nfile.write("newPlace = self.createNew"+ename+" (self, wherex, wherey)\\\\n\'))\\n")\nfile.write("   self.obj"+ename+".graphClass_= graph_ButtonConfig\\n")\nfile.write("   if self.genGraphics:\\n")\nfile.write("      from graph_ButtonConfig import *\\n")\nfile.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self.obj"+ename+")\\n")\nfile.write("      new_obj.DrawObject(self.UMLmodel)\\n")\nfile.write("      self.UMLmodel.addtag_withtag(\'ButtonConfig\', new_obj.tag)\\n")\nfile.write("   else: new_obj = None\\n")\nfile.write("   self.obj"+ename+".graphObject_ = new_obj\\n")\nfile.write("   rootNode.addNode(self.obj"+ename+")\\n")\nfile.write("   self.globalAndLocalPostcondition(self.obj"+ename+", rootNode)\\n")\n\n\n\n\n'))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.rewritingSystem.name = \\\n                        self.rewritingSystem.parent.ASGroot.keyword_.toString()\nself.rewritingSystem.NButtons = 0\nfileName = self.rewritingSystem.name+".py"\ncgd = self.rewritingSystem.parent.codeGenDir\nself.rewritingSystem.file = open(cgd+"/"+fileName,"w+t")\nfile = self.rewritingSystem.file\nfile.write("from ASG_Buttons import *\\n")\nfile.write("from ButtonConfig import *\\n")\nfile.write("from ATOM3Enum import *\\n")\nfile.write("from ATOM3List import *\\n")\nfile.write("from ATOM3Float import *\\n")\nfile.write("from ATOM3Integer import *\\n")\nfile.write("from ATOM3Attribute import *\\n")\nfile.write("from ATOM3Constraint import *\\n")\nfile.write("from ATOM3Action import *\\n")\nfile.write("from ATOM3String import *\\n")\nfile.write("from ATOM3BottomType import *\\n")\nfile.write("from ATOM3Boolean import *\\n")\nfile.write("from ATOM3Appearance import *\\n")\nfile.write("from ATOM3Link import *\\n")\nfile.write("def "+self.rewritingSystem.name+"(self, rootNode):\\n")\nfile.write("   rootNode.Formalism_Name.setValue(\'"\n                                            +self.rewritingSystem.name+"\')\\n")\nfile.write("   rootNode.RowSize.setValue(4)\\n")\n\nimport os\nformFile = self.rewritingSystem.name + "_MM.py" \nfile.write("   rootNode.Formalism_File.setValue( \'" + formFile + "\' )\\n" )\nfor nt in graph.listNodes.keys():\n for node in graph.listNodes[nt]:\n    node.visited = 0  \n\n'))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'file = self.rewritingSystem.file\n\nfile.write("newfunction = "+self.rewritingSystem.name+"\\n")\nfile.write("loadedMMName = \'Buttons\'\\n")\n\nfor nt in graph.listNodes.keys():\n for node in graph.listNodes[nt]:\n    del node.visited     \n\ndel self.rewritingSystem.file\ndel self.rewritingSystem.NButtons\n\n'))


