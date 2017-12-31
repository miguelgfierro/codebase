% Demo GIST descriptors based on original scripts from Oliva and Torralba
% source: http://people.csail.mit.edu/torralba/code/spatialenvelope/

% EXAMPLE 
% Load image
img1 = imread('../../../share/Lenna.png');

% Parameters:
clear param
%param.imageSize. If we do not specify the image size, the function LMgist
%   will use the current image size. If we specify a size, the function will
%   resize and crop the input to match the specified size. This is better when
%   trying to compute image similarities.
param.imageSize = [256 256]; % it works also with non-square images
param.orientationsPerScale = [8 8 8 8];
param.numberBlocks = 4;
param.fc_prefilt = 4;

% Computing gist requires 1) prefilter image, 2) filter image and collect
% output energies
tic
[gist1, param] = LMgist(img1, '', param);
toc

% Visualization
figure
subplot(121)
imshow(img1)
title('Input image')
subplot(122)
showGist(gist1, param)
title('Descriptor')




