import tensorflow as tf
from keras import layers
from keras.preprocessing.image import ImageDataGenerator
import os

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

data_dir = 'dataset'
training_dir = os.path.join(data_dir, 'train')
validation_dir = os.path.join(data_dir, 'val')

train_datagen = ImageDataGenerator(
    rotation_range=40,
    shear_range=0.2,
    rescale=1 / 255.0,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest',
)

val_datagen = ImageDataGenerator(rescale=1 / 255.0)

train_generator = train_datagen.flow_from_directory(
    training_dir,
    target_size=(224, 224),
    shuffle=True,
    batch_size=32,
    class_mode='categorical'
)

val_generator = val_datagen.flow_from_directory(
    validation_dir,
    target_size=(224, 224),
    shuffle=False,
    batch_size=32,
    class_mode='categorical'
)

model = tf.keras.Sequential([
    layers.Conv2D(16, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D(2, 2),
    layers.BatchNormalization(),
    layers.Conv2D(16, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.BatchNormalization(),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.BatchNormalization(),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.BatchNormalization(),
    layers.Conv2D(128, (3, 3), activation='relu'),  # Increase complexity
    layers.MaxPooling2D(2, 2),
    layers.BatchNormalization(),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),  # Add L2 regularization
    layers.Dropout(0.5),  # Adjust dropout rate
    layers.Dense(13, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(
    train_generator,
    epochs=20,  # Adjust the number of epochs
    validation_data=val_generator
)

model.save('model/bungaku.h5')
