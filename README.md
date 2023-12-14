# Flower Classification Model using MobileNetV2

## Overview

The script focuses on developing a flower classification model using a pre-trained MobileNetV2 architecture with TensorFlow and Keras. The workflow involves data preprocessing, model building, training, and conversion to TensorFlow Lite format.

## Data Preparation
- **Dataset:** [Flower Classification Dataset](https://www.kaggle.com/datasets/marquis03/flower-classification/code)
- Training and validation data directories are specified.
- Image dimensions are set to 256x256 pixels.
- Batch size for training is set to 32.
- `ImageDataGenerator` is used for data augmentation on the training set, including rescaling, shearing, zooming, and horizontal flipping.

## Data Generators

Data generators are created for training and validation using the specified directories, target size, batch size, and categorical class mode.

## Model Building

- MobileNetV2, pre-trained on ImageNet, is loaded as the base model.
- The base model layers are frozen to retain pre-trained weights.
- A Sequential model is built by adding:
  - Base model
  - GlobalAveragePooling2D layer
  - Dense layer with 128 units and ReLU activation
  - Dropout layer with a dropout rate of 0.5
  - Final Dense layer with 14 units (number of classes) and softmax activation.

## Model Compilation

The model is compiled with the Adam optimizer, categorical crossentropy loss, and accuracy as the metric.

## Model Training

- The model is trained using the `fit` method on the training generator.
- The number of epochs is set to 10.
- Validation data is provided to monitor model performance on unseen data.

## TensorFlow Lite Conversion

The trained model is converted to TensorFlow Lite format using the `TFLiteConverter`.
The converted model is saved to a .tflite file in the specified directory.

## Conclusion

The script successfully develops and trains a flower classification model using transfer learning with MobileNetV2. The resulting model is converted to TensorFlow Lite, making it suitable for deployment on resource-constrained environments, such as mobile devices or edge devices.

**Note:** Ensure that the directory paths and the number of classes in the final Dense layer match your specific dataset and requirements.