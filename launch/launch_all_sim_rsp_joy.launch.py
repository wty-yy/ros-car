from pathlib import Path

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
  """ Include robot_state_publisher(rsp) launcher file `rsp.launch.py`
  Force sim time to be enable.
  """

  package_name = "ros_car"
  path_current_pkg = Path(get_package_share_directory(package_name))
  sim_launch = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
      str(path_current_pkg / "launch/launch_sim.launch.py")
    ), launch_arguments={'world': str(path_current_pkg / "worlds/empty.world")}.items()
  )
  
  joy_launch = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
      str(path_current_pkg / "launch/joy.launch.py")
    )
  )

  rviz2 = Node(
    package="rviz2",
    executable="rviz2",
    arguments=['-d', str(path_current_pkg / "config/drive_robot.rviz")]
  )

  return LaunchDescription([
    sim_launch, joy_launch, rviz2
  ])
