
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, GlobalAveragePooling2D
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import image_dataset_from_directory
from sklearn.metrics import f1_score


train_dir = '/gdrive/MyDrive/Resized'
validation_dir = '/gdrive/MyDrive/Resized'

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

validation_datagen = ImageDataGenerator(rescale=1./255)


train_dataset = image_dataset_from_directory(
    train_dir,
    labels='inferred',
    image_size=(224, 224),
    interpolation='nearest',
    batch_size=10,
    shuffle=True
)

validation_dataset = image_dataset_from_directory(
    validation_dir,
    labels='inferred',
    image_size=(224, 224),
    interpolation='nearest',
    batch_size=10,
    shuffle=False
)

base_model = DenseNet121(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

base_model.trainable = False

model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer=Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=10
)

