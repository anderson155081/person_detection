# person_detection

# Overview

This project aims to detect the presence of a person in a frame captured by a webcam. It uses YOLO (You Only Look Once) for real-time object detection. The project has two main Python scripts:

1. `run_noview.py`: Detects a person and prints a message to the console. Does not display the webcam feed.
2. `run_withview.py`: Similar to run_noview.py, but also displays the webcam feed with the detection overlay.
   
The model file `yolov8n.pt` is used for detection.

# Dependencies

The project has the following dependencies:
```bash
numpy==1.25.2
opencv_python==4.8.0.76
Pillow==10.0.1
ultralytics==8.0.180
```
You can install these using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
# Files

1. `requirements.txt`: Contains the list of dependencies for the project.
2. `run_noview.py`: Python script for person detection without displaying the webcam feed.
3. `run_withview.py`: Python script for person detection with a display of the webcam feed.
4. `yolov8n.pt`: Pre-trained YOLO model for object detection.

# Usage

## Running without Display
To run the detection without displaying the webcam feed, execute the following command:  
```bash
python run_noview.py
```
Press q to quit the application.

## Running with Display
To run the detection without displaying the webcam feed, execute the following command:  
```bash
python run_withview.py
```
Press q to quit the application.  

# Future Work

- Integrate with MQTT to control devices based on detection results.
- Optimize the detection algorithm for better performance.
