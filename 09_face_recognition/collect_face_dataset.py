# Step 1 of 2 - collect face images for training.
#
# Opens the webcam, detects faces with a Haar cascade and, each time SPACE is pressed, saves the cropped grayscale face
# to Image_Dataset/<person_name>/N.jpg. Press Q to quit.
#
# Pipeline: collect_face_dataset.py  ->  train_face_recognizer.py  ->  face_model.yml
# Run from this folder. Requires: opencv-python and haarcascade_frontalface_default.xml (included in this folder).

import cv2
import os

# Change name here
person_name = "Piyush"

# Create dataset folder
dataset_path = "Image_Dataset"
person_path = os.path.join(dataset_path, person_name)
os.makedirs(person_path, exist_ok=True)

# Haar Cascade
# Using the XML file present in Face_Recognition folder
base_dir = os.path.dirname(os.path.abspath(__file__))

cascade_path = os.path.join(
    base_dir,
    "haarcascade_frontalface_default.xml"
)

# Haar cascade: a classic pre-trained face detector that scans the image with simple rectangular features
face_cascade = cv2.CascadeClassifier(cascade_path)

# Check Haar Cascade
if face_cascade.empty():
    print("ERROR: Haar Cascade file not found!")
    print("Expected path:")
    print(cascade_path)
    exit()

print("Haar Cascade loaded successfully!")

# Webcam
cap = cv2.VideoCapture(0)

# Check webcam
if not cap.isOpened():
    print("Camera not detected")
    exit()

count = 0
# Stop automatically after this many face images have been saved
MAX_IMAGES = 3

print("Press SPACE to capture image")
print("Press Q to quit")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera not detected")
        break

    # Haar cascades work on grayscale images
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Returns one (x, y, w, h) box per face. Arguments: scaleFactor=1.3 and minNeighbors=5.
    # A larger scaleFactor is faster but may miss faces; a higher minNeighbors gives fewer false positives.
    faces = face_cascade.detectMultiScale(
        gray,
        1.3,
        5
    )

    # Draw rectangle
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.imshow(
        "Capture Images",
        frame
    )

    # Read a key press (the & 0xFF keeps only the last byte of the key code)
    key = cv2.waitKey(1) & 0xFF

    # Space pressed
    if key == 32:

        if len(faces) > 0:

            (x, y, w, h) = faces[0]

            # Crop face from grayscale image
            face_crop = gray[
                y:y + h,
                x:x + w
            ]

            count += 1

            file_path = os.path.join(
                person_path,
                f"{count}.jpg"
            )

            # Save the cropped face as an image file
            cv2.imwrite(
                file_path,
                face_crop
            )

            print("Saved:", file_path)

            if count >= MAX_IMAGES:

                print("Finished capturing images")
                break

        else:

            print("No face detected")

    # Quit
    if key == ord("q") or key == ord("Q"):
        break


# Cleanup
cap.release()
cv2.destroyAllWindows()

print("Images in path:", person_path)