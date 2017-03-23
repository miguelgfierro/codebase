function [R_right, R_left] = determine_matrixes_rotation (alfa)
% matrix rotation in axis z of angle alfa1
R = [cos(alfa/2), -sin(alfa/2), 0;
     sin(alfa/2), cos(alfa/2),  0;
     0,           0,            1];

%rotation from reference to matrix rotation R
rot = [0, -1, 0;
       1,  0, 0;
       0,  0, 1];

%rotation matrix for right leg (from origin to end-point)
rot_right = [1,  0, 0;
             0,  0, 1;
             0, -1, 0];

R_left = rot*R*rot';
R_right = rot_right*R_left;