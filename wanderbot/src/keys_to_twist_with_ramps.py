#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on July 28, 2016 by 9:44 PM

import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# W-A-S-D video game key mapping paradigm with x as the stop key
key_mapping = {'w':[0,1],'a':[-1,0],'s':[0,-1],'d':[1,0],'x':[0,0]}

class KeysTTWR(object):
    '''
    Ramp Motion Commands
    '''
    def __init__(self):
        rospy.init_node('keys_to_twist_using_rate')
        self.g_twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.g_last_twist = Twist()
        self.g_target_twist = Twist()
        self.g_last_twist_send_time = rospy.Time.now()
        self.rate = rospy.Rate(20) #20hz
        self.g_vel_scales = [0.1, 0.1]  # initialize scale at a small value
        self.g_vel_ramps = [1,1] # ms^-2

    def ramped_vel(self, v_prev, v_target, t_prev, t_now, ramp_rate):
        '''
        Take a step toward the target velocity. If target velocity i within a step away, go directly to it
        :param v_prev:
        :param v_target:
        :param t_prev:
        :param t_now:
        :param ramp_rate:
        :return: v_target or v_prev + sign * step
        '''
        step = ramp_rate * (t_now - t_prev).to_sec() #convert time to seconds
        sign = 1.0 if (v_target > v_prev) else -1.0
        error = math.fabs(v_target-v_prev)
        if error < step: # we can get there within this timestep we're done
            return v_target
        else:
            return v_prev + sign * step # take a step toward the target

    def ramped_twist(self,prev, target, t_prev, t_now, ramps):
        '''

        :param prev: prior velocity
        :param target: target velocity
        :param t_prev: previous time
        :param t_now: current time
        :param ramps:
        :return: tw, a 'ramped' twist message
        '''
        tw = Twist()
        tw.angular.z = self.ramped_vel(prev.angular.z, target.angular.z, t_prev, t_now, ramps[0])
        tw.linear.x =  self.ramped_vel(prev.linear.x, target.linear.x, t_prev, t_now, ramps[1])
        return tw

    def send_twist(self):
        '''

        :return: None
        '''
        t_now = rospy.Time.now()
        #The ramp is applied to the twist message being publishe
        self.g_last_twist = self.ramped_twist(self.g_last_twist,self.g_target_twist,self.g_last_twist_send_time,t_now,self.g_vel_ramps)
        self.g_last_twist_send_time = t_now #reset current time for next function call
        self.g_twist_pub.publish(self.g_last_twist)

    def keys_callback(self, msg):
        if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
            return  # unknown key
        vels = key_mapping[msg.data[0]]  # dictionary pair stored as a list
        self.g_target_twist.angular.z = vels[0] * self.g_vel_scales[0]
        self.g_target_twist.linear.x = vels[1] * self.g_vel_scales[1]
        # self.g_last_twist.linear.y = vels[0] * self.g_vel_scales[0]


    def fetch_param(self,name,default):
        '''
        Get param name or use default values
        :param name:
        :param default:
        :return:
        '''
        if rospy.has_param(name):
            return rospy.get_param(name)
        else:
            rospy.logwarn("parameter %s not defined. Defaulting to %.3f" % (name, default))
            return default


def main():
    key_pub_rate = KeysTTWR()
    rospy.Subscriber('keys', String, key_pub_rate.keys_callback)
    # set the scale and ramp values to the parameter values
    key_pub_rate.g_vel_scales[0] = key_pub_rate.fetch_param('~angular_scale', 0.1)
    key_pub_rate.g_vel_scales[1] = key_pub_rate.fetch_param('~linear_scale', 0.1)
    key_pub_rate.g_vel_ramps[0]  = key_pub_rate.fetch_param('~angular_accel', 1.0)
    key_pub_rate.g_vel_ramps[1]  = key_pub_rate.fetch_param('~linear_accel', 1.0)

    while not rospy.is_shutdown():
        key_pub_rate.send_twist()
        key_pub_rate.rate.sleep()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

if __name__=='__main__':
    main()