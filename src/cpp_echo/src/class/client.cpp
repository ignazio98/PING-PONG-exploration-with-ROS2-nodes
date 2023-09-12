class Client : public rclcpp::Node{
public:
  Client() : Node("client"), count_(0)
  { 
<<<<<<< HEAD
	/***
	 * define Client Node
	 * 
	 * Args:
	 * 		number_publisher ([int]): number of current client
	 * 		publisher_max ([int]): total number of client
	 * 		message_size ([int]): size of a single messagge
	*/
=======
>>>>>>> origin/main
	//declare parameter
	this->declare_parameter("message_size",rclcpp::PARAMETER_INTEGER);
	this->declare_parameter("number_publisher",rclcpp::PARAMETER_INTEGER);
	this->declare_parameter("publisher_max",rclcpp::PARAMETER_INTEGER);

	//convert the local number_publisher to char
	std::string lettera(1, intToAlphabet(this->get_parameter("number_publisher").as_int()+1));
		
	//create dynamically name of pub and sub 
	std::string topic_name = "topic_" + lettera;
	std::string echo_name = "echo_" + lettera;
	
	//define file name to save result
<<<<<<< HEAD
	filename_ = "result-" + this->get_parameter("publisher_max").value_to_string() 
				+ "-" + this->get_parameter("message_size").value_to_string() + ".txt";

	//ceare pub and sub
	publisher_ = this->create_publisher<std_msgs::msg::String>(
		topic_name, 100);

	subscription_ = this->create_subscription<std_msgs::msg::String>(
		echo_name, 100, std::bind(&Client::topic_callback, this, _1));

	timer_ = this->create_wall_timer(
		500ms, std::bind(&Client::timer_callback, this));

=======
	filename_ = "result-" + this->get_parameter("publisher_max").value_to_string() + "-" + this->get_parameter("message_size").value_to_string() + ".txt";

	//ceare pub and sub
	publisher_ = this->create_publisher<std_msgs::msg::String>(topic_name, 10);
	subscription_ = this->create_subscription<std_msgs::msg::String>(echo_name, 10, std::bind(&Client::topic_callback, this, _1));
	timer_ = this->create_wall_timer(500ms, std::bind(&Client::timer_callback, this));
>>>>>>> origin/main
	clk_ = new rclcpp::Clock();
  }

private:
  void timer_callback()
  {
<<<<<<< HEAD
	/***
	 * function to create and send message each 500ms 
	*/

	//declare parameter
	auto m = std_msgs::msg::String();
	std::string message;
	message.append(this->get_parameter("message_size").as_int(), 'c');
	m.data = std::to_string(this->get_parameter("number_publisher").as_int()) + "-" + message;

	//save publish time of this message
	rclcpp::Time time = clk_->now();
	start_ns_.push_back(time.nanoseconds());

	//publish
	publisher_->publish(m);
	count_++;

	if(count_ <= NUM_MESSAGES)
	{
		this->timer_->cancel();
=======
	//execute this command until it reach 50 iterations
	if(count_ <= NUM_MESSAGES)
	{
		//message creation
		auto m = std_msgs::msg::String();
		std::string message;
		message.append(this->get_parameter("message_size").as_int(), 'c');
		m.data = std::to_string(this->get_parameter("number_publisher").as_int()) + "-" + message;

		//save publish time of this message
		rclcpp::Time time = clk_->now();
		start_ns_.push_back(time.nanoseconds());

		//publish
		publisher_->publish(m);
		count_++;
>>>>>>> origin/main
	}
  }

  //attibute of Client class
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
<<<<<<< HEAD
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
=======
>>>>>>> origin/main
  size_t count_, arrived_;
  const size_t NUM_MESSAGES = 50;
  std::string filename_;
  
  rclcpp::Clock *clk_;
  std::vector<rcl_time_point_value_t> start_ns_;

  void topic_callback(const std_msgs::msg::String::SharedPtr msg)
  {
<<<<<<< HEAD
	/***
	 * read response from server
	 * 
	 * Args:
	 * 		msg ([std_msgs]): message rom server node
	*/
	//declare parameter
=======
	//we have receive a response from the server
	
>>>>>>> origin/main
	//we get the time
    rcl_time_point_value_t end_ns = clk_->now().nanoseconds();
    
    //check dimension of the message from lan error
    int l = ((int) msg->data.length() - 2);
    if(l != this->get_parameter("message_size").as_int())
    {
<<<<<<< HEAD
		return ;
	}
	
	//create result of current iteration
	int np = this->get_parameter("number_publisher").as_int();
	int pm = this->get_parameter("publisher_max").as_int();
	int ms = this->get_parameter("message_size").as_int();
	std::string result_ = concatenete_result(np, pm, ms,  end_ns,  start_ns_[arrived_]);
=======
		return;
	}
	
	//create result of current iteration
	std::string result_ = concatenete_result(this->get_parameter("number_publisher").as_int(), 
											 this->get_parameter("publisher_max").as_int(),
											 this->get_parameter("message_size").as_int(),
											 end_ns,
											 start_ns_[arrived_]);
>>>>>>> origin/main
    
    //save to file
    if(save_to_file(filename_, result_) != 0)
    {
		return ;
	}
	
	//print the result on terminal
	RCLCPP_INFO(this->get_logger(), "I heard: '%s'", result_.c_str());
  
	//check how many message we receive
	arrived_++;
	if(arrived_ == NUM_MESSAGES)
	{
		rclcpp::shutdown();
	}
  }	
<<<<<<< HEAD
};

=======

  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};
>>>>>>> origin/main
