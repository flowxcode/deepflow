import tensorflow as tf
import numpy as np

print(tf.__version__)
print("--------------")

# Load and prepare data, convert labels to one-hot encoding

housing = tf.keras.datasets.boston_housing
(x_train, y_train), (x_test, y_test) = housing.load_data()

print(x_train)
np.set_printoptions(suppress=True)
print(x_train)



xasdf = x_train.shape







x_train, x_test= x_train/ 255.0, x_test/ 255.0
y_train= tf.keras.utils.to_categorical(y_train, num_classes=10)
y_test= tf.keras.utils.to_categorical(y_test, num_classes=10)

print(x_train)
print(y_train)
print(y_test)

# Configure the model layers
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(100, activation='relu'))
model.add(tf.keras.layers.Dense(50, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
model.summary()

# Configure the model training procedure
model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.01, momentum=0.9),
  loss=tf.keras.losses.CategoricalCrossentropy(from_logits=False),
  metrics=['accuracy'])
model.fit(x_train, y_train, epochs=20, batch_size=64, validation_split=0.2)
model.evaluate(x_test, y_test, batch_size=64)

