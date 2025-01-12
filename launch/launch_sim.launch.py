from pathlib import Path
import os

from ament_index_python.packages import get_package_share_directory, get_package_prefix

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
  """ Include robot_state_publisher(rsp) launcher file `rsp.launch.py`
  Force sim time to be enable.
  """

  package_name = "cubot"
  rsp = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
      str(Path(get_package_share_directory(package_name)) / "launch/rsp.launch.py")
    ), launch_arguments={'use_sim_time': 'true'}.items()
  )
  
  gazebo = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
      str(Path(get_package_share_directory('gazebo_ros')) / "launch/gazebo.launch.py")
    )
  )

  spawn_entity = Node(
    package='gazebo_ros', executable='spawn_entity.py',
    arguments=['-topic', 'robot_description', '-entity', 'my_'+package_name],
    output='screen'
  )
  pkg_share = os.pathsep + os.path.join(get_package_prefix(package_name), 'share')
  if 'GAZEBO_MODEL_PATH' in os.environ:
    os.environ['GAZEBO_MODEL_PATH'] += pkg_share
  else:
    os.environ['GAZEBO_MODEL_PATH'] = "/usr/share/gazebo-11/models" + pkg_share

  return LaunchDescription([
    rsp, gazebo, spawn_entity
  ])
