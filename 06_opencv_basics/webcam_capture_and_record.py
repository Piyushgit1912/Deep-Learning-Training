# OpenCV basics: capture video from the webcam, display it live and record it to output.avi.
#
# Run from this folder:  python webcam_capture_and_record.py
# Requires: opencv-python and a webcam. Press '1' to stop.

import cv2

# Open the default webcam (index 0)
cap = cv2.VideoCapture(0)

# NOTE: comparing a bool with the *string* 'False' is never true, so this check never fires; use `if not cap.isOpened():`
if (cap.isOpened() == 'False'):
    print("Error Reading the video")

# Read the camera's frame size (3 = width, 4 = height)
