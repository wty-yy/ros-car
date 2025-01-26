import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription

def generate_launch_description():

  # Check if we're told to use sim time
  use_sim_time = LaunchConfiguration('use_sim_time')

  rsp = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([os.path.join(
      get_package_share_directory('ros_car'), 'launch', 'rsp.launch.py'
    )]), launch_arguments={'use_sim_time': use_sim_time}.items()
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

    rsp,
    node_joint_state_publisher_gui,
    node_rviz2
  ])
