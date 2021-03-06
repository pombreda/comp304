#---------------------------------------------------------------------
#    SVM (DCharts Virtual Machine)
#         -- an interpreter for an extended DCharts formalism
#---------------------------------------------------------------------
#
# Copyright (C) 2003 Thomas Huining Feng
#
#---------------------------------------------------------------------
# Address:      MSDL, SOCS, McGill Univ., Montreal, Canada
# HomePage:     http://msdl.cs.mcgill.ca/people/tfeng/
# SVM HomePage: http://msdl.cs.mcgill.ca/people/tfeng/?research=svm
# Download:     http://savannah.nongnu.org/files/?group=svm
# CVS:          :pserver:anoncvs@subversions.gnu.org:/cvsroot/svm
#               (projects "svm" and "jsvm")
# Email:        hfeng2@cs.mcgill.ca
#---------------------------------------------------------------------
#
# This file is part of SVM.
#
#---------------------------------------------------------------------
# SVM is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# SVM is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SVM; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#---------------------------------------------------------------------


######################################################################
# SVM plugin (textural description generator for AToM3)
# Supporting:
#   state hierarchy
#   default states
#   orthogonal components
#   (deep) history
#   enter/exit actions
#   transitions with:
#     source/destination state
#     trigger (if written as "AFTER(...)", schedule transition)
#     action (a list of python commands or pre-defined macros)
#     guard (a one-line python boolean expression)
# Requirement:
#   SVM and SCC can be found in PATH or PYTHONPATH
######################################################################

from StatusBar import *
import tkFileDialog
import sys
import os
import time
from string import *

# Try to import SVM modules
svm_paths=split(os.environ["PATH"], os.pathsep)
oldpath=sys.path
sys.path=svm_paths+sys.path
if(1):#try:
  from Exception import *
  from Debugger import *
  from EventHandler import EventHandler
  from Clock import Clock
  import sys
  import os
  from StringUtil import *
  import DefaultUI
  import ThreadUtil
  try:
    import PVMUtil
  except:
    print "PVM support is disabled."
  from JavaGenerator import JavaGenerator
  DefaultInterpreter.runsource("import SVMAToM3Plugin")
else:#except:
  sys.path=oldpath
  raise "ERROR: SVM module is not in the PATH or PYTHONPATH environment variable."

sys.path=oldpath

def append_path(path1, path2):
  if path1=='':
    return path2
  else:
    return path1+'.'+path2

def generate_description(canvas, savetofile=1):
  root=canvas.ASGroot.listNodes
  # root is a DCharts model with these keys:
  # ['Hyperedge', 'Orthogonal', 'Composite', 'contains',
  #  'orthogonality', 'ASG_DCharts', 'visual_settings',
  #  'Basic', 'History']

  sc=generate_DCharts(root)
  
  localtime=time.localtime()
  months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  mname=canvas.statusbar.getState(StatusBar.MODEL)[1][0]
  desc="\
# DCharts description generated by SVM-AToM3-plugin, written by Thomas Feng\n\
#   Source: %s\n\
#   Date:   %s %d, %d\n\
#   Time:   %d:%d:%d\n\n" % (mname, months[localtime[1]-1], localtime[2], localtime[0], localtime[3], localtime[4], localtime[5]) \
  + generate_servers(sc["servers"]) \
  + generate_ports(sc["ports"]) \
  + generate_connections(sc["connections"]) + "\n" \
  + generate_desc(sc["states"]) + "\n" \
  + generate_enter_exit_actions(sc["enter"], sc["exit"]) + "\n" \
  + generate_trans(sc["trans"])

  if savetofile:
    if not mname or mname=="Nonamed":
      mname=tkFileDialog.asksaveasfilename(filetypes=[("SVM descriptions", "*.des")])
    else:
      if StringUtil.endswith(mname, ".py"):
        mname=mname[:len(mname)-3]+".des"
      mname=os.path.split(mname)[1]
      mname=tkFileDialog.asksaveasfilename(initialfile=mname, filetypes=[("SVM descriptions", "*.des")], initialdir=canvas.codeGenDir)
      
    if mname:
      # Save .des file
      mf=open(mname, "w")
      mf.write(desc)
      mf.close()
      # Print on success
      print "SVM description saved to: " + mname

  sc["desc"]=desc
  return sc

