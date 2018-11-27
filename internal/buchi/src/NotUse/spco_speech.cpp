#include <ros/ros.h>
#include <std_msgs/String.h>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>

int i = 0;
std::string temp;

void speech_callback(const std_msgs::String::ConstPtr& msg) {
	//場所の名前リスト
	std::vector<std::string> list;
	int size;
	list.push_back("玄関");
	list.push_back("キッチン");
	list.push_back("本棚");
	size = list.size();

	//認識結果から場所の名前を取り出す
	std::string result = msg->data;
	int k;
	std::size_t found;
	bool csv_flag = false;
	for(k=0; k<size; k++) {
		found = result.find(list[k]);
		if(found!=std::string::npos) {
			result = list[k];
			csv_flag = true;
			break;
		}
	}

	//csvファイル出力
	const char *file_name;
	if(i==0) {
		temp = "/home/ubuntu/catkin_ws/src/buchi/data/spco_speech.csv"; /////////////////////
		std::cout << temp << std::endl;
	}
	file_name = temp.c_str();

	std::ofstream fout;
	if(csv_flag == true) {
		//CSVファイルに認識結果を書き込み
		std::cout << "\t[write to csv : " << result << "]"<< std::endl;
		if(i==0) {
			fout.open(file_name, std::ios::trunc); //新規書き込み
			i++;
		}
		else if(i==1)
			fout.open(file_name, std::ios::app); //追記
		fout << result << std::endl;
		fout.close();
	}
	else if(csv_flag == false)
		std::cout << "\t[not write to csv]"<< std::endl;
}

int main(int argc, char **argv) {
	ros::init(argc, argv, "spco_speech");
	ros::NodeHandle nh;

	ros::Subscriber speech_sub = nh.subscribe<std_msgs::String>("/s_recog/result",5,speech_callback);

	ros::spin();
	return 0;
}
