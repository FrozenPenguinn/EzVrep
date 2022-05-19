"""
Using variables directly instead of numbers allows a more direct understanding of the program's inner working,
despite causing deterioration in performance, which will not be a problem in an education project like this one.
"""
import numpy as np
from sympy import *
from math import pi


def test1():
    """
    brief description: calculation in symbols instead of numbers, like that in MATLAB
    update log: FrozenPenguinn on 2022/05/18
    """
    x, y = symbols('x y')
    f = sin(x) + cos(x)
    print(f.evalf(6, subs={x: pi/2, y: 1}))


def test2():
    """
    brief description: combining symbolic calculation with numpy matrix
    update log: FrozenPenguinn on 2022/05/19
    """
    a, b = symbols('a, b')
    f1 = Matrix([[a, 0, 0], [0, a, 0], [0, 0, a]])
    f2 = Matrix([[b, 0, 0], [0, b, 0], [0, 0, b]])
    f = f1 * f2
    print(f)  # print symbolic representation of matrix
    print(f.evalf(6, subs={a: 1, b: 2}))  # print matrix with symbols replaced by numbers


if __name__ == "__main__":
    test2()
