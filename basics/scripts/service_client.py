#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on July 05, 2016 by 8:19 PM

import rospy
from basics.srv import WordCount,WordCountRequest #1
import basics
import sys

def client():
	rospy.init_node('service_client')
	rospy.wait_for_service('word_count') #wait till service is available
	try:
		word_counter = rospy.ServiceProxy('word_count',WordCount) #name, service_class call a service
		words = ' '.join(sys.argv[1:])
		word_count = word_counter(words)
		# word_count = word_counter(words='The quick brown fox jumped over the lazy dog')
		# word_count = word_counter('The quick brown fox jumped over the lazy dog')
		# print 'words', '->', word_count.count

		# req = basics.srv.WordCountRequest("I am Batman")
		# word_count = word_counter(req)
		print words, '->', word_count.count
	except rospy.ServiceException as exc:
		print "Service did not process request: + str(exc)"


if __name__ == '__main__':
	try:
		client()
	except rospy.ROSInterruptException:
		pass

