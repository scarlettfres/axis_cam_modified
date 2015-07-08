#!/usr/bin/env python

import rospy
import math
from axis_camera.msg import Axis
import tf
from tf.transformations import quaternion_from_euler, euler_from_quaternion

base_name = "/axis_camera"
base_frame = "/axis_camera_init"
broadcaster = tf.TransformBroadcaster()
PAN = -29.9032001495
TILT = -69.8181991577


def axis_cb(data):

    listener = tf.TransformListener()  # ????

    print '111111111'
    # (trans, rot) = listener.lookupTransform(
    #     "/axis_camera_init", '/map', rospy.Time(0))

    rot = (0.6287990110164235, 0.7480819940486101, -0.1563927862398917,
           -0.14327047964303885)

    print "22222"
    # il y avait un plus pi ici

    pan = (data.pan - PAN) * math.pi / 180.
    tilt = -(data.tilt - TILT) * math.pi / 180.
    print "pan = ", pan
    print "tilt", tilt
    euler = euler_from_quaternion(rot)
    euler_modif = (euler[0] - tilt, euler[1], euler[2] - pan)
    q = quaternion_from_euler(euler_modif[0], euler_modif[1], euler_modif[2])
    now = rospy.Time.now()
    broadcaster.sendTransform((0.6251185950728501, -0.9568288250572693, 2.5808307217613855),
                              q, now, base_name, "/map")


if __name__ == '__main__':
    try:
        rospy.init_node("axis_tf_broadcaster")
        # base_frame = rospy.get_param("~base_frame", base_frame)
        # base_name = rospy.get_param("~base_name", base_name)
        # print base_name, base_frame

        axis_sub = rospy.Subscriber("/state", Axis, axis_cb)
        rospy.loginfo("Started Axis TF broadcaster")
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
