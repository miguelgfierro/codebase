% Set timer with tic and stop timer with toc
tic
A = rand(12000, 4400);
B = rand(12000, 4400);
toc
C = A'.*B';
t = toc;
t
