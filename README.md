# CuBot

This is a cube small car, designed by wty-yy.

Create template from [joshnewans/my_bot](https://github.com/joshnewans/my_bot).

## Install
Download relate packages: `colcon, gazebo, xacro, joint_state_publisher_gui`, or pull from my docker hub [wtyyy/ros:ros2-humble-cuda11.8.0-ubuntu22.04](https://hub.docker.com/repository/docker/wtyyy/ros/general)
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
1. RSP(robot state publisher) + Gazebo simulator + Joystick control
    ```bash
    ros2 launch cubot launch_all_sim_rsp_joy.launch.py