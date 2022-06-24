import client
import arm
from time import sleep
from sympy import *
from math import pi

# ================ Step 1 ====================== #
client = client.Client(ip='127.0.0.1', port=19999) # 连接 Vrep 服务器

robot = arm.UR5(client, id="") # 连接ABB机器人
# camera = sensor.Camera(client, id="") # 连接摄像头

# ================ Step 2 ====================== #
robot.moveAbsJ(1,0,0,0,0)

sleep(1)
# image = camera.read()
