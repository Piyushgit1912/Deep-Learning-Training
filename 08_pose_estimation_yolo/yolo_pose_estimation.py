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
# NOTE: in images the y axis grows DOWNWARD, so 'wrist y < shoulder y' means the wrist is ABOVE the shoulder.
def detect_pose(keypoints):



    # Pick out the joints we need
    left_shoulder=keypoints[5]
    right_shoulder=keypoints[6]
    left_wrist=keypoints[9]
    right_wrist=keypoints[10]
    left_hip=keypoints[11]
    right_hip=keypoints[12]


    # Both wrists above the shoulders -> hands up
    if left_wrist[1] < left_shoulder[1] and right_wrist[1] < right_shoulder[1]:
        return 'Hands up POSE'

    # Both wrists roughly level with the shoulders (within 40 px) -> T-pose
    if abs( left_wrist[1]- left_shoulder[1])< 40 and abs( right_wrist[1] - right_shoulder[1]) < 40:
                                            return 'T pose'

    # Shoulders above the hips -> upright / standing
    if left_shoulder[1] < left_hip[1] and right_shoulder[1] < right_hip[1]:
            return 'Standing'

    # No rule matched
    return 'Unknown Pose'

# Main loop: grab a frame, detect poses, overlay the result
while True:
        ret, frame= cap.read()
        if not ret:
         break

        # Run pose estimation on the frame
        results = model(frame)

        # Default label when nobody is detected
        pose_name= 'No Person'


        for r in results:
                 if r.keypoints is not None:
                         # Keypoint coordinates for every detected person, shape (people, 17, 2)
                         keypoints= r.keypoints.xy.cpu().numpy()

                         if len(keypoints)>0:
                                 # Use only the first detected person
                                 kp=keypoints[0]
                                 pose_name= detect_pose(kp)

        # Draw the skeleton and boxes on the frame
        annotated= results[0].plot()

        # Overlay the pose name on the image
        cv2.putText(
                annotated,pose_name,(30,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2,)
        
        # Show the annotated frame
        cv2.imshow('YOLO Pose Detection', annotated)

        # Press 'q' to quit
        if cv2.waitKey(1)& 0xFF== ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
