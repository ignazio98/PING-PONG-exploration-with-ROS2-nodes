from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression, TextSubstitution
from launch.launch_context import LaunchContext
import sys

def generate_launch_description():
	ld = LaunchDescription()
	
	context = LaunchContext()
	
	message_size_ = LaunchConfiguration("message_size")
	publisher_max_ = LaunchConfiguration("publisher_max")
    
	for i in range(0, 4):
		ld.add_action(
			Node(
				package="py_echo",
				executable="talker",
				name="Node" + str(i),
				parameters=[
					{"message_size" : message_size_},
					{"number_publisher" : TextSubstitution(text=str(i))},
					{"publisher_max" : publisher_max_}
				]
			)
		)
	
	return ld
	
