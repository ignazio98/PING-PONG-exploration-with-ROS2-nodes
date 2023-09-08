from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory

def generate_launch_description():
	ld = LaunchDescription()
	
	size_ = [4, 16]
	pub_ = [1, 2, 4, 8]
	
	for i in pub_:
		for j in size_:
			ld.add_action(
				IncludeLaunchDescription(
					PythonLaunchDescriptionSource(
						os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch' + str(i) + '-' + str(j) +'.py'))
				)
			)
	
	return ld
	
