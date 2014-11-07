format 71

classinstance 128097 class_ref 128013 // SudokuGUI
  name ""   xyz 14 4 2000 life_line_z 2000
classinstance 128225 class_ref 128481 // SudokuSaver
  name ""   xyz 144 4 2000 life_line_z 2000
classinstance 128353 class_ref 128141 // SudokuBoardState
  name ""   xyz 276 4 2000 life_line_z 2000
durationcanvas 128481 classinstance_ref 128097 // :SudokuGUI
  xyzwh 39 67 2010 11 126
  overlappingdurationcanvas 128993
    xyzwh 45 114 2020 11 55
  end
end
durationcanvas 128609 classinstance_ref 128225 // :SudokuSaver
  xyzwh 171 62 2010 11 39
end
durationcanvas 129249 classinstance_ref 128353 // :SudokuBoardState
  xyzwh 314 130 2010 11 29
end
msg 128737 synchronous
  from durationcanvas_ref 128481
  to durationcanvas_ref 128609
  yz 67 2015 explicitmsg "<<creates>>"
  show_full_operations_definition default drawing_language default
  label_xy 86 56
msg 128865 return
  from durationcanvas_ref 128609
  to durationcanvas_ref 128481
  yz 90 2015 unspecifiedmsg
  show_full_operations_definition default drawing_language default
reflexivemsg 129121 synchronous
  to durationcanvas_ref 128993
  yz 114 2025 msg operation_ref 129633 // "accept(in self : , in visitor : )"
  show_full_operations_definition default drawing_language default
  label_xy 57 103
msg 129377 synchronous
  from durationcanvas_ref 128993
  to durationcanvas_ref 129249
  yz 131 2030 msg operation_ref 128737 // "accept(in self : , in visitor : )"
  show_full_operations_definition default drawing_language default
  label_xy 169 120
msg 129505 return
  from durationcanvas_ref 129249
  to durationcanvas_ref 128993
  yz 148 2025 unspecifiedmsg
  show_full_operations_definition default drawing_language default
end
