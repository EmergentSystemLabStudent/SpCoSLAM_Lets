#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, os.path#, caffe
import glob
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
#from sklearn.cluster import KMeans
from __init__LetsBot import *

def Makedir(dir):
	try:
		os.mkdir( dir )
	except:
		pass

CNNfolder = '/home/akira/Dropbox/SpCoSLAM/PlaceCNN/'

if (Descriptor == "CNN_Place205"):
	#CNN_FILE = "placesCNN"
	#FULL PATH
	MEAN_FILE = CNNfolder + 'placesCNN/places205_mean.npy'
	#'/home/akira/Caffe/python/caffe/imagenet/ilsvrc_2012_mean.npy'
	MODEL_FILE = CNNfolder + 'placesCNN/places205CNN_deploy.prototxt'
	#'/home/akira/Caffe/examples/imagenet/imagenet_feature.prototxt'
	PRETRAINED = CNNfolder + 'placesCNN/places205CNN_iter_300000.caffemodel'
	#'/home/akira/Caffe/examples/imagenet/caffe_reference_imagenet_model'
elif (Descriptor == "hybridCNN"):
	#CNN_FILE = "hybridCNN"
	#FULL PATH
	MEAN_FILE = CNNfolder + 'hybridCNN/hybridCNN__mean.npy'
	#'/home/akira/Caffe/python/caffe/imagenet/ilsvrc_2012_mean.npy'
	MODEL_FILE = CNNfolder + 'hybridCNN/hybridCNN_deploy.prototxt'
	#'/home/akira/Caffe/examples/imagenet/imagenet_feature.prototxt'
	PRETRAINED = CNNfolder + 'hybridCNN/hybridCNN_iter_700000.caffemodel'
	#'/home/akira/Caffe/examples/imagenet/caffe_reference_imagenet_model'

LAYER = 'prob' #'fc6wi'
INDEX = 4

class CNN_Place(object):

	# トピックが送られてきた時に画像を保存
	def recog_callback(self, hoge):
    
		self.count += 1
		count_padded = '%05d' % self.count

		trialname = datasetfolder + dataset1 + "image/"
		#"/home/akira/Dropbox/SpCoSLAM/rosbag/albert-b-laser-vision/albert-B-laser-vision-dataset/image/"
		write_file_name = trialname + count_padded + ".jpg"
		cv2.imwrite(write_file_name, self.frame)

		print write_file_name
		'''
		timename = write_file_name[len(trialname):-4]
	
		net = caffe.Classifier(MODEL_FILE, PRETRAINED)
		#caffe.set_phase_test()
		caffe.set_mode_cpu()
		net.transformer.set_mean('data', np.load(MEAN_FILE))
		#net.set_mean
		#net.set_raw_scale
		net.transformer.set_raw_scale('data', 255)
		net.transformer.set_channel_swap('data', (2,1,0))
		image = caffe.io.load_image(write_file_name)
		net.predict([ image ])
		feat = net.blobs[LAYER].data[INDEX].flatten().tolist()
		#print(','.join(map(str, feat)))
		fp = open(trialname+ Descriptor + "/" + timename+'.csv','w')
		fp.write(','.join(map(str, feat)))
		fp.close()
		print('This image was extracted by CNN.\n')
		'''

	# 画像が読み込まれるごとに画像の情報を保持
	def image_callback(self, ros_image):

		#Create the cv_bridge object
		# cv_bridge（OpenCVとROSの相互変換のための） オブジェクトの作成
		bridge = CvBridge()

		# Use cv_bridge() to convert the ROS image to OpenCV format
		# cv_bridge() で ROS image を OpenCV formatに変換する
		try:
			self.frame = bridge.imgmsg_to_cv2(ros_image, "bgr8")
		except CvBridgeError, e:
			print e

	def __init__(self):

		rospy.Subscriber("/s_recog/result", String, self.recog_callback, queue_size=1)
		rospy.Subscriber("/usb_cam/image_raw", Image, self.image_callback, queue_size=1)
		self.count = 0

if __name__ == '__main__':

	rospy.init_node('Image_saver', anonymous=True)
	cnn = CNN_Place()
	rospy.spin()
 
  

'''
trialname = datasetfolder + dataset1
#"/home/akira/Dropbox/SpCoSLAM/rosbag/albert-b-laser-vision/albert-B-laser-vision-dataset/"
filelist = glob.glob(trialname+"*.jpg")
filelist.sort()
Data = len(filelist)

#trialname = raw_input("trialname?(folder) >")
#start = raw_input("start number?>")
#end   = raw_input("end number?>")

#sn = int(start)
#en = int(end)
#Data = int(en) - int(sn) +1

#descriptors = []
#descriptors_bgr = []
#object_feature = [ [] for j in range(Data) ]
#object_color   = [ [] for j in range(Data) ]

#foldername = datafolder + trialname
#フォルダ作成
Makedir( trialname + Descriptor )

for imgname in filelist:
    #filename = foldername+str(trial+sn).zfill(3)+'/'

    #物体数の読み込み
    #gyo = 0
    #for line in open(filename + 'object_center.txt', 'r'):
    #  #itemList = line[:-1].split(',')
    #  if gyo == 0:
    #    object_num = int(line)
    #  gyo = gyo + 1    


    #for object in range(object_num):
    #imgname = filename + 'image/object_' + str(object+1).zfill(2) + '.ppm' 
    print imgname  
    
    timename = imgname[len(trialname):-4]

    net = caffe.Classifier(MODEL_FILE, PRETRAINED)
    #caffe.set_phase_test()
    caffe.set_mode_cpu()
    net.transformer.set_mean('data', np.load(MEAN_FILE))
    #net.set_mean
    #net.set_raw_scale
    net.transformer.set_raw_scale('data', 255)
    net.transformer.set_channel_swap('data', (2,1,0))
    image = caffe.io.load_image(imgname)
    net.predict([ image ])
    feat = net.blobs[LAYER].data[INDEX].flatten().tolist()
    #print(','.join(map(str, feat)))
    fp = open(trialname+ Descriptor + "/" + timename+'.csv','w')
    fp.write(','.join(map(str, feat)))
    fp.close() 
 '''
