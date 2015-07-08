#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from axis_camera.msg import Axis
import sys
import select
import termios
import tty
import time


if __name__ == "__main__":

    rospy.init_node('_init_pose_axis')
    pub = rospy.Publisher('cmd', Axis, queue_size=5)
    state = Axis()

    state.pan = -107.709701538
    state.tilt = -36.0
    time.sleep(1)
    pub.publish(state)
    time.sleep(1)
