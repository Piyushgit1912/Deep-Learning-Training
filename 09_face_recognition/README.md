# 09 - Face Recognition (classic OpenCV pipeline)

```
collect_face_dataset.py  ->  Image_Dataset/<person>/*.jpg  ->  train_face_recognizer.py  ->  face_model.yml
```

1. `collect_face_dataset.py` - webcam + Haar-cascade face detection; SPACE saves a cropped face, Q quits
2. `train_face_recognizer.py` - trains an LBPH recognizer on `Image_Dataset/` and saves `face_model.yml`

Included: `haarcascade_frontalface_default.xml`, `haarcascade_eye.xml`, a trained `face_model.yml` and a small sample dataset in `Image_Dataset/`.
`drafts/` holds an earlier version of the capture script.

> A recognition (prediction) script that loads `face_model.yml` is not part of this folder yet.
> If you publish this repo, consider replacing the sample face photos and the trained model with non-personal data.

Requires `opencv-contrib-python` (provides `cv2.face`). Run the scripts from this folder.
