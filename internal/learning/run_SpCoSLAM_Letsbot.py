#coding:utf-8
#rosbag play for learning and theaching
#スペースキー情報を送ることで一時停止と再開を行う。
#Akira Taniguchi 2017/02/03-
import sys
import os
import shutil
import signal
import subprocess
import time
import rospy
from std_msgs.msg import String
from __init__ import *

trialname = sys.argv[1]
datasetNUM = sys.argv[2]

#init.pyをコピー
shutil.copy("./__init__.py", datafolder + trialname )

SpCoSLAM = "python ./learnSpCoSLAM3.2.py " + trialname + " " + str(datasetNUM)

def callback(msg):
  print "Subprocess SpCoSLAM."
  p = subprocess.Popen(SpCoSLAM, shell=True)
  time.sleep(2.0)

time.sleep(2.0)
rospy.init_node('SpCoSLAM')
sub = rospy.Subscriber('/s_recog/result', String, callback)

rospy.spin()

