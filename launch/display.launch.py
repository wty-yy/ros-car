import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from pathlib import Path

def generate_launch_description():

  # Check if we're told to use sim time
  use_sim_time = LaunchConfiguration('use_sim_time')

  # Process the URDF file
  with (Path(get_package_share_directory("cubot")) / "description/cubot_v2/urdf/cubot_v2_sw2urdf.urdf").open('r') as file:
    robot_description = file.read()
  
  # Create a robot_state_publisher node
  params = {'robot_description': robot_description, 'use_sim_time': use_sim_time}
  node_robot_state_publisher = Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    output='screen',
    parameters=[params]
  )

  # Create a joint_state_publisher_gui node
  node_joint_state_publisher_gui = Node(
    package='joint_state_publisher_gui',
    executable='joint_state_publisher_gui',
    output='screen'
  )

  # Create a rviz2 node
  node_rviz2 = Node(
    package='rviz2',
    executable='rviz2',
    output='screen'
  )

  # Launch!
  return LaunchDescription([
    DeclareLaunchArgument(
      'use_sim_time',
      default_value='false',
      description='Use sim time if true'),

    node_robot_state_publisher,
    node_joint_state_publisher_gui,
    node_rviz2
  ])
