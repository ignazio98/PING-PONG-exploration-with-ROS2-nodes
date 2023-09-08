from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	ld = LaunchDescription()
	
	node1 = Node(
		package="cpp_echo",
		executable="client",
		name="Node1",
		parameters=[
			{"message_size" : 4},
			{"number_publisher" : 0},
			{"publisher_max" : 1}
		]
	)
	
	ld.add_action(node1)
	
	return ld
	
