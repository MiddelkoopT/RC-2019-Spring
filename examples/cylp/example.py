#!/usr/bin/python3

## https://github.com/coin-or/CyLP 

"""
Maximize
  x1 + 2*x2
Subject To
  C1: x1 + x2 <= 40
  C2: 2*x1 + x2 <= 60
Bounds
  x1 >= 0
  x2 >= 0
End

Solution
80
x1=0
x2=40
"""

import numpy as np
from cylp.cy import CyClpSimplex

s = CyClpSimplex()

# Add variables
x1 = s.addVariable('x1', 1)
x2 = s.addVariable('x2', 1)

s += x1 + x2 <= 40
s += 2*x1 + x2 <= 60

## Negative to Maximize
s.objective = -x1 - 2*x2

# Solve using primal Simplex
s.primal()
print(-s.objectiveValue,s.primalVariableSolution['x1'],s.primalVariableSolution['x2'])

s.writeMps("example.mps")
