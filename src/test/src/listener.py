#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # my_topic으로 메시지를 발행
    pub.publish(data)

def listener():
    global pub
    rospy.init_node('listener', anonymous=True)
    pub = rospy.Publisher('point', String, queue_size=10)
    rospy.Subscriber("my_topic", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
