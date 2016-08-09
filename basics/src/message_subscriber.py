#!/usr/bin/env python
import rospy
from basics.msg import Complex

def callback(msg):
	print "Real:", msg.real
	print "Imaginary:", msg.imaginary
	print ''

def msg_subscriber():
	rospy.init_node('message_subscriber')
	rospy.Subscriber('complex', Complex, callback)
	rospy.spin()

if __name__ == '__main__':
    msg_subscriber()	