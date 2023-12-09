import tensorflow as tf
from keras.models import load_model

# Load the Keras model
model = load_model('model/bungaku-dava.h5')

# Convert the Keras model to TFLite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model to a file
with open('model/bungaku-dava.tflite', 'wb') as f:
    f.write(tflite_model)
