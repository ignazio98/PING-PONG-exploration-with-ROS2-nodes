import os

class Utils:
    def save_to_file(filename_, data_):
        """
        /***
        Save result on file a specific file
        Args:
        	filename_ ([std::string]): name of file into save result
        	data_ ([std::string]): result from a specific message recived back from server
         
        Return:
        	0 if there isn't error
        	1 is file can't be open
        """

        try:
            f = open("result/data/" + filename_, "a")
        except OSError:
            return 1

        with f:
            f.write(data_ + "\n")
        
        f.close()
        return 0

    def concatenate_result(publisher_, publisher_max_, message_size_, time_, provenance_):
        """
        /***
        Create the result string 
         
        Args:
        	publisher_ ([int]): number of current client
        	publisher_max_ ([int]): total number of client
        	message_size_ ([int]): size of a single messagge
        	time_ ([int]): time of message
         
        Return:
        	([String]) string contained all the parameter
        
        """						
        return "client" + str(publisher_) + "-" + str(publisher_max_) + "-" + str(message_size_) + "-" + str(time_) + "-" + provenance_