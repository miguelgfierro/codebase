function x = interpolation (T, t, x0, x1, v0, v1)
a = x0;
b = v0;
c = (3*(x1-x0) - T*(2*v0+v1))/T^2;
d = (2*(x0-x1) + T*(v0+v1))/T^3;
x = a + b*t + c*t.^2 + d*t.^3;