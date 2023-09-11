class Server(Node):
	def __init__(self):
		super().__init__('subscriber')
		self.declare_parameter('number_publisher', 0)
		my_callback_group = MutuallyExclusiveCallbackGroup()
		pub = []
		sub = []
       
		for i in range(0, int(self.get_parameter('number_publisher').value)):
			lettera = chr( ord('a') + (i % 26))
			pub.append(self.create_publisher(String, 'echo_' + lettera, 100))
			sub.append(self.create_subscription(String, 'topic_' + lettera, self.listener_callback, 100, callback_group=my_callback_group))
			
		self.publisher_ = pub
		self.subscription_ = sub

	def listener_callback(self, msg):
		self.get_logger().info('[__TIME__]: "I heard: %s' % msg.data)
		self.get_logger().info('[__TIME__]: "I publish: %s' % msg.data)
		self.publisher_[int(msg.data[0: msg.data.find("-")])].publish(msg)

