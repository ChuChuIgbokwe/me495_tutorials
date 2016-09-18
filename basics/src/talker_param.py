#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on August 01, 2016 by 2:23 PM

import rospy
from std_msgs.msg import String
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker_param', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = rospy.get_param('~name',default='Anybody')
    while not rospy.is_shutdown():
        hello_str = "Hello I'm %s %s" % (msg,rospy.get_time())
        rospy.loginfo(hello_str)
        pub.publish(hello_str)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

