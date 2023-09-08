import rclpy
from rclpy.node import Node
from std_msgs.msg import String

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
		self.start_ns_ = 0
		self.NUM_MESSAGES = 10
		self.publisher_
		self.subscription_

	def timer_callback(self):
		msg = String()
		msg.data = str(self.get_parameter('number_publisher').value) + "-" + "x" * self.get_parameter('message_size').value
		self.start_ns_ = self.get_clock().now().nanoseconds
		
		self.publisher_.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.data)
		self.count_ += 1
        
	def topic_callback(self,msg):
		time = int(self.get_clock().now().nanoseconds) - int(self.start_ns_)
		self.arrived_ += 1
		self.get_logger().info('[__TIME__]: "%d' % time)
		
		if(self.arrived_ >= self.NUM_MESSAGES):
			self.shutdown()
			return;

def main(args=None):
	rclpy.init(args=args)
	
	publisher = Client()
	
	rclpy.spin(publisher)
	
	publisher.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
    main()
