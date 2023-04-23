#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import json
from geometry_msgs.msg import PoseStamped, Point, Quaternion


def callback(data):
    # x, y= map(int, data.data)
    parsed_data = json.loads(data.data)
    x = float(parsed_data[1])
    y = float(parsed_data[2])
    z = 0.0
    # PoseStamped 메시지 생성
    pose = PoseStamped()
    pose.header.stamp = rospy.Time.now()
    pose.header.frame_id = "map"
    pose.pose.position = Point(x, y, z)
    pose.pose.orientation = Quaternion(0, 0, 0, 1)
    # point로 PoseStamped 메시지를 발행
    pub.publish(pose)

def listener():
    global pub
    rospy.init_node('listener', anonymous=True)
    pub = rospy.Publisher('point', PoseStamped, queue_size=10)
    rospy.Subscriber("my_topic", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()