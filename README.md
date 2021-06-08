# Traffic Surveillance

# Abstract
In This Project, We Identified Some Traffic Violations With the Help of Road Cameras. Some of the Specialized Operations Performed Include Identifying the Vehicle on the Road, Identifying the Location of the License Plate in the Image of a Vehicle, Identifying the License Plate Characters and Registering It, as Well as Identifying the Vehicle Line on the Highway, Mainly Through yolov5 Network, Neural Networks, and Computer Vision Algorithms Are Done.

## Introduction
In this project, we intend to detect common traffic violations using surveillance cameras on roads.
Some of the specialized operations performed during this task include identifying different vehicles on the road, detecting the license plate of each vehicle, recognizing the characters on each license plate and recording them, as well as specifying the lane number of each vehicle. 
The YOLOv5 network[1] has been widely used throughout this project.


### Identifying vehicles on the road
Below, you can see a sample result of identifying different vehicles on the road. The YOLOv5 network has been used to perform this operation.

![10](https://user-images.githubusercontent.com/61683254/117567325-12808c80-b0d1-11eb-906c-80c51df0fde1.PNG)

### Detecting the license plate location of each vehicle
In this section, you can see the performance of the model trained for detecting the location of license plates from the vehicle images.
The training of the detection model was done with the help of the YOLOv5 network, but the collection and preparation of the training dataset has been conducted by the team members. 

![20](https://user-images.githubusercontent.com/61683254/117567443-a94d4900-b0d1-11eb-9653-d4ec5f55b8c5.PNG)

### Recognition of license plate characters
The result of recognizing different license plate characters can be seen in the following section.
This task involved collecting and annotating a large amount of image data and training the YOLOv5 network with them. Other methods and algorithms such as OCR have also been examined for this part.

![40](https://user-images.githubusercontent.com/61683254/117567713-8d967280-b0d2-11eb-99cf-084b9f4dd8e6.PNG)

### Identifying lane numbers and masks
In this part, line segments on the roads have been identified using the YOLOv5 network. 
However, to generate the lane masks and their number, image processing methods such as Hough transform[2] and other neural networks such as UNet[3] have been employed.

![30](https://user-images.githubusercontent.com/61683254/117567846-4361c100-b0d3-11eb-909e-062b24d50791.PNG)

### Future plans
All of the codes and model weights in this repository will be made publicly available upon the completion of the project. Also we intend to implement this project on NVIDIA Jetson Nano Developer Kit.

### Introducing our team
All of the activities of this project have been under the supervision of the National Elite Foundation of Iran and the team members have received elite points in exchange for carrying out this project.

- Abbas Omidi --- [Linkedin](https://www.linkedin.com/in/abbasomidi77/), [Github](https://github.com/abbasomidi77), [Email](mailto:abbasomidi77@gmail.com)

- Amirhossein Heydarian ---  [Linkedin](https://www.linkedin.com/in/amirhosseinh77/), [Github](https://github.com/amirhosseinh77), [Email](mailto:amirhossein4633@gmail.com )

- Aida Mohammadshahi ---  [Linkedin](https://www.linkedin.com/in/aida-mohammadshahi-9845861b3/), [Github](https://github.com/aidamohammadshahi), [Email](mailto:aidamoshahi@gmail.com)

- Ali Salehi [Email](mailto:thealisalehi96@gmail.com)

- Behnam Asghari [Email](mailto:behnam.asghari1370@gmail.com)

- Ehsan Noshahri [Email](mailto:noshahriehsan@gmail.com)

### Citations
1.https://github.com/ultralytics/yolov5

2.https://en.wikipedia.org/wiki/Hough_transform

3.https://github.com/zhixuhao/unet

download Unet model from [here](https://drive.google.com/file/d/1P-LwX_eisBQULqKOQajFWTH011QPLutS/view?usp=sharing)
