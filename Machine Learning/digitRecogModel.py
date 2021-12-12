#!/usr/bin/env python
# coding: utf-8

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
import seaborn as sn

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train/255
x_test = x_test/255


x_train.shape, len(y_test)


plt.matshow(x_train[1])


x_train_flattern = x_train.reshape(len(x_train), 28*28)
x_test_flattern = x_test.reshape(len(x_test), 28*28)


model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(28*28,), activation='sigmoid')
])


model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics='accuracy'
)


model.fit(x_train_flattern, y_train, epochs=5)


model.evaluate(x_test_flattern, y_test)


plt.matshow(x_test[0])


y_predict = model.predict(x_test_flattern)


y_predict[0]


np.argmax(y_predict[0])


y_predicted_labels = [np.argmax(i) for i in y_predict]


cm = tf.math.confusion_matrix(y_test, predictions=y_predicted_labels)


plt.figure(figsize=(10, 7))
sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')


model_with_layers = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(10, activation='sigmoid')
])
model_with_layers.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model_with_layers.fit(x_train, y_train, epochs=5)


model_with_layers.evaluate(x_test, y_test)


y_predict = model_with_layers.predict(x_test)


y_predicted_labels = [np.argmax(i) for i in y_predict]


cm = tf.math.confusion_matrix(y_test, predictions=y_predicted_labels)


plt.figure(figsize=(10, 7))
sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.plot()




