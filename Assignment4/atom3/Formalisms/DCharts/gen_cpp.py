

# The following demonstrates the API provided byAToM3

# to access a model on the canvas.

#

# Hans Vangheluwe Fall 2005

#



def gen_cpp(parentApp, model):
  
  print '\n\nDEMONSTRATION TEMPLATE START\n\n'

  # <parentApp> is the "parent" application object

  # It is visible from all buttons, nodes, ...

  # Hence, it can be used to store "global" information in.

  # It is also from here that new Toplevel (Tkinter) GUI windows 

  # should be created.



  # <model> is a hypergraph structure consisting of 

  # connected "nodes". The nodes in the data structure

  # are both DChart nodes (basic states, composite states, ...)

  # and DChart links (transitions and "insideness" relationships).



  # The <model> node has attributes corresponding to the

  # global "model attributes" (none in case of DCharts models).

  # Node attributes can be accessed directly as attributes

  # They are AToM3 entities however and thus need .getValue()

  # to access their value, e.g., node.name.getValue()



  # model.listNodes is a dictionary

  # Its keys are the names of all node types in the model

  # 

  print "model.listNodes"

  print model.listNodes

  print ""



  # model.listNodes.keys() gives us the keys only"

  print "model.listNodes.keys()"

  print model.listNodes.keys()

  print ""



  # Keys can be used to access the list of all nodes

  # of a particular type directly, for example

  print "model.listNodes['Basic']"

  print model.listNodes["Basic"]

  print ""

  # Note that Basic, History, Composite, and Orthogonal

  # are the main types of nodes used in DCharts.

  # The main connection types (also nodes) are

  # contains, orthogonality and Hyperedge.

  # (the above information comes from the DCharts meta-model) 



  # We can thus iterate over all "Block" nodes

  print "Iterating over all 'Basic' nodes"

  print ""

  for node in model.listNodes["Basic"]:

   print "  Node "+str(node)+":"



   # To highlight this node, uncomment the next line

   # node.graphObject_.HighLight(1)



   # Node attributes can be accessed directly as attributes

   # They are AToM3 entities however and thus need .getValue()

   # to access their value, e.g., node.name.getValue()

   print ""

   print "  node name: "+node.name.getValue()



   print "  node is_default Python type: "+str(type(node.is_default.getValue()))

   print "  node value: "+str(node.is_default.getValue())



   # It is possible to change node attributes

   print "  Adding 'X' to node block_name attribute"

   node.name.setValue(node.name.getValue()+"X")

   print "  node name is now: "+node.name.getValue()



   # Update the model display to reflect change

   node.graphObject_.ModifyAttribute("name", node.name.toString())



#   print "  Adding '1.0' to node block_out_value attribute"

#   node.block_out_value.setValue(node.block_out_value.getValue()+1.0)

#   print "  Constant node block_out_value is now: "+str(node.block_out_value.getValue())



   # Update the model display to reflect change

#   node.graphObject_.ModifyAttribute("block_out_value", node.block_out_value.toString())

   

   # We can access any node's

   # in_connections_ and out_connections_ lists

   # Note how a link is also a node in the model!

   print ""

   print "  Iterating over all links out of node:"

   print ""

   for link in node.out_connections_:



    print "    link: "+str(link)



    # all Hyperedge links (transitions) have a trigger attribute (a string)

    signal = link.trigger.getValue()

    print signal



    # Highlight this link 

    link.graphObject_.HighLight(1)



    # Now go to the nodes this link connects to. 

    for node in link.out_connections_:

     print "      node: "+str(node)

     # We can find out a node's type

     print "      node type: "+node.getClass()



#     # Not be be confused with the node's block_type attribute

#     # block_type only makes sense for Block nodes,

#     # so we need to test for that

#     if node.getClass() == "Block":

#       blockType = node.block_type.getValue() 

#       print "      node's block_type attribute (enum): "+str(blockType)

#  

#       # An object of enum type is a tuple consisting of

#       # a list of unique enum names and an index into that

#       # list indicating which of the 

#       # For example, for an Integrator block, the block_type enum

#       # is (['Generic', 'Negator', 'Inverter', 'Adder', 'Product', 

#       # 'Delay', 'Integrator', 'Derivative', 'Constant', 'Time'], 6)

#       # To find out the string representation of the block_type,

#       # the second element of the tuple (6) is used as an index

#       # into the first element of the typle ['Generic', ... ]

#       blockTypeString = blockType[0][blockType[1]]

#       print "      node's block_type attribute (enum): "+blockTypeString

#  

#       # Some connections are "named ports"

#       # Rather than using in_connections_ or out_connections_,

#       # we can access them directly by their port name

#       if blockTypeString == "Integrator":

#        print "     This is an 'Integrator' block"

#        print "     Its block_IC_port (InitialCondition) port is connected to:"

#        print node.block_IC_port

#        print ""

#  

#       # Note how many blocks have a port called "block_output_port"

#

#  

  print '\n\nDEMONSTRATION TEMPLATE END\n\n'
