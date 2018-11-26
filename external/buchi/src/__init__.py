#coding:utf-8
#This file for setting parameters (パラメータ設定ファイル)
#Akira Taniguchi 2017/01/18-2018/11/26-
import numpy as np

####################パス設定####################
#出力フォルダのパス設定
datafolder   = "/external/buchi/data/"              #/home/yuki/catkin_ws/src/buchi/data/
CNNfolder = '/home/yuki/SpCoSLAM-master/PlaceCNN/'  #Folder of CNN model files
datasetfolder = "/catkin_ws/src/buchi/data/"        #May be the same as datafolder

####################パラメータ####################
R = 30                    #場所概念側のパーティクル数(gmappingを起動するlaunchファイルの設定の値と合わせる必要あり：未設定時は30)
dimx = 2                  #xtの次元数（x,y）

##初期(ハイパー)パラメータ
##事後分布（∝尤度×事前分布）の計算式（参考）：https://en.wikipedia.org/wiki/Conjugate_prior
alpha0 = 10.0             #場所概念のindexの多項分布P(Ct)のCRPハイパーパラメータ
gamma0 = 1.0              #位置分布のindexの多項分布P(it)のCRPハイパーパラメータ
beta0 = 0.1               #場所の名前の多項分布P(W)のハイパーパラメータ
chi0  = 0.1               #画像特徴の多項分布P(φ)のハイパーパラメータ
k0 = 1e-3                 #ガウス分布P(μ)のハイパーパラメータ（μの事前分布の影響度合い）
m0 = np.zeros(dimx)       #ガウス分布P(μ)のハイパーパラメータ（平均ベクトルに対応）
V0 = np.eye(dimx)*2       #逆ウィシャート分布p(Σ)のハイパーパラメータ（共分散行列に対応）
n0 = 3.0                  #逆ウィシャート分布p(Σ)のハイパーパラメータ［＞次元数］（Σの事前分布の影響度合い）
k0m0m0 = k0*np.dot(np.array([m0]).T,np.array([m0]))

####################パーティクルのクラス（構造体）####################
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

####################オプション設定(暫定不可)####################
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
  Descriptor = "CNN_Place205"
  DimImg = 205  #画像特徴の次元数
elif CNNmode == 4:
  Descriptor = "CNN_Place365"
  DimImg = 365  #画像特徴の次元数
elif CNNmode == 5:
  Descriptor = "hybridCNN"
  DimImg = 1183  #画像特徴の次元数	
  

####################不必要####################
"""
#Juliusパラメータ
#Juliusフォルダのsyllable.jconf参照
JuliusVer = "v4.4" #"v.4.3.1"
if (JuliusVer ==  "v4.4"):
  Juliusfolder = "/Julius/dictation-kit-v4.4/"
else:
  Juliusfolder = "/Julius/dictation-kit-v4.3.1-linux/"

speech_folder = "*.wav" #*.wav" #音声の教示データフォルダ(Ubuntuフルパス)
speech_folder_go = "*.wav" #*.wav" #音声の教示データフォルダ(Ubuntuフルパス)
lmfolder = "/SpCoSLAM-master/learning/lang_m/"

lang_init = 'web.000.htkdic' # 'trueword_syllable.htkdic' #'phonemes.htkdic' # 初期の単語辞書（./lang_mフォルダ内）
lang_init_DNN = 'syllableDNN.htkdic' 

datasetfolder = "/catkin_ws/src/buchi/data/"
dataset1 = "albert-b-laser-vision/albert-B-laser-vision-dataset"
bag1 = "albertBimg.bag"
datasets = [dataset1]
bags = [bag1]
scantopic = ["scan", "base_scan _odom_frame:=odom_combined"]

correct_Ct = 'Ct_correct.csv'  #データごとの正解のCt番号
correct_It = 'It_correct.csv'  #データごとの正解のIt番号
correct_data = 'SpCoSLAM_human.csv'  #データごとの正解の文章（単語列、区切り文字つき）(./data/)
correct_data_SEG = 'SpCoSLAM_SEG.csv'  #データごとの正解の文章（単語列、区切り文字つき）(./data/)
correct_name = 'name_correct.csv'  #データごとの正解の場所の名前（音素列）

NbestNum = 10 #n-bestのｎをどこまでとるか（n<=10）
N_best_number = 10  #PRR評価用のN-bestのN
margin = 10*0.05 # 地図のグリッドと位置の値の関係が不明のため(0.05m/grid)*margin(grid)=0.05*margin(m)

##rosbag data playing speed (normal = 1.0)
rosbagSpeed = 0.5#2

#L = 100                  #場所概念の数50#
#K = 100                  #位置分布の数50#
"""
