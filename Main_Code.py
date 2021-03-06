#importing required libraries

import cv2
import os

#Creating bg files
#Paths are wrt to my system directories

path_pos='/home/aryashukla/Desktop/Project/Cascade/dataset25X25/pos_resized/'
path_neg='/home/aryashukla/Desktop/Project/Cascade/dataset25X25/neg_resized/'
pos_img=os.listdir(path_pos)
neg_img=os.listdir(path_neg)

#Create bg file for positive images
for img in pos_img:
    line=path_pos+img+' '+'1 0 0 25 25'+'\n'
    with open('/home/aryashukla/Desktop/Project/Cascade/bg_pos.lst', 'a') as f:
        f.write(line)
#Create bg file for negative images
for img in neg_img:
    line=path_neg+img+'\n'
    with open('/home/aryashukla/Desktop/Project/Cascade/bg_neg.txt', 'a') as f:
        f.write(line)


#Below mentioned command are excuted on linux terminal

#Updating packages
sudo apt-get update

#Cloning OpenCV library from its git repo 
git clone https://github.com/Itseez/opencv.git

#Installing cmake
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

#Installing OpenCV development library
sudo apt-get install libopencv-dev

#Creating positive vector files
opencv_createsamples -info bg_pos.lst -num 5540 -w 25 -h 25 -vec positives_5540.vec

#Training Cascade
opencv_traincascade -data data -vec positives_1316.vec -bg bg_negmid_1600.txt -numPos 5000 -numNeg 2700 -numStages 5 -w 25 -h 25
