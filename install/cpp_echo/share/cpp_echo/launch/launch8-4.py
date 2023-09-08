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
			{"publisher_max" : 8}
		]
	)
	
	node2 = Node(
		package="cpp_echo",
		executable="client",
		name="Node2",
		parameters=[
			{"message_size" : 4},
			{"number_publisher" : 1},
			{"publisher_max" : 8}
		]
	)
	
	node3 = Node(
		package="cpp_echo",
		executable="client",
		name="Node3",
		parameters=[
			{"message_size" : 4},
			{"number_publisher" : 2},
			{"publisher_max" : 8}
		]
	)
	
	node4 = Node(
		package="cpp_echo",
		executable="client",
		name="Node4",
		parameters=[
			{"message_size" : 4},
			{"number_publisher" : 3},
			{"publisher_max" : 8}
		]
	)
	
	node5 = Node(
		package="cpp_echo",
		executable="client",
		name="Node5",
		parameters=[
			{"message_size" : 4},
			{"number_publisher" : 4},
			{"publisher_max" : 8}
		]
	)
	
	node6 = Node(
		package="cpp_echo",
		executable="client",
		name="Node6",
		parameters=[
			{"message_size" : 4},
			{"number_publisher" : 5},
			{"publisher_max" : 8}
		]
	)
	
	node7 = Node(
		package="cpp_echo",
		executable="client",
		name="Node7",
		parameters=[
			{"message_size" : 4},
			{"number_publisher" : 6},
			{"publisher_max" : 8}
		]
	)
	
	node8 = Node(
		package="cpp_echo",
		executable="client",
		name="Node8",
		parameters=[
			{"message_size" : 4},
			{"number_publisher" : 7},
			{"publisher_max" : 8}
		]
	)
	
	ld.add_action(node1)
	ld.add_action(node2)
	ld.add_action(node3)
	ld.add_action(node4)
	ld.add_action(node5)
	ld.add_action(node6)
	ld.add_action(node7)
	ld.add_action(node8)
	
	return ld
	
