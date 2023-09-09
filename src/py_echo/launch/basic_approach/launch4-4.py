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
			{"publisher_max" : 4}
		]
	)
	
	node2 = Node(
		package="cpp_echo",
		executable="client",
		name="Node2",
		parameters=[
			{"message_size" : 4},
			{"number_publisher" : 1},
			{"publisher_max" : 4}
		]
	)
	
	node3 = Node(
		package="cpp_echo",
		executable="client",
		name="Node3",
		parameters=[
			{"message_size" : 4},
			{"number_publisher" : 2},
			{"publisher_max" : 4}
		]
	)
	
	node4 = Node(
		package="cpp_echo",
		executable="client",
		name="Node4",
		parameters=[
			{"message_size" : 4},
			{"number_publisher" : 3},
			{"publisher_max" : 4}
		]
	)
	
	ld.add_action(node1)
	ld.add_action(node2)
	ld.add_action(node3)
	ld.add_action(node4)
	
	return ld
	
