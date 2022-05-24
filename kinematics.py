from sympy import *
import numpy as np
from math import pi


class Kinematics():

    def __init__(self, dh):
        self.T01 = get_tmat(dh[0, 0], dh[1, 0], dh[2, 0])
        self.T12 = get_tmat(dh[0, 1], dh[1, 1], dh[2, 1])
        self.T23 = get_tmat(dh[0, 2], dh[1, 2], dh[2, 2])
        self.T34 = get_tmat(dh[0, 3], dh[1, 3], dh[2, 3])
        self.T45 = get_tmat(dh[0, 4], dh[1, 4], dh[2, 4])
        self.T56 = get_tmat(dh[0, 5], dh[1, 5], dh[2, 5])
        return

    def fk(self, joint_angles):
        t01 = self.T01.evalf(6, subs={theta: joint_angles[0]})
        t12 = self.T01.evalf(6, subs={theta: joint_angles[1]})
        t23 = self.T01.evalf(6, subs={theta: joint_angles[2]})
        t34 = self.T01.evalf(6, subs={theta: joint_angles[3]})
        t45 = self.T01.evalf(6, subs={theta: joint_angles[4]})
        t56 = self.T01.evalf(6, subs={theta: joint_angles[5]})
        return t01 * t12 * t23 * t34 * t45 * t56

    def ik(self, goal_pos):
        return


theta = symbols('theta')


def get_tmat(d, a, alpha):
    """
    Brief description: generate a symbolic representation of transformation matrix based on DH parameters
    Parameters:
        d:
        a:
        alpha:
    Return values: a symbolic representation of transformation matrix
    update log: FrozenPenguinn on 2022/05/19
    """
    tmat = Matrix([[cos(theta), -sin(theta) * cos(alpha), sin(theta) * sin(alpha), a * cos(theta)],
                       [sin(theta), cos(theta) * cos(alpha), -cos(theta) * sin(alpha), a * sin(theta)],
                       [0, sin(alpha), cos(alpha), d],
                       [0, 0, 0, 1]])
    return tmat


dh = np.matrix([[89.459, 0, 0, 109.15, 94.65, 82.3],
                [0, -425, -392.25, 0, 0, 0],
                [pi/2, 0, 0, pi/2, -pi/2, 0]])
solver = Kinematics(dh)
print(solver.T01)