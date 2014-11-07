* Infeasible SOS1 example problem from the CPLEX reference manual made feasible
* by converting to a SOS2 problem and a reindexing the last two SOS members.
*
NAME          ex1sos
ROWS
 N  obj
 L  c1
 L  c2
 E  c3
COLUMNS
    x1        obj                 -1   c1                  -1
    x1        c2                   1
    x2        obj                 -2   c1                   1
    x2        c2                  -3   c3                   1
    x3        obj                 -3   c1                   1
    x3        c2                   1
    x4        obj                 -1   c1                  10
    x4        c3                -3.5
RHS
    rhs       c1                  20   c2                  30
BOUNDS
 UP BOUND     x1                  40
 LI BOUND     x3                   2
 UI BOUND     x3                   3
SOS
 S2 SOS       SOS2                10
    SOS       x1               10000
    SOS       x2               20000
    SOS       x3               40000
    SOS       x4               50000
ENDATA
