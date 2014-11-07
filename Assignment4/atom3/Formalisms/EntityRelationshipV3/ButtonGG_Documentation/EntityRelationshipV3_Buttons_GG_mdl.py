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

   self.obj62=Entity3(self)

   self.obj62.name.setValue('')
   self.obj62.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
   self.obj62.displaySelect.config = 0
   self.obj62.Actions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj62.Actions.setValue(lcobj2)
   self.obj62.Actions.setNone()
   self.obj62.Graphical_Appearance.setValue( ('Entity_', self.obj62))
   self.obj62.Graphical_Appearance.setNone()
   self.obj62.attributes.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj62.attributes.setValue(lcobj2)
   self.obj62.attributes.setNone()
   self.obj62.cardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj2 =[]
   self.obj62.cardinality.setValue(lcobj2)
   self.obj62.cardinality.setNone()
   self.obj62.display.setValue('')
   self.obj62.Constraints.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj62.Constraints.setValue(lcobj2)
   self.obj62.Constraints.setNone()
   self.obj62.GGLabel.setValue(1)
   self.obj62.graphClass_= graph_Entity3
   cobj0.LHS.addNode(self.obj62)
   cobj0.RHS = ASG_EntityRelationshipV3(self)

   self.obj64=Entity3(self)

   self.obj64.name.setValue('')
   self.obj64.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
   self.obj64.displaySelect.config = 0
   self.obj64.Actions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj64.Actions.setValue(lcobj2)
   self.obj64.Actions.setNone()
   self.obj64.Graphical_Appearance.setValue( ('Entity_', self.obj64))
   self.obj64.Graphical_Appearance.setNone()
   self.obj64.attributes.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj64.attributes.setValue(lcobj2)
   self.obj64.attributes.setNone()
   self.obj64.cardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj2 =[]
   self.obj64.cardinality.setValue(lcobj2)
   self.obj64.cardinality.setNone()
   self.obj64.display.setValue('')
   self.obj64.Constraints.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj64.Constraints.setValue(lcobj2)
   self.obj64.Constraints.setNone()
   self.obj64.GGLabel.setValue(1)
   self.obj64.graphClass_= graph_Entity3
   self.obj640= AttrCalc()
   self.obj640.Copy=ATOM3Boolean()
   self.obj640.Copy.setValue(('Copy from LHS', 1))
   self.obj640.Copy.config = 0
   self.obj640.Specify=ATOM3Constraint()
   self.obj640.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj64.GGset2Any['name']= self.obj640
   self.obj641= AttrCalc()
   self.obj641.Copy=ATOM3Boolean()
   self.obj641.Copy.setValue(('Copy from LHS', 1))
   self.obj641.Copy.config = 0
   self.obj641.Specify=ATOM3Constraint()
   self.obj641.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj64.GGset2Any['displaySelect']= self.obj641
   self.obj642= AttrCalc()
   self.obj642.Copy=ATOM3Boolean()
   self.obj642.Copy.setValue(('Copy from LHS', 1))
   self.obj642.Copy.config = 0
   self.obj642.Specify=ATOM3Constraint()
   self.obj642.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj64.GGset2Any['Actions']= self.obj642
   self.obj643= AttrCalc()
   self.obj643.Copy=ATOM3Boolean()
   self.obj643.Copy.setValue(('Copy from LHS', 1))
   self.obj643.Copy.config = 0
   self.obj643.Specify=ATOM3Constraint()
   self.obj643.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj64.GGset2Any['Graphical_Appearance']= self.obj643
   self.obj644= AttrCalc()
   self.obj644.Copy=ATOM3Boolean()
   self.obj644.Copy.setValue(('Copy from LHS', 1))
   self.obj644.Copy.config = 0
   self.obj644.Specify=ATOM3Constraint()
   self.obj644.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj64.GGset2Any['attributes']= self.obj644
   self.obj645= AttrCalc()
   self.obj645.Copy=ATOM3Boolean()
   self.obj645.Copy.setValue(('Copy from LHS', 1))
   self.obj645.Copy.config = 0
   self.obj645.Specify=ATOM3Constraint()
   self.obj645.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj64.GGset2Any['cardinality']= self.obj645
   self.obj646= AttrCalc()
   self.obj646.Copy=ATOM3Boolean()
   self.obj646.Copy.setValue(('Copy from LHS', 1))
   self.obj646.Copy.config = 0
   self.obj646.Specify=ATOM3Constraint()
   self.obj646.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj64.GGset2Any['display']= self.obj646
   self.obj647= AttrCalc()
   self.obj647.Copy=ATOM3Boolean()
   self.obj647.Copy.setValue(('Copy from LHS', 1))
   self.obj647.Copy.config = 0
   self.obj647.Specify=ATOM3Constraint()
   self.obj647.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj64.GGset2Any['Constraints']= self.obj647
   cobj0.RHS.addNode(self.obj64)
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

   self.obj69=Relationship3(self)

   self.obj69.name.setValue('')
   self.obj69.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
   self.obj69.displaySelect.config = 0
   self.obj69.Actions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj69.Actions.setValue(lcobj2)
   self.obj69.Actions.setNone()
   self.obj69.Graphical_Appearance.setNone()
   self.obj69.Graphical_Appearance.linkInfo=linkEditor(self,self.obj69.Graphical_Appearance.semObject, "")
   self.obj69.Graphical_Appearance.linkInfo.FirstLink= stickylink()
   self.obj69.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
   self.obj69.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
   self.obj69.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
   self.obj69.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
   self.obj69.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
   self.obj69.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
   self.obj69.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
   self.obj69.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('_1stLink', self.obj69.Graphical_Appearance.linkInfo.FirstLink))
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('_1stSegment', self.obj69.Graphical_Appearance.linkInfo.FirstSegment))
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
   self.obj69.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
   self.obj69.Graphical_Appearance.linkInfo.Center.setValue( ('_Center', self.obj69.Graphical_Appearance.linkInfo))
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('_2ndSegment', self.obj69.Graphical_Appearance.linkInfo.SecondSegment))
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
   self.obj69.Graphical_Appearance.linkInfo.SecondLink= stickylink()
   self.obj69.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
   self.obj69.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
   self.obj69.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
   self.obj69.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
   self.obj69.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
   self.obj69.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
   self.obj69.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
   self.obj69.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('_2ndLink', self.obj69.Graphical_Appearance.linkInfo.SecondLink))
   self.obj69.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj69.Graphical_Appearance.semObject
   self.obj69.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj69.Graphical_Appearance.semObject
   self.obj69.Graphical_Appearance.linkInfo.Center.semObject=self.obj69.Graphical_Appearance.semObject
   self.obj69.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj69.Graphical_Appearance.semObject
   self.obj69.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj69.Graphical_Appearance.semObject
   self.obj69.attributes.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj69.attributes.setValue(lcobj2)
   self.obj69.attributes.setNone()
   self.obj69.cardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj2 =[]
   self.obj69.cardinality.setValue(lcobj2)
   self.obj69.cardinality.setNone()
   self.obj69.display.setValue('')
   self.obj69.Constraints.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj69.Constraints.setValue(lcobj2)
   self.obj69.Constraints.setNone()
   self.obj69.GGLabel.setValue(1)
   self.obj69.graphClass_= graph_Relationship3
   cobj0.LHS.addNode(self.obj69)
   cobj0.RHS = ASG_EntityRelationshipV3(self)

   self.obj71=Relationship3(self)

   self.obj71.name.setValue('')
   self.obj71.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
   self.obj71.displaySelect.config = 0
   self.obj71.Actions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj71.Actions.setValue(lcobj2)
   self.obj71.Actions.setNone()
   self.obj71.Graphical_Appearance.setNone()
   self.obj71.Graphical_Appearance.linkInfo=linkEditor(self,self.obj71.Graphical_Appearance.semObject, "")
   self.obj71.Graphical_Appearance.linkInfo.FirstLink= stickylink()
   self.obj71.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
   self.obj71.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
   self.obj71.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
   self.obj71.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
   self.obj71.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
   self.obj71.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
   self.obj71.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
   self.obj71.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('_1stLink', self.obj71.Graphical_Appearance.linkInfo.FirstLink))
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('_1stSegment', self.obj71.Graphical_Appearance.linkInfo.FirstSegment))
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
   self.obj71.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
   self.obj71.Graphical_Appearance.linkInfo.Center.setValue( ('_Center', self.obj71.Graphical_Appearance.linkInfo))
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('_2ndSegment', self.obj71.Graphical_Appearance.linkInfo.SecondSegment))
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
   self.obj71.Graphical_Appearance.linkInfo.SecondLink= stickylink()
   self.obj71.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
   self.obj71.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
   self.obj71.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
   self.obj71.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
   self.obj71.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
   self.obj71.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
   self.obj71.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
   self.obj71.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('_2ndLink', self.obj71.Graphical_Appearance.linkInfo.SecondLink))
   self.obj71.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj71.Graphical_Appearance.semObject
   self.obj71.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj71.Graphical_Appearance.semObject
   self.obj71.Graphical_Appearance.linkInfo.Center.semObject=self.obj71.Graphical_Appearance.semObject
   self.obj71.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj71.Graphical_Appearance.semObject
   self.obj71.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj71.Graphical_Appearance.semObject
   self.obj71.attributes.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj71.attributes.setValue(lcobj2)
   self.obj71.attributes.setNone()
   self.obj71.cardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj2 =[]
   self.obj71.cardinality.setValue(lcobj2)
   self.obj71.cardinality.setNone()
   self.obj71.display.setValue('')
   self.obj71.Constraints.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   self.obj71.Constraints.setValue(lcobj2)
   self.obj71.Constraints.setNone()
   self.obj71.GGLabel.setValue(1)
   self.obj71.graphClass_= graph_Relationship3
   self.obj710= AttrCalc()
   self.obj710.Copy=ATOM3Boolean()
   self.obj710.Copy.setValue(('Copy from LHS', 1))
   self.obj710.Copy.config = 0
   self.obj710.Specify=ATOM3Constraint()
   self.obj710.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj71.GGset2Any['name']= self.obj710
   self.obj711= AttrCalc()
   self.obj711.Copy=ATOM3Boolean()
   self.obj711.Copy.setValue(('Copy from LHS', 1))
   self.obj711.Copy.config = 0
   self.obj711.Specify=ATOM3Constraint()
   self.obj711.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj71.GGset2Any['displaySelect']= self.obj711
   self.obj712= AttrCalc()
   self.obj712.Copy=ATOM3Boolean()
   self.obj712.Copy.setValue(('Copy from LHS', 1))
   self.obj712.Copy.config = 0
   self.obj712.Specify=ATOM3Constraint()
   self.obj712.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj71.GGset2Any['Actions']= self.obj712
   self.obj713= AttrCalc()
   self.obj713.Copy=ATOM3Boolean()
   self.obj713.Copy.setValue(('Copy from LHS', 1))
   self.obj713.Copy.config = 0
   self.obj713.Specify=ATOM3Constraint()
   self.obj713.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj71.GGset2Any['Graphical_Appearance']= self.obj713
   self.obj714= AttrCalc()
   self.obj714.Copy=ATOM3Boolean()
   self.obj714.Copy.setValue(('Copy from LHS', 1))
   self.obj714.Copy.config = 0
   self.obj714.Specify=ATOM3Constraint()
   self.obj714.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj71.GGset2Any['attributes']= self.obj714
   self.obj715= AttrCalc()
   self.obj715.Copy=ATOM3Boolean()
   self.obj715.Copy.setValue(('Copy from LHS', 1))
   self.obj715.Copy.config = 0
   self.obj715.Specify=ATOM3Constraint()
   self.obj715.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj71.GGset2Any['cardinality']= self.obj715
   self.obj716= AttrCalc()
   self.obj716.Copy=ATOM3Boolean()
   self.obj716.Copy.setValue(('Copy from LHS', 1))
   self.obj716.Copy.config = 0
   self.obj716.Specify=ATOM3Constraint()
   self.obj716.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj71.GGset2Any['display']= self.obj716
   self.obj717= AttrCalc()
   self.obj717.Copy=ATOM3Boolean()
   self.obj717.Copy.setValue(('Copy from LHS', 1))
   self.obj717.Copy.config = 0
   self.obj717.Specify=ATOM3Constraint()
   self.obj717.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj71.GGset2Any['Constraints']= self.obj717
   cobj0.RHS.addNode(self.obj71)
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


