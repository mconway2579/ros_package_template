#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(f" received {data.data}")

def subscriber():
    rospy.init_node('hello_world_subscriber', anonymous=True)
    rospy.Subscriber('example_topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.loginfo("main loop entered, subscriber")
    subscriber()
