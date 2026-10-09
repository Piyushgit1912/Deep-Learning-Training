# 07 - Object Detection with YOLOv8

| Script | Input |
|---|---|
| `yolo_image_detection.py` | image (`image3.png`) |
| `yolo_video_detection.py` | video file (`car_vedio.mp4`), saves `output.avi` |
| `yolo_video_detection_v2.py` | same, cleaned-up version with error checks |
| `yolo_webcam_detection.py` | live webcam feed |

`yolov8n.pt` are the pre-trained YOLOv8-nano weights (COCO, 80 classes). Run the scripts from this folder.

```bash
pip install ultralytics opencv-python
python yolo_image_detection.py
```


## Tested with YOLOv8n
