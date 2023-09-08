
def save_to_file(filename_, 
				 result_):
	
	try:
		f = open("result/" + filename_, "a")
	except OSError:
		print "Could not open/read file:", fname
		sys.exit()

	with f:
		f.write(result_)
	
	f.close()
	
	return;

def concatenate_result(number_publisher_, 
						publisher_max_, 
						message_size_,
						end_ns_
						start_ns_):
							
	return "client" + str(number_publisher_) + "-" 
					+ str(publisher_max_) + "-" 
					+ str(message_size_) + "-"
					+ str(int(end_ns_) - int(start_ns_));
