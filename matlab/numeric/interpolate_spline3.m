% 3 degree spline
function q = interpolate_spline3 (Ts, T, q0, q1)
time = 0 : Ts : T-Ts;
a = -2*(q1-q0)/T^3;
b = 3*(q1-q0)/T^2;
q = a * time.^3 + b * time.^2 + q0*ones(1,T/Ts);