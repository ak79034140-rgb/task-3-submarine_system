cmake_minimum_required(VERSION 3.8)
project(submarine_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 1. Find the required packages
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# 2. Tell ROS to look for your .msg file
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/BotPose.msg"
)

# 3. Export the package
ament_package()
