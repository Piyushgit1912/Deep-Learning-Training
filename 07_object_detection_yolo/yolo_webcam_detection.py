# Real-time object detection from the webcam with YOLOv8; the annotated video is saved to output.avi.
#
# Run from this folder:  python yolo_webcam_detection.py   (needs yolov8n.pt here and a webcam)
# Requires: pip install ultralytics opencv-python
# yolov8n.pt = YOLOv8 'nano' weights pre-trained on the COCO dataset (80 object classes).

import cv2 
from ultralytics import YOLO
import math
# Open the default webcam
cap = cv2.VideoCapture(0)
# Class names in YOLO's index order.
# NOTE: the last five names (idcard, watch, cable, window, charger) are not COCO classes; the pretrained yolov8n never
# predicts those indices - they would only matter for a custom-trained model.
classNames = [
    "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
    "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
    "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
    "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
    "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake",
    "chair", "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop",
    "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
    "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier",
    "toothbrush","idcard","watch", "cable", "window", "charger"
]
# Load the pre-trained YOLOv8-nano model
model = YOLO("yolov8n.pt")
# NOTE: comparing a bool with the *string* 'False' is never true, so this check never fires; use `if not cap.isOpened():`
