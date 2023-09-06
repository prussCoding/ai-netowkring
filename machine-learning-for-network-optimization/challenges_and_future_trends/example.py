import tensorflow as tf

# Check if TensorFlow supports distributed training
if tf.config.experimental.list_physical_devices('GPU'):
    strategy = tf.distribute.MirroredStrategy()
    print('Number of devices: {}'.format(strategy.num_replicas_in_sync))

    # Define a simple neural network model
    with strategy.scope():
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
            tf.keras.layers.Dense(10, activation='softmax')
        ])

    # Compile the model
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # Load and preprocess your large dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Create a data input pipeline (e.g., tf.data.Dataset)

    # Use the fit method with distributed strategy
    model.fit(train_dataset, epochs=5)

else:
    print("Distributed training is not supported. Use a machine with GPUs.")
