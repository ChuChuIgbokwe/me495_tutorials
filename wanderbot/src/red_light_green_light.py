#!usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on July 26, 2016 by 2:19 PM

import rospy
from geometry_msgs import Twist

def main():
    cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.init_node('red_light_green_light')

    red_light_twist = Twist()
    green_light_twist = Twist()
    green_light_twist.linear.x = 0.5

    driving_forward = False
    light_change_time = rospy.Time.now()
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        if driving_forward:
            cmd_vel_pub.publish(green_light_twist)
        else:
            cmd_vel_pub.publish(red_light_twist)
        if light_change_time > rospy.Time.now():
            driving_forward = not driving_forward
            light_change_time  = rospy.Time.now() + rospy.Duration(3)

        rate.sleep()

if __name__=='__main__':
    main()

