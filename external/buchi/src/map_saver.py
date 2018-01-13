#coding:utf-8
#map saver for each m_count
#Akira Taniguchi 2017/02/04-
import sys
import os
import signal
import subprocess
import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8
#import map_store.srv as map_store_srvs
from __init__ import *

trialname = sys.argv[1]
#datasetNUM = sys.argv[2]

mapsave = "rosrun map_server map_saver -f "
clocktime = 0.0

#trialname = "test" #raw_input("trialname?(output_folder) >")
#datasetNUM = 0 #raw_input("dataset_number?(0:albert,1:MIT) >")
#datasetname = datasets[int(datasetNUM)]
#datasetPATH = datasetfolder + datasetname

m_temp = 0

def callback(message):

  global m_temp
  #print clocktime,rospy.get_time()
  
  #m_countのindexは1から始まる
  #while (os.path.exists( datafolder + trialname + "/particle/" + str(message.data) + ".csv" ) == True):
   
    #print "m_count",message.data, "m_temp",m_temp
  
  if (m_temp != message.data):
    #rospy.loginfo("%s", message)
    #rospy.loginfo("%s", clocktime)
    MSC = mapsave + datafolder + trialname + "/map/map"+ str(message.data)
    p = subprocess.Popen(MSC, shell=True) #, stdin=subprocess.PIPE, stdout=subprocess.PIPE) 
    time.sleep(2.0)
    #rospy.sleep(3.0)
    p.terminate()
    p.kill()
    m_temp = message.data
      
time.sleep(2.0)
rospy.init_node('map_savering')
sub = rospy.Subscriber('/m_count', Int8, callback)
#rosbagがpauseの間はずっと同じ時刻を受け取り続ける


rospy.spin()


"""
#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#
def process_save_map(req):
    map_path = os.path.expanduser(rospy.get_param('map_path'))
    filename = map_path+rospy.get_param('filename', req.map_name)
    map_topic = rospy.get_param('map_topic', '/map')
    tmp_name = filename + '_ori'
    tmp_output = subprocess.check_output(['rosrun','map_server','map_saver','-f',tmp_name, 'map:=%s'%map_topic])
    rospy.sleep(2.0)
    tmp_name = tmp_name + '.yaml'
    crop_output = subprocess.check_output(['rosrun','map_server','crop_map',tmp_name,filename])
    rospy.loginfo('Map Saved into %s'%str(filename))
    #return map_store_srvs.SaveMapResponse()

if __name__ == '__main__':
    rospy.init_node('map_saver_with_crop',anonymous=True)
    srv_saver = rospy.Service('save_map', map_store_srvs.SaveMap, process_save_map)
rospy.spin()
"""
