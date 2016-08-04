#!/usr/bin/env python
import rospy
from beginner_tutorials.msg import Complex
from random import random

def msg_pub():
	rospy.init_node('message_publisher')
	pub = rospy.Publisher('complex',Complex,queue_size=10)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		msg = Complex()
		msg.real = random()
		msg.imaginary = random()
		# numbers_str =  "real =" ,msg.real, "imaginary =", msg.imaginary
		# rospy.loginfo(numbers_str)
		rospy.loginfo("real = %f ,imaginary = %f", msg.real,msg.imaginary)

		pub.publish(msg)
		rate.sleep()

if __name__ == '__main__':
    try:
        msg_pub()
    except rospy.ROSInterruptException:
        pass
