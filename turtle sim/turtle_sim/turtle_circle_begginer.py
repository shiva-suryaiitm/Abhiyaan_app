#!/usr/bin/env python3
from pickletools import read_unicodestring1
import rospy
from geometry_msgs.msg import Twist
import sys
import turtle


def turtle_circle(radius=1):
    t = 0
    rospy.init_node('turtlesim', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',
                        Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    t=0
    while not rospy.is_shutdown():
        t = t+0.01
        vel.linear.x = radius
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = radius-t
        rospy.loginfo("Radius = %f",
                    radius)
        pub.publish(vel)
        rate.sleep()


if __name__ == '__main__':
	try:
		turtle_circle(float(sys.argv[1]))
	except rospy.ROSInterruptException:
		pass
#turtle.circle(80,90)
#k = input('')