#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on July 28, 2016 by 9:05 PM

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# W-A-S-D video game key mapping paradigm with x as the stop key
key_mapping = {'w':[0,1],'a':[-1,0],'s':[0,-1],'d':[1,0],'x':[0,0]}


class KeysTTP(object):
    '''
    Publish message stream at 10 hz
    '''
    def __init__(self):
        rospy.init_node('keys_to_twist_using_rate')
        self.twist_pub = rospy.Publisher('cmd_vel',Twist,queue_size=1)
        self.g_last_twist = Twist()
        self.rate = rospy.Rate(10) #10hz
        self.g_vel_scales = [0.1, 0.1]  # initialize scale at a small value

    def keys_callback(self, msg):
        if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
            return  # unknown key
        vels = key_mapping[msg.data[0]]  # dictionary pair stored as a list
        self.g_last_twist.angular.z = vels[0] * self.g_vel_scales[0]
        self.g_last_twist.linear.x = vels[1] * self.g_vel_scales[1]
        # self.g_last_twist.linear.y = vels[0] * self.g_vel_scales[0]
        self.twist_pub.publish(self.g_last_twist)


def main():
    key_pub_rate = KeysTTP()
    rospy.Subscriber('keys', String, key_pub_rate.keys_callback)
    if rospy.has_param('~linear_scale'):
        key_pub_rate.g_vel_scales[1] = rospy.get_param('~linear_scale') #set the scale value to the parameter values
    else:
        rospy.logwarn("linear scale not provided; using %.1f" % key_pub_rate.g_vel_scales[1])

    if rospy.has_param('~angular_scale'):
        key_pub_rate.g_vel_scales[0] = rospy.get_param('~angular_scale') #set the scale value to the parameter values
    else:
        rospy.logwarn("angular scale not provided; using %.1f" % key_pub_rate.g_vel_scales[0])

    while not rospy.is_shutdown():
        key_pub_rate.twist_pub.publish(key_pub_rate.g_last_twist)
        key_pub_rate.rate.sleep()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

if __name__=='__main__':
    main()