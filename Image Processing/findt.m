clear
clc
tic

fileName = 'GOPR0002.MP4'; 
obj = VideoReader(fileName);
lastFrame = read(obj, inf);
numFrames = obj.NumberOfFrames;% ֡������
 for k = 750 : 5 :numFrames% ��ȡ����
    frame = read(obj,k);
%     frame(1:90,:,1:3)=0;
%     frame(:,1:90:,1:3)=0;
    uavtarget( frame,k );%Ŀ����������
    fprintf('Process... %3.1f%%',100*k/numFrames)
    fprintf('\n');
    k
 end
 disp('All Done!')
 [y,Fs]=audioread('0165.wav');
 sound(y,Fs);
toc