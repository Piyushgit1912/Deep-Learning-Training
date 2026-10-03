# 03 - Image Classification with CNNs

| Notebook | Dataset | Idea |
|---|---|---|
| `01_mnist_digit_classifier_ann.ipynb` | MNIST (digits) | simple dense network + confusion matrix |
| `02_fashion_mnist_ann_vs_cnn.ipynb` | Fashion-MNIST | ANN baseline vs convolutional network |
| `03_cifar10_ann_vs_cnn.ipynb` | CIFAR-10 | colour images: ANN vs CNN |
| `04_cats_vs_dogs_cnn.ipynb` | cats_vs_dogs (TFDS) | binary CNN, `tf.data` pipeline, dropout |
| `05_flower_cnn_v1_initial_attempt.ipynb` | flower_photos | first attempt (contains bugs, kept for the learning history) |
| `06_flower_cnn_v2_augmentation_dropout.ipynb` | flower_photos | fixed version + data augmentation + dropout |

Datasets download automatically on first run (internet required).

**Requires:** tensorflow, matplotlib, scikit-learn, opencv, tensorflow-datasets (notebook 04)
