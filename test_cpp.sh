#!/bin/bash

export ROS_DOMAIN_ID=5
for i in 1 2 4 8
do
	for j in 4 16 64 256 1024 4096 16384 65356
	do
		ros2 launch cpp_echo launch$i.py message_size:=$j publisher_max:=$i test:=$1
	done
done
