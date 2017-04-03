# Real-time-Face-Recognition-using-GPU
Using Caffe and OpenCV for face recognition.

Institution: San Jose State University


This basically explains how to execute the demo for face recognition system.
It only works on TX1 and need to set the path properly. 
If downladed and extracted in "/home/ubuntu/".
change the related paths.

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

	  	
Some important notes:

A simple ConvNet is a sequence of layers, and every layer of a ConvNet transforms one volume of activations to another through a differentiable function. We use three main types of layers to build ConvNet architectures: Convolutional Layer, Pooling Layer, and Fully-Connected Layer (exactly as seen in regular Neural Networks). We will stack these layers to form a full ConvNet architecture.

Example Architecture: Simple ConvNet for CIFAR-10 classification could have the architecture [INPUT - CONV - RELU - POOL - FC]. In more detail:

INPUT [32x32x3] will hold the raw pixel values of the image, in this case an image of width 32, height 32, and with three color channels R,G,B.
CONV layer will compute the output of neurons that are connected to local regions in the input, each computing a dot product between their weights and a small region they are connected to in the input volume. This may result in volume such as [32x32x12] if we decided to use 12 filters.
RELU layer will apply an elementwise activation function, such as the \(max(0,x)\) thresholding at zero. This leaves the size of the volume unchanged ([32x32x12]).
POOL layer will perform a downsampling operation along the spatial dimensions (width, height), resulting in volume such as [16x16x12].
FC (i.e. fully-connected) layer will compute the class scores, resulting in volume of size [1x1x10], where each of the 10 numbers correspond to a class score, such as among the 10 categories of CIFAR-10. As with ordinary Neural Networks and as the name implies, each neuron in this layer will be connected to all the numbers in the previous volume.

In this way, ConvNets transform the original image layer by layer from the original pixel values to the final class scores. Note that some layers contain parameters and other don’t. In particular, the CONV/FC layers perform transformations that are a function of not only the activations in the input volume, but also of the parameters (the weights and biases of the neurons). On the other hand, the RELU/POOL layers will implement a fixed function. The parameters in the CONV/FC layers will be trained with gradient descent so that the class scores that the ConvNet computes are consistent with the labels in the training set for each image.

In summary:

A ConvNet architecture is in the simplest case a list of Layers that transform the image volume into an output volume (e.g. holding the class scores)
There are a few distinct types of Layers (e.g. CONV/FC/RELU/POOL are by far the most popular)
Each Layer accepts an input 3D volume and transforms it to an output 3D volume through a differentiable function
Each Layer may or may not have parameters (e.g. CONV/FC do, RELU/POOL don’t)
Each Layer may or may not have additional hyperparameters (e.g. CONV/FC/POOL do, RELU doesn’t)
