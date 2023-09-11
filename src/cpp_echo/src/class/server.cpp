class Server : public rclcpp::Node{
public:
  Server() : Node("server")
  {
	//declare parameter
	this->declare_parameter("number_publisher",rclcpp::PARAMETER_INTEGER); 
	
	//define callback group to implement mutual exclusion
	auto my_callback_group = create_callback_group(rclcpp::CallbackGroupType::MutuallyExclusive);
	rclcpp::SubscriptionOptions options;
	options.callback_group = my_callback_group;
	
	//create n pub/sub, one for each publisher
	for(int i = 0; i < this->get_parameter("number_publisher").as_int(); i++)
	{
		//convert number into alphabetic char
		std::string lettera(1, intToAlphabet(i+1));
		
		std::string topic_name = "topic_" + lettera;
		std::string echo_name = "echo_" + lettera;
		
		publisher_.push_back(this->create_publisher<std_msgs::msg::String>(echo_name, 100));
		subscription_.push_back(this->create_subscription<std_msgs::msg::String>(topic_name, 100, std::bind(&Server::topic_callback, this, _1), options));
	}
  }

private:
  void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
  {
	//read message from a subscription
    RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
    
    //exctract which subscriptions it is
    std::string sub = msg->data.substr(0, msg->data.find("-"));

    auto message = std_msgs::msg::String();
    message.data = msg->data;
    
    //reply using publisher
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    publisher_[atoi(sub.c_str())]->publish(message);
  }

  //vector of all publisher and subscriber
  std::vector<rclcpp::Publisher<std_msgs::msg::String>::SharedPtr> publisher_;
  std::vector<rclcpp::Subscription<std_msgs::msg::String>::SharedPtr> subscription_;
};
