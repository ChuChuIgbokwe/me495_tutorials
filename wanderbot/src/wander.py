#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on July 27, 2016 by 4:55 PM

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Wandering(object):
    def __init__(self):
        '''
        Initialize parameters
        '''
        rospy.init_node('wander')
        self.cmd_vel_pub = rospy.Publisher('cmd_vel',Twist,queue_size=1)
        self.twist = Twist()
        self.state_change_time = rospy.Time.now()
        self.driving_forward = True
        self.rate = rospy.Rate(10)

    def scan_callback(self,msg):
        '''
        The callback function contains what you want to do with the data stream you receive
        In this case the turtlebot will drive in a straight line until it detects an obstacle within 1.2m.If it doesn't
        detect an obstacle after 10 seconds it will stop moving forward and spin for five seconds befor moving forward
        again.
        :param msg:
        :return: nothing to return
        '''
        g_range_ahead = min(msg.ranges)
        rospy.loginfo("range ahead: %0.1f" % g_range_ahead)
        if self.driving_forward:
            self.twist.linear.x = 0.2
            self.twist.angular.z = 0
            rospy.loginfo('Moving')
            if g_range_ahead < 1.2 or rospy.Time.now() > self.state_change_time:
                self.driving_forward = False
                self.state_change_time = rospy.Time.now() + rospy.Duration(5)
        else:
            self.twist.angular.z = 1
            self.twist.linear.x = 0
            rospy.loginfo('Spinning')
            if rospy.Time.now() > self.state_change_time: #check that 5 seconds have elapsed
                self.driving_forward = True
                rospy.loginfo('Switch')
                self.state_change_time = rospy.Time.now() + rospy.Duration(10) #change states after 10 seconds

        self.cmd_vel_pub.publish(self.twist)
        self.rate.sleep()

def main():
    wandering = Wandering()
    rospy.Subscriber('/scan', LaserScan, wandering.scan_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

if __name__=='__main__':
    main()