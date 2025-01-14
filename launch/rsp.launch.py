import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from pathlib import Path
import xacro

def generate_launch_description():

  # Check if we're told to use sim time
  use_sim_time = LaunchConfiguration('use_sim_time')

  # Process xacro file
  path_xacro_file = os.path.join(get_package_share_directory("cubot"), "description/robot.xacro")
  # path_xacro_file = os.path.join(get_package_share_directory("cubot"), "description/demo/robot.urdf.xacro")
  robot_xacro = xacro.process_file(path_xacro_file)
  robot_description = robot_xacro.toxml()  # 转为URDF的xml格式
  
  # Create a robot_state_publisher node
  params = {'robot_description': robot_description, 'use_sim_time': use_sim_time}
  node_robot_state_publisher = Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    output='screen',
    parameters=[params]
  )


  # Launch!
  return LaunchDescription([
    DeclareLaunchArgument(
      'use_sim_time',
      default_value='false',
      description='Use sim time if true'),

    node_robot_state_publisher
  ])
