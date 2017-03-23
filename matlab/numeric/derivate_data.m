% This function derivates a vector or a matrix with respect to time

function [xd xdd] = derivate_data(t,x)

t = trajectoriesToColumns(t);
x = trajectoriesToColumns(x);
n_elements = length(t);


if (length(x) ~= n_elements)
  error('Trajectory and time must have the same lenght');
end
[n_trajectories vector_type] = min(size(x));


% Fitting and obtantion of velocity and acceleration
options = fitoptions('Method','SmoothingSpline','SmoothingParam',0.999); %r² = 0.999
xd = [];
xdd = [];
for i = 1:n_trajectories
  fit1 = fit(t,x(:,i),'SmoothingSpline',options); % Más lento, resultado =
  [qd qdd] = differentiate(fit1, t); % Es la derivada
  xd = [xd qd];
  xdd = [xdd qdd];
%   xm = x(1:10:end,i);
%   tm = t(1:10:end);
%   s = spline(tm,xm);
%   ds = fnder(s);
%   xd = [xd smooth(fnval(ds,t),20)];
%   dds = fnder(ds);
%   xdd = [xdd smooth(fnval(dds,t),20)];
end

% We return the solution with the same size of the input x
if (vector_type == 1)
  xd = xd';
  xdd = xdd';
end
