from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from pathlib import Path

def generate_launch_description():
  package_name = "ros_car"
  path_current_pkg = Path(get_package_share_directory(package_name))
  launch_robot = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
      str(path_current_pkg / "launch/launch_robot.launch.py")
    )
  )
  
  launch_joy = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
      str(path_current_pkg / "launch/joy.launch.py")
    )
  )

  twist_to_twist_stamped = Node(
    package=package_name,
    executable="twist_to_twist_stamped.py"
  )

  return LaunchDescription([
    launch_robot,
    launch_joy,
    twist_to_twist_stamped
  ])