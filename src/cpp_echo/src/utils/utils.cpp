#include <memory>
#include <iostream>
#include <fstream>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
using std::placeholders::_1;

//convert int number into alphabetic char
char intToAlphabet( int i )
{
   return static_cast<char>('A' - 1 + i);
}

//save result on file
int save_to_file(std::string filename_, 
				 std::string data_)
{
	//check if file exists, and if it will not, we create it
	std::ofstream writer(filename_, std::ios::app);

	//check if we can write on it
	if (!writer)
	{
		std::cout << "There was an error opening file for output" << std::endl;
		return -1;
	}

	//write and close
	writer << data_ << std::endl;
	writer.close();

	return 0;
}

std::string concatenete_result( int publisher_, 
								int publisher_max_, 
								int message_size_, 
								int end_, 
								int start_)
{
	//concate result and return it
	std::string result_ = 
	
	return "client" + std::to_string(publisher_) + "-"
			+ std::to_string(publisher_max_) + "-"
			+ std::to_string(message_size_) + "-"
			+ std::to_string(end_ - start_);
}



