#! /bin/sh
#Akira Taniguchi 2017/02/03-


echo -n "trialname?(output_folder) >"
read trialname

#echo -n "dataset_number?(0:albert,1:MIT) >"
#read datasetNUM

#trialname=test3
datasetNUM=0

echo $trialname > /home/yuki/catkin_ws/src/buchi/data/trialname.txt

mkdir /home/yuki/catkin_ws/src/buchi/data/$trialname
mkdir /home/yuki/catkin_ws/src/buchi/data/$trialname/particle
mkdir /home/yuki/catkin_ws/src/buchi/data/$trialname/weight
mkdir /home/yuki/catkin_ws/src/buchi/data/$trialname/map
mkdir /home/yuki/catkin_ws/src/buchi/data/$trialname/img

gnome-terminal --command 'python particle_saver.py '$trialname
gnome-terminal --command 'python ./map_saver.py '$trialname
gnome-terminal --command 'python ./run_SpCoSLAM_Letsbot.py '$trialname' '$datasetNUM

#python ./learning/learnSpCoSLAM2.py $trialname $datasetNUM


