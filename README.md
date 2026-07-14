# ROS2 Autonomous Maze Robot

A custom differential-drive mobile robot built using ROS2 Humble and Gazebo capable of mapping an unknown maze using SLAM and designed for autonomous navigation using Nav2.

---

## Features

- Custom URDF/Xacro robot model
- Differential drive robot
- LiDAR integration
- RGB-D camera
- Gazebo simulation
- SLAM Toolbox mapping
- Occupancy grid map generation
- Nav2 integration (Work in Progress)

---

## Demo

### Robot Model

(Add screenshot)

### Gazebo World

(Add screenshot)

### Generated Occupancy Map

(Add screenshot)

---

## Tech Stack

- ROS2 Humble
- Gazebo Classic
- Nav2
- SLAM Toolbox
- RViz2
- URDF/Xacro
- C++
- Python

---

## Repository Structure

```
config/
description/
launch/
models/
world/
```

---

## Running

### Build

```bash
colcon build
source install/setup.bash
```

### Launch Simulation

```bash
ros2 launch finalProject disp.launch.py
```

### Run SLAM

```bash
ros2 launch slam_toolbox online_async_launch.py \
params_file:=config/mapper_params_online_async.yaml \
use_sim_time:=True
```

### Save Map

```bash
ros2 run nav2_map_server map_saver_cli -f my_map
```

---

## Future Improvements

- Autonomous navigation using Nav2
- Path planning
- Goal selection in RViz
- Obstacle avoidance
- C++ node implementation
- Improved robot dynamics

---

## Author

Aman Tayal
