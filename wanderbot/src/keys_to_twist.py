#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on July 28, 2016 by 5:34 PM

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# W-A-S-D video game key mapping paradigm with x as the stop key
key_mapping = {'w':[0,1],'a':[-1,0],'s':[0,-1],'d':[1,0],'x':[0,0]}

def keys_cb(msg,twist_pub):
    if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
        return #unknown key
    vels = key_mapping[msg.data[0]] #dictionary pair stored as a list
    t = Twist()
    # t.angular.z = vels[0]
    t.linear.x = vels[1]
    t.linear.y = vels[0]
    twist_pub.publish(t)

if __name__== '__main__':
    rospy.init_node('keys_to_twist')
    twist_pub = rospy.Publisher('cmd_vel',Twist,queue_size=1)
    rospy.Subscriber('keys',String,keys_cb,twist_pub)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")