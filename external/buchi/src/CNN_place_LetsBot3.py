#! /usr/bin/env python
# -*- coding: utf-8 -*-
# CNNモデルファイルを毎回読み込まない形に変更。出力ファイル保存先変更。(Akira Taniguchi 2018/11/25)
import sys, os, os.path, caffe
import glob
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
#from sklearn.cluster import KMeans
from __init__ import *

def Makedir(dir):
	try:
		os.mkdir( dir )
	except:
		pass

# CNNfolder = '/home/yuki/SpCoSLAM-master/PlaceCNN/' #Go to "__init__,py"

if (Descriptor == "CNN_Place205"):
	#FULL PATH
	MEAN_FILE = CNNfolder + 'placesCNN/places205_mean.npy'
	MODEL_FILE = CNNfolder + 'placesCNN/places205CNN_deploy.prototxt'
	PRETRAINED = CNNfolder + 'placesCNN/places205CNN_iter_300000.caffemodel'
elif (Descriptor == "CNN_Place365"):
  #FULL PATH
  MEAN_FILE = CNNfolder + 'places365resnet/places365CNN_mean.npy'
  MODEL_FILE = CNNfolder + 'places365resnet/deploy_resnet152_places365.prototxt'
  PRETRAINED = CNNfolder + 'places365resnet/resnet152_places365.caffemodel'

LAYER = 'prob' #'fc6wi'
INDEX = 4

for line in open( datafolder + 'trialname.txt', 'r'):
    itemList = line[:].split(',')
    trialname = itemList[0]
#Makedir(datafolder + trialname + "/image/")

class CNN_Place(object):

	# トピックが送られてきた時に画像を保存
	def recog_callback(self, hoge):
		
		#count_paddedの値と実際の教示step数がずれると危ういかも
		self.count += 1
		count_padded = '%05d' % self.count
		
		#ImageFile = datafolder + trialname + "/img/"
		#"/home/yuki/catkin_ws/src/buchi/data/image/"
		write_file_name = datafolder + trialname + "/img/" + count_padded + ".jpg"
		cv2.imwrite(write_file_name, self.frame)

		print(write_file_name)
		
		#timename = write_file_name[len(trialname):-4]
		
		image = caffe.io.load_image(write_file_name)
		net.predict([ image ])
		feat = net.blobs[LAYER].data[INDEX].flatten().tolist()
		#print(','.join(map(str, feat)))
		#trialname = datasetfolder
		fp = open(datafolder + trialname + "/img/ft" + str(int(count_padded)) + '.csv','w')
		fp.write(','.join(map(str, feat)))
		fp.close()
		print('This image was extracted by CNN.\n')
		

	# 画像が読み込まれるごとに画像の情報を保持
	def image_callback(self, ros_image):
		# Create the cv_bridge object
		# cv_bridge（OpenCVとROSの相互変換のための） オブジェクトの作成
		bridge = CvBridge()

		# Use cv_bridge() to convert the ROS image to OpenCV format
		# cv_bridge() で ROS image を OpenCV formatに変換する
		try:
			self.frame = bridge.imgmsg_to_cv2(ros_image, "bgr8")
		except CvBridgeError, e:
			print(e)

	def __init__(self):
		rospy.Subscriber("/image/signal", String, self.recog_callback, queue_size=1)
		rospy.Subscriber("/usb_cam/image_raw", Image, self.image_callback, queue_size=1)
		self.count = 0

if __name__ == '__main__':
	net = caffe.Classifier(MODEL_FILE, PRETRAINED)
	#caffe.set_phase_test()
	caffe.set_mode_cpu()
	net.transformer.set_mean('data', np.load(MEAN_FILE))
	#net.set_mean
	#net.set_raw_scale
	net.transformer.set_raw_scale('data', 255)
	net.transformer.set_channel_swap('data', (2,1,0))
	
	rospy.init_node('Image_saver', anonymous=True)
	cnn = CNN_Place()
	rospy.spin()
 
