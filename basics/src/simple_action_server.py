#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on August 01, 2016 by 10:51 AM

import rospy
import time, actionlib
from beginner_tutorials.msg import TimerAction, TimerGoal, TimerResult

def do_timer(goal): #goal is of type TimerGoal which corresponds to the goal part of timer.action
    start_time = time.time()
    time.sleep(goal.time_to_wait.to_sec())
    result = TimerResult()
    #fill out the time_elapsed field by subtracting start time from currnet time and converting to a ROS duration
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = 0 #do not send any updates
    server.set_succeeded(result) #tell SimpleActionServer we successfully achieved the goal

rospy.init_node('timer_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer,False) #always set autostart to False
server.start() #start action server
rospy.spin()
