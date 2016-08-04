#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on July 27, 2016 by 4:31 PM

import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
    range_ahead = msg.ranges[len(msg.ranges)/2] #select middle element of the ranges array
    #closest_range = min(msg.ranges) #range of closest obstacle detected by the scanner
    rospy.loginfo("range ahead: %0.1f" % range_ahead)

def main():
    rospy.init_node('range_ahead')
    scan_sub = rospy.Subscriber('/scan',LaserScan,scan_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting Down")

if __name__=='__main__':
    main()