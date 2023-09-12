#include <memory>
#include <iostream>
#include <fstream>

char intToAlphabet( int i )
{
	/***
	 * convert int number into alphabetic char
	 * 
	 * Args:
	 * 		i ([int]): number to convert into char
	 * 
	 * Return:
	 * 		char alphabetic letter
	*/
	return static_cast<char>('A' - 1 + i);
}

int save_to_file(std::string filename_, 
				 std::string data_)
{
	/***
	 * save result on file a specific file
	 * 
	 * Args:
	 * 		filename_ ([std::string]): name of file into save result
	 * 		data_ ([std::string]): result from a specific message recived back from server
	 * 
	 * Return:
	 * 		0 if there isn't error
	 * 		1 is file can't be open
	*/
	
	std::ofstream writer("result/" + filename_, std::ios::app);

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
	/***
	 * create the result string 
	 * 
	 * Args:
	 * 		publisher_ ([int]): number of current client
	 * 		publisher_max ([int]): total number of client
	 * 		message_size_ ([int]): size of a single messagge
	 * 		end_ ([int]): arrival time of message
	 * 		start_ ([int]): send time of message
	 * 
	 * Return:
	 * 		string contained all the parameter
	*/
	std::string result_ = 
	
	return "client" + std::to_string(publisher_) + "-"
			+ std::to_string(publisher_max_) + "-"
			+ std::to_string(message_size_) + "-"
			+ std::to_string(end_ - start_);
}



