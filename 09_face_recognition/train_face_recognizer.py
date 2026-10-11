# Step 2 of 2 - train a face recognizer on the collected images.
#
# Reads Image_Dataset/<person_name>/*.jpg (one sub-folder per person), trains an LBPH face recognizer
# (Local Binary Pattern Histograms - a classic, non-deep-learning method) and saves it to face_model.yml.
#
# Requires: pip install opencv-contrib-python   (cv2.face is not part of the main opencv-python package)
# Run from this folder after collect_face_dataset.py.

import cv2
import os
import numpy as np

dataset_path = "Image_Dataset"
# LBPH compares local texture patterns (histograms) of faces
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Training images (grayscale arrays)
faces = []
# A numeric id for each image
labels = []
# Maps the numeric id back to the person's name
label_map = {}

current_label = 0
# Every sub-folder of Image_Dataset is one person
for person_name in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_path):
        continue

    # Remember which name belongs to this id
    label_map[current_label] = person_name

    # Load each of this person's images in grayscale
    for image_name in os.listdir(person_path):
        img_path = os.path.join(person_path, image_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        faces.append(img)
        labels.append(current_label)

    # The next person gets the next id
    current_label +=1

# Fit the recognizer on all faces and their labels
face_recognizer.train(faces, np.array(labels))
# Save the trained model to disk
face_recognizer.save("face_model.yml")

print("Training Complete !")
print(label_map)