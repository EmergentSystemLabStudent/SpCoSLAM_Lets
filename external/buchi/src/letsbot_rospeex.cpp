#include <ros/ros.h>
#include <std_msgs/Bool.h>
#include <std_msgs/String.h>
#include <rospeex_if/rospeex.h>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <time.h>
#include <stdio.h>

static rospeex::Interface interface;

int i = 0;
bool state = true;	//音声認識の状態、初期値はtrue
//std::string temp;

ros::Publisher recog_pub;
ros::Publisher speech_finish_pub;

//発話内容を受け取るコールバック関数
void speech_callback(const std_msgs::String::ConstPtr& msg) {
	std::string text;
	text = msg->data;
	std::cout << "\t[HSR said : " << text << "]"<< std::endl;
	interface.say(text,"ja","nict");
}

//音声認識OnOffのコールバック関数
void state_callback(const std_msgs::Bool::ConstPtr& state_signal) {
	state = state_signal->data;
	//On
	if(state == true)
		std::cout << "\ttrue!!!" << std::endl;
	//Off
	else if(state == false)
		std::cout << "\tfalse!!!" << std::endl;
}

/*//スタートボタンが押されたら、音声認識on
void start_callback(const std_msgs::Bool::ConstPtr& start_signal) {
	if(start_signal->data == true)
		state = true;
		std::cout << "\ttrue!!!" << std::endl;
}*/

//認識結果を受け取るコールバック関数
void recognition_callback(const std::string& msg) {
	//timestamp取得
	/*time_t now = time(NULL);
	struct tm *n_stamp = localtime(&now);
	char t_stamp[] = "";
	sprintf(t_stamp, "%02d-%02d-%202d_%02d:%02d:%02d", n_stamp->tm_year+1900,n_stamp->tm_mon+1,n_stamp->tm_mday,n_stamp->tm_hour, n_stamp->tm_min, n_stamp->tm_sec);
	std::string time_stamp = std::string(t_stamp);*/

	//csvファイル出力
	/*const char *file_name;
	if(i==0) {
		temp = "/home/tabuchi/catkin_ws/src/buchi/data/spco_speech.csv";
		std::cout << temp << std::endl;
		i++;
	}
	file_name = temp.c_str();*/

	std_msgs::String result;
	//std::ofstream fout;
	//trueの時のみ認識結果をpublish,CSVファイルに認識結果を書き込み
	if(state == true) {
		std::cout << "\t[you said : " << msg << "]"<< std::endl;
		result.data = msg;
		recog_pub.publish(result);
		/*fout.open(file_name, std::ios::app); //追記
		fout << msg << std::endl;
		fout.close();*/
	}
	else if(state == false) {
		std::cout << "\t<<<NOT RECOGNITION>>>" << std::endl;
	}
}

//発話が終了したらtrueをpublish
void speech_finish_callback(const std::string& msg) {
	std_msgs::Bool finish;
	finish.data = true;
	speech_finish_pub.publish(finish);
}

int main(int argc, char **argv) {
	ros::init(argc, argv, "letsbot_rospeex");
	ros::NodeHandle nh;

	recog_pub			 = nh.advertise<std_msgs::String>("/s_recog/result",5);
	speech_finish_pub	 = nh.advertise<std_msgs::Bool>("/speech/finish",1);

	ros::Subscriber speech_sub	 = nh.subscribe<std_msgs::String>("/speech/text",5,speech_callback);
	ros::Subscriber state_sub	 = nh.subscribe<std_msgs::Bool>("/s_recog/state",5,state_callback);
	//ros::Subscriber start_sub	 = nh.subscribe<std_msgs::Bool>("/start/button",1,start_callback);

	interface.init();
	interface.registerSRResponse(recognition_callback);
	interface.registerSSResponse(speech_finish_callback);
	interface.setSPIConfig("ja");

	ros::spin();
	return 0;
}
