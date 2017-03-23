% This function put a set of several trajectories in rows
% WARNING: It takes the longer dimension as the time dimension
function [traj_new columns rows] = trajectoriesToRows(traj)

[traj_c cs rs] = trajectoriesToColumns(traj);
traj_new = traj_c';
columns = rs;
rows = cs;