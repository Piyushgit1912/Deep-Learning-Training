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

# Read the frame size (3 = width, 4 = height)
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))

# Writer for the annotated video: MJPG codec, 10 fps, original frame size
output= cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height))

# Process the video frame by frame
while(cap.isOpened()):
    # ret is False when the video ends / the camera stops
    ret,frame=cap.read()
    if ret:
        # Run YOLO on this frame (stream=True returns a generator, which saves memory)
        results=model(frame,stream=True)
        for r in results:
            boxes=r.boxes
            # Loop over every detected object
            for box in boxes:
                # Bounding-box corners (top-left and bottom-right) in pixels
                x1,y1,x2,y2=box.xyxy[0]

                print(x1,y1,x2,y2)
                x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
                # Draw the bounding box
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
                # Confidence score rounded up to 2 decimals
                conf=math.ceil((box.conf[0]*100))/100
                # Class index; used to look up the class name
                cls=int(box.cls[0])
                class_name=classNames[cls]
                label=f'{class_name}{conf}'
                # Measure the label so a filled background rectangle fits behind the text
                text_size=cv2.getTextSize(label,0,fontScale=1,thickness=2)[0]
                c2=x1+text_size[0],y1-text_size[1]-3
                cv2.rectangle(frame,(x1,y1),c2,(255,0,0),-1,cv2.LINE_AA)
                cv2.putText(frame,label,(x1,y1-2),0,1,[255,255,255],thickness=1,lineType=cv2.LINE_AA)
        # Shrink to 60% for display only; the saved video keeps full size
        resize_frame=cv2.resize(frame,(0,0),fx=0.6,fy=0.6,interpolation=cv2.INTER_AREA)
        # Save the annotated frame
        output.write(frame)
        # Show the annotated frame
        cv2.imshow('Frame',resize_frame)

        # Press '1' to quit (waitKey(1) also lets the window refresh)
        if cv2.waitKey(1)&0xFF==ord('1'):
            break
    else:
        break
# Release the file, video and windows
output.release()
cap.release()
# NOTE: the parentheses are missing, so this line does nothing; it should be cv2.destroyAllWindows()
cv2.destroyAllWindows