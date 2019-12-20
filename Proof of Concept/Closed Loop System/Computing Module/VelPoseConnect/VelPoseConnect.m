%start the ROS node in MATLAB and connect to the existing ROS network
rosinit();

%determine the location of the Vel_pose_connect file
vel_pose_connect_folder = fullfile(autoware.getRootDirectory(), ...
                        'benchmark', 'computing', 'perception', 'localization', 'autoware_connector', 'vel_pose_connect');

% add the location of the Vel_pose_connect file to MATLAB path
addpath(vel_pose_connect_folder);

%run the model
model = 'vel_pose_connect_sl';
open_system(model);
set_param(model, 'SimulationCommand', 'Start');
