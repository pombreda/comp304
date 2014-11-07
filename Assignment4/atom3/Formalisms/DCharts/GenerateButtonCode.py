"""
GenrateButtonCode.py 

What it does:
  Creates a DES description of the statechart
  Compiles the DES description into working Python code (at users request)
  Gives the user some sample code to make using the compiled code a snap!

When it does it:
  When a user presses the Generate .DES button in the DChart formalism
  
How code is compiled:
  os.system() is used to pretend the user called up scc in the console

Author: Mainly Denis Dube, 2005 
(there were probably 5-10 lines by Thomas Feng before...)
"""

import sys
import os
import string
import tkFileDialog
import Dialog
from tkMessageBox import showinfo, showerror
from tkSimpleDialog import askstring

try:
  import SVMAToM3Plugin
  import TkinterGenerator
except:
  showerror('SVM/SCC package not found!', 
            'Please download it and add it to the "AToM3 User" directory in the'
            + ' "User Externals" sub-directory'
            + '\nYou cannot generate DES code without it!')
            
def generate(self):
  """
  Code triggered by the "Generate DES" button in DCharts formalism
  """
  
  sc = SVMAToM3Plugin.generate_description(self, savetofile=None)
  desc = sc["desc"]
  
  mname=self.statusbar.getState(self.statusbar.MODEL)[1][0]
  if not mname or mname=="Nonamed":
      mname=tkFileDialog.asksaveasfilename(
                          filetypes=[("SVM descriptions", "*.des")],
                          initialdir=self.initialDirectoryDict[ 'OpenSaveModel' ])
  else:
      if( string.split( mname, '.' )[1] == 'py' ): 
          mname=mname[:-2]+"des"
      mname=os.path.split(mname)[1]
      mname=tkFileDialog.asksaveasfilename(initialfile=mname, 
                      filetypes=[("SVM descriptions", "*.des")], 
                      initialdir=self.initialDirectoryDict[ 'OpenSaveModel' ])
  
  # User cancelled
  if( not mname ): return
  
  # Force naming convention
  if( mname[-4:] != '.des' ): mname = mname + '.des'
  
  if( os.path.exists( mname ) ): os.remove( mname )
  
  # Save .des file
  mf=open(mname, "w")
  mf.write(desc)
  mf.close()
  # Print on success
  print "SVM description saved to: " + mname
  

#================================================================================
#  Stop here or compile code right away?
#================================================================================
  pythonPath = persistentMemory.pythonPath
  compilerOptions = persistentMemory.compilerOptions
  
  dialogResult = Dialog.Dialog(None, 
                    {'title': 'Compile DES?', 
                     'text': 'Do you want to compile the DES file immediately?'
                             + '\n\nCurrent Python path:\n' + pythonPath
                             + '\n\nCurrent compiler options:\n' 
                             + compilerOptions,
                     'bitmap' : '',
                     'default': 0, 
                     'strings': ['No compilation', 
                                 'Compile DES',
                                 'Configure compiler']})
  
  if(dialogResult.num == 0):
    return
  elif(dialogResult.num == 2):
    pythonPath = askstring('Configure compiler', 
              'Python path (on Windows just python is enough)', 
              **{'initialvalue':persistentMemory.pythonPath})
    compilerOptions = askstring('Configure compiler', 
              'Compilation options:' +  """
      -l <lang>: generate code in language <lang>
                 supported languages: java (default), cpp, csharp, python, tkinter
      -i <file>: include a file (to the head)
      -I <file>: include a file (to the tail)
      -q:        quiet
      -c:        print out the command only (do not generate output)
  language-specific options:
    cpp:
      --head:    generate head file
      --ext:     include extensions for actions (require Python dynamic library)
      --gnu:     print only GNU C++ related commands (default)
      --vc:      print only Visual C++ related commands
    csharp:
      --mono:    print only Mono related commands (default)
      --dotnet:  print only .Net related commands
    python:
      --ext:     include extensions for actions
  """,  **{'initialvalue':persistentMemory.compilerOptions})
 
  
    
#================================================================================
#  Generate the code
#================================================================================
  # WARNING: I get the path to scc.py because TkinterGenerator just happens
  # to be in the same directory. I don't import scc to get the path to it
  # because just the act of importing would trigger code in scc.py which
  # I don't want! 
  scc = os.path.join(os.path.split(TkinterGenerator.__file__)[0], 'scc.py')
  os.system(pythonPath + ' "' + scc + '" ' + compilerOptions + ' "' + mname + '"' )
       
#================================================================================
#  Find the name & path of the generated code file
#================================================================================
  compiledFilePath = os.path.join(os.getcwd(), DES_filepath2Pythonfile(mname))
  if( os.path.exists( compiledFilePath ) ):
    print '\n"%s" was succesfully compiled as "%s"' % (os.path.split(mname)[1],
                                          os.path.split(compiledFilePath)[1] )
  else:
    print '\n"%s" could not be compiled' % (os.path.split(mname)[1])
    return
    
#================================================================================
#  Now lets put the compiled code somewhere useful.. like where the original
#  model was!  
#================================================================================
  newName = mname[:-4] + '_Compiled.py'
  if(os.path.exists(newName)):
    backupName = newName + '.backup'
    if(os.path.exists(backupName)):
      os.remove(backupName)
    os.rename(newName, backupName)    
  os.rename(compiledFilePath, newName)
  
#================================================================================
#  Inform the user
#================================================================================
  print 'DES code compilation successful'
  compiledModuleName = os.path.split(newName)[1][:-3]
  compiledClassName = os.path.split(mname)[1][:-4] 
  text = 'Compiled code: ' + newName
  text += '\n\nYou can now use your compiled code as follows '
  text += '(assuming Python generated):' 
  text += '\n\nfrom ' + compiledModuleName + ' import ' + compiledClassName
  text += '\nself.myChart = ' + compiledClassName + '()'
  if(compilerOptions == '-l tkinter'):
    text += '\nself.myChart.initModel(TkInstance=myInstanceOfTkinter)'
  else:
    text += '\nself.myChart.initModel()'
  text += '\nself.myChart.event("myTriggerString", myOptionalParameter)'
  text += '\n\nYou can copy and paste this from the console'
  print text
  showinfo('DES code compilation successful', text)

  persistentMemory.pythonPath = pythonPath
  persistentMemory.compilerOptions = compilerOptions

def DES_filepath2Pythonfile(path):
  DESfilename = os.path.split(path)[1] # get rid of path, just the filename
  return DESfilename[:-3] + 'py' # Remove des, replace it with py
  
  
class persistentMemory:
  pythonPath = sys.executable # Path to Python executable #'python'
  compilerOptions = '-l tkinter'
