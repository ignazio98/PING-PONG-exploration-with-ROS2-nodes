from launch_ros.actions import Node
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, TextSubstitution

def generate_launch_description():
	ld = LaunchDescription()
	
	message_size_ = LaunchConfiguration("message_size")
	publisher_max_ = LaunchConfiguration("publisher_max")
    
	for i in range(0, 2):
		ld.add_action(
			Node(
				package="cpp_echo",
				executable="client",
				name="Node" + str(i),
				parameters=[
					{"message_size" : message_size_},
					{"number_publisher" : TextSubstitution(text=str(i))},
					{"publisher_max" : publisher_max_}
				]
			)
		)
	
	return ld
	
