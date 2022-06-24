import sympy as sym
import numpy as np
from math import pi, atan2, acos, sqrt


class Kinematics(object):
    def __init__(self, dh):
        # inverse kinematics parameters
        self.d1 = dh[0, 0]
        self.d2 = dh[0, 1]
        self.d3 = dh[0, 2]
        self.d4 = dh[0, 3]
        self.d5 = dh[0, 4]
        self.d6 = dh[0, 5]
        self.a1 = dh[1, 0]
        self.a2 = dh[1, 1]
        self.a3 = dh[1, 2]
        self.a4 = dh[1, 3]
        self.a5 = dh[1, 4]
        self.a6 = dh[1, 5]
        self.alpha1 = dh[2, 0]
        self.alpha2 = dh[2, 1]
        self.alpha3 = dh[2, 2]
        self.alpha4 = dh[2, 3]
        self.alpha5 = dh[2, 4]
        self.alpha6 = dh[2, 5]
        # forward kinematics parameters
        self.T01 = get_tmat(dh[0, 0], dh[1, 0], dh[2, 0])
        self.T12 = get_tmat(dh[0, 1], dh[1, 1], dh[2, 1])
        self.T23 = get_tmat(dh[0, 2], dh[1, 2], dh[2, 2])
        self.T34 = get_tmat(dh[0, 3], dh[1, 3], dh[2, 3])
        self.T45 = get_tmat(dh[0, 4], dh[1, 4], dh[2, 4])
        self.T56 = get_tmat(dh[0, 5], dh[1, 5], dh[2, 5])

    def fk(self, joint_angles):
        """
            Brief description: obtain destination pos and ori given a set of joint angles
            Parameters:
                joint_angles: a set of 6 joint angles
            Return values: a transformation matrix expression of destination pos and ori
            update log: FrozenPenguinn on 2022/06/24
        """
        t01 = self.T01.evalf(6, subs={theta: joint_angles[0]})
        t12 = self.T01.evalf(6, subs={theta: joint_angles[1]})
        t23 = self.T01.evalf(6, subs={theta: joint_angles[2]})
        t34 = self.T01.evalf(6, subs={theta: joint_angles[3]})
        t45 = self.T01.evalf(6, subs={theta: joint_angles[4]})
        t56 = self.T01.evalf(6, subs={theta: joint_angles[5]})
        return (t01 * t12 * t23 * t34 * t45 * t56).applyfunc(lambda x: round(x, 3))

    def ik(self, dest):
        """
            Brief description: obtain workable joint angles to obtain desired destination pos and ori
            Parameters:
                dest: transformation matrix expression of destination pos and ori
            Return values: a matrix of 8 workable joint angles
            Reference: https://www.bbsmax.com/A/MyJxe4Ya5n/
            update log: FrozenPenguinn on 2022/06/24
        """
        # rearrange symbols in matrix for better understanding
        nx, ny, nz = dest[0, 0], dest[1, 0], dest[2, 0]  # this is different from x,y,z = dest[:,0]
        ox, oy, oz = dest[0, 1], dest[1, 1], dest[2, 1]
        ax, ay, az = dest[0, 2], dest[1, 2], dest[2, 2]
        px, py, pz = dest[0, 3], dest[1, 3], dest[2, 3]
        # container for saving the 8 ik results
        thetas = np.zeros([8, 6])
        # solve for theta 1
        print((px - self.d6*ax)**2)
        #print(acos(self.d4 / sqrt((self.d6*ay - py)**2 + (px - self.d6*ax)**2)))
        #thetas[0:4, 0] = acos(self.d4 / sqrt((self.d6*ay - py)**2 + (px - self.d6*ax)**2)) + atan2(px - self.d6*ax, self.d6*ay - py)
        #thetas[4:8, 0] = alpha1 - alpha2 + pi / 2
        # solve for theta 5
        #for i in range(0, 2):
            #thetas[i, 1] = acos((px*sin(thetas[i, 0]) - py*cos(thetas[i, 1]) - self.d4) / self.d6)
        return


theta = sym.symbols('theta')


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
    tmat = sym.Matrix([[sym.cos(theta), -sym.sin(theta) * sym.cos(alpha), sym.sin(theta) * sym.sin(alpha), a * sym.cos(theta)],
                       [sym.sin(theta), sym.cos(theta) * sym.cos(alpha), -sym.cos(theta) * sym.sin(alpha), a * sym.sin(theta)],
                       [0, sym.sin(alpha), sym.cos(alpha), d],
                       [0, 0, 0, 1]])
    return tmat


dh = np.matrix([[89.459, 0, 0, 109.15, 94.65, 82.3],
                [0, -425, -392.25, 0, 0, 0],
                [pi/2, 0, 0, pi/2, -pi/2, 0]])
solver = Kinematics(dh)
fk_reult = solver.fk([0,0,0,0,0,0])
print(fk_reult)
destination = np.matrix(fk_reult)
print(solver.ik(destination))