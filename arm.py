from Core.model import Model, Joint
from Core.vrep import simxPauseCommunication
import yaml
import client
import numpy as np


class Arm(Model):
    def __init__(self, client: int, object_name, id, dh_path=''):
        self.objectName = object_name + id  # to differentiate between robots of the same type
        super().__init__(client, self.objectName)
        # joint units
        self.joint1 = Joint(client, "joint1")
        self.joint2 = Joint(client, "joint2")
        self.joint3 = Joint(client, "joint3")
        self.joint4 = Joint(client, "joint4")
        self.joint5 = Joint(client, "joint5")
        self.joint6 = Joint(client, "joint6")
        # dh table
        self.dhdict = yaml.safe_load(dh_path)
        # save forward kinematics matrix to avoid repeated calculations
        self.fkmat = fkInit(self.dhdict)

    def _fkInit(self, dhdict):
        Tmat = _getTmat()
        return 0

    def fk(self, joint_angles):
        """
        Brief description: move robot in joint-space directly
        Parameters:
            joint_angles: a list of six desired joint angles to move to
        Return values: None
        update log: FrozenPenguinn on 2022/05/18
        """
        end_effector_pos = 0
        return end_effector_pos

    def ik(self, goal):
        joint_angles = 0
        return joint_angles

    def moveJ(self, dest):
        return

    def moveL(self, dest):
        return

    def moveC(self, dest):
        return

    def moveAbsJ(self, dest_angles: list):
        """
        Brief description: move robot in joint-space directly
        Parameters:
            joint_angles: a list of six desired joint angles to move to
        Return values: None
        update log: FrozenPenguinn on 2022/05/18
        """
        simxPauseCommunication(self.client.ID, True)
        self.joint1.set_angle(dest_angles[0])
        self.joint2.set_angle(dest_angles[1])
        self.joint3.set_angle(dest_angles[2])
        self.joint4.set_angle(dest_angles[3])
        self.joint5.set_angle(dest_angles[4])
        self.joint6.set_angle(dest_angles[5])
        simxPauseCommunication(self.client.ID, False)
        return


class IRB140(Arm):
    def __init__(self, client, object_name="IRB140", id=""):
        super().__init__(client, object_name, id)


class UR5(Arm):
    def __init__(self, client, object_name="UR5", id=""):
        super().__init__(client, object_name, id)
