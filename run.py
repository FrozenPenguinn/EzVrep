import client, arm # 服务器，机械臂
import time

client = client.Client(ip='127.0.0.1', port=19999) # 连接 Vrep 服务器

robot = arm.UR5(client, id="") # 连接ABB机器人
# camera = sensor.Camera(client, id="") # 连接摄像头

robot.moveAbsJ([90, 45, -45, 0, 0, 0])

time.sleep(1)
help(robot.moveAbsJ)
# image = camera.read()
