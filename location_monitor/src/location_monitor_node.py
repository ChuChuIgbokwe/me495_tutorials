#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# #Created by Chukwunyere Igbokwe on July 27, 2016 by 2:23 PM
# import rospy
# import math
# from nav_msgs.msg import Odometry
# from location_monitor.msg import LandmarkDistance


# def distance(x1, y1, x2, y2):
# 	xd = x1 - x2
# 	yd = y1 - y2
# 	return math.sqrt(xd*xd + yd*yd)

# class LandmarkMonitor(object):
# 	def __init__(self,landmark_pub, landmarks):
# 		self._landmark_pub = landmark_pub
# 		self._landmarks = landmarks

# 	def callback(self,msg):
# 		x = msg.pose.pose.position.x
# 		y = msg.pose.pose.position.y
# 		# rospy.loginfo("x: {}, y: {}".format(x,y))
# 		closest_name = None
# 		closest_distance = None
# 		for l_name,l_x, l_y in self._landmarks:
# 			dist = distance(x, y, l_x, l_y)
# 			if closest_distance is None or dist < closest_distance:
# 				closest_name = l_name
# 				closest_distance = dist
# 		ld = LandmarkDistance()
# 		ld.name = closest_name
# 		ld.distance = closest_distance
# 		self._landmark_pub.publish(ld)
# 		if closest_distance < 0.5:
# 			rospy.loginfo("I'm near the {}".format(closest_name))
# 		# rospy.loginfo("closest : {}".format(closest_name))


# def main():
# 	rospy.init_node('location_monitor_node')
# 	landmarks = []
# 	landmarks.append(("Cube", 0.31, -0.99));
# 	landmarks.append(("Dumpster", 0.11, -2.42));
# 	landmarks.append(("Cylinder", -1.14, -2.88));
# 	landmarks.append(("Barrier", -2.59, -0.83));
# 	landmarks.append(("Bookshelf", -0.09, 0.53));

# 	landmark_pub = rospy.Publisher("closest_landmark", LandmarkDistance, queue_size=10)
# 	monitor = LandmarkMonitor(landmark_pub,landmarks)
# 	rospy.Subscriber("/odom", Odometry, monitor.callback)

# 	try:
# 		rospy.spin()
# 	except KeyboardInterrupt:
# 		print("Shutting down")


# if __name__ == '__main__':
# 	main()

#your python node and package/message should always have different names

import rospy
from nav_msgs.msg import Odometry
import math

landmarks = []
landmarks.append(("Cube",0.31,-0.99));
landmarks.append(("Dumpster", 0.11,-2.42));
landmarks.append(("Cylinder", -1.14,-2.88));
landmarks.append(("Barrier", -2.59,-0.83));
landmarks.append(("Bookshelf", -0.09, 0.53));

def distance(x1, y1, x2, y2):
    xd = x1 - x2
    yd = y1 - y2
    return math.sqrt(xd*xd + yd*yd)

def callback(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    # rospy.loginfo("x: {}, y: {}".format(x,y))
    closest_name = None
    closest_distance = None
    for l_name,l_x, l_y in landmarks:
        dist = distance(x, y, l_x, l_y)
        if closest_distance is None or dist < closest_distance:
            closest_name = l_name
            closest_distance = dist
    rospy.loginfo("Landmark: {} || Distance: {}".format(closest_name,closest_distance))

def main():
    rospy.init_node('location_monitor')
    rospy.Subscriber("/odom", Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
