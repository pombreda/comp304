* Feasible SOS2 example problem from the article "Interpolation with GAMS",
* by Erwin Kalvelagen (erwin@gams.com), January 26, 2002.
*
* Optimal value is 105.75 with the (non-zero) solution vector:
*
* Problem variables         x2           =      100.0000
*                           x3           =      260.0000
*                           x4           =      325.0000
*                           x5           =      200.0000
*                           x6           =       15.0000
*                           x7           =      105.7500
*                           x39          =       12.2400
*                           x40          =       26.5680
*                           x41          =       42.7500
*                           x42          =       22.6800
*                           x43          =        1.5120
* SOS2.A                    x8           =        1.0000
* SOS2.B                    x14          =        1.0000
* SOS2.C                    x20          =        0.8000
*                           x21          =        0.2000
* SOS2.D                    x25          =        0.5833
*                           x26          =        0.4167
* SOS2.E                    x30          =        1.0000
* SOS2.F                    x33          =        0.8500
*                           x34          =        0.1500
*
NAME          ex5sos
ROWS
 N  obj
 L  c1
 L  c2
 G  c3
 G  c4
 G  c5
 E  c6
 E  c7
 E  c8
 E  c9
 E  c10
 E  c11
 E  c12
 E  c13
 E  c14
 E  c15
 E  c16
 E  c17
 E  c18
 E  c19
 E  c20
 E  c21
 E  c22
 E  c23
 E  c24
COLUMNS
    x1        c1                   1   c3                   1
    x1        c6                   1
    x2        c1                   1   c4                   1
    x2        c7                   1
    x3        c1                   1   c5                   1
    x3        c8                   1
    x4        c2                   1   c3                   1
    x4        c9                   1
    x5        c2                   1   c4                   1
    x5        c10                  1
    x6        c2                   1   c5                   1
    x6        c11                  1
    x7        obj                  1   c24                  1
    x8        c18                  1
    x9        c6                -100   c12                -18
    x9        c18                  1
    x10       c6                -200   c12              -31.5
    x10       c18                  1
    x11       c6                -500   c12              -58.5
    x11       c18                  1
    x12       c6               -1000   c12                -81
    x12       c18                  1
    x13       c19                  1
    x14       c7                -100   c13             -12.24
    x14       c19                  1
    x15       c7                -200   c13             -21.42
    x15       c19                  1
    x16       c7                -500   c13             -39.78
    x16       c19                  1
    x17       c7               -1000   c13             -55.08
    x17       c19                  1
    x18       c20                  1
    x19       c8                -100   c14             -12.96
    x19       c20                  1
    x20       c8                -200   c14             -22.68
    x20       c20                  1
    x21       c8                -500   c14             -42.12
    x21       c20                  1
    x22       c8               -1000   c14             -58.32
    x22       c20                  1
    x23       c21                  1
    x24       c9                -100   c15                -18
    x24       c21                  1
    x25       c9                -200   c15              -31.5
    x25       c21                  1
    x26       c9                -500   c15              -58.5
    x26       c21                  1
    x27       c9               -1000   c15                -81
    x27       c21                  1
    x28       c22                  1
    x29       c10               -100   c16             -12.96
    x29       c22                  1
    x30       c10               -200   c16             -22.68
    x30       c22                  1
    x31       c10               -500   c16             -42.12
    x31       c22                  1
    x32       c10              -1000   c16             -58.32
    x32       c22                  1
    x33       c23                  1
    x34       c11               -100   c17             -10.08
    x34       c23                  1
    x35       c11               -200   c17             -17.64
    x35       c23                  1
    x36       c11               -500   c17             -32.76
    x36       c23                  1
    x37       c11              -1000   c17             -45.36
    x37       c23                  1
    x38       c12                  1   c24                 -1
    x39       c13                  1   c24                 -1
    x40       c14                  1   c24                 -1
    x41       c15                  1   c24                 -1
    x42       c16                  1   c24                 -1
    x43       c17                  1   c24                 -1
RHS
    rhs       c1                 350   c2                 600
    rhs       c3                 325   c4                 300
    rhs       c5                 275   c18                  1
    rhs       c19                  1   c20                  1
    rhs       c21                  1   c22                  1
    rhs       c23                  1
BOUNDS
 FR bnd       x7
SOS
 S2 set       SOS2.A              10
    set       x8               10000
    set       x9               20000
    set       x10              40000
    set       x11              50000
    set       x12              60000
 S2 set       SOS2.B              10
    set       x13              10000
    set       x14              20000
    set       x15              40000
    set       x16              50000
    set       x17              60000
 S2 set       SOS2.C              10
    set       x18              10000
    set       x19              20000
    set       x20              40000
    set       x21              50000
    set       x22              60000
 S2 set       SOS2.D              10
    set       x23              10000
    set       x24              20000
    set       x25              40000
    set       x26              50000
    set       x27              60000
 S2 set       SOS2.E              10
    set       x28              10000
    set       x29              20000
    set       x30              40000
    set       x31              50000
    set       x32              60000
 S2 set       SOS2.F              10
    set       x33              10000
    set       x34              20000
    set       x35              40000
    set       x36              50000
    set       x37              60000
ENDATA
