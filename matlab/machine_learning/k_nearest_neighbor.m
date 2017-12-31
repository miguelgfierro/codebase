% K nearest neighbor
%
% knnsearch finds the nearest neighbor in X for each point in Y.
% IDX is the index of the K nearest neighbors in X. 
% D is the distance of the K nearest neighbor in X to Y.
% IDX, D and Y have the same number of rows.
% source: https://es.mathworks.com/help/stats/knnsearch.html

rng('default') % for reproducibility
X = randn(100000,512);
Y = randn(2,512);
tic
[IDX,D] = knnsearch(X,Y,'K',5,'Distance','euclidean')
toc
