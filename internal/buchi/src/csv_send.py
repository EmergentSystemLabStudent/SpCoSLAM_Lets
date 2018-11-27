#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, os.path
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8
from sensor_msgs.msg import LaserScan
# import numpy as np
from __init__ import *

trialname = 'test' #外部から取得できるようにすべき
#datafolder = '/home/ubuntu/SpCoSLAM-master/data/'

class CSV_SEND(object):

    def csvSendCallback(self, hoge):

        if os.path.exists( datafolder + trialname + "/particle/" + str(self.m_count+1) + ".csv") == True:
            self.m_count = self.m_count + 1

        count_padded = '%d' % self.m_count
        
        particle = ''
        for line in open(self.read_file_name + count_padded + '.csv','r'):
            particle = particle + line

        self.pub_mcount.publish(self.m_count)
        rospy.sleep(0.5)
        self.pub_csv.publish(particle)
        rospy.sleep(0.5)
        print self.m_count, '.csv file send'

    def __init__(self):

        rospy.Subscriber("/scan", LaserScan, self.csvSendCallback, queue_size=1)
        self.pub_csv = rospy.Publisher("/particle_csv", String, queue_size=10)
        self.pub_mcount = rospy.Publisher("/m_count", Int8, queue_size=10)
        self.m_count = 0
        self.read_file_name = datafolder + trialname + "/particle/"

if __name__ == '__main__':

    rospy.init_node('csv_send', anonymous=True)
    csv_send = CSV_SEND()
    rospy.spin()



