#!/bin/bash

tmux new -d -s project11_sim_robot
tmux setenv ROS_MASTER_URI http://localhost:11312
tmux send-keys "ROS_MASTER_URI=http://localhost:11312 roscore -p 11312" C-m
tmux splitw -p 90
tmux send-keys "rosrun rosmon rosmon project11_simulation sim_robot_with_bridge.launch" C-m
tmux splitw -p 50
tmux attach -t project11_sim_robot
