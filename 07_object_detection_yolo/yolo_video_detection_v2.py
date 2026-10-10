# Object detection on a video file with YOLOv8 - cleaned-up version of yolo_video_detection.py
# (adds an error check when the video cannot be opened and a fallback for the frame rate).
# The annotated video is saved to output.avi.
#
# Run from this folder:  python yolo_video_detection_v2.py   (needs car_vedio.mp4 and yolov8n.pt here)
# Requires: pip install ultralytics opencv-python
# yolov8n.pt = YOLOv8 'nano' weights pre-trained on the COCO dataset (80 object classes).

import cv2
from ultralytics import YOLO
import math

# Use the exact filename as it exists in your directory ('car_vedio.mp4')
video_path = 'car_vedio.mp4'
cap = cv2.VideoCapture(video_path)

# Correct check to ensure the video opened
if not cap.isOpened():
    print(f"Error: Could not open video file '{video_path}'. Check if the file exists and the filename is spelled correctly.")
    exit()

# The 80 COCO class names, in the index order YOLO uses
classNames = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
    "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
    "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
    "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
    "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
    "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
    "teddy bear", "hair drier", "toothbrush"
]

