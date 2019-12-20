%start ROS node in MATLAB and connect to existing network
rosinit();

%define a subscriber in the node
carpos = rossubscriber('/gnss_pose',@CarPosCallback);

%define variables to store postion data
global posX;
global posY;
% global posZ;
% global orient;
% plot(posX,posY);

%define the callback function
function CarPosCallback(~, message)
    global posX;
    global posY;
    global posZ;
%     global orient;
    posX = message.Pose.Position.X;
    posY = message.Pose.Position.Y;
%     posZ = message.Pose.Position.Z;
    hold on;
    xlabel('X POSITION (m)');
    ylabel('Y POSITION (m)');
    title('INSTANTANEOUS CAR POSITION');
    plot(posX,posY,'-.ro');
%     orient = [message.Pose.Orientation.X message.Pose.Orientation.Y message.Pose.Orientation.Z];
end
