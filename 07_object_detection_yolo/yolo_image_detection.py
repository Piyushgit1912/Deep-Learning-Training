# Object detection on a single image with YOLOv8.
#
# Run from this folder:  python yolo_image_detection.py   (needs image3.png and yolov8n.pt here)
# Requires: pip install ultralytics opencv-python
# yolov8n.pt = YOLOv8 'nano' weights pre-trained on the COCO dataset (80 object classes).

import  cv2
from ultralytics import YOLO

# Load the pre-trained YOLOv8-nano model (Ultralytics downloads the weights if the file is missing)
