# SpCoSLAM_Lets
A wrapper of SpCoSLAM for a mobile robot (Let'sBot)
It can learn the spatial concepts (multimodal place categories) and the environmental map by online learning manner of SpCoSLAM.

Note that this implementation does not include lexical acquisition part.
(Without unsupervised word segmentation, i.e., updating a language model)
The word dictionary of the speech recognition is required in advance.

There are robot internal programs and external PC programs.
Because of the specification of the robot used for mounting, programs are divided, but it is possible to make it all operate on the same device.


＜Internal device of the robot＞  
Start gmapping  
    $ source SpCoSLAM-master/catkin_ws/devel/setup.bash  
    $ roslaunch buchi letsbot_gmapping.launch  

Management of `m_count`, and Sending particle data to external PC
    $ cd ~/SpCoSLAM-master/learning  
    $ python csv_send.py  

Start sensors (web camera, Lider, and controller)  
    $ roslaunch buchi spco.launch  

Receive weights of particles from external PC
    $ rosrun buchi data_write.py  

Delete the previous temporal files if it remains 
    $ cd ~/SpCoSLAM-master/data/test/particle  
    $ rm -f *  
    $ cd ~/SpCoSLAM-master/data/test/weight  
    $ rm -f *  

[Option] Record a rosbag file for drawing a map, a robot position, and position distribution  
    $ rosbag record /map /draw_position /draw_space  

＜External PC＞  
Start rospeex (a speech recognition tool)   
    $ export ROS_MASTER_URI=http://133.19.30.134:11311  
    $ roslaunch buchi letsbot_rospeex.launch  

Start `spco_speech.cpp` and `CNN_place_LetsBot.py` 
    $ export ROS_MASTER_URI=http://133.19.30.134:11311  
    $ roslaunch buchi spco_external.launch  

Start `particle_saver.py`, `map_saver.py`, and `run_SpCoSLAM_Letsbot.py`  
    $ export ROS_MASTER_URI=http://133.19.30.134:11311  
    $ cd ./catkin_ws/src/buchi/src  
    $ ./SpCoSLAM.sh  
    ->trialname?(output_folder) >output_folder_name  


## Other information
https://github.com/EmergentSystemLabStudent/SpCoSLAM


---
If you use this program to publish something, please describe the following citation information.

Reference:  
Akira Taniguchi, Yoshinobu Hagiwara, Tadahiro Taniguchi, and Tetsunari Inamura, "Online Spatial Concept and Lexical Acquisition with Simultaneous Localization and Mapping", IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS2017), 2017.

Original paper:
https://arxiv.org/abs/1704.04664

Sample video:
https://youtu.be/z73iqwKL-Qk

2018/01/15  Akira Taniguchi  
2018/04/24  Akira Taniguchi
