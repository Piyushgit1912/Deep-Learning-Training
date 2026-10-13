import cv2
from ultralytics import YOLO
import math

cap=cv2.VideoCapture('car_vedio.mp4')
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

model= YOLO('yolov8n.pt')
if(cap.isOpened()=='False'):
    print('error reading the video')

frame_width=int(cap.get(3))
frame_height=int(cap.get(4))

output= cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height))

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret:
        results=model(frame,stream=True)
        for r in results:
            boxes=r.boxes
            for box in boxes:
                x1,y1,x2,y2=box.xyxy[0]

                print(x1,y1,x2,y2)
                x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
                conf=math.ceil((box.conf[0]*100))/100
                cls=int(box.cls[0])
                class_name=classNames[cls]
                label=f'{class_name}{conf}'
                text_size=cv2.getTextSize(label,0,fontScale=1,thickness=2)[0]
                c2=x1+text_size[0],y1-text_size[1]-3
                cv2.rectangle(frame,(x1,y1),c2,(255,0,0),-1,cv2.LINE_AA)
                cv2.putText(frame,label,(x1,y1-2),0,1,[255,255,255],thickness=1,lineType=cv2.LINE_AA)
        resize_frame=cv2.resize(frame,(0,0),fx=0.6,fy=0.6,interpolation=cv2.INTER_AREA)
        output.write(frame)
        cv2.imshow('Frame',resize_frame)

        if cv2.waitKey(1)&0xFF==ord('1'):
            break
    else:
        break
output.release()
cap.release()
cv2.destroyAllWindows