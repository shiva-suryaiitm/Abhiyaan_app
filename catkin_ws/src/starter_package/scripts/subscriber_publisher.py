#!/usr/bin/python3
import string
import rospy
from std_msgs.msg import String
from string import digits


def inverter(data):
    data1 = data.data[::-1]
    data1 = data1.translate(digits)
    #print(data1)
    try:
        reproduce(data1)
    except:
       pass
    
def absorber():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    rospy.init_node('sub_node', anonymous=True)

    rospy.Subscriber("team_abhiyaan", String, inverter)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def reproduce(x):
    pub = rospy.Publisher('abhiyaan_team', String,queue_size=10)
    hello_str = x
    pub.publish(hello_str)
    #print('1')
        
if __name__ == '__main__':
    absorber()
