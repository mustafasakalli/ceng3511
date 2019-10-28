
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model

import csv

with open('kokuros_input.txt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        numbers=[i for row in spamreader for i in row]
       

def kokuros_solver():

    rows = numbers[:len(numbers)//2]
    columns = numbers[len(numbers)//2:]

    model = cp_model.CpModel()

    domain = 10
    a1 = model.NewIntVar(1, domain - 1, 'a1')
    a2 = model.NewIntVar(1, domain - 1, 'a2')
    a3 = model.NewIntVar(1, domain - 1, 'a3')
    b1 = model.NewIntVar(1, domain - 1, 'b1')
    b2 = model.NewIntVar(1, domain - 1, 'b2')
    b3 = model.NewIntVar(1, domain - 1, 'b3')
    c1 = model.NewIntVar(1, domain - 1, 'c1')
    c2 = model.NewIntVar(1, domain - 1, 'c2')
    c3 = model.NewIntVar(1 , domain - 1, 'c3')

    cells = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    
    rowA = [a1, a2, a3]
    rowB = [b1, b2, b3]
    rowC = [c1, c2, c3]
    colA = [a1, b1, c1]
    colB = [a2, b2, c2]
    colC = [a3, b3, c3]

    model.AddAllDifferent(rowA)
    model.AddAllDifferent(rowB)
    model.AddAllDifferent(rowC)
    model.AddAllDifferent(colA)
    model.AddAllDifferent(colB)
    model.AddAllDifferent(colC)
    
    row0add = a1 + a2 + a3 
    row1add = b1 + b2 + b3
    row2add = c1 + c2 + c3
    column0add = a1 + b1 + c1
    column1add = a2 + b2 + c2
    column2add = a3 + b3 + c3
    
    model.Add(int(rows[0]) == row0add )
    model.Add(int(rows[1]) == row1add )
    model.Add(int(rows[2]) == row2add  )
    model.Add(int(columns[0]) == column0add )
    model.Add(int(columns[1]) == column1add )
    model.Add(int(columns[2]) == column2add )
   

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
            print('%i' % solver.Value(a1), '%i' % solver.Value(a2), '%i' % solver.Value(a3))
           
            print('%i' % solver.Value(b1), '%i' % solver.Value(b2), '%i' % solver.Value(b3))
            
            print('%i' % solver.Value(c1), '%i' % solver.Value(c2), '%i' % solver.Value(c3))
            
    
    
kokuros_solver()