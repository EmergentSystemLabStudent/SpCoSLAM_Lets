#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8

filename = "/home/ubuntu/SpCoSLAM-master/data"
trialname = "/test/" #sys.argv[1]
mcount = "0"

"""
def data_callback(msg):
    global dataname
    dataname = msg.data

def trial_callback(msg):
    global trialname
    trialname = msg.data
"""

def m_count_callback(msg):
    global mcount
    mcount = msg.data

def weight_write(msg):
    global dataname
    global trialname
    global mcount

    print msg.data
    msglist = msg.data.split("@")
    print msglist

    #fp = open("/home/ubuntu/catkin_ws/src/buchi/data/m_count-1.csv", "w")
    fp = open(filename + trialname + "weight/" + str(mcount) + ".csv", "w")
    for i in xrange(len(msglist)):
        if i==0:
            fp.write(msglist[i] + "\n")
        else:
            fp.write(msglist[i] + ",")
    fp.write("\n")
    fp.close()


def gwait_write(msg):
    global dataname
    global trialname

    fp = open(filename + trialname + "/gwaitflag.txt", "w")
    fp.write(msg.data)
    fp.close()


def run():
    rospy.init_node('data_write', anonymous=True)
    #rospy.Subscriber("data",String,data_callback)
    #rospy.Subscriber("trial",String,trial_callback)
    rospy.Subscriber("/m_count",Int8,m_count_callback)
    rospy.Subscriber("/weight",String,weight_write)
    rospy.Subscriber("/gwait",String,gwait_write)
    rospy.spin()

if __name__ == '__main__':
    fp = open(filename + trialname + "/gwaitflag.txt", "w")
    fp.write(str(0))
    fp.close()
    run()

