#! /bin/sh
#Akira Taniguchi 2017/02/03-2018/11/25
#The path setting of the output data folder is necessary.

DATAPATH='/home/yuki/catkin_ws/src/buchi/data/'

echo -n "trialname?(output_folder) >"
read trialname


echo $trialname > $DATAPATH'trialname.txt'

mkdir $DATAPATH$trialname
mkdir $DATAPATH$trialname'/particle'
mkdir $DATAPATH$trialname'/weight'
mkdir $DATAPATH$trialname'/map'
mkdir $DATAPATH$trialname'/img'

gnome-terminal --command 'python ./particle_saver.py '$trialname
gnome-terminal --command 'python ./map_saver.py '$trialname
gnome-terminal --command 'python ./run_SpCoSLAM_Letsbot.py '$trialname

