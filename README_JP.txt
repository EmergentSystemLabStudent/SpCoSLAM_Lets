SpCoSLAM
�ړ����{�b�g(Let�fsBot/Turtlebot2)�p���b�p�[
��b�l���Ȃ�(�����F���̒P�ꎫ�����m�A���t�Ȃ��P�ꕪ���Ȃ�)

���{�b�g�����p�v���O�����ƊO��PC�p�v���O����������܂��B
�������Ɏg�p�������{�b�g�̎d�l��A�v���O�����𕪂��Ă��܂����A���ׂē���f�o�C�X��œ��삳����悤�ɂ��邱�Ƃ��\�ł��B

�����{�b�g������
gmapping�̋N��
$ source SpCoSLAM-master/catkin_ws/devel/setup.bash
$ roslaunch buchi letsbot_gmapping.launch

m_count�̊Ǘ��Eparticle���O��PC�ɑ���
$ cd ~/SpCoSLAM-master/learning
$ python csv_send.py

�e��Z���T�[�N���iweb�J�����ELider�E�R���g���[���[�j
$ roslaunch buchi spco.launch

weight���O��PC����󂯎��
$ rosrun buchi data_write.py

�O��̃f�[�^���c���Ă����ꍇ�A�폜����
$ cd ~/SpCoSLAM-master/data/test/particle
;1
$ cd ~/SpCoSLAM-master/data/test/weight
$ rm -f *

�`���rosbag
$ rosbag record /map /draw_position /draw_space

���O��PC��
rospeex�N�����@
$ export ROS_MASTER_URI=http://133.19.30.134:11311
$ roslaunch buchi letsbot_rospeex.launch

spco_speech.cpp��CNN_place_LetsBot.py�̎��s
$ export ROS_MASTER_URI=http://133.19.30.134:11311
$ roslaunch buchi spco_external.launch

particle_saver.py��map_saver.py��run_SpCoSLAM_Letsbot.py�̎��s
$ export ROS_MASTER_URI=http://133.19.30.134:11311
$ cd ./catkin_ws/src/buchi/src
$ ./SpCoSLAM.sh
->trialname?(output_folder) >output_folder_name

## Other information  
���҂�IROS2017�̘_���̎����Ŏg�p�����\�[�X�R�[�h�ł��B
https://github.com/EmergentSystemLabStudent/SpCoSLAM


---
���̃v���O�������g�p�������̂����J�����ꍇ�́A�K�����p���𖾋L���Ă��������B

Reference:
Akira Taniguchi, Yoshinobu Hagiwara, Tadahiro Taniguchi, and Tetsunari Inamura, "Online Spatial Concept and Lexical Acquisition with Simultaneous Localization and Mapping", IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS2017), 2017.

Original paper:
https://arxiv.org/abs/1704.04664

Sample video:
https://youtu.be/z73iqwKL-Qk

2018/01/15  Akira Taniguchi
2018/11/24  Akira Taniguchi (update)
