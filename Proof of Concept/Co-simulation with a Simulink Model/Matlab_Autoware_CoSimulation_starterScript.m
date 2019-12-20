clear all
close all
clc

%error threshold definition for Twist Filter Node
ERROR = 1;
% ROS Initialization
rosshutdown();
rosinit();
% Defining acceleration rate and starting WF_Simulator Node
acc_rate = 20;
wf_simulator_ml_obj = WfSimulator(acc_rate);
wf_simulator_ml_obj.run();

% name of the model
model = 'Matlab_Autoware_CoSimulation';
open_system(model);
set_param(model, 'SimulationCommand', 'Start');

% after finishing, delete wf_node
pause();
delete(wf_simulator_ml_obj)


