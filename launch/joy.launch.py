from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
  joy_params = str(Path(get_package_share_directory('cubot'))/"config/joystick.yaml")

  node_robot_state_publisher = Node(
    package='joy',
    executable='joy_node',
    parameters=[joy_params]
  )

  teleop_node = Node(
    package="teleop_twist_joy",
    executable="teleop_node",
    name="teleop_node",
    parameters=[joy_params]
  )

  return LaunchDescription([
    node_robot_state_publisher, teleop_node
  ])

if __name__ == '__main__':
  generate_launch_description()
