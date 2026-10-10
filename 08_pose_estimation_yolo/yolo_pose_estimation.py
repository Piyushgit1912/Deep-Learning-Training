# Real-time human pose estimation from the webcam with YOLOv8-pose, plus a simple rule-based pose classifier.
#
# YOLOv8-pose detects 17 body keypoints (COCO format) per person. detect_pose() then applies simple geometric rules
# to those keypoints to name the pose: 'Hands up POSE', 'T pose' or 'Standing'.
#
# Run from this folder:  python yolo_pose_estimation.py   (needs yolov8n-pose.pt here and a webcam)
# Requires: pip install ultralytics opencv-python numpy. Press 'q' to quit.

import cv2
from ultralytics import YOLO
import numpy as np

# landd yolo pose model 
model= YOLO('yolov8n-pose.pt')

# Open the default webcam
cap=cv2.VideoCapture(0)

# Rule-based pose classifier. `keypoints` is a (17, 2) array of (x, y) pixel coordinates.
# Indices used: 5/6 = left/right shoulder, 9/10 = left/right wrist, 11/12 = left/right hip.
