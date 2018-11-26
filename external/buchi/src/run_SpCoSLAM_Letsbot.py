#coding:utf-8
#This file is the program for learning program
#Akira Taniguchi 2017/02/03-2018/11/25-
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
#datasetNUM = sys.argv[2]

#Copy of "__init__.py"
shutil.copy("./__init__.py", datafolder + trialname )

SpCoSLAM = "python ./learnSpCoSLAM1.0.py " + trialname #+ " " + str(datasetNUM)

def callback(msg):
  print "Subprocess SpCoSLAM."
  p = subprocess.Popen(SpCoSLAM, shell=True)
  time.sleep(2.0)

time.sleep(2.0)
rospy.init_node('SpCoSLAM')
sub = rospy.Subscriber('/image/signal', String, callback)

rospy.spin()

