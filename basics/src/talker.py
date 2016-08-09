#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    count = 0
    while not rospy.is_shutdown():
        hello_str = "hello I'm Chu-Chu, my number is %d, the ROS time is %s" % (count,rospy.get_time())
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        count +=1

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass