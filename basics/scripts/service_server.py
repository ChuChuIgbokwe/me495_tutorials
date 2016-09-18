#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on July 05, 2016 by 5:03 PM

import rospy
from basics.srv import WordCount,WordCountResponse #1

def count_words(request): #2
	print "There are %s words" % WordCountResponse(len(request.words.split()))
	return WordCountResponse(len(request.words.split())) #wordcountResponse takes uint32 as its argument

# def count_words(request): #my preference
# 	return len(request.words.split())
#
# def count_words(request):
# 	return [len(request.words.split())]
#
# def count_words(request):
# 	return {'count': len(request.words.split())}
def main():
	rospy.init_node('service_server')
	service = rospy.Service('word_count', WordCount,count_words) #(service name, type, callback) name, service_class, handler)

	rospy.spin()

if __name__=='__main__':
	main()