def generate_DCharts(root):
  sc={"states":[], "trans":[], "statedict1":{}, "statedict2":{}, "history":{}, "enter":{}, "exit":{}, "colors":{}, "ports":[], "servers":[], "connections":[]}
  states=sc["states"]
  trans=sc["trans"]
  statedict1=sc["statedict1"]
  statedict2=sc["statedict2"]
  history=sc["history"]
  enter=sc["enter"]
  exit=sc["exit"]
  ports=sc["ports"]
  servers=sc["servers"]
  connections=sc["connections"]
  
  basic=root["Basic"]
  composite=root["Composite"]
  orthogonal=root["Orthogonal"]
  edges=root["Hyperedge"]
  
  # Find all the top-level states
  toplevel=basic+composite+orthogonal
  for c in composite+orthogonal:
    for ch in c.children:
      if ch in toplevel:
        toplevel.remove(ch)

  # Generate state hierarchy
  for t in toplevel:
    generate_DCharts_rec(t, states, statedict1, statedict2, history, "", 0)

  # Generate enter/exit actions
  for s in states:
    if hasattr(s[4], "enter_action"):
      e1=s[4].enter_action.getValue()
      enter[s[2]]=e1
    if hasattr(s[4], "exit_action"):
      e2=s[4].exit_action.getValue()
      exit[s[2]]=e2

  # Generate transitions
  i = 0
  for e in edges:
    inc=e.in_connections_
    outc=e.out_connections_
    ## if( len( inc ) > 1):
        ## for item in inc:
            ## print item.name.getValue()
    ## print e.in_connections_,e.out_connections_, " <-- Connection #", i
    i += 1
    assert len(inc)==1, "ERROR: There must be exactly 1 source node for a hyperedge."
    assert len(outc)==1, "ERROR: There must be exactly 1 destination node for a hyperedge."
    ins=inc[0]
    outs=outc[0]
    t={'S':states[statedict1[ins]][2],
       'E':e.trigger.getValue(), 'O':e.action.getValue(),
       'C':e.guard.getValue(), 'e':e}
    if outs.getTypeName()=="History":
      t['N']=states[statedict1[history[outs]]][2]
      t['HS']=1
    else:
      t['N']=states[statedict1[outs]][2]
      t['HS']=0
    
    trans.append(t)

  # Generate servers
  for s in root["Server"]:
    server={"id":s.id.getValue(), "name":s.name_pattern.getValue()}
    servers.append(server)

  # Generate ports
  for p in root["Port"]:
    port={"name":p.name.getValue()}
    if p.is_in.getValue()[1] and p.is_out.getValue()[1]:
      port["type"]="inout"
    elif p.is_in.getValue()[1]:
      port["type"]="in"
    elif p.is_out.getValue()[1]:
      port["type"]="out"
    else:
      print "One port is neither in-port nor out-port. Ignoring ..."
      continue
    ports.append(port)

  # Generating connections
  for p in root["Port"]:
    port_name=strip(p.name.getValue())
    for c in p.out_connections_:
      oc=c.out_connections_[0]
      server_name=strip(oc.id.getValue())
      server_port=strip(c.getAttrValue("server_port").getValue())
      if port_name and server_name and server_port:
        connections.append([port_name, server_name+"."+server_port])
      else:
        print "Port name, server name or server port is missing. Ignoring a connection ..."
        continue

  record_colors(sc)

  return sc

def record_colors(sc):
  colors=sc["colors"]
  states=sc["states"]
  for s in states:
    for gf in s[4].graphObject_.graphForms:
      colors[gf]=gf.Color

def generate_DCharts_rec(state, states, statedict1, statedict2, history, path, level):
  if state.getTypeName() in ["contains", "Hyperedge", "orthogonality"]:
    return
  sname=state.name.getValue()
  props=""
  if state.getTypeName()=="Orthogonal":
    props=props+" [DS] [CS]"
  elif state.is_default.getValue()[1]:
    props=props+" [DS]"
  newpath=append_path(path, sname)
  sdesc=[sname, level, newpath, props, state]
  snum=len(states)
  statedict1[state]=snum
  statedict2[newpath]=snum
  states.append(sdesc)
  if "children" in dir(state):
    for c in state.children:
      if c.getTypeName()=="History":
	if c.star.getValue()[1]:
	  sdesc[3]=sdesc[3]+" [HS*]"
	else:
	  sdesc[3]=sdesc[3]+" [HS]"
	history[c]=state
      else:
        generate_DCharts_rec(c, states, statedict1, statedict2, history, newpath, level+1)

def generate_servers(servers):
  code=""
  for s in servers:
    code=code+"\
COMPONENT:\n"
    code=code+"\
  id = %s\n" % strip(s["id"])
    code=code+"\
  name = %s\n" % strip(s["name"])
    code=code+"\n"
  return code

def generate_ports(ports):
  code=""
  for p in ports:
    code=code+"\
PORT:\n"
    code=code+"\
  name = %s\n" % strip(p["name"])
    code=code+"\
  type = %s\n" % p["type"]
    code=code+"\n"
  return code 

def generate_connections(connections):
  code="\
CONNECTIONS:\n"
  for c in connections:
    code=code + "  " + c[0] + " -- " + c[1] + "\n"
  return code

def generate_desc(states):
  code="\
STATECHART:\n"
  for s in states:
    code=code+"  "*(s[1]+1)+s[0]+s[3]+"\n"
  return code

