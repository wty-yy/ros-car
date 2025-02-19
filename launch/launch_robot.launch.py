from pathlib import Path
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessStart

def generate_launch_description():
  """ Include robot_state_publisher(rsp) launcher file `rsp.launch.py`
  Force sim time to be enable.
  """

  package_name = "ros_car"
  rsp = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
      str(Path(get_package_share_directory(package_name)) / "launch/rsp.launch.py")
    ), launch_arguments={'use_sim_time': 'false'}.items()
  )

  controller_params_file = os.path.join(
    get_package_share_directory(package_name),
    'config',
    'my_controllers.yaml'
  )
  
  controller_manager = Node(
    package="controller_manager",
    executable="ros2_control_node",
    parameters=[controller_params_file],
    remappings=[
      ("~/robot_description", "robot_description"),
    ],
  )

  rviz = Node(
    package="rviz2",
    executable="rviz2",
    name="rviz2",
    output="log",
  )

  diff_drive_spawner = Node(
    package="controller_manager",
    executable="spawner",
    arguments=["mecanum_controller"],
  )

  joint_broad_spawner = Node(
    package="controller_manager",
    executable="spawner",
    arguments=["joint_broad"],
  )

  delayed_spawners = RegisterEventHandler(
    event_handler=OnProcessStart(
      target_action=controller_manager,
      on_start=[diff_drive_spawner, joint_broad_spawner]
    )
  )

  return LaunchDescription([
    rsp, # rviz,
    controller_manager,
    delayed_spawners
  ])
