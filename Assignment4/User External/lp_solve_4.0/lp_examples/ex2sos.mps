* Infeasible SOS1 example problem from the CPLEX reference manual, here made
* feasible by converting to a SOS2 problem and reindexing the last two SOS members.
* Optimal value is -30 with the solution vector [ 0, 10.5, 3, 0].
*
NAME          ex2sos
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
    x3        c3                -3.5
    x4        obj                 -1   c1                  10
RHS
    rhs       c1                  20   c2                  30
BOUNDS
 UP BOUND     x1                  40
 LI BOUND     x3                   2
 UI BOUND     x3                   3
SOS
 S2 SET       SOS2                10
    SET       x1               10000
    SET       x2               20000
    SET       x3               40000
    SET       x4               50000
ENDATA
