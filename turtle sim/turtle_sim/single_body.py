#!/usr/bin/env python3
from pickletools import read_unicodestring1
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys
import time
import math 
x_vel = 0
y_vel = 0



initial_x = float(input("Enter  x position (Which is used as a center): "))
initial_y = float(input("Enter  y position (Which is used as a cemter): "))
a = float(input("Enter alpha value (Which is used as F= alpha/d^2) "))
initial_vel_x = float(input("Enter Intial x vel : "))
initial_vel_y = float(input("Enter Intial y vel : "))

def position(data):
    x = round(data.x,3)
    y = round(data.y,3)
    force_vel(x,y,initial_x,initial_y,a)
    
def get_position():
    rospy.Subscriber("/turtle1/pose",Pose,callback=position)

    
def publish_vel():
    rospy.init_node('check_odometry',anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
    vel = Twist()
    vel.linear.x= initial_vel_x
    vel.linear.y= initial_vel_y
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        get_position()
        vel.linear.x += x_vel
        vel.linear.y += y_vel
        #print(vel.linear.x ,vel.linear.y )
        #print(c-time.time())
        pub.publish(vel)
        #c = time.time()
        rate.sleep()
        
def force_vel(x,y,x0,y0,alpha):
    d = ((-x+x0)**2 + (y-y0)**2)**0.5
    F = alpha / (d)**2
    global x_vel , y_vel
    vel_x = F*0.005*(x0-x)/d
    vel_y = F*0.005*(y0-y)/d
    #print(vel_x , vel_y)
    x_vel , y_vel = vel_x , vel_y
    k = time.time()
    return None
        
        
if __name__ == '__main__':
    try:
        publish_vel()
    except rospy.ROSInterruptException:
        pass
    
