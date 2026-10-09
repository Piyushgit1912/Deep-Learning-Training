# Object detection on a single image with YOLOv8.
#
# Run from this folder:  python yolo_image_detection.py   (needs image3.png and yolov8n.pt here)
# Requires: pip install ultralytics opencv-python
# yolov8n.pt = YOLOv8 'nano' weights pre-trained on the COCO dataset (80 object classes).

import  cv2
from ultralytics import YOLO

# Load the pre-trained YOLOv8-nano model (Ultralytics downloads the weights if the file is missing)
model= YOLO('./yolov8n.pt')
# Run inference on the image; returns a list of Results objects (one per image)
results=model('image3.png')

# load original data 

img= cv2.imread('image3.png')

# results[0].plot() returns a copy of the image with boxes, class names and confidence scores drawn on it
annotated= results[0].plot()

# Display the annotated image
cv2.imshow('Result', annotated)
# Wait for a key press before closing
cv2.waitKey(0)
cv2.destroyAllWindows()