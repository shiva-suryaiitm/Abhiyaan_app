#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String

def talking_tom():
    pub = rospy.Publisher('team_abhiyaan', String, queue_size=100)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(2) 
    while not rospy.is_shutdown():
        hello_str = "Team Abhiyaan Rocks"
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talking_tom()
    except rospy.ROSInterruptException:
        pass