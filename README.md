# PING PONG exploration with ROS2 nodes

this project is done for the course of Real Time Embedded System(2022-2023) by Prof. Marko Bertogna and Prof. Paolo Burgio at Unimore (University of Modena and Reggio Emilia)

## Requirements

Due to use this repository, is necessary to install a ROS humble distro.
You can check the installation process on ros2 documentation page at this [link](https://docs.ros.org/en/humble/Installation.html)

## Installation


Clone this repo using

```bash
user@user-desktop:~$ git clone https://github.com/ignazio98/tesina-RTES.git
```

## Usage
Open a terminal and use the following command

```bash
# replace <version> with your current ROS2 version
user@user-desktop:~$ source /opt/ros/<version>/setup.bash

#open your workspace
#if you haven't already done:
   #user@user-desktop:~$ mkdir ros2_ws
#else:
user@user-desktop:~$ cd ros2_ws

#build the project using colcon
user@user-desktop:/ros2_ws$ colcon build

#upload the local variable
user@user-desktop:/ros2_ws$ source install/local_setup.bash

#to launch the server, define n="How many node you need":
user@user-desktop:/ros2_ws$ ros2 run cpp_echo server --ros-args number_puplisher:=2

#to launch the 2 client with a message_size = 4096:
#Use launch file
user@user-desktop:/ros2_ws$ ros2 launch cpp_echo launch2-4096.py


---------------------------------------------------------------

#if you want to execute all the possible combination:
user@user-desktop:/ros2_ws$ ros2 run cpp_echo server --ros-args number_puplisher:=8

user@user-desktop:/ros2_ws$ ./test
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)