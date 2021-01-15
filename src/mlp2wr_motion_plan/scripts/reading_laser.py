#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan


def callback_laser(msg):
    #Samples 720, se divide el robot en 4 regiones
    regions = [
    min(msg.ranges[0:179]),
    min(msg.ranges[180:359]),
    min(msg.ranges[360:539]),
    min(msg.ranges[540:719]),
    ]
    rospy.loginfo(regions)




def main():
    rospy.init_node('reading_laser')
    sub = rospy.Subscriber('/mlp2wr/laser/scan',LaserScan,callback_laser)
    rospy.spin()
if __name__ == '__main__':
    main()
