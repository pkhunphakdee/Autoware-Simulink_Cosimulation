%start the ROS node in MATLAB and connect to the existing ROS network
rosinit();
pause(5);

%determine the location of the voxel_grid_filter file
voxel_grid_filter_folder = fullfile(autoware.getRootDirectory(), ...
                                    'benchmark', 'sensing', 'filters', 'points_downsampler', ...
                                    'voxel_grid_filter');

% add the location of the Vel_pose_connect file to MATLAB path
addpath(voxel_grid_filter_folder);

%run the model
voxel_grid_filter_obj = VoxelGridFilter();
