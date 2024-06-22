from robot import Robot
from config.config import ROBOT_PORTS

# init robots
leader = Robot(device_name=ROBOT_PORTS['leader'], servo_ids=[7, 8, 9, 10, 11, 12])
follower = Robot(device_name=ROBOT_PORTS['follower'], servo_ids=[1, 2, 3, 4, 5, 6])

leader._disable_torque()
follower._disable_torque()