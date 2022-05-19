from Core.model import Model, Joint
from Core.vrep import simxPauseCommunication
from sympy import *


class Arm(Model):
    def __init__(self, client, object_name, id=""):
        self.objectName = object_name + id  # to differentiate between robots of the same type
        super().__init__(client, self.objectName)
        # control units
        self.joint1 = Joint(client, "joint1")
        self.joint2 = Joint(client, "joint2")
        self.joint3 = Joint(client, "joint3")
        self.joint4 = Joint(client, "joint4")
        self.joint5 = Joint(client, "joint5")
        self.joint6 = Joint(client, "joint6")

    def Tmat(self, theta, alpha, d, l):
        """
        Brief description: generate a symbolic representation of transformation matrix based on DH parameters
        Parameters:
            theta:
            alpha:
            d:
            l:
        Return values: a symbolic representation of transformation matrix
        update log: FrozenPenguinn on 2022/05/19
        """

        return tmat

    def _fk(self, joint_angles):
        """
        Brief description: move robot in joint-space directly
        Parameters:
            joint_angles: a list of six desired joint angles to move to
        Return values: None
        update log: FrozenPenguinn on 2022/05/18
        """
        end_effector_pos = 0
        return end_effector_pos

    def _ik(self, goal):
        joint_angles = 0
        return joint_angles

    def moveJ(self, pos):
        return

    def moveL(self, pos):
        return

    def moveC(self, pos):
        return

    def moveAbsJ(self, joint_angles: list):
        """
        Brief description: move robot in joint-space directly
        Parameters:
            joint_angles: a list of six desired joint angles to move to
        Return values: None
        update log: FrozenPenguinn on 2022/05/18
        """
        simxPauseCommunication(self.client.ID, True)
        self.joint1.set_angle(joint_angles[0])
        self.joint2.set_angle(joint_angles[1])
        self.joint3.set_angle(joint_angles[2])
        self.joint4.set_angle(joint_angles[3])
        self.joint5.set_angle(joint_angles[4])
        self.joint6.set_angle(joint_angles[5])
        simxPauseCommunication(self.client.ID, False)
        return


class IRB140(Arm):
    def __init__(self, client, object_name="IRB140", id=""):
        super().__init__(client, object_name, id)


class UR5(Arm):
    def __init__(self, client, object_name="UR5", id=""):
        super().__init__(client, object_name, id)