def generate_enter_exit_actions(enters, exits):
  code=""
  for k in enters.keys():
    a=strip(enters[k])
    if a:
      a=replace(a, "\n", "\n     ")
      code=code+"\
ENTER:\n\
  N: %s\n\
  O: %s\n\n" % (k, a)
      
  for k in exits.keys():
    a=strip(exits[k])
    if a:
      a=replace(a, "\n", "\n     ")
      code=code+"\
EXIT:\n\
  S: %s\n\
  O: %s\n\n" % (k, a)
  return code

def get_after_time(ev):
  if StringUtil.startswith(ev, "AFTER(") and StringUtil.endswith(ev, ")"):
    return ev[6:len(ev)-1]
  else:
    return None

def generate_trans(trans):
  code=""
  tnum=0
  for t in trans:
    t['*']=tnum
    tnum=tnum+1
    code=code+"\
TRANSITION:"
    if t['HS']:
      code=code+" [HS]\n"
    else:
      code=code+"\n"
    code=code+"  S: "+t['S']+"\n"
    code=code+"  N: "+t['N']+"\n"

    after=get_after_time(t['E'])
    if not after:
      if strip(t['E']):
        code=code+"  E: "+t['E']+"\n"
      else:
	code=code+"  T: 0 [RTT]\n"
    else:
      code=code+"  T: "+after+" [RTT]\n"

    code=code+"  C: "+t['C']+"\n"
      
    act=strip(t['O'])
    if act:
      act=replace(act, "\n", "\n     ")
      code=code+"  O: "+act+"\n"
    
    code=code+"\n"
  return code

def simulate(canvas):
  global theCanvas
  theCanvas=canvas
  mname=canvas.statusbar.getState(StatusBar.MODEL)[1][0]
  if not mname:
    mname="Nonamed.des"
  else:
    if mname.endswith(".py"):
      mname=mname[:len(mname)-3]
    mname=mname+".des"

  global sc
  sc=generate_description(canvas, 0)

  global debugger
  debugger=Debugger()

  global eventhandler
  eventhandler=EventHandler(mname, callback=debugger.EventDebugger, use_gui=1, modeltext=sc["desc"])
  eventhandler.final.append("SVMAToM3Plugin.finalize_simulation()")
  debugger.CustomizeEvent(event_callback, None, 1)
  
  global root
  root=canvas.ASGroot.listNodes

  DefaultInterpreter.runsource("eventhandler=SVMAToM3Plugin.eventhandler")
  DefaultInterpreter.runsource("debugger=SVMAToM3Plugin.debugger")
  
  debugger.SetEventHandler(eventhandler)
  
  eventhandler.run_initializer()
  highlight_states(eventhandler.state, sc)
  highlight_trans(eventhandler, sc, root)
  
  # Cannot start the Tk mainloop again
  # eventhandler.run_interactor()
  DefaultInterpreter.runsource("setup_gui_debugger(eventhandler, debugger, 0, 0)")

def highlight_states(states, sc):
  for s in sc["states"]:
    s[4].graphObject_.HighLight(0)
  for s in states:
    sc["states"][sc["statedict2"][s]][4].graphObject_.HighLight(1)

def highlight_trans(eventhandler, sc, root):
  trans=sc["trans"]
  edges=root["Hyperedge"]
  for e in edges:
    try:
      e.graphObject_.HighLight(0)
    except:
      pass
  for t in trans:
    if eventhandler.is_in_state(t['S'], 1):
      edges[int(t['*'])].graphObject_.HighLight(1)

def event_callback(event, before=None, oldstate=None, newstate=None):
  highlight_states(eventhandler.state, sc)
  highlight_trans(eventhandler, sc, root)

def generate_java(canvas):
  jname=canvas.statusbar.getState(StatusBar.MODEL)[1][0]
  if not jname or jname=="Nonamed":
    jname=tkFileDialog.asksaveasfilename(filetypes=[("Java source code", "*.java")])
  else:
    if StringUtil.endswith(jname, ".py"):
      jname=jname[:len(jname)-3]+".java"
    jname=os.path.split(jname)[1]
    jname=tkFileDialog.asksaveasfilename(initialfile=jname, filetypes=[("Java source code", "*.java")], initialdir=canvas.codeGenDir)
  if jname:
    if StringUtil.endswith(jname, ".java"):
      mname=jname[:len(jname)-5]+".des"
    else:
      mname=jname+".java"

    desc=generate_description(canvas, 0)["desc"]
    eventhandler=EventHandler(mname, modeltext=desc)
    g=JavaGenerator(eventhandler)
    code=g.generate_code()

    # Save .java file
    jf=open(jname, "w")
    jf.write(code)
    jf.close()
    # Print on success
    print "Java code saved to: " + jname

def finalize_simulation():
  # Reset all the colors
  colors=sc["colors"]
  trans=sc["trans"]
  for c in colors.keys():
    c.HighLight(0)
    c.setColor(colors[c])
  for t in trans:
    try:
      t['e'].graphObject_.HighLight(0)
    except:
      pass
