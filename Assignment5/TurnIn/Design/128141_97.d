format 71

classinstance 128097 class_ref 128397 // GridWindow
  name ""   xyz 63 4 2000 life_line_z 2000
classinstance 128225 class_ref 128013 // SudokuGUI
  name ""   xyz 197 4 2000 life_line_z 2000
classinstance 128481 class_ref 128141 // SudokuBoardState
  name ""   xyz 481 4 2000 life_line_z 2000
classinstance 129377 class_ref 135137 // Command
  name "command"   xyz 328 7 2000 life_line_z 2000
durationcanvas 128609 classinstance_ref 128097 // :GridWindow
  xyzwh 89 52 2010 11 246
  overlappingdurationcanvas 131297
    xyzwh 95 156 2020 11 77
    overlappingdurationcanvas 131553
      xyzwh 101 180 2030 11 26
    end
  end
  overlappingdurationcanvas 131809
    xyzwh 95 55 2020 11 25
  end
end
durationcanvas 128737 classinstance_ref 128225 // :SudokuGUI
  xyzwh 222 79 2010 11 206
end
durationcanvas 129505 classinstance_ref 129377 // command:Command
  xyzwh 371 85 2010 11 40
end
durationcanvas 130529 classinstance_ref 129377 // command:Command
  xyzwh 371 128 2010 11 124
end
durationcanvas 130785 classinstance_ref 128481 // :SudokuBoardState
  xyzwh 519 142 2010 11 102
end
msg 128865 synchronous
  from durationcanvas_ref 128609
  to durationcanvas_ref 128737
  yz 85 2015 msg operation_ref 130273 // "makePlay(in self : , in location : , in value : )"
  show_full_operations_definition default drawing_language default
  label_xy 138 74
msg 129633 synchronous
  from durationcanvas_ref 128737
  to durationcanvas_ref 129505
  yz 92 2020 explicitmsg "<<creates>>"
  show_full_operations_definition default drawing_language default
  label_xy 275 81
msg 130017 return
  from durationcanvas_ref 129505
  to durationcanvas_ref 128737
  yz 113 2015 unspecifiedmsg
  show_full_operations_definition default drawing_language default
msg 130657 synchronous
  from durationcanvas_ref 128737
  to durationcanvas_ref 130529
  yz 134 2015 msg operation_ref 147553 // "do(in self : )"
  show_full_operations_definition default drawing_language default
  label_xy 293 123
msg 130913 synchronous
  from durationcanvas_ref 130529
  to durationcanvas_ref 130785
  yz 144 2020 msg operation_ref 128481 // "setCell(in self : , in position : , in value : )"
  show_full_operations_definition default drawing_language default
  label_xy 434 133
msg 131041 return
  from durationcanvas_ref 130785
  to durationcanvas_ref 130529
  yz 228 2015 unspecifiedmsg
  show_full_operations_definition default drawing_language default
msg 131169 return
  from durationcanvas_ref 130529
  to durationcanvas_ref 128737
  yz 233 2020 unspecifiedmsg
  show_full_operations_definition default drawing_language default
msg 131425 synchronous
  from durationcanvas_ref 130785
  to durationcanvas_ref 131297
  yz 159 2025 msg operation_ref 131553 // "boardStateChanged(in self : , in board : )"
  show_full_operations_definition default drawing_language default
  label_xy 287 148
reflexivemsg 131681 synchronous
  to durationcanvas_ref 131553
  yz 180 2035 msg operation_ref 129421 // "setNumber(in self : , in location : , in number : )"
  show_full_operations_definition default drawing_language default
  label_xy 113 169
reflexivemsg 131937 synchronous
  to durationcanvas_ref 131809
  yz 55 2025 msg operation_ref 129761 // "onKey(in self : , in event : )"
  show_full_operations_definition default drawing_language default
  label_xy 100 44
msg 132065 return
  from durationcanvas_ref 131297
  to durationcanvas_ref 130785
  yz 212 2025 unspecifiedmsg
  show_full_operations_definition default drawing_language default
msg 132193 return
  from durationcanvas_ref 128737
  to durationcanvas_ref 128609
  yz 271 2015 unspecifiedmsg
  show_full_operations_definition default drawing_language default
end
