# Traffic Surveillance

## Introduction
In this project, we intend to detect some traffic violations with the help of cameras located on the road.
Some of the specialized operations performed include identifying the vehicle on the road, identifying the location of the license plate in the image of a vehicle, identifying the license plate characters and registering it, as well as identifying the vehicle lane on the highway, which is mainly done through yolov5 network.[1]

### identifying the vehicle on the road
In this section, you can see a picture of the result of identifying the cars on the road. The same type as before was done with the help of the yolov5 network.

![10](https://user-images.githubusercontent.com/61683254/117567325-12808c80-b0d1-11eb-906c-80c51df0fde1.PNG)


### identifying the location of the license plate in the image of a vehicle
In this section, you will see a picture of the result of identifying the location of the license plate in a photo of a car.
The process of training the model was done with the help of the yolov5 network, but the collection of data and training images was the responsibility of the team members. 

![20](https://user-images.githubusercontent.com/61683254/117567443-a94d4900-b0d1-11eb-9653-d4ec5f55b8c5.PNG)

### identifying the license plate characters and registering it
The result of identifying different license plate characters can also be seen in the following section, which is done by collecting a lot of training Data and the yolov5 network, although the result of different algorithms such as OCR has been examined during the project.

![40](https://user-images.githubusercontent.com/61683254/117567713-8d967280-b0d2-11eb-99cf-084b9f4dd8e6.PNG)


### identifying the vehicle lane on the highway
In this part, the final result is obtained by identifying the highway lines by the yolov5 network, but during the final result, different methods and algorithms such as classical image processing methods such as the Huff algorithm[2] and the network Unet have been used.[3]

![30](https://user-images.githubusercontent.com/61683254/117567846-4361c100-b0d3-11eb-909e-062b24d50791.PNG)

### future plans
All the codes are available in the repository and also one of the future plans of our team is to implement these algorithms embedded on the Jetson Nano processor.

### Introducing our team
All activities of this project have been under the supervision of the National Elite Foundation of Iran and the team members have received elite points in exchange for carrying out this project.
1.Abbas Omidi (abbasomidi77@gmail.com)
linkedin : https://www.linkedin.com/in/abbasomidi77/

2.Amirhossein Heydarian (amirhossein4633@gmail.com )
linkedin : https://www.linkedin.com/in/amirhosseinh77/

3.Aida Mohammadshahi (https://www.linkedin.com/in/aida-mohammadshahi-9845861b3/)
linkdein : https://www.linkedin.com/in/aida-mohammadshahi-9845861b3/

4.Ali Salehi (thealisalehi96@gmail.com)

5.Behnam Asghari (behnam.asghari1370@gmail.com)

6.Ehsan Noshahri (noshahriehsan@gmail.com)

### citations
1.https://github.com/ultralytics/yolov5

2.https://en.wikipedia.org/wiki/Hough_transform

3.https://github.com/zhixuhao/unet

download Unet model from [here](https://drive.google.com/file/d/1P-LwX_eisBQULqKOQajFWTH011QPLutS/view?usp=sharing)
