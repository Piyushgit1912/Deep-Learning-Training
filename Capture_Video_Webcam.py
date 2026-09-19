import cv2

cap = cv2.VideoCapture(0)

if (cap.isOpened() == 'False'):
    print("Error Reading the video")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        resize_frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
        output.write(frame)
        cv2.imshow("Frame", resize_frame)

        if cv2.waitKey(1)&0xFF==ord('1'):
            break
    else:
        break
output.release()
cap.release()
cv2.destroyAllWindows()