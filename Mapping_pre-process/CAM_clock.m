clear
clc
tic
%************************�������ļ�����**********************************
%*************************�����������**********************************
tic
fileName = 'arup.MP4'; 
cam_ori=imread('G0010005.JPG');%��һ��trigger��Ƭ
load('32.log-359302.mat')%��ȡlog����
% start_time=1; %��ʼʱ��,min
%***********************************************************************
% st=start_time*60*25; %��ʼ����֡
fprintf('Loading the video...')
fprintf('\n');
obj = VideoReader(fileName);
numFrames = obj.NumberOfFrames;% ֡������
cam=imresize(cam_ori,[1080 1920]);
sum_cam=sum(cam(:));
for k = 311: 1 :1000 % ��ȡ����
    frame = read(obj,k);
    m=cam-frame;
    allk(k)=std2(m(:))%/sum_cam;    
    if allk(k)<=10
      imwrite(frame,strcat(num2str(k),'r.jpg'),'jpg');
%       break
    end
    fprintf('Processing... %5d%',k)%���̱���
    fprintf('\n');
end
re_frame_no=k    %�ο�֡
save('targets_info.mat','re_frame_no','CAM','GPS','ATT');
% re_Line_no=CAM(1,1);
% re_yaw=CAM(1,10);
% [y,Fs]=audioread('0165.wav');
% sound(y,Fs);
toc