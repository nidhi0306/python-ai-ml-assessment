import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import RandomRotation, RandomFlip, RandomZoom

data_augmentation = Sequential([
    RandomRotation(0.055),
    RandomFlip("horizontal"),
    RandomZoom(0.2)
])

print(data_augmentation)