#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def take_actions(regions):

def command_velocity(msg):
    regions = {
        'right':  min(min(msg.ranges[0:143]), 10),
        'fright': min(min(msg.ranges[144:287]), 10),
        'front':  min(min(msg.ranges[288:431]), 10),
        'fleft':  min(min(msg.ranges[432:575]), 10),
        'left':   min(min(msg.ranges[576:713]), 10),
    }

    


    take_action(regions)

def main():
    rospy.init_node("plan_motion")
    pub = rospy.Publisher("/cmd_vel",Twist,queue_size = 1) #Publicar
    sub = rospy.Subscriber('mlp2wr/laser/scan',LaserScan,call_move)
    rospy.spin()


if __name__ == '__main__':
    main()
