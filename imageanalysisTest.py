import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras import backend as K
from tensorflow.keras.models import load_model
import numpy as np

def imageAnalyze(imageName):
    img_width, img_height = 155, 155

    #loadModel path needs to be updated
    loadModel = tf.keras.models.load_model('Image_model/assets')

    loadImage = load_img("temp/" + imageName, target_size=(img_width, img_height))
    arrImge = image.img_to_array(loadImage)
    predImage = np.expand_dims(arrImge, axis = 0)
    prediction = loadModel.predict_classes(predImage)

    #0 is Negative is before p (Positive)
    if prediction[0] == 0:
        return "negative. "
    else:
        return "positive. "
