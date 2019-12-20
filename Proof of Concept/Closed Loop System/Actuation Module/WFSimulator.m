%start the ROS node in MATLAB and connect to the existing ROS network
rosinit();

%determine the location of the Vel_pose_connect file
wf_sim_folder = fullfile(autoware.getRootDirectory(), ...
                        'benchmark', 'computing', 'planning', 'motion', 'waypoint_follower', 'wf_simulator');

% add the location of the Vel_pose_connect file to MATLAB path                    
addpath(wf_sim_folder);

%run the model
wf_simulator_ml_obj = WfSimulator();
wf_simulator_ml_obj.run();
