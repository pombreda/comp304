# _ EntityRelationshipV3_Buttons_GG_exec.py ____________________________________________________________________________
# EntityRelationshipV3_Buttons : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from buttonFromEntity3_GG_rule import *
from buttonFromRelationship3_GG_rule import *
class EntityRelationshipV3_Buttons_GG_exec (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [buttonFromEntity3_GG_rule(parent) , buttonFromRelationship3_GG_rule(parent)])
   def initialAction(self, graph):
      self.rewritingSystem.name = \
                              self.rewritingSystem.parent.ASGroot.keyword_.toString()
      self.rewritingSystem.NButtons = 0
      fileName = self.rewritingSystem.name+".py"
      cgd = self.rewritingSystem.parent.codeGenDir
      self.rewritingSystem.file = open(cgd+"/"+fileName,"w+t")
      file = self.rewritingSystem.file
      file.write("from ASG_Buttons import *\n")
      file.write("from ButtonConfig import *\n")
      file.write("from ATOM3Enum import *\n")
      file.write("from ATOM3List import *\n")
      file.write("from ATOM3Float import *\n")
      file.write("from ATOM3Integer import *\n")
      file.write("from ATOM3Attribute import *\n")
      file.write("from ATOM3Constraint import *\n")
      file.write("from ATOM3Action import *\n")
      file.write("from ATOM3String import *\n")
      file.write("from ATOM3BottomType import *\n")
      file.write("from ATOM3Boolean import *\n")
      file.write("from ATOM3Appearance import *\n")
      file.write("from ATOM3Link import *\n")
      file.write("def "+self.rewritingSystem.name+"(self, rootNode, ButtonsRootNode):\n")
      file.write("   ButtonsRootNode.Formalism_Name.setValue('"
                                                  +self.rewritingSystem.name+"')\n")
      file.write("   ButtonsRootNode.RowSize.setValue(4)\n")
      
      import os
      formFile = self.rewritingSystem.name + "_MM.py" 
      file.write("   ButtonsRootNode.Formalism_File.setValue( '" + formFile + "' )\n" )
      for nt in graph.listNodes.keys():
       for node in graph.listNodes[nt]:
          node.visited = 0  
      
      
      """
      Automatically insert a 'Edit' button
      """
      file.write("\n\n")
      posx, posy = 10+125*(self.rewritingSystem.NButtons%3), 10+70*(self.rewritingSystem.NButtons/3)
      self.rewritingSystem.NButtons = self.rewritingSystem.NButtons + 1
      ename = 'Edit'
      file.write("   self.globalPrecondition(rootNode)\n\n")
      file.write("   self.obj"+ename+"=ButtonConfig(self)\n")
      file.write("   self.obj"+ename+".Contents.Text.setValue('New "+ename+"')\n")
      file.write("   self.obj"+ename+".Contents.Image.setValue('')\n")
      file.write("   self.obj"+ename+".Contents.lastSelected= 'Text'\n")
      file.write("   self.obj"+ename+".Drawing_Mode.setValue(0)\n")
      file.write("   self.obj"+ename+".Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), ")
      file.write("(['PREcondition', 'POSTcondition'], 1),")
      file.write("(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], ")
      file.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")
      file.write("'# This method has as parameters:\\n")
      file.write("#   - wherex : X Position in window coordinates where the user clicked.\\n")
      file.write("#   - wherey : Y Position in window coordinates where the user clicked.\\n")
      file.write("self.modelAttributes(self.ASGroot.getASGbyName(\"%s\")) ') )\n" % 
                                              (self.rewritingSystem.name+'_META') )
      ename = 'obj' + ename
      file.write("   self."+ename+".graphClass_= graph_ButtonConfig\n")
      file.write("   if self.genGraphics:\n")
      file.write("      from graph_ButtonConfig import *\n")
      file.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self."+ename+")\n")
      file.write("      new_obj.DrawObject(self.UMLmodel)\n")
      file.write("      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)\n")
      file.write("   else: new_obj = None\n")
      file.write("   self."+ename+".graphObject_ = new_obj\n")
      file.write("   rootNode.addNode(self."+ename+")\n")
      file.write("   self.globalAndLocalPostcondition(self."+ename+", rootNode)\n\n")
      
      """
      Automatically insert a 'Help' button
      """
      file.write("\n\n")
      posx, posy = 10+125*(self.rewritingSystem.NButtons%3), 10+70*(self.rewritingSystem.NButtons/3)
      self.rewritingSystem.NButtons = self.rewritingSystem.NButtons + 1
      ename = 'Help'
      file.write("   self.globalPrecondition(rootNode)\n\n")
      file.write("   self.obj"+ename+"=ButtonConfig(self)\n")
      file.write("   self.obj"+ename+".Contents.Text.setValue('New "+ename+"')\n")
      file.write("   self.obj"+ename+".Contents.Image.setValue('')\n")
      file.write("   self.obj"+ename+".Contents.lastSelected= 'Text'\n")
      file.write("   self.obj"+ename+".Drawing_Mode.setValue(0)\n")
      file.write("   self.obj"+ename+".Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), ")
      file.write("(['PREcondition', 'POSTcondition'], 1),")
      file.write("(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], ")
      file.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")
      
      file.write("'# This method has as parameters:\\n")
      file.write("#   - wherex : X Position in window coordinates where the user clicked.\\n")
      file.write("#   - wherey : Y Position in window coordinates where the user clicked.\\n")
      file.write("from HelpDialog import HelpDialog\\n")
      file.write("HelpDialog([\"%s\"])\\n" % (self.rewritingSystem.name+'Help.txt') ) 
      file.write(" ') )\n" )
      
      ename = 'obj' + ename
      file.write("   self."+ename+".graphClass_= graph_ButtonConfig\n")
      file.write("   if self.genGraphics:\n")
      file.write("      from graph_ButtonConfig import *\n")
      file.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self."+ename+")\n")
      file.write("      new_obj.DrawObject(self.UMLmodel)\n")
      file.write("      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)\n")
      file.write("   else: new_obj = None\n")
      file.write("   self."+ename+".graphObject_ = new_obj\n")
      file.write("   rootNode.addNode(self."+ename+")\n")
      file.write("   self.globalAndLocalPostcondition(self."+ename+", rootNode)\n\n")
      
      

   def finalAction(self, graph):
      file = self.rewritingSystem.file
      
      file.write("\nnewfunction = "+self.rewritingSystem.name+"\n")
      file.write("\nloadedMMName = 'Buttons'\n")
      file.write( '\natom3version = \'0.3\'\n' )
      
      for nt in graph.listNodes.keys():
       for node in graph.listNodes[nt]:
          del node.visited     
      
      del self.rewritingSystem.file
      del self.rewritingSystem.NButtons
      
      

importedModules = ['buttonFromEntity3_GG_rule', 'buttonFromRelationship3_GG_rule']

