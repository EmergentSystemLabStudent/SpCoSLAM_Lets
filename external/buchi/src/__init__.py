#coding:utf-8
#This file for setting parameters
#Akira Taniguchi 2017/01/18-2018/11/27-2018/12/13-
import numpy as np

####################Setting File PATH####################
#Setting of PATH for output folder
datafolder    = "/home/*/SpCoSLAM_Lets/external/buchi/data/"        #PATH of data out put folder  /home/yuki/catkin_ws/src/buchi/data/
CNNfolder     = "/home/*/CNN/CNN_Places365/"                        #Folder of CNN model files
datasetfolder = "/home/*/SpCoSLAM_Lets/catkin_ws/src/buchi/data/"   #May be the same as datafolder

####################Parameters####################
R = 30               #The number of particles in spatial concept learning 
                     #(It's need to set to the same value in launch file of gmapping: no setting=30)
dimx = 2             #The number of dimensions of xt (x,y)

##Initial (hyper) parameters
##Posterior (∝likelihood×prior): https://en.wikipedia.org/wiki/Conjugate_prior
alpha0 = 10.0        #Hyperparameter of CRP in multinomial distribution for index of spatial concept
gamma0 = 1.0         #Hyperparameter of CRP in multinomial distribution for index of position distribution
beta0 = 0.1          #Hyperparameter in multinomial distribution P(W) for place names 
chi0  = 0.1          #Hyperparameter in multinomial distribution P(φ) for image feature
k0 = 1e-3            #Hyperparameter in Gaussina distribution P(μ) (Influence degree of prior distribution of μ)
m0 = np.zeros(dimx)  #Hyperparameter in Gaussina distribution P(μ) (prior mean vector)
V0 = np.eye(dimx)*2  #Hyperparameter in Inverse Wishart distribution P(Σ)（prior covariance matrix）
n0 = 3.0             #Hyperparameter in Inverse Wishart distribution P(Σ) {>the number of dimenssions] (Influence degree of prior distribution of Σ)
k0m0m0 = k0*np.dot(np.array([m0]).T,np.array([m0]))

####################Particle Class (structure)####################
class Particle:
  def __init__(self,id,x,y,theta,weight,pid):
    self.id = id
    self.x = x
    self.y = y
    self.theta = theta
    self.weight = weight
    self.pid = pid
    #self.Ct = -1
    #self.it = -1

####################Option setting (NOT USE)####################
SaveParam = 1   #ステップごとに学習結果をファイル保存する（１）、しない（０）

wic = 1         #1:wic重みつき(理論的にはこちらがより正しい)、0:wic重みなし(Orignal paper of SpCoSLAM)
UseFT = 1       #画像特徴を使う場合（１）、使わない場合（０）
UseLM = 1       #言語モデルを更新する場合（１）、しない場合（０）[Without update language modelのため無関係]

CNNmode = 3     #AlexNet最終層(1)、AlexNet中間層(2)、Places-CNN最終層(3)、Places2-CNN最終層(4)、hybridCNN最終層

if CNNmode == 1:
  Descriptor = "CNN_softmax"
  DimImg = 1000 #画像特徴の次元数
elif CNNmode == 2:
  Descriptor = "CNN_fc6"
  DimImg = 4096 #画像特徴の次元数（高次元）
elif CNNmode == 3:
  Descriptor = "CNN_Places205"
  DimImg = 205  #画像特徴の次元数
elif CNNmode == 4:
  Descriptor = "CNN_Places365"
  DimImg = 365  #画像特徴の次元数
elif CNNmode == 5:
  Descriptor = "hybridCNN"
  DimImg = 1183  #画像特徴の次元数	
  
