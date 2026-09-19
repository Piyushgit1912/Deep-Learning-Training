import cv2
from ultralytics import YOLO
import numpy as np

# landd yolo pose model 
model= YOLO('yolov8n-pose.pt')

cap=cv2.VideoCapture(0)

def detect_pose(keypoints):



    left_shoulder=keypoints[5]
    right_shoulder=keypoints[6]
    left_wrist=keypoints[9]
    right_wrist=keypoints[10]
    left_hip=keypoints[11]
    right_hip=keypoints[12]


    if left_wrist[1] < left_shoulder[1] and right_wrist[1] < right_shoulder[1]:
        return 'Hands up POSE'

    if abs( left_wrist[1]- left_shoulder[1])< 40 and abs( right_wrist[1] - right_shoulder[1]) < 40:
                                            return 'T pose'

    if left_shoulder[1] < left_hip[1] and right_shoulder[1] < right_hip[1]:
            return 'Standing'

    return 'Unknown Pose'

while True:
        ret, frame= cap.read()
        if not ret:
         break

        results = model(frame)

        pose_name= 'No Person'


        for r in results:
                 if r.keypoints is not None:
                         keypoints= r.keypoints.xy.cpu().numpy()

                         if len(keypoints)>0:
                                 kp=keypoints[0]
                                 pose_name= detect_pose(kp)

        annotated= results[0].plot()

        cv2.putText(
                annotated,pose_name,(30,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2,)
        
        cv2.imshow('YOLO Pose Detection', annotated)

        if cv2.waitKey(1)& 0xFF== ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
