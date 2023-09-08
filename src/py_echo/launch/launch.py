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
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1_4.py'))
	)
	file2 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1_16.py'))
	)
	file3 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1_64.py'))
	)
	file4 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1_256.py'))
	)
	file5 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1_1024.py'))
	)
	file6 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1_4096.py'))
	)
	file7 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1_16384.py'))
	)
	
	file8 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2_4.py'))
	)
	file9 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2_16.py'))
	)
	file10 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2_64.py'))
	)
	file11 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2_256.py'))
	)
	file12 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2_1024.py'))
	)
	file13 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2_4096.py'))
	)
	file14 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2_16384.py'))
	)
	
	file15 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4_4.py'))
	)
	file16 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4_16.py'))
	)
	file17 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4_64.py'))
	)
	file18 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4_256.py'))
	)
	file19 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4_1024.py'))
	)
	file20 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4_4096.py'))
	)
	file21 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4_16384.py'))
	)
	
	file22 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8_4.py'))
	)
	file23 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8_16.py'))
	)
	file24 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8_64.py'))
	)
	file25 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8_256.py'))
	)
	file26 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8_1024.py'))
	)
	file27 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8_4096.py'))
	)
	file28 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8_16384.py'))
	)
	
	file29 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch1_65356.py'))
	)
	
	file31 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch2_65356.py'))
	)
	
	file33 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch4_65356.py'))
	)
	
	file35 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(get_package_share_directory('cpp_echo'), 'launch/launch8_65356.py'))
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
	
