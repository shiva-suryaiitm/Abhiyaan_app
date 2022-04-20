#!/usr/bin/python3
import string
import rospy
from std_msgs.msg import String



def remake(data):
    data1 = data.data
    print(data1)
    
def inv_lis():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True) # anonymous = true helps to avoid name conflict

    rospy.Subscriber("abhiyaan_team", String, remake) #callback is a function

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


        
if __name__ == '__main__':
    inv_lis()