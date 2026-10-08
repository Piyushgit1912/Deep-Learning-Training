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

# Video writer: MJPG codec, 10 frames per second, original frame size
output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

# Read the video frame by frame
while (cap.isOpened()):
    # ret is False when there are no more frames
    ret, frame = cap.read()
    if ret:
        # Shrink to 60% for display only
        resize_frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
        # Save the original-size frame to output.avi
        output.write(frame)
        # Show the (resized) frame
        cv2.imshow("Frame", resize_frame)

        # Press '1' to quit early (waitKey also lets the window refresh)
        if cv2.waitKey(1)&0xFF==ord('1'):
            break
    else:
        break
# Release the file and window resources
output.release()
cap.release()
cv2.destroyAllWindows()