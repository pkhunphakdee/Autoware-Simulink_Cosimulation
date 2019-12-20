#To run the demo, make sure that AUtoware, MATLAB/Simulink are already installed as well as all the required data and toolboxes.
#In some nodes that require to load the data, make sure that you change the file locations in the commands according to where you install the data ion your computer


import subprocess
import time

#go to the directory of Autoware
cmd1 = 'cd ~; cd autoware.ai;'

#source the terminal
cmd2 = 'source install/setup.bash;'

#run the runtime manager node
cmd3 = 'roslaunch runtime_manager runtime_manager.launch;'

#load the vehicle model 
#change the location according to where you store the vehicle data on your computer
cmd4 = 'roslaunch vehicle_description vehicle_model.launch model_path:=/home/phuris/autoware.ai/install/vehicle_description/share/vehicle_description/urdf/sim_default.urdf;'

#load vector map files 
#change the location according to where you store the vector map data on your computer
cmd5 = 'rosrun map_file vector_map_loader /home/phuris/.autoware/data/map/vector_map/area.csv /home/phuris/.autoware/data/map/vector_map/crosswalk.csv /home/phuris/.autoware/data/map/vector_map/curb.csv /home/phuris/.autoware/data/map/vector_map/dtlane.csv /home/phuris/.autoware/data/map/vector_map/gutter.csv /home/phuris/.autoware/data/map/vector_map/idx.csv /home/phuris/.autoware/data/map/vector_map/lane.csv /home/phuris/.autoware/data/map/vector_map/line.csv /home/phuris/.autoware/data/map/vector_map/node.csv /home/phuris/.autoware/data/map/vector_map/point.csv /home/phuris/.autoware/data/map/vector_map/pole.csv /home/phuris/.autoware/data/map/vector_map/poledata.csv /home/phuris/.autoware/data/map/vector_map/road_surface_mark.csv /home/phuris/.autoware/data/map/vector_map/roadedge.csv /home/phuris/.autoware/data/map/vector_map/roadsign.csv /home/phuris/.autoware/data/map/vector_map/signaldata.csv /home/phuris/.autoware/data/map/vector_map/stopline.csv /home/phuris/.autoware/data/map/vector_map/streetlight.csv /home/phuris/.autoware/data/map/vector_map/utilitypole.csv /home/phuris/.autoware/data/map/vector_map/vector.csv /home/phuris/.autoware/data/map/vector_map/whiteline.csv /home/phuris/.autoware/data/map/vector_map/zebrazone.csv;'

#load the TF data
cmd6 = 'roslaunch /home/phuris/.autoware/data/tf/tf.launch;'

#run the node 'vel_pose_connect'
cmd7 = 'roslaunch autoware_connector vel_pose_connect.launch topic_pose_stamped:=/ndt_pose topic_twist_stamped:=/estimate_twist sim_mode:=True;'

#run the node 'lane_rule'
cmd8 = 'rosrun lane_planner lane_rule;'

#run the node 'lane_stop'
cmd9 = 'rosrun lane_planner lane_stop;'

#run the node 'lane_select'
cmd10 = 'roslaunch lane_planner lane_select.launch search_closest_waypoint_minimum_dt:=5;'

#run the node 'way_point_loader' and load the path file
#change the location according to where you store the path data on your computer
cmd11 = 'roslaunch waypoint_maker waypoint_loader.launch load_csv:=True multi_lane_csv:=/home/phuris/.autoware/data/path/moriyama_path.txt replanning_mode:=False realtime_tuning_mode:=False resample_mode:=True resample_interval:=1 replan_curve_mode:=False overwrite_vmax_mode:=False replan_endpoint_mode:=True velocity_max:=20 radius_thresh:=20 radius_min:=6 velocity_min:=4 accel_limit:=0.5 decel_limit:=0.3 velocity_offset:=4 braking_distance:=5 end_point_offset:=1;'

#run the node 'astar_avoid'
cmd12 = 'roslaunch waypoint_planner astar_avoid.launch enable_avoidance:=False avoid_waypoints_velocity:=10 avoid_start_velocity:=3 replan_interval:=2 costmap_topic:=semantics/costmap_generator/occupancy_grid;'

#run the node 'velocity_set'
cmd13 = 'roslaunch waypoint_planner velocity_set.launch use_crosswalk_detection:=False enable_multiple_crosswalk_detection:=False points_topic:=points_no_ground;'

#run the node 'twist_filter'
cmd14 = 'roslaunch waypoint_follower twist_filter.launch;'

#launch Rviz
cmd15 = 'rosrun rviz rviz;'

#navigate terminal to location of MATLAB
cmd16 = 'cd ~; cd /usr/local/MATLAB/R2018b/bin;'

#launch MATLAB
cmd17 = './matlab'

cmdnode1 = cmd1 + cmd2 + cmd3
cmdnode2 = cmd1 + cmd2 + cmd4
cmdnode3 = cmd1 + cmd2 + cmd5
cmdnode4 = cmd1 + cmd2 + cmd6
cmdnode5 = cmd1 + cmd2 + cmd7
cmdnode6 = cmd1 + cmd2 + cmd8
cmdnode7 = cmd1 + cmd2 + cmd9
cmdnode8 = cmd1 + cmd2 + cmd10
cmdnode9 = cmd1 + cmd2 + cmd11
cmdnode10 = cmd1 + cmd2 + cmd12
cmdnode11 = cmd1 + cmd2 + cmd13
cmdnode12 = cmd1 + cmd2 + cmd14
cmdnode13 = cmd1 + cmd2 + cmd15
cmdnode14 = cmd16 + cmd17


subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode1])
time.sleep(10)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode2])
time.sleep(5)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode3])
time.sleep(5)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode4])
time.sleep(5)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode5])
time.sleep(5)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode6])
time.sleep(5)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode7])
time.sleep(5)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode8])
time.sleep(5)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode9])
time.sleep(5)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode10])
time.sleep(5)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode11])
time.sleep(5)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode12])
time.sleep(5)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode13])
time.sleep(5)
subprocess.call(['/bin/bash', '-i', '-c', cmdnode14])



