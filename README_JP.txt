SpCoSLAM
移動ロボット(Let’sBot/Turtlebot2)用ラッパー
語彙獲得なし(音声認識の単語辞書既知、教師なし単語分割なし)

ロボット内部用プログラムと外部PC用プログラムがあります。
※実装に使用したロボットの仕様上、プログラムを分けていますが、すべて同一デバイス上で動作させるようにすることも可能です。

＜ロボット内部＞
gmappingの起動
$ source SpCoSLAM-master/catkin_ws/devel/setup.bash
$ roslaunch buchi letsbot_gmapping.launch

m_countの管理・particleを外部PCに送る
$ cd ~/SpCoSLAM-master/learning
$ python csv_send.py

各種センサー起動（webカメラ・Lider・コントローラー）
$ roslaunch buchi spco.launch

weightを外部PCから受け取る
$ rosrun buchi data_write.py

前回のデータが残っていた場合、削除する
$ cd ~/SpCoSLAM-master/data/test/particle
;1
$ cd ~/SpCoSLAM-master/data/test/weight
$ rm -f *

描画のrosbag
$ rosbag record /map /draw_position /draw_space

＜外部PC＞
rospeex起動方法
$ export ROS_MASTER_URI=http://133.19.30.134:11311
$ roslaunch buchi letsbot_rospeex.launch

spco_speech.cppとCNN_place_LetsBot.pyの実行
$ export ROS_MASTER_URI=http://133.19.30.134:11311
$ roslaunch buchi spco_external.launch

particle_saver.pyとmap_saver.pyとrun_SpCoSLAM_Letsbot.pyの実行
$ export ROS_MASTER_URI=http://133.19.30.134:11311
$ cd ./catkin_ws/src/buchi/src
$ ./SpCoSLAM.sh
->trialname?(output_folder) >output_folder_name

## Other information  
著者がIROS2017の論文の実験で使用したソースコードです。
https://github.com/EmergentSystemLabStudent/SpCoSLAM


---
このプログラムを使用したものを公開される場合は、必ず引用情報を明記してください。

Reference:
Akira Taniguchi, Yoshinobu Hagiwara, Tadahiro Taniguchi, and Tetsunari Inamura, "Online Spatial Concept and Lexical Acquisition with Simultaneous Localization and Mapping", IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS2017), 2017.

Original paper:
https://arxiv.org/abs/1704.04664

Sample video:
https://youtu.be/z73iqwKL-Qk

2018/01/15  Akira Taniguchi
2018/11/24  Akira Taniguchi (update)
