from rclpy.node import Node
from std_msgs.msg import String
import rclpy
from utils.utils_function import utils_function as uf

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
		self.filename_ = "result" + str(self.get_parameter("publisher_max").value) + "-" + str(self.get_parameter("message_size").value) + ".txt"

	def timer_callback(self):
		msg = String()
		msg.data = str(self.get_parameter('number_publisher').value) + "-" + "x" * self.get_parameter('message_size').value
		
		self.start_ns_.append(self.get_clock().now().nanoseconds)
		self.publisher_.publish(msg)
		self.count_ += 1
		
		if(self.count_ <= self.NUM_MESSAGES_):
			self.timer.cancel()
        
	def topic_callback(self,msg):
		if(len(msg.data) != (int(self.get_parameter('message_size').value) + 2)):
			return
		np = int(self.get_parameter('number_publisher').value)
		pm = int(self.get_parameter('publisher_max').value)
		ms = int(self.get_parameter('message_size').value)
		end_ns = int(self.get_clock().now().nanoseconds)
		start_ns = int(self.start_ns_[self.arrived_])
		
		result_ = uf.concatenate_result(np, pm, ms, end_ns - start_ns)
		
		if(uf.save_to_file(self.filename_, result_) == 1):
			return 
		
		self.arrived_ += 1
		self.get_logger().info('"%s"' % result_)
		
		if(self.arrived_ >= self.NUM_MESSAGES_):
			exit()