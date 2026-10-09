# Object detection on a video file with YOLOv8; the annotated video is saved to output.avi.
#
# Run from this folder:  python yolo_video_detection.py   (needs car_vedio.mp4 and yolov8n.pt here)
# Requires: pip install ultralytics opencv-python
# yolov8n.pt = YOLOv8 'nano' weights pre-trained on the COCO dataset (80 object classes).

import cv2
from ultralytics import YOLO
import math

# Open the input video
cap=cv2.VideoCapture('car_vedio.mp4')
# The 80 COCO class names, in the index order YOLO uses
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
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

# Load the pre-trained YOLOv8-nano model
model= YOLO('yolov8n.pt')
# NOTE: comparing a bool with the *string* 'False' is never true, so this check never fires; use `if not cap.isOpened():`
if(cap.isOpened()=='False'):
    print('error reading the video')
