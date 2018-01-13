#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, os.path
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8
import numpy as np
import subprocess
#from sklearn.cluster import KMeans
from __init__ import *


trialname = sys.argv[1]


class CSV_Save(object):

	def csv_callback(self, particle_data):
    
		self.frame = particle_data.data
		write_file_name = datasetfolder + trialname + "/particle/"

 		if (self.m_temp != self.mcount):
			fp = open(write_file_name + str(self.mcount) + '.csv','w')
			fp.write(self.frame)
			fp.close()
			print('csv_file saved.\n')
			
			for line in open ( datafolder + trialname + "/particle/" + str(self.mcount) + ".csv" ):
				itemList = line[:-1].split(',')
				if (int(itemList[0])==0):
					x = float(itemList[1])
					y = float(itemList[2])
			
			drawposition = "python ./new_position_draw_online.py "+trialname+" "+str(self.mcount)+" "+str(0)+" "+str(x)+" "+str(y)
			print drawposition
			p3 = subprocess.Popen(drawposition, shell=True)
			self.m_temp = self.mcount


	def m_count_callback(self, m_count_data):

		self.mcount = m_count_data.data

	def __init__(self):
		self.m_temp = 0
		self.mcount = 0
		rospy.Subscriber("/particle_csv", String, self.csv_callback, queue_size=10)
		rospy.Subscriber("/m_count", Int8, self.m_count_callback, queue_size=1)

if __name__ == '__main__':

	rospy.init_node('csv_saver', anonymous=True)
	csv_save = CSV_Save()
	rospy.spin()


