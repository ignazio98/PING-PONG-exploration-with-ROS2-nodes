from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory

def generate_launch_description():
	ld = LaunchDescription()
	
	file1 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1-4.py'))
	)
	file2 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1-16.py'))
	)
	file3 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1-64.py'))
	)
	file4 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1-256.py'))
	)
	file5 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1-1024.py'))
	)
	file6 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1-4096.py'))
	)
	file7 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1-16384.py'))
	)
	
	file8 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2-4.py'))
	)
	file9 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2-16.py'))
	)
	file10 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2-64.py'))
	)
	file11 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2-256.py'))
	)
	file12 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2-1024.py'))
	)
	file13 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2-4096.py'))
	)
	file14 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2-16384.py'))
	)
	
	file15 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4-4.py'))
	)
	file16 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4-16.py'))
	)
	file17 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4-64.py'))
	)
	file18 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4-256.py'))
	)
	file19 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4-1024.py'))
	)
	file20 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4-4096.py'))
	)
	file21 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4-16384.py'))
	)
	
	file22 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8-4.py'))
	)
	file23 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8-16.py'))
	)
	file24 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8-64.py'))
	)
	file25 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8-256.py'))
	)
	file26 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8-1024.py'))
	)
	file27 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8-4096.py'))
	)
	file28 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8-16384.py'))
	)
	
	file29 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1-65356.py'))
	)
	
	file31 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2-65356.py'))
	)
	
	file33 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4-65356.py'))
	)
	
	file35 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8-65356.py'))
	)
	
	ld.add_action(file1)
	ld.add_action(file2)
	ld.add_action(file3)
	ld.add_action(file4)
	ld.add_action(file5)
	ld.add_action(file6)
	ld.add_action(file7)
	ld.add_action(file8)
	ld.add_action(file9)
	ld.add_action(file10)
	ld.add_action(file11)
	ld.add_action(file12)
	ld.add_action(file13)
	ld.add_action(file14)
	ld.add_action(file15)
	ld.add_action(file16)
	ld.add_action(file17)
	ld.add_action(file18)
	ld.add_action(file19)
	ld.add_action(file20)
	ld.add_action(file21)
	ld.add_action(file22)
	ld.add_action(file23)
	ld.add_action(file24)
	ld.add_action(file25)
	ld.add_action(file26)
	ld.add_action(file27)
	ld.add_action(file28)
	ld.add_action(file29)
	ld.add_action(file31)
	ld.add_action(file33)
	ld.add_action(file35)
	
	return ld
	
