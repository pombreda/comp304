format 71

classcanvas 128097 class_ref 128353 // SudokuVisitor
  draw_all_relations default hide_attributes default hide_operations default hide_getset_operations default show_members_full_definition default show_members_visibility default show_members_stereotype default show_members_multiplicity default show_members_initialization default show_attribute_modifiers default member_max_width 0 show_parameter_dir default show_parameter_name default package_name_in_tab default class_drawing_mode default drawing_language default show_context_mode default auto_label_position default show_relation_modifiers default show_relation_visibility default show_infonote default shadow default show_stereotype_properties default
  xyz 23 85 2000
end
classcanvas 128225 class_ref 128481 // SudokuSaver
  draw_all_relations default hide_attributes default hide_operations default hide_getset_operations default show_members_full_definition default show_members_visibility default show_members_stereotype default show_members_multiplicity default show_members_initialization default show_attribute_modifiers default member_max_width 0 show_parameter_dir default show_parameter_name default package_name_in_tab default class_drawing_mode default drawing_language default show_context_mode default auto_label_position default show_relation_modifiers default show_relation_visibility default show_infonote default shadow default show_stereotype_properties default
  xyz 22 211 2006
end
classcanvas 129249 class_ref 128141 // SudokuBoardState
  draw_all_relations default hide_attributes default hide_operations default hide_getset_operations default show_members_full_definition default show_members_visibility default show_members_stereotype default show_members_multiplicity default show_members_initialization default show_attribute_modifiers default member_max_width 0 show_parameter_dir default show_parameter_name default package_name_in_tab default class_drawing_mode default drawing_language default show_context_mode default auto_label_position default show_relation_modifiers default show_relation_visibility default show_infonote default shadow default show_stereotype_properties default
  xyz 370 23 2000
end
classcanvas 129633 class_ref 128013 // SudokuGUI
  draw_all_relations default hide_attributes default hide_operations default hide_getset_operations default show_members_full_definition default show_members_visibility default show_members_stereotype default show_members_multiplicity default show_members_initialization default show_attribute_modifiers default member_max_width 0 show_parameter_dir default show_parameter_name default package_name_in_tab default class_drawing_mode default drawing_language default show_context_mode default auto_label_position default show_relation_modifiers default show_relation_visibility default show_infonote default shadow default show_stereotype_properties default
  xyz 191 159 3005
end
relationcanvas 128353 relation_ref 128353 // <realization>
  from ref 128225 z 2007 to ref 128097
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 130017 relation_ref 143201 // <dependency>
  from ref 129249 z 2001 to ref 128097
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 130145 relation_ref 143329 // <dependency>
  from ref 129633 z 3006 to ref 128097
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 130273 relation_ref 143841 // <unidirectional association>
  from ref 129633 z 3006 to ref 129249
  role_a_pos 336 127 3000 no_role_b
  no_multiplicity_a no_multiplicity_b
end
end
