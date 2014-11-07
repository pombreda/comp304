format 71

classinstance 128225 class_ref 128013 // SudokuGUI
  name ""   xyz 41 4 2000 life_line_z 2000
classinstance 128353 class_ref 128225 // BoardStateObserver
  name ""   xyz 165 4 2000 life_line_z 2000
classinstance 128481 class_ref 128141 // SudokuBoardState
  name ""   xyz 334 4 2000 life_line_z 2000
durationcanvas 128609 classinstance_ref 128225 // :SudokuGUI
  xyzwh 66 71 2010 11 93
end
durationcanvas 128737 classinstance_ref 128353 // :BoardStateObserver
  xyzwh 207 69 2010 11 34
end
durationcanvas 129121 classinstance_ref 128481 // :SudokuBoardState
  xyzwh 372 119 2010 11 40
end
durationcanvas 129889 classinstance_ref 128481 // :SudokuBoardState
  xyzwh 372 186 2010 11 79
end
durationcanvas 130145 classinstance_ref 128353 // :BoardStateObserver
  xyzwh 207 214 2010 11 39
end
msg 128865 synchronous
  from durationcanvas_ref 128609
  to durationcanvas_ref 128737
  yz 71 2015 explicitmsg "<<creates>>"
  show_full_operations_definition default drawing_language default
  label_xy 118 60
msg 128993 return
  from durationcanvas_ref 128737
  to durationcanvas_ref 128609
  yz 92 2020 unspecifiedmsg
  show_full_operations_definition default drawing_language default
msg 129249 synchronous
  from durationcanvas_ref 128609
  to durationcanvas_ref 129121
  yz 121 2025 msg operation_ref 128097 // "addObserver(in self : , in observer : )"
  show_full_operations_definition default drawing_language default
  label_xy 225 113
msg 129377 return
  from durationcanvas_ref 129121
  to durationcanvas_ref 128609
  yz 141 2030 unspecifiedmsg
  show_full_operations_definition default drawing_language default
reflexivemsg 130017 synchronous
  to durationcanvas_ref 129889
  yz 186 2015 msg operation_ref 128353 // "notifyObservers(in self : )"
  show_full_operations_definition default drawing_language default
  label_xy 389 175
msg 130273 synchronous
  from durationcanvas_ref 129889
  to durationcanvas_ref 130145
  yz 215 2015 msg operation_ref 129505 // "boardStateChanged(in self : , in board : )"
  show_full_operations_definition default drawing_language default
  label_xy 252 204
msg 130401 return
  from durationcanvas_ref 130145
  to durationcanvas_ref 129889
  yz 237 2020 unspecifiedmsg
  show_full_operations_definition default drawing_language default
end
