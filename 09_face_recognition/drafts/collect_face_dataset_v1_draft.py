# Earlier draft of collect_face_dataset.py (see that file for the working, improved version).
#
# NOTE: cv2.VideoCapture(dataset_path) is given a folder path instead of a camera index, so the camera never opens.
# The improved script uses cv2.VideoCapture(0). The variable name MaAX_IMAGES contains a typo, but it is used consistently so it still works.

import cv2
import os

# Change name here
person_name = "Piyush"

# Create dataset folder
dataset_path = "Image_Dataset"
person_path = os.path.join(dataset_path, person_name)
os.makedirs(person_path, exist_ok=True)

# Haar Cascade
# Load the Haar cascade that ships with OpenCV (no separate XML file needed)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

)

# Webcam
# url='https://192.0.0.4:8080'
# NOTE: a camera index such as 0 (or a stream URL) belongs here, not a folder path
cap = cv2.VideoCapture(dataset_path)

count = 0
MaAX_IMAGES = 3

print("Press SPACE to capture image")
print("Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not detected")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces: scaleFactor=1.3, minNeighbors=5
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangle
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Capture Images", frame)

    key = cv2.waitKey(1)

    # Space pressed
    if key == 32:
        if len(faces) > 0:
            (x, y, w, h) = faces[0]

            # Crop the face from the COLOUR frame (the improved script saves grayscale crops)
            face_crop = frame[y:y+h, x:x+w]

            count +=1

            file_path = os.path.join(person_path, f"{count}.jpg")
            cv2.imwrite(file_path, face_crop)
            print("Saved", file_path)

            if count >= MaAX_IMAGES:
                print("Finished capturing images")
                break
        else:
            print("No face detected")

    # Quit
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Images in path", person_path)