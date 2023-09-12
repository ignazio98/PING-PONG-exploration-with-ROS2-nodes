import sys

class utils_function():
    def save_to_file(filename_, result_):
        try:
            f = open("result/n" + filename_, "a")
        except OSError:
            return 1

        with f:
            f.write(result_ + "\n")
        
        f.close()
        return 0

    def concatenate_result(number_publisher_, publisher_max_, message_size_, time_):						
	    return "client" + str(number_publisher_) + "-" + str(publisher_max_) + "-" + str(message_size_) + "-" + str(time_);
