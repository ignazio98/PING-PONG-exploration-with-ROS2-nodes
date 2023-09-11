
class Client(Node):
	def __init__(self):
		super().__init__('publisher')
		self.declare_parameter('message_size', rclpy.Parameter.Type.INTEGER)
		self.declare_parameter('number_publisher', rclpy.Parameter.Type.INTEGER)
		self.declare_parameter('publisher_max', rclpy.Parameter.Type.INTEGER)
		
		lettera = chr(ord('a') + (self.get_parameter('number_publisher').value % 26))
		self.publisher_ = self.create_publisher(String, 'topic_' + lettera, 100)
		self.subscription_ = self.create_subscription(String, 'echo_' + lettera, self.topic_callback, 100)
		self.timer = self.create_timer(0.5, self.timer_callback)
		
		self.i = 0
		self.count_ = 0
		self.arrived_ = 0
		self.start_ns_ = []
		self.NUM_MESSAGES_ = 50
		self.publisher_
		self.subscription_

	def timer_callback(self):
		if(self.count_ <= self.NUM_MESSAGES_):
			msg = String()
			msg.data = str(self.get_parameter('number_publisher').value) + "-" + "x" * self.get_parameter('message_size').value
			
			self.start_ns_.append(self.get_clock().now().nanoseconds)
			
			self.publisher_.publish(msg)
			self.get_logger().info('Publishing: "%s"' % msg.data)
			self.count_ += 1
        
	def topic_callback(self,msg):
		if(len(msg.data) != (self.get_parameter('message_size') + 2)):
			return ;
		
		string result_ = concatenate_result(self.get_parameter('number_publisher').value,
											self.get_parameter('publisher_max').value,
											self.get_parameter('message_size').value,
											int(self.get_clock().now().nanoseconds),
											int(self.start_ns_[self.arrived_]))
		
		if(!save_to_file(filename_, result_))
			return;
		
		self.arrived_ += 1
		self.get_logger().info('[__TIME__]: "%d' % time)
		
		if(self.arrived_ >= self.NUM_MESSAGES):
			self.shutdown()
			return;