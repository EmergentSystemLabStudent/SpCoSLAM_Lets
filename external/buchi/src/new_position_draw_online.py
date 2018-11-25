#!/usr/bin/env python
# -*- coding:utf-8 -*-
#推定されたロボット位置をrviz上に可視化するプログラム
#作成者 石伏智 #作成日 2015年12月
#サンプリング点プロット→ガウスの概形描画に変更（磯部、2016卒論）
#編集、更新：谷口彰 更新日：2017/02/10-2018/11/25-
#自己位置だけ取得して描画する(TF、ロボットモデルの表示等で代用できるのであればそちらでも良いはず)

"""
実行前に指定されているフォルダが正しいかをチェックする

実行方法
python place_draw.py (parameterフォルダの絶対パス) (表示するPosition distribution (Gauss)を指定したい場合は数字を入力)

実行例
python place_draw.py /home/emlab/py-faster-rcnn/work/gibbs_sampling_program

"""

import glob
import re
import os
import rospy
import math
import sys
import time
import geometry_msgs.msg as gm
from geometry_msgs.msg import Point
import sensor_msgs.msg as sm
from  visualization_msgs.msg import Marker
from  visualization_msgs.msg import MarkerArray
import numpy as np
import struct
#import PyKDLs
sys.path.append("lib/")
from __init__ import *


#実験ファイル名trialnameを取得
trialname = sys.argv[1]
print trialname

#step番号を取得
step = int(sys.argv[2])
print step

#maxparticle = 0
#i = 0
##datafolder+trialname+"/"+stepにおける最大尤度のパーティクルを読み込み
#for line in open( filename50 + 'weights.csv', 'r'):
#      #itemList = line[:].split(',')
#      if (i == 0):
#        maxparticle = int(line)
#        i +=1

maxparticle = int(sys.argv[3]) #どのIDのパーティクルか
#pid  = int(sys.argv[3])
#filename=sys.argv[1]

#Class_NUM=0#read_result(filename)
RAD_90=math.radians(90)
color_all=1   #1 or 0 、(0ならばすべて赤)
mu_draw =1    #1 or 0 、(0ならば中心値を表示しない)
sigma_draw=1  #1 or 0, (0ならば分散を表示しない)
mu_arrow=0    #矢印を可視化する場合
COLOR=[
[0,0,0], #ロボット自己位置用
]

#特定の番号のガウス分布のみ描画したいとき
try: 
    Number=None #int(sys.argv[3])
except IndexError:
    Number=None


def place_draw():
    #class_list=class_check()
    #print class_list
    
    
    pub = rospy.Publisher('draw_position',MarkerArray, queue_size = 10)
    rospy.init_node('draw_position_info', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    #ロボットの自己位置を読み込み
    mu_temp = [[float(sys.argv[4]),float(sys.argv[5]),0,0]]
    sigma_temp = [[[0.02,0,0,0],[0,0.02,0,0],[0,0,0,0],[0,0,0,0]]]
    
    mu_all = mu_temp #+ mumu
    sigma = sigma_temp #+ sigsig
    print mu_all
    print sigma
    Class_NUM = 1
    
    data_class=[i for i in xrange(Class_NUM)]
    #for n in range(Class_NUM):
    #    #if len(class_list[n])!=0:
    #    data_class.append(n)
    
    marker_array=MarkerArray()
    id=0
    for c in data_class:
        #Positionの中心値を示す場合
        #===Positionの範囲の可視化====================
        if sigma_draw==1:
            
            marker =Marker()
            marker.type=Marker.CYLINDER
            
            (eigValues,eigVectors) = np.linalg.eig(sigma[c])
            angle = (math.atan2(eigVectors[1, 0], eigVectors[0, 0]));
            
            marker.scale.x = 2*math.sqrt(eigValues[0]);
            marker.scale.y = 2*math.sqrt(eigValues[1]);
            
            marker.pose.orientation.w = math.cos(angle*0.5);
            marker.pose.orientation.z = math.sin(angle*0.5);
            
            
            marker.scale.z=0.02 # default: 0.05
            marker.color.a=1.0
            marker.header.frame_id='map'
            marker.header.stamp=rospy.get_rostime()
            marker.id=id
            id +=1
            marker.action=Marker.ADD
            marker.pose.position.x=mu_all[c][0]
            marker.pose.position.y=mu_all[c][1]
            marker.color.r = COLOR[c][0] # default: COLOR[c][0] 色のばらつきを広げる
            marker.color.g = COLOR[c][1] # default: COLOR[c][1] 色のばらつきを広げる
            marker.color.b = COLOR[c][2] # default: COLOR[c][2] 色のばらつきを広げる

            if Number != None:
                if Number==c:
                    marker_array.markers.append(marker)
            else:
                    marker_array.markers.append(marker)
        if mu_draw==1:
            mu_marker =Marker()
            
            if mu_arrow==1: #矢印を可視化する場合
                mu_marker.type=Marker.ARROW
                orient_cos=mu_all[c][3]
                orient_sin=mu_all[c][2]
                if orient_sin>1.0:
                    orient_sin=1.0
                elif orient_sin<-1.0:
                    orient_sin=-1.0
                #radian xを導出
                radian=math.asin(orient_sin)
                if orient_sin>0 and orient_cos<0:
                    radian=radian+RAD_90
                elif orient_sin<0 and orient_cos<0:
                    radian=radian-RAD_90
            
                mu_marker.pose.orientation.z=math.sin(radian/2.0)
                mu_marker.pose.orientation.w=math.cos(radian/2.0)
                #<<<<<<<矢印の大きさ変更>>>>>>>>>>>>>>>>>>>>>>>>
                mu_marker.scale.x=0.5 # default: 0.4
                mu_marker.scale.y=0.07 # default: 0.1
                mu_marker.scale.z=0.001 # default: 1.0
                mu_marker.color.a=1.0
                
            elif mu_arrow==0:
                mu_marker.type=Marker.SPHERE
                mu_marker.scale.x=0.1
                mu_marker.scale.y=0.1
                mu_marker.scale.z=0.01 # default: 0.05
                mu_marker.color.a=1.0
            
            mu_marker.header.frame_id='map'
            mu_marker.header.stamp=rospy.get_rostime()
            mu_marker.id=id
            id +=1  
            mu_marker.action=Marker.ADD
            mu_marker.pose.position.x=mu_all[c][0]
            mu_marker.pose.position.y=mu_all[c][1]
            #print c,mu_marker.pose.position.x,mu_marker.pose.position.y
            
            if color_all==1:
                mu_marker.color.r = COLOR[c][0] # default: COLOR[c][0]
                mu_marker.color.g = COLOR[c][1] # default: COLOR[c][1]
                mu_marker.color.b = COLOR[c][2] # default: COLOR[c][2]
            elif color_all==0:
                mu_marker.color.r = 1.0
                mu_marker.color.g = 0
                mu_marker.color.b = 0
                
            if Number != None:
                if Number==c:
                    marker_array.markers.append(mu_marker)
            else:
                    marker_array.markers.append(mu_marker)

    print marker_array.markers
    count =0
    #while not rospy.is_shutdown():
    while(count <= 5):    
        #pub.publish(marker)
        pub.publish(marker_array)
        rate.sleep()
        #time.sleep(5.0)
        count = count+1
    

if __name__ == '__main__':
    try:
        place_draw()
    except rospy.ROSInterruptException:
        pass
