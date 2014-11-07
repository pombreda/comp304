"""
__testButtonTest_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Denis Dube
Modified: Sun Apr 09 10:29:42 2006
____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from FSB_Button import *
from graph_xyz2 import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def testButtonTest_MDL(self, rootNode, FSB_ButtonsRootNode=None):

    # --- Generating attributes code for ASG FSB_Buttons ---
    if( FSB_ButtonsRootNode ): 
        # author
        FSB_ButtonsRootNode.author.setValue('Annonymous')

        # description
        FSB_ButtonsRootNode.description.setValue('\n')
        FSB_ButtonsRootNode.description.setHeight(15)

        # name
        FSB_ButtonsRootNode.name.setValue('')
        FSB_ButtonsRootNode.name.setNone()
    # --- ASG attributes over ---


    self.obj22=FSB_Button(self)
    self.obj22.isGraphObjectVisual = True

    if(hasattr(self.obj22, '_setHierarchicalLink')):
      self.obj22._setHierarchicalLink(False)

    # info
    self.obj22.info.iconPath.setValue('FSB_Buttons\\graph_xyz2.py')
    self.obj22.info.ltypename.setValue('# Button action code\n# The following is generated for you: \n# def action(self): # self = ATOM3 instance\n# Typical contents of action:\n# newPlace = self.createNew<CLASS NAME IN META-MODEL>(self, wherex, wherey)\n# Action that shows dialog to edit ASG attributes:\n# self.modelAttributes(self.ASGroot.getASGbyName("<META-MODEL NAME>_META")) \n')
    self.obj22.info.ltypename.setHeight(9)

    self.obj22.graphClass_= graph_FSB_Button
    if self.genGraphics:
       new_obj = graph_xyz2(300.0,200.0,self.obj22)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("FSB_Button", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj22.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj22)
    self.globalAndLocalPostcondition(self.obj22, rootNode)
    self.obj22.postAction( rootNode.CREATE )

    # Connections for obj22 (graphObject_: Obj6) of type FSB_Button
    self.drawConnections(
 )

newfunction = testButtonTest_MDL

loadedMMName = 'FSB_Buttons_META'

atom3version = '0.3'
