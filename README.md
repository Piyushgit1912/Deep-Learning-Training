# Deep Learning Journey

A hands-on, code-first learning path through deep learning - from a single artificial neuron and backpropagation written in pure NumPy,
to CNNs, transfer learning, RNN/LSTM sequence models, YOLO object detection, face recognition and NLP chatbots.

Every notebook and script is commented so it can be read as a tutorial: each one starts with a short explanation of the concept,
and the code is annotated step by step.

## Learning path

| # | Folder | What you learn | Tools |
|---|---|---|---|
| 01 | [`01_neural_network_fundamentals`](01_neural_network_fundamentals) | neuron, activation functions, loss functions, gradient descent, optimizers, backpropagation | NumPy, Matplotlib |
| 02 | [`02_keras_regression_and_classification_labs`](02_keras_regression_and_classification_labs) | linear and logistic regression, XOR, function approximation, stock prediction (linear -> LSTM) | Keras |
| 03 | [`03_image_classification_cnn`](03_image_classification_cnn) | ANN vs CNN on MNIST, Fashion-MNIST, CIFAR-10, cats vs dogs, flower photos (augmentation, dropout) | TensorFlow / Keras |
| 04 | [`04_transfer_learning`](04_transfer_learning) | re-using a pre-trained MobileNetV2 | TensorFlow / Keras |
| 05 | [`05_sequence_models_rnn`](05_sequence_models_rnn) | RNN text (spam) classifier | TensorFlow / Keras |
| 06 | [`06_opencv_basics`](06_opencv_basics) | read / resize / display images, process video and webcam streams | OpenCV |
| 07 | [`07_object_detection_yolo`](07_object_detection_yolo) | object detection on images, videos and webcam with YOLOv8 | Ultralytics, OpenCV |
| 08 | [`08_pose_estimation_yolo`](08_pose_estimation_yolo) | human pose keypoints and a rule-based pose classifier | Ultralytics, OpenCV |
| 09 | [`09_face_recognition`](09_face_recognition) | face dataset collection and LBPH face-recognizer training | OpenCV |
| 10 | [`10_nlp_and_chatbots`](10_nlp_and_chatbots) | rule-based, embedding-based and voice-enabled chatbots | spaCy, SpeechRecognition, pyttsx3 |

Suggested order: follow the numbers. Sections 01-02 are the foundation; 03-05 build on them; 06-10 are applications.

## Getting started

```bash
git clone <your-repo-url>
cd deep-learning-journey

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# only needed for the chatbot section (10)
python -m spacy download en_core_web_md

jupyter notebook
```

### Running the code

* **Run each notebook or script from inside its own folder.** Data files, images, videos and model weights are loaded with
  relative paths (for example `image3.png`, `yolov8n.pt`, the CSV files), and they are stored next to the code that uses them.
* Notebooks that use the flower dataset or MNIST/CIFAR-10 download the data automatically on first run.
* Scripts that use a webcam or microphone (06, 07 webcam, 08, 09, 10 voice assistant) need that hardware.

## Repository layout

```
deep-learning-journey/
|-- 01_neural_network_fundamentals/           6 notebooks (+ 1 scratch notebook)
|-- 02_keras_regression_and_classification_labs/  6 notebooks + 4 CSV datasets
|-- 03_image_classification_cnn/              6 notebooks
|-- 04_transfer_learning/                     1 notebook + sample image + ImageNet labels
|-- 05_sequence_models_rnn/                   RNN spam classifier
|-- 06_opencv_basics/                         3 scripts + sample image
|-- 07_object_detection_yolo/                 4 scripts + weights + sample image/video
|-- 08_pose_estimation_yolo/                  1 script + pose weights
|-- 09_face_recognition/                      2 scripts + trained model + sample dataset (+ drafts/)
|-- 10_nlp_and_chatbots/
|   |-- rule_based/                           regex / if-elif chatbots (+ drafts/)
|   |-- embedding_based/                      spaCy similarity Q&A bots (+ drafts/)
|   `-- voice_assistant/                      speech-to-text, text-to-speech, voice Q&A
|-- requirements.txt
`-- README.md
```

## Notes on the code

* **`NOTE:` comments** mark places where the original code has a known bug or surprising behaviour (for example a typo that raises an
