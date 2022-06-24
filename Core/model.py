from .vrep import *
from .vrepConst import *
from math import pi

class Model(object):
    def __init__(self, client, objectName):
        self.client = client
        self.objectName = objectName
        self.objectHandle = client.bind(self.objectName)
        return

    def place(self, position, orientation):
        return


class Joint(Model):

    def set_velocity(self, speed):
        simxSetJointTargetVelocity(self.client.ID, self.objectHandle, speed, simx_opmode_streaming)
        return

    def set_angle(self, angle):
        simxSetJointTargetPosition(self.client.ID,  self.objectHandle, angle * pi / 180, simx_opmode_oneshot)
        return
