# ROS 2 Submarine Navigation System
This project implements a submarine control system in ROS 2 using **Custom Interfaces**. It allows a user to send directional commands through a terminal and tracks the submarine's (x, y) coordinates and facing direction.
#  Features
- **Custom Message:** Uses `submarine_interfaces/msg/BotPose` to store $x$, $y$ (float32), and facing direction (string).
- **Commander Node:** Captures user keyboard input (`forward`, `backward`, `turn left`, `turn right`).
-  **Navigator Node:** Tracks the submarine state and updates coordinates based on the current heading.
# Project Structure
- `submarine_interfaces/`: C++ package defining the custom `BotPose.msg`.
-  `submarine_system/`: Python package containing the logic for the Commander and Navigator nodes.
# Installation & Setup
# 1.Build the workspace
```bash
cd ~/submarine_ws
colon build
source install/setup.bash
```
# 2. Run the system 
open two terminals and source the workspace in both:

Terminal 1 (Navigator):
```bash
ros2 run submarine_system navigator
```
Terminal 2(Commander):
```bash
ros2 run submarine_system commander
```

# How to Control
once the Commander is running , type one of the following commands:
- forward / backward : Move 1.0 unit in current direction.
- turn left / turn right : Change heading (North,East,South,West).

# Example Output
If you type forward while facing North, the Navigator will output:

[INFO] [navigator]: Pose: x=0.0, y=1.0, Facing=North
