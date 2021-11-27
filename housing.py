import tensorflow as tf
import numpy as np

print(tf.__version__)
print("--------------")

# Load and prepare data, convert labels to one-hot encoding

housing = tf.keras.datasets.boston_housing
(x_train, y_train), (x_test, y_test) = housing.load_data()

#print(x_train)
np.set_printoptions(suppress=True)
#print(x_train)

#print("CRIM:", x_train[:,0])
print(type(x_train[:,0]))
#print(np.max(x_train[:,0]))

#print("ZN:", x_train[:,1])
# print("indus:", x_train[:,2])
# print("age:", x_train[:,6])

# print("dis:", x_train[:,7])
# print(np.max(x_train[:,7]))

#rad

# print("tax:", x_train[:,9])

print("medv:", y_train)

xasdf = x_train.shape




