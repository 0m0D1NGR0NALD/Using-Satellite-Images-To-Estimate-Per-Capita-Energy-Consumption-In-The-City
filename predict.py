import tensorflow as tf
import numpy as np

model =  tf.keras.models.load_model('model.h5')

image_path = 'Freeetown_testing1.png' 

def preprocess(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path,target_size=(224,224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    preprocessed_img = tf.keras.applications.vgg16.preprocess_input(img_array)
    array = np.expand_dims(preprocessed_img,axis=0)
    return array

def predict(array):
    prediction = model.predict(array)
    results = np.argmax(prediction)
    if results == 0:
        output = print('Commercial Area')
    elif results == 1:
        output = print('Industrial Area')
    elif results == 2:
        output = print('Residential Area')
    return output


predict(preprocess(image_path))



