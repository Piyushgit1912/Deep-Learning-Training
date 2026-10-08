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
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Video writer: MJPG codec, 10 frames per second
output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

# Grab frames until the camera stops or the user quits
while (cap.isOpened()):
    # ret is False if no frame could be read
    ret, frame = cap.read()
    if ret:
        # Shrink to 60% for display only
        resize_frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
        # Record the original-size frame
        output.write(frame)
        # Show the live preview
        cv2.imshow("Frame", resize_frame)

        # Press '1' to quit
        if cv2.waitKey(1)&0xFF==ord('1'):
            break
    else:
        break
# Release the writer, camera and windows
output.release()
cap.release()
cv2.destroyAllWindows()