import tensorflow as tf
from tensorflow.keras import layers, models

# Define the neural network model
model = models.Sequential([
    layers.Dense(32, activation='relu', input_shape=(1,)),
    layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')
