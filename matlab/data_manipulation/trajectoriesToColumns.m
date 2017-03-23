% This function put a set of several trajectories in columns
% WARNING: It takes the longer dimension as the time dimension
function [traj_new columns rows] = trajectoriesToColumns(traj)

%if (isvector(traj))
%    traj_new = traj';
%    columns = 1;
%    rows = length(traj_new);
%elseif (ismatrix(traj))
    [dim1 dim2] = size(traj);
    if (dim1 > dim2) % Column trajectory
      rows = dim1;
      columns = dim2;
      traj_new = traj;
    else
      rows = dim2;
      columns = dim1;
      traj_new = traj';
    end
%else
%    traj_new = traj;
%    columns = 1;
%    rows = length(traj_new);
%end