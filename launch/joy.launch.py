from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration


def launch_setup(context, *args, **kwargs):
  joystick_type = LaunchConfiguration('joystick').perform(context)
  joy_params = str(Path(get_package_share_directory('ros_car'))/f"config/joysticks/joystick_{joystick_type}.yaml")

  node_robot_state_publisher = Node(
    package='joy',
    executable='joy_node',
    parameters=[joy_params]
  )

  teleop_node = Node(
    package="teleop_twist_joy",
    executable="teleop_node",
    name="teleop_node",
    parameters=[joy_params],
    # remappings=[
    #   ('/cmd_vel', '/diffbot_base_controller/cmd_vel_unstamped')
    # ]
  )
  return [
    node_robot_state_publisher,
    teleop_node
  ]

def generate_launch_description():
  return LaunchDescription([
    DeclareLaunchArgument(
      'joystick',
      default_value='xbox_series',
      description='Available joysticks: [xbox_series, xbox360]'),
    OpaqueFunction(function=launch_setup)
  ])

if __name__ == '__main__':
  generate_launch_description()
