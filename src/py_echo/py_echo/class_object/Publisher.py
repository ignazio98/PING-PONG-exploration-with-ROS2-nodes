import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from ..support.function import Utils

class Client(Node):
	"""
	define Client Node
	 
	Args:
		number_publisher ([int]): number of current client
		publisher_max ([int]): total number of client
	 	message_size ([int]): size of a single messagge
	
	"""

	def __init__(self):

		super().__init__('publisher')
		self.declare_parameter('message_size', rclpy.Parameter.Type.INTEGER)
		self.declare_parameter('number_publisher', rclpy.Parameter.Type.INTEGER)
		self.declare_parameter('publisher_max', rclpy.Parameter.Type.INTEGER)
		self.declare_parameter('test', rclpy.Parameter.Type.STRING)
		
		lettera = chr(ord('a') + (self.get_parameter('number_publisher').value % 26))
		self.publisher_ = self.create_publisher(String, 'topic_' + lettera, 100)
		self.subscription_ = self.create_subscription(String, 'echo_' + lettera, self.topic_callback, 100)
		self.timer = self.create_timer(0.5, self.timer_callback)
		
		self.NUM_MESSAGES_ = 100
		if self.get_parameter('test').value == "LAN":
			self.NUM_MESSAGES_ = 50
		
		self.count_ = 0
		self.arrived_ = 0
		self.start_ns_ = []
		self.publisher_
		self.subscription_
		self.filename_ = "result" + str(self.get_parameter("publisher_max").value) + "-" + str(self.get_parameter("message_size").value) + ".txt"

	def timer_callback(self):
		"""
			function to create and send message each 500ms 
		"""		

		msg = String()
		msg.data = str(self.get_parameter('number_publisher').value) + "-" + "x" * self.get_parameter('message_size').value
		
		self.start_ns_.append(self.get_clock().now().nanoseconds)
		self.publisher_.publish(msg)
		self.count_ += 1
		
		if(self.count_ >= self.NUM_MESSAGES_):
			self.timer.cancel()
        
	def topic_callback(self,msg):
		"""
		Read response from server

		Args:
			msg ([std_msgs]): message rom server node
		"""
		
		if(len(msg.data) != (int(self.get_parameter('message_size').value) + 2)):
			return
		
		np_ = int(self.get_parameter('number_publisher').value)
		pm_ = int(self.get_parameter('publisher_max').value)
		ms_ = int(self.get_parameter('message_size').value)
		end_ns_ = int(self.get_clock().now().nanoseconds)
		start_ns_ = int(self.start_ns_[self.arrived_])
		provenance_ = str(self.get_parameter('test').value)
		
		result_ = Utils.concatenate_result(np_, pm_, ms_, end_ns_ - start_ns_, provenance_)
		
		if(Utils.save_to_file(self.filename_, result_) == 1):
			return 
		
		self.arrived_ += 1
		self.get_logger().info('"%s"' % result_)
		
		if(self.arrived_ >= self.NUM_MESSAGES_):
			exit()
