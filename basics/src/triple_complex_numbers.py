#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on August 08, 2016 by 7:38 PM

import rospy
from basics.msg import Complex

def callback(data):
    '''
    Triple the complex numbers published on the complex topic
    :param data:
    :return: tripled complex numbers
    '''
    data.real *= 3
    data.imaginary *= 3
    pub.publish(data)
    rospy.loginfo('tripled complex number %d is %f + %fi' % (data.real, data.imaginary))


if __name__=='__main__':
    rospy.init_node('tripler')
    pub = rospy.Publisher('tripled',Complex, queue_size=1)
    rospy.Subscriber('complex',Complex,callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")