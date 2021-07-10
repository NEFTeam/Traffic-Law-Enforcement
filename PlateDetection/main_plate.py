from elements.yolo import CAR_DETECTION, PLATE_DETECTION, CHAR_EXTRACTION
import numpy as np
import cv2
import os
from glob import glob
from time import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--image', type = str, default = 'test_images/test1.jpg' , help = 'Name of the input image.')
args = parser.parse_args()

frame = cv2.imread(args.image)

car_classes = {2: 'car', 5: 'bus', 7: 'truck'}
plate_classes = {0: 'plate'}
char_classes = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
 10: 'a', 11: 'b', 12: 'p', 13: 't', 14: 'c', 15: 'j', 16: 'ch', 17: 'h', 18: 'kh', 19: 'd', 20: 'zal', 21: 'r', 22: 'z', 23: 'zh',
 24: 's', 25: 'sh', 26: 'sad', 27: 'zad', 28: 'ta', 29: 'za', 30: 'ain', 31: 'q', 32: 'f', 33: 'qaf', 34: 'k', 35: 'g', 36: 'l', 37: 'm',
 38: 'n', 39: 'v', 40: 'he', 41: 'y', 42: 'malool'}

# detector objects
car_detector = CAR_DETECTION('weights/car_model.pt', car_classes)
plate_detector = PLATE_DETECTION('weights/plate_model.pt', plate_classes)
char_extractor = CHAR_EXTRACTION('weights/char_model.pt', char_classes)

# detection process
cars = car_detector.detect(frame)
plates = plate_detector.detect(frame, cars)
chars = char_extractor.detect(frame, plates)

# plotting
for car in cars:
    print(car)
    label = car['label']
    score = car['score']
    [(xmin,ymin),(xmax,ymax)] = car['bbox']
    frame = cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), [0,255,255] , 2) 
    frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin,ymin), cv2.FONT_HERSHEY_SIMPLEX , 0.75, [0,255,255], 2, cv2.LINE_AA)

    if car['plate_bbox'] is not None:
        [(xmin,ymin),(xmax,ymax)] = car['plate_bbox']
        frame = cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), [255,0,0] , 2) 
        frame = cv2.putText(frame, 'plate', (xmin,ymin), cv2.FONT_HERSHEY_SIMPLEX , 0.75, [255,0,0], 2, cv2.LINE_AA)


cv2.imshow('output', cv2.resize(frame,(1000,700)))
cv2.waitKey()