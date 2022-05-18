"""
Using variables directly instead of numbers allows a more direct understanding of the program's inner working,
despite causing deterioration in performance, which will not be a problem in an education project like this one.
"""

from sympy import *
from math import pi


def test1():
    """
    brief description: calculation in symbols instead of numbers, like that in MATLAB
    """
    x, y = symbols('x y')
    f = sin(x) + cos(x)
    print(f.evalf(6, subs={x: pi/2, y: 1}))


if __name__ == "__main__":
    test1()
