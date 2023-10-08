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
#open your workspace
#if you haven't already done:
   #user@user-desktop:~$ mkdir ros2_ws
#else:
#Replace <project_name> with you project name
user@user-desktop:~$ cd ros2_ws/<project_name>

# replace <version> with your current ROS2 version
user@user-desktop:~/ros2_ws/<project_name>$ source /opt/ros/<version>/setup.bash

#build the project using colcon
user@user-desktop:/ros2_ws/<project_name>$ colcon build

#upload the local variable
user@user-desktop:/ros2_ws/<project_name>$ source install/local_setup.bash

#to launch the server, define n="How many node you need":
user@user-desktop:/ros2_ws/<project_name>$ ros2 run cpp_echo server --ros-args -p number_publisher:=2

#to launch the 2 client with a message_size = 40:
#Use launch file
user@user-desktop:/ros2_ws/<project_name>$ ros2 launch cpp_echo launch2.py message_size:=40 publisher_max:=2 test:=LOCAL


-------------------------------------------------------------------------------------------------

#if you want to execute all the possible combination:
user@user-desktop:/ros2_ws/<project_name>$ export ROS_DOMAIN_ID=5
user@user-desktop:/ros2_ws/<project_name>$ ros2 run cpp_echo server --ros-args number_puplisher:=8

#Specify the location of the test
user@user-desktop:/ros2_ws/<project_name>$ ./test_cpp.sh LOCAL

#To try the py_echo, You need to replace cpp with py, on the 

-------------------------------------------------------------------------------------------------

#To generate all the plot on the data generated from the test you can run this command:
#Generate a single file from all the file.
user@user-desktop:/ros2_ws/<project_name>$ ./merge_file.sh

#Keep in mind, For each group, in particular, for each Message_size and Writer number are generate from the script
#Two different amount of request, for LAN comunication are 50, and for LOCAL comunication are 100.
#Before run the Perform_analisys script check the size.
#The script will show the first 50 or 100 element for each group.

user@user-desktop:/ros2_ws/<project_name>$ python3 Perform_analysis.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)