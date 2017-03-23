function [Rd, wd] = desired_orientations (T, Ts, Rd0)
iterations = T/Ts;
Rd = zeros(3,3, iterations);
for ii=1:iterations
    Rd(:,:,ii) = Rd0;
end
wd = zeros(3,iterations);