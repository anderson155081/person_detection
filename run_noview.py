import cv2
from PIL import Image
import numpy as np
from ultralytics import YOLO
import time

model = YOLO('yolov8n.pt')  # load an official model

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:

    # Capture frame-by-frame
    ret, frame = cap.read()
    results = model(frame, classes=0, show_labels=False, show_conf=False)

    if(results[0].__len__() == 0):
        # TODO: send mqtt message turn down all the devices
        print("No person detected, turn down all the devices")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # set the time interval to 3 seconds
    time.sleep(3)

cap.release()