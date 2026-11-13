# 🎯 RViz Marker Playground

A ROS 2 Python package that publishes **Markers, Points, and Poses** to **RViz2** for quick and easy visualization.

[RViz Demo]
<br><br>
<img width="1220" height="862" alt="Screenshot From 2026-11-13 16-33-34" src="https://github.com/user-attachments/assets/d513201c-b249-4e49-b2e3-f3e4a86a8e91" />

##  Features

-  **MarkerArray Publisher**: publishes a cylinder marker at a fixed rate (1 Hz)
-  **Point Publisher**: publishes point data for visualization
-  **Pose Publisher**: publishes pose data for visualization
-  **One-command launch** with a pre-configured RViz layout

##  Tech Stack

- Python 3
- ROS 2 (`rclpy`)
- `visualization_msgs`, `geometry_msgs`, `std_msgs`
- RViz2

##  Project Structure

```
visualization_pkg/
├── config/
│   └── visualization.rviz        # Saved RViz configuration
├── launch/
│   └── visualization.launch.py   # Launch file
├── visualization_pkg/
│   ├── __init__.py
│   ├── marker.py                 # MarkerArray publisher
│   ├── publish_point.py          # Point publisher
│   └── publish_pose.py           # Pose publisher
├── test/
├── package.xml
├── setup.py
├── setup.cfg
└── LICENSE
```

##  Prerequisites

- ROS 2 installed (Humble / Jazzy / your distro)
- `colcon` build tools
- RViz2

##  Installation

```bash
# 1. Go to your ROS 2 workspace
cd ~/ros2_ws/src

# 2. Clone this repository
git clone https://github.com/<your-username>/<repo-name>.git

# 3. Build the package
cd ~/ros2_ws
colcon build --packages-select visualization_pkg

# 4. Source the workspace
source install/setup.bash
```

##  Usage

Launch everything (nodes + RViz):

```bash
ros2 launch visualization_pkg visualization.launch.py
```

Or run a node individually:

```bash
ros2 run visualization_pkg <executable_name>
```

> Replace `<executable_name>` with the entry points defined in `setup.py`.

##  Topics

| Topic          | Message Type                       | Description                |
|----------------|------------------------------------|----------------------------|
| `/marker_array`| `visualization_msgs/MarkerArray`   | Cylinder markers for RViz  |

##  Output

RViz displays a grid with colored cylinder markers (red, green, blue) positioned in the `map` frame.

##  Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

##  License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

##  Author

**Dinesh Kumar**
GitHub: [K N DINESH KUMAR](https://github.com/30DineshKumar)
