import subprocess
import time

#go to the directory of Autoware
cmd1 = 'cd ~; cd autoware.ai;'

#source the terminal
cmd2 = 'source install/setup.bash;'

#run the runtime manager node
cmd3 = 'roslaunch runtime_manager runtime_manager.launch;'

#start the simulation time
cmd4 = 'rosparam set /use_sim_time true;'

#play the ROSBAG file
cmd5 = 'rosbag play --start=140 --clock /home/phuris/.autoware/sample_moriyama_150324.bag;' 

#load the vehicle model
cmd6 = 'roslaunch vehicle_description vehicle_model.launch;'

#load point cloud map files
#change the location according to where you store the point cloud map data on your computer
cmd7 = 'rosrun map_file points_map_loader noupdate /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00147_-00846.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00147_-00847.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00147_-00849.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00147_-00850.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00147_-00851.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00148_-00847.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00148_-00848.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00148_-00849.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00149_-00846.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00149_-00847.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00149_-00848.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00150_-00846.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00150_-00847.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00150_-00848.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00151_-00848.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00151_-00849.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00151_-00850.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00152_-00849.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00152_-00850.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00152_-00851.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00153_-00850.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00153_-00851.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00153_-00852.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00154_-00851.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00154_-00852.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00154_-00853.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00155_-00852.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00155_-00853.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00155_-00854.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00155_-00855.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00156_-00854.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00156_-00855.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00156_-00856.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00157_-00856.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00157_-00857.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00158_-00856.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00158_-00857.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00158_-00858.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00159_-00857.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00159_-00858.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00159_-00859.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00160_-00858.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00160_-00859.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00160_-00860.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00160_-00861.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00161_-00860.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00161_-00861.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00162_-00861.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00162_-00862.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00163_-00861.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00163_-00862.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00164_-00862.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00164_-00863.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00165_-00863.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00165_-00864.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00166_-00864.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00166_-00865.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00167_-00864.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00167_-00865.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00167_-00866.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00167_-00867.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00168_-00865.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00168_-00866.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00168_-00867.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00168_-00868.pcd /home/phuris/.autoware/data/map/pointcloud_map/bin_Laser-00169_-00868.pcd;'

#load vector map files
#change the location according to where you store the vector map data on your computer
cmd8 = 'rosrun map_file vector_map_loader /home/phuris/.autoware/data/map/vector_map/area.csv /home/phuris/.autoware/data/map/vector_map/crosswalk.csv /home/phuris/.autoware/data/map/vector_map/curb.csv /home/phuris/.autoware/data/map/vector_map/dtlane.csv /home/phuris/.autoware/data/map/vector_map/gutter.csv /home/phuris/.autoware/data/map/vector_map/idx.csv /home/phuris/.autoware/data/map/vector_map/lane.csv /home/phuris/.autoware/data/map/vector_map/line.csv /home/phuris/.autoware/data/map/vector_map/node.csv /home/phuris/.autoware/data/map/vector_map/point.csv /home/phuris/.autoware/data/map/vector_map/pole.csv /home/phuris/.autoware/data/map/vector_map/poledata.csv /home/phuris/.autoware/data/map/vector_map/road_surface_mark.csv /home/phuris/.autoware/data/map/vector_map/roadedge.csv /home/phuris/.autoware/data/map/vector_map/roadsign.csv /home/phuris/.autoware/data/map/vector_map/signaldata.csv /home/phuris/.autoware/data/map/vector_map/stopline.csv /home/phuris/.autoware/data/map/vector_map/streetlight.csv /home/phuris/.autoware/data/map/vector_map/utilitypole.csv /home/phuris/.autoware/data/map/vector_map/vector.csv /home/phuris/.autoware/data/map/vector_map/whiteline.csv /home/phuris/.autoware/data/map/vector_map/zebrazone.csv;'

#run the node 'voxel_grid_filter'
cmd9 = 'roslaunch points_downsampler points_downsample.launch;'

#run the node 'nmea2tfpose'
cmd10 = 'roslaunch gnss_localizer nmea2tfpose.launch;' 

#run the node 'ndt_matching'
cmd11 = 'roslaunch lidar_localizer ndt_matching.launch;' 

#load the TF data
cmd12 = 'roslaunch /home/phuris/.autoware/data/tf/tf.launch;'

#launch Rviz
cmd13 = 'rosrun rviz rviz;' 

#navigate terminal to location of MATLAB
cmd14 = 'cd ~; cd /usr/local/MATLAB/R2018b/bin;'

#launch MATLAB
cmd15 = './matlab'

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
cmdnode12 = cmd14 + cmd15

subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode1])
time.sleep(10)
subprocess.call(['gnome-terminal','-x','/bin/bash','-i','-c',cmdnode2])
time.sleep(10)
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
subprocess.call(['/bin/bash', '-i', '-c', cmdnode12])



