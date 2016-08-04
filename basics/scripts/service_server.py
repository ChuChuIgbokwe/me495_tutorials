#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on July 05, 2016 by 5:03 PM

import rospy
from basics.srv import wordcount,wordcountResponse

def count_words(request):
	print "There are %s words" % wordcountResponse(len(request.words.split()))
	return wordcountResponse(len(request.words.split())) #wordcountResponse takes uint32 as its argument

# def count_words(request): #my preference
# 	return len(request.words.split())
#
# def count_words(request):
# 	return [len(request.words.split())]
#
# def count_words(request):
# 	return {'count': len(request.words.split())}

rospy.init_node('service_server')
service = rospy.Service('word_count', wordcount,count_words) #(service name, type, callback)

rospy.spin()




