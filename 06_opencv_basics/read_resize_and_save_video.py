# OpenCV basics: read a video file frame by frame, display it and save it to output.avi.
#
# Run from this folder:  python read_resize_and_save_video.py
# NOTE: the script expects a file called video1.mp4 in this folder. That video is NOT included in the repo - add your own.
# Requires: opencv-python. Press '1' to stop.

import cv2

# Open a video file (use 0 instead of a filename for the webcam)
cap = cv2.VideoCapture("video1.mp4")

# NOTE: comparing a bool with the *string* 'False' is never true, so this check never fires; use `if not cap.isOpened():`
if (cap.isOpened() == 'False'):
    print("Error Reading the video")

# Frame size: property id 3 = width, 4 = height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
