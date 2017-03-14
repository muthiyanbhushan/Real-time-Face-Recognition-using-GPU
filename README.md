# Real-time-Face-Recognition-using-GPU
Using Caffe and OpenCV for face recognition.


==============================================================================================================
Institution: San Jose State University
==============================================================================================================

This basically explains how to execute the demo for face recognition system.
It only works on TX1 and need to set the path properly. 
If downladed and extracted in "/home/ubuntu/".
change the related paths.
==============================================================================================================
1. testing_GoogLeNet.py [Main Demo File]
RUN: $ python testing_GoogLeNet.py

- shows real time camera video streaming on the screen.
- detects face with rectangle line
- when you are ready to take picture, push "ctrl + c" on terminal where you executed
- terminal shows: Classify (y/n)? 
- shows top-5 prediction results with name and percentage
- if it is not people trained before, shows "Image does not belong to top-1 category of the class" on terminal

2. test_GoogLeNet_test_v2.py [You can try with your own input image]
RUN: $ python test_GoogLeNet_test_v2.py -i [input_image]

- download the people's picture from web, and try to test here
- works the same as above without camera operation
- it shows the picture with prediction result

3. testing_AlexNet.py 
- RUN: $ python testing_AlexNet.py
- Follow same commands as for Googlenet testing.

	  	
