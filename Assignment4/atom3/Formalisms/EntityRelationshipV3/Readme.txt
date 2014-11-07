Formalism: Entity Relationship V3

Author: Denis Dube

Date: Feb 26, 2005

Description: A fully boostrapped formalism, in the sense that generating code from the model 'EntityRelationshipV3inV3_ER_MDL.py' you will re-generate the Entity Relationship V3 formalism. In other words, this model is *itself* created with the Entity Relationship V3 formalism and re-creates the formalism when you generate code. This is extremely convenient if you wish to add/modify features of ER, such as adding text-fitting post-actions. 

Code Generation Grammar: if you wish to generate code with the Entity Relationship V3 formalism, make sure you use the code transformation 'createButtonsV3_GG_exec'. You need to set this in options (F1). Failure to do this means you will get no automatically generated buttons. 

Drawback: If code generation fails half-way through (unlikely), you would lose the formalism ER3 and then be unable to generate it again! Of course since the formalism is included in the AToM3 distribution package it shouldn't be too hard to restore it :D