# An Embedded Deep Learning-based Package for Traffic Law Enforcement


## Introduction
In this project, we intend to detect common traffic violations using surveillance cameras on roads.
Some of the specialized operations performed during this task include identifying different vehicles on the road, detecting the license plate of each vehicle, recognizing the characters on each license plate and recording them, as well as specifying the lane number of each vehicle. 
The YOLOv5 network[1] has been widely used throughout this project. Finally, the project is embedded on the NVIDIA® Jetson Nano B01 ™ Developer Kit and all parts of the project are implemented as embedded hardware.


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

### Dataset
To train the system and evaluate its overall performance in real-world scenarios, an embedded camera was utilized to collect a dataset of urban streets and out-of-town roads containing 314 different samples of HGVs. These films cover various roads, heavy goods vehicles, and license plates and vary in location and time. They also feature light and heavy traffic areas to cover various roads, heavy vehicles, and license plates. In each stage, such as overtaking lane detection, HGV detection, license plate detection, and character detection, the integrated model was trained on 250 photos from this data set. Finally, 45 photos from the data set were used to test the model, which included various types of heavy vehicles. There are 20 violating cars and 25 non-violating automobiles in the evaluation data set.

Some photos of Dataset:

![2](https://user-images.githubusercontent.com/61683254/125813984-98dbece1-a542-4345-8196-2d0b6e5a6344.png)
![20](https://user-images.githubusercontent.com/61683254/125813994-1fd1c8fb-26e1-4b9a-9cf3-fc45938b1ba8.png)
![25](https://user-images.githubusercontent.com/61683254/125814011-58181439-a756-491e-80bf-782388b9fcf5.png)
![17_2](https://user-images.githubusercontent.com/61683254/125814065-bb7ee05e-7d1f-4339-8946-0482f0cead60.png)



### Hardware
The Jetson Nano ™ built by NVIDIA® and Waveshare 12.3MP camera were employed in this study's hardware. The NVIDIA® Jetson Nano B01 ™ Developer Kit with GPU processor is a compact, powerful computer that allows many neural networks to run in parallel for image classification, object identification, segmentation, and speech processing applications. Waveshare's 12.3MP camera captured images with a resolution of 4056 x 3040 pixels. The Sony IMX477-160 sensor powers the camera, which can take up to 90 frames per second. In addition, the operating system on this hardware is Ubuntu 18.04.

Some photos that show the embedded system:

![100](https://user-images.githubusercontent.com/61683254/125813066-3b3f3291-bf8c-4281-bfd8-6f65125c462e.png)
![101](https://user-images.githubusercontent.com/61683254/125813174-1a66cc32-49a4-4958-8ba7-6594565a849c.jpg)


### Contact us
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
