from flask import Flask, render_template, request
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Limit GPU memory usage
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        print(e)

# Load the pre-trained model
model = load_model('../model/bungaku-dava.h5')

# Class names used during training
class_names = [
    'astilbe', 'bellflower', 'black_eyed_susan', 'calendula', 'california_poppy',
    'common_daisy', 'coreopsis', 'dandelion', 'iris', 'rose',
    'sunflower', 'tulip', 'water_lily'
]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.files['file']

        if uploaded_file.filename != '':
            # Save the file to a temporary location
            file_path = os.path.join('static/uploads', uploaded_file.filename)
            uploaded_file.save(file_path)

            # Load and preprocess the image
            img = image.load_img(file_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0

            # Make predictions
            predictions = model.predict(img_array)

            # Get the predicted class
            predicted_class = np.argmax(predictions[0])

            # Get the predicted class label
            predicted_label = class_names[predicted_class]

            # Provide the prediction to the HTML template
            return render_template('index.html', prediction=predicted_label, image_path=file_path)

    return render_template('index.html', prediction=None, image_path=None)


if __name__ == '__main__':
    app.run(debug=True)
