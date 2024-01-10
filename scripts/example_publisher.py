#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('example_topic', String, queue_size=10)
    rospy.init_node('example_publisher', anonymous=True)
    rate = rospy.Rate(1) # 1 Hz
    while not rospy.is_shutdown():
        hello_str = "Hello World"
        rospy.loginfo(f"sent {hello_str}")
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    rospy.loginfo("main loop entered, publisher")
    publisher()
