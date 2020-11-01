# Coughing_Detection

Coughind detection by camera using Artificial Inteligent and a network of microphones

## Introduction
The Main objective of this project was detecting people who are coughing with camera, of course using AI and a network of microphones for registering the sounds and classify them.

For that we switched between 2 solutions to get an accurate results at the end :
1. If the person was far away from the zone (ex. the room) we need to get the result from the programm of camera 
2. If the person was inside the zone we need to cofirm the results using the network of microphones

The simulation of our programs was made by the camera & microphone of the computer, in order to use Raspberry Pi 3b+ with a raspbian OS.

## Resuluts
Here are some pictures of our results, some of them were a screenshots of a video and other were just a simple images passed as an input of the program :
![image](https://github.com/tahajadid/Coughing_Detection/blob/main/img_result/result5.png)
To see a demo video on my youtube chanel you can follow [this link](https://www.youtube.com/watch?v=6zsvt4dfRoQ)

## Require
1. [Pyhton](https://github.com/python/cpython)
2. [OpenCV](https://github.com/opencv/opencv)
3. [Keras](https://keras.io/)
4. [Caffe - docker ](https://hub.docker.com/r/bvlc/caffe/) required if you would like to convert caffe model to keras model. You don't have to compile/install caffe on your local machine.
5. [keras_Realtime_Multi-Person_Pose_Estimation](https://github.com/michalfaber/keras_Realtime_Multi-Person_Pose_Estimation#converting-caffe-model-to-keras-model)

