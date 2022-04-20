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
a = float(input("Enter alpha value (Which is used as F= alpha/d^2) "))            # getting inputs
initial_vel_x = float(input("Enter Intial x vel : "))
initial_vel_y = float(input("Enter Intial y vel : "))

def position(data):
    x = round(data.x,3)
    y = round(data.y,3)                             # getting position of turtle
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
    global x_vel , y_vel                        # calculates force via the formula F = alpha / d^2
    vel_x = F*0.005*(x0-x)/d                    # Finds velocity using formula v = at (Here avg velocity is used) v = 1/2*at 
    vel_y = F*0.005*(y0-y)/d                    # Vx and Vy is find using the x and y comp of force , os trignometry is used here
    # print(vel_x , vel_y)                       # Vx = Fx * 0.005  ( 0.005 = 1/100 * 1/2 ) frametime = 1/100th second and 1/100*1/2 = 0.005
    x_vel , y_vel = vel_x , vel_y
    # k = time.time()
    return None
        
        
if __name__ == '__main__':
    try:
        publish_vel()
    except rospy.ROSInterruptException:
        pass
    
