# OpenCV basics: read an image, resize it and display it in a window.
#
# Run from this folder:  python read_and_display_image.py   (needs image3.png here)
# Requires: opencv-python

import cv2
# Load the image as a NumPy array (channel order is BGR, not RGB)
image=cv2.imread('image3.png')
# fx / fy are scale factors (0.6 = 60% size); INTER_AREA is the best interpolation for shrinking
resize_image=cv2.resize(image,(0,0),fx=0.6,fy=0.6, interpolation=cv2.INTER_AREA)
# Open a window showing the image
cv2.imshow('image1',resize_image)
# Wait indefinitely until a key is pressed
cv2.waitKey(0)