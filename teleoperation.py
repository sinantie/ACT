from robot import Robot
from config.config import ROBOT_PORTS

# init robots
leader = Robot(device_name=ROBOT_PORTS['leader'], servo_ids=[7, 8, 9, 10, 11, 12])
follower = Robot(device_name=ROBOT_PORTS['follower'], servo_ids=[1, 2, 3, 4, 5, 6])
# activate the leader gripper torque
leader.set_trigger_torque()

while True:
    follower.set_goal_pos(leader.read_position())

leader._disable_torque()
follower._disable_torque()