# -*- coding: utf-8 -*-
"""prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hXf9EtcO2Yepic9e17hW8d-jPaAVxyE6
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def get_img_array(img_path, size):
   img = load_img(img_path, target_size=size)
   array = img_to_array(img)
   # расширяем размерность для преобразования массива в пакеты
   array = np.expand_dims(array, axis=0)
   return array

def predictions(img_path):
  img_size = (224, 224)
  EfficientNet_model = load_model('EfficientNet.h5')

  preprocess_input = tf.keras.applications.efficientnet.preprocess_input
  img_array = preprocess_input(get_img_array(img_path, size=img_size))
  pred = EfficientNet_model.predict(img_array)
  if pred < 0.5:
    return 'изображение сгенерировано нейросетью'
  else:
    return 'изображение создано человеком'