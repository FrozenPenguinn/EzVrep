from sympy import *
from decimal import *

x = Matrix(4, 3, range(12))
x[2, 2]=x[2, 2]+0.2
print(x)
print(x.evalf(3))