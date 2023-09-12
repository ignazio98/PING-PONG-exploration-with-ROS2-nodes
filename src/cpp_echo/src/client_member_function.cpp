#include <stdio.h>
#include <string>
#include <chrono>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
using std::placeholders::_1;

#include "rclcpp/clock.hpp"
using namespace std::chrono_literals;

#include "utils/utils.cpp"
#include "class/client.cpp"
<<<<<<< HEAD

=======
>>>>>>> origin/main

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Client>());
  rclcpp::shutdown();
  return 0;
}
