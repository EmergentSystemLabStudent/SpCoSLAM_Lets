#coding:utf-8
#rosbag play for learning and theaching
#スペースキー情報を送ることで一時停止と再開を行う。
#Akira Taniguchi 2017/02/03-
import sys
import os
import signal
import subprocess
import time
import rospy
from std_msgs.msg import String
from __init__ import *

# 初期化
trialname = sys.argv[1]
datasetNUM = sys.argv[2]

datasetname = datasets[int(datasetNUM)]
bagname = bags[int(datasetNUM)]
datasetPATH = datasetfolder + datasetname + bagname

flag = 0
t_count = 0
teachingtime = []

# teachingtimeにteaching.csvの内容を書き込み
for line in open( datasetfolder + datasetname + 'teaching.csv', 'r'):
  teachingtime.append(float(line))

# teachingflag.txtとgwaitflag.txtに0を書き込み
fp = open( datafolder + trialname + "/teachingflag.txt", 'w')
fp.write(str(flag))
fp.close()
fp = open( datafolder + trialname + "/gwaitflag.txt", 'w')
fp.write(str(0))
fp.close()

# rosbagをpause moodで実行
rosbag = "rosbag play -r " + str(rosbagSpeed) + " --clock "+ datasetPATH +" --pause"
p = subprocess.Popen(rosbag, shell=True, stdin=subprocess.PIPE)
print "Subprocess run rosbag."


#教示時刻回数、一時停止処理
def callback(endflag):

  # 初期化
  global flag, t_count
  ctime = float(rospy.get_time())
  
  # flag == 1かつteachingflag.txtの内容が0ならrosbagを再開
  if (flag == 1):
    for line in open( datafolder + trialname + "/teachingflag.txt", 'r'):
      gflag = int(line)
    if (gflag == 0):
      # flagに0を代入
      flag = 0
      # rosbagした端末のpause modeにスペースキーを送る
      p.stdin.write('%s\n' % " ")
      print t_count,"start!",ctime
      time.sleep(1.0)
  # flag == 0かつtimestampがteachingtimeならrosbagを一時停止, 教示の回数の最後のときはこっちに入らない（？）
  elif (int(ctime) == int(teachingtime[t_count]) and (flag == 0) and len(teachingtime) != t_count):
    # flagに1を代入
    flag = 1
    # teachingflag.txtの内容を1にする
    fp = open( datafolder + trialname + "/teachingflag.txt", 'w')
    fp.write(str(flag))
    fp.close()
    # rosbagした端末のpause modeにスペースキーを送る
    p.stdin.write('%s\n' % " ")
    print t_count,"pause.",ctime
    time.sleep(10.0)
    # 次のteachingtimeに移る
    t_count += 1

time.sleep(2.0)
p.stdin.write('%s\n' % " ")
print "start."
rospy.init_node('play_rosbag')
sub = rospy.Subscriber('clock', String, callback)

rospy.spin()

if (len(teachingtime) == t_count):
  #よくわからないがどうやっても子プロセスが止められない。（Topicがpublishされたままになる）
  time.sleep(2.0)
  p.send_signal(signal.SIGINT)
  p.stdin.write("\n")  
  p.stdin.close()
  
  # Get the process id
  pid = p.pid
  os.kill(pid, signal.SIGINT)
  
  p.terminate()
  p.kill()
  print "Done."
