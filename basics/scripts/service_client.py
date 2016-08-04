#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on July 05, 2016 by 8:19 PM

import rospy
from basics.srv import wordcount,wordcountRequest
import sys

def client():
	rospy.init_node('service_client')
	rospy.wait_for_service('word_count')
	try:
		word_counter = rospy.ServiceProxy('word_count',wordcount)
		words = ' '.join(sys.argv[1:])
		word_count = word_counter(words)
		print words, '->', word_count.count
	except rospy.ServiceException as exc:
		print "Service did not process request: + str(exc)"


if __name__ == '__main__':
	try:
		client()
	except rospy.ROSInterruptException:
		pass