from Tkinter import Button, Label, E, W, EW
from tkMessageBox import showinfo, showerror
import tkFileDialog
import os
import string

from ATOM3Type import *
from ATOM3String import ATOM3String
from ATOM3Text import ATOM3Text
from ATOM3Boolean import ATOM3Boolean

from ATOM3 import ATOM3
from FilePaths import META_MODEL_PATH
from GraphicEditor import Editor

class iconPathXaction (ATOM3Type):
   def __init__(self):
      ATOM3Type.__init__(self)
      self.iconPath= None
      self.action= None
      self.takesActionImmediately= None
      
   def createComponents(self):
      if not self.iconPath:
         self.iconPath=ATOM3String('', 20)
      if not self.action:
         self.action=ATOM3Text('# Button action code\n# The following is generated for you: \n# def action(self): # self = ATOM3 instance\n# Typical contents of action:\n# newPlace = self.createNew<CLASS NAME IN META-MODEL>(self, wherex, wherey)\n# Action that shows dialog to edit ASG attributes:\n# self.modelAttributes(self.ASGroot.getASGbyName("<META-MODEL NAME>_META")) \n', 80,15 )
      if not self.takesActionImmediately:
         self.takesActionImmediately=ATOM3Boolean()
         self.takesActionImmediately.setValue(('', 0))
         self.takesActionImmediately.config = 0
         
   def show(self, parent, parentWindowInfo=None):
      self.createComponents()
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      
      if(self.iconPath.getValue()):
        text = 'Edit Button Icon'
      else:
        text = 'Create Button Icon'
      b = Button(self.containerFrame, text=text, command=self.callback)
      b.grid(row=0, column=0, columnspan=2, sticky=EW)
      #Label(self.containerFrame, text='iconPath').grid(row=0,column=0,sticky=W)
      #self.iconPath.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
      
      Label(self.containerFrame, text='action').grid(row=1,column=0,sticky=W)
      self.action.show(self.containerFrame, parentWindowInfo).grid(row=1,column=1,sticky=W)
      
      Label(self.containerFrame, text='takesActionImmediately').grid(row=2,column=0,sticky=W)
      self.takesActionImmediately.show(self.containerFrame, parentWindowInfo).grid(row=2,column=1,sticky=W)
      
      return self.containerFrame

   def callback(self):
     """ Create/Edit Button callback """
     class FakeSemObject:
       def __init__(self):
         self.parent = ATOM3.ROOT_ATOM3_INSTANCE
       def attributesToDraw(self):
         return []
         
     iconPath = self.iconPath.getValue()
     if(iconPath):
       absolutePath = self.getAbsolutePath()
       if(not absolutePath):
         showerror('Icon not found', 
                   'The icon was not found anywhere in the sys.path!' \
                   + '\nPlease move it to a formalism directory...')
         return
       Editor(FakeSemObject(), self.getClassName(), absolutePath)
     
     else:
       text = """
 In the following dialog, choose a directory and name for your icon.
 
 IMPORTANT: 
   1) Name must be unique or an icon mixup will occur (BAD)
   2) /myDir/myIcon will be automatically changed to /myDir/graph_myIcon.py
   3) The directory should be the same one as the formalism that this button 
      icon will be used with.
 """
       showinfo('Create Button Icon', text)
       
       iconPath = tkFileDialog.asksaveasfilename(
                      title="Add source path",
                      filetypes=[("Python files", "*.py"),("All files","*")],
                      initialdir=META_MODEL_PATH )  
       if(iconPath):
         dir, fileName = os.path.split(iconPath)
         if(fileName[-3:] != '.py'):
           fileName = fileName + '.py'
         if(fileName[:6] != 'graph_'):
           fileName = 'graph_' + fileName
         iconPath = os.path.join(dir, fileName)
         self.iconPath.setValue(iconPath)
         Editor(FakeSemObject(), self.getClassName(), iconPath)

         # Make path relative
         if(os.path.split(dir)[1]):    # 'c:\foo\bar\atom3\formalisms\'
           dir = os.path.split(dir)[1] # Becomes 'formalisms'
         iconPath = os.path.join(dir, fileName)
         self.iconPath.setValue(iconPath)
       else:
         self.iconPath.setValue('')
         
       
   def getClassName(self):
     """ Returns the class name given an icon path """
     iconPath = self.iconPath.getValue()
     if(not iconPath):
       return ''
     fileName = os.path.split(iconPath)[1]
     return fileName[6:-3] # Exract CLASSNAME from 'graph_CLASSNAME.py'
         
         
   def getAbsolutePath(self):
     """ 
     Returns the absolute path to the icon
     ASSUMPTION: The icon is in a directory that is in the sys.path
     This assumption holds if the directory of the button icon is the same as 
     that of the formalism to which it belongs!
     """
     iconPath = self.iconPath.getValue()
     if(iconPath):                                  # formalism/graph_FOOBAR.py
      importName = os.path.split(iconPath)[1][:-3] # Get graph_FOOBAR
      exec 'import ' + importName + '\n'
      absolutePath = eval(importName + '.__file__')
      if(absolutePath):
        if(absolutePath[-1:] == 'c'):
          return absolutePath[:-1] # In case it ends in *.pyc convert to *.py
        else:
          return absolutePath
     return  None
     
     
   def hasActionCode(self):
     """ Returns True if executable code is found in action field """
     code = self.action.getValue()
     codeList = code.split('\n')
     for line in codeList:
       strippedLine = line.lstrip(' ')
       if(strippedLine and strippedLine[0] != '#'):
         return True
     return False
     
     
   def getActionCode(self):
     """ Returns action code, minus lines starting with # """
     code = self.action.getValue()
     codeList = code.split('\n')
     commentLessCode = ''
     
     for line in codeList:
       strippedLine = line.lstrip(' ')
       if(strippedLine and strippedLine[0] != '#'):
         commentLessCode += line + '\n'
     return commentLessCode
         
         
          

   def getActionMethod(self):
     """
     Intention in context:
       Get a method that performs the button action when called
     Returns:
       A tuple with the name of the fuction (string) and a method
     Action method parameters:
       self = ATOM3 instance
       wherex, wherey = coordinates
     Pattern:
       method = self.getActionMethod()
       method(atom3i, 0, 0)
     """
     if(not self.hasActionCode()):
       def buttonError(self, wherex, wherey):
         showerror('No action code', 'Button has no action code, does nothing')
       return ('buttonError', buttonError)
     
     code = self.getActionCode()
     hashString = hash(code)
     if(hashString < 0): 
       hashString = '__' + str(-hashString)
     else:
       hashString = '_' + str(hashString)
     
     # Compose function header
     functionName = 'Button' + hashString
     functionHeader = "def "+functionName+"(self, wherex, wherey):\n"  
     # Compose function body 
     functionBody   = "   " +string.replace(code,'\n', '\n   ')+"\n"     
     
     exec functionHeader + functionBody in self.__dict__, self.__dict__ 
     return (functionName, self.__dict__[functionName])

  
   def isActionImmediate(self):
     return self.takesActionImmediately.getValueBoolean()


   def toString(self):
      self.createComponents()
      return  self.iconPath.toString()+' '+ self.action.toString()+' '+ self.takesActionImmediately.toString()

   def getValue(self):
      self.createComponents()
      return (self.iconPath.getValue(),self.action.getValue(),self.takesActionImmediately.getValue(),)

   def setValue(self, value):
      self.createComponents()
      if value == None:
         self.iconPath.setNone()
         self.action.setNone()
         self.takesActionImmediately.setNone()
      else:
         self.iconPath.setValue(value[0])
         self.action.setValue(value[1])
         self.takesActionImmediately.setValue(value[2])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      self.createComponents()
      file.write(indent+objName+'= iconPathXaction()\n')
      self.iconPath.writeConstructor2File(file, indent, objName+'.iconPath', depth, generatingCode)
      self.action.writeConstructor2File(file, indent, objName+'.action', depth, generatingCode)
      self.takesActionImmediately.writeConstructor2File(file, indent, objName+'.takesActionImmediately', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      self.createComponents()
      self.iconPath.writeValue2File(file, indent, objName+'.iconPath', depth, generatingCode)
      self.action.writeValue2File(file, indent, objName+'.action', depth, generatingCode)
      self.takesActionImmediately.writeValue2File(file, indent, objName+'.takesActionImmediately', depth, generatingCode)

   def clone(self):
     "Makes an exact copy of itself"
     cloneObject = iconPathXaction()
     if self.iconPath: cloneObject.iconPath = self.iconPath.clone()
     if self.action: cloneObject.action = self.action.clone()
     if self.takesActionImmediately: cloneObject.takesActionImmediately = self.takesActionImmediately.clone()
     return cloneObject
     
   def destroy(self):
     "Destroys (i.e. updates) each field"
     if self.iconPath: self.iconPath.destroy()
     if self.action: self.action.destroy()
     if self.takesActionImmediately: self.takesActionImmediately.destroy()

   def invalid(self):
     "checks whether the entity is valid or not"
     inval = 0
     if self.iconPath: inval = inval or self.iconPath.invalid()
     if self.action: inval = inval or self.action.invalid()
     if self.takesActionImmediately: inval = inval or self.takesActionImmediately.invalid()
     return inval
