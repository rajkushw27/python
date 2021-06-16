import numpy as np
from tensorflow import keras
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#import matplotlib.pyplot as plt

mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape, y_train.shape)

# normalize: 0,255 -> 0,1
x_train, x_test = x_train / 255.0, x_test / 255.0

# model
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10),
])

print(model.summary())

# another way to build the Sequential model:
#model = keras.models.Sequential()
# model.add(keras.layers.Flatten(input_shape=(28,28))
#model.add(keras.layers.Dense(128, activation='relu'))
# model.add(keras.layers.Dense(10))

# loss and optimizer
loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optim = keras.optimizers.Adam(learning_rate=0.001)
metrics = ["accuracy"]

model.compile(loss=loss, optimizer=optim, metrics=metrics)

# training
batch_size = 64
epochs = 5

model.fit(x_train, y_train, batch_size=batch_size,
          epochs=epochs, shuffle=True, verbose=2)

model.save("nn.h5")

# evaulate
print("Evaluate both model:")
model.evaluate(x_test, y_test, batch_size=batch_size, verbose=2)

new_model = keras.models.load_model("nn.h5")
new_model.evaluate(x_test, y_test, batch_size=batch_size, verbose=2)
