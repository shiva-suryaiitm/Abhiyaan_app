#!/usr/bin/env python3
from pickletools import read_unicodestring1
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys
import time
import math 

x_vel1 = 0
y_vel1 = 0
x_vel2 = 0
y_vel2 = 0

x2 = 0
y2 = 0
x1 = 0
y1 = 0
 


a = float(input("Enter alpha value (Which is used as F = alpha/d^2) : "))
initial_vel_x1 = float(input("Enter Intial x1 vel : "))
initial_vel_y1 = float(input("Enter Intial y1 vel : "))
initial_vel_x2 = float(input("Enter Intial x2 vel : "))
initial_vel_y2 = float(input("Enter Intial y2 vel : "))


def position1(data):
    global x1 ,y1
    x1 = round(data.x,3)
    y1 = round(data.y,3)

    
def position2(data):
    global x2,y2
    x2 = round(data.x,3)
    y2 = round(data.y,3)
    force_vel1(x1,y1,x2,y2,a)
    force_vel2(x2,y2,x1,y1,a)

    
def get_position():
    rospy.Subscriber("/turtle1/pose",Pose,callback=position1)
    rospy.Subscriber("/turtle2/pose",Pose,callback=position2)

    
def publish_vel():
    rospy.init_node('check_odometry',anonymous=True)
    pub1 = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
    pub2 = rospy.Publisher('/turtle2/cmd_vel',Twist, queue_size=10)
    rate = rospy.Rate(100)
    vel1 = Twist()
    vel2 = Twist()
    vel1.linear.x= initial_vel_x1
    vel1.linear.y= initial_vel_y1
    vel2.linear.x= initial_vel_x2
    vel2.linear.y= initial_vel_y2
    
    while not rospy.is_shutdown():
        get_position()
        vel1.linear.x += x_vel1
        vel1.linear.y += y_vel1
        vel2.linear.x += x_vel2
        vel2.linear.y += y_vel2
        
        '''if vel1.linear.x > 0.5:
            vel1.linear.x = vel1.linear.x * 0.99
        if vel1.linear.y > 0.5:
            vel1.linear.y = vel1.linear.y * 0.99
        if vel2.linear.x > 0.5:
            vel2.linear.x = vel2.linear.x * 0.99
        if vel2.linear.y > 0.5:
            vel2.linear.y = vel2.linear.y * 0.99'''
            
        pub1.publish(vel1)
        pub2.publish(vel2)
        rate.sleep()
        #c = time.time()
        
def force_vel1(x,y,x0,y0,alpha):
    d = ((-x+x0)**2 + (-y+y0)**2)**0.5
    F = alpha / (d)**2
    global x_vel1 , y_vel1
    temp_vel_x = (F*0.005*(x0-x)/d)
    temp_vel_y = (F*0.005*(y0-y)/d)
    x_vel1 , y_vel1 = temp_vel_x , temp_vel_y
    return None


def force_vel2(x,y,x0,y0,alpha):
    d = ((-x+x0)**2 + (-y+y0)**2)**0.5
    F = alpha / (d)**2
    global x_vel2 , y_vel2
    temp_vel_x = F*0.005*(x0-x)/d
    temp_vel_y = F*0.005*(y0-y)/d
    #print(temp_vel_x , temp_vel_y)
    x_vel2 , y_vel2 = temp_vel_x , temp_vel_y
    return None
        
        
if __name__ == '__main__':
    try:
        publish_vel()
    except rospy.ROSInterruptException:
        pass
    
