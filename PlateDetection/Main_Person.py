from elements.yolo import CAR_DETECTION as Person_Detection
import numpy as np
import cv2
import os
from glob import glob
from time import time
import argparse
import matplotlib.pyplot as plt
parser = argparse.ArgumentParser()
parser.add_argument('--image', type = str, default = 'a.jpg' , help = 'Name of the input image.')
args = parser.parse_args()

frame = cv2.imread(args.image)

Person_classes = {0: 'Person'}

# detector objects
Person_Detector = Person_Detection('weights/car_model.pt', Person_classes)


# detection process
Persons = Person_Detector.detect(frame)

# plotting
for Person in Persons:
    print(Person)
    label = Person['label']
    score = Person['score']
    [(xmin,ymin),(xmax,ymax)] = Person['bbox']
    frame = cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), [0,255,255] , 2) 
    frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin,ymin), cv2.FONT_HERSHEY_SIMPLEX , 0.75, [0,255,255], 2, cv2.LINE_AA)

plt.imshow(frame)

