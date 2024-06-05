import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

def evaluar_cnn():
    model = tf.keras.models.load_model('modelo_redes.h5')
    def preprocess_image(img_path, target_size):
        img = image.load_img(img_path, target_size=target_size)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalizar los valores de los píxeles
        return img_array

    img_path = './pred/predicción.jpg'
    target_size = (128, 128) 

    img_array = preprocess_image(img_path, target_size)

    predictions = model.predict(img_array)

    max_prob = max(predictions[0])

    return predictions