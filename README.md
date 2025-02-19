# ROS Car

This is a cube small car, designed by wty-yy.

Create template from [joshnewans/my_bot](https://github.com/joshnewans/my_bot).

## Install
Download relate packages: `colcon, gazebo, xacro, joint_state_publisher_gui, ros_controllers`, or pull from my docker image [wtyyy/ros:ros2-jazzy-ubuntu24.04](https://hub.docker.com/repository/docker/wtyyy/ros/general), **we need use latest ros2 distribution JAZZY, because mecanum_drive_controller only supports Rolling and Jazzy from [ros2_controllers:4.17.0](https://github.com/ros-controls/ros2_controllers/tree/4.17.0)**
```bash
docker pull wtyyy/ros:ros2-humble-cuda11.8.0-ubuntu22.04
```

Clone repository in `/your_ws/src/`
```bash
cd /your_ws/src
git clone https://github.com/wty-yy/ros-car-cubot.git
cd /your_ws
colcon build
source ./install/setup.sh
```

## Launch
```bash
source /ros2_ws/install/setup.sh
```

1. RSP(robot state publisher) + Gazebo simulator + Joystick control
    ```bash
    ros2 launch ros_car launch_all_sim_rsp_joy.launch.py
    ```

2. Real humburobot + Joystick control
    ```bash
    ros2 launch ros_car launch_real_robot_joy.launch.py
    ```