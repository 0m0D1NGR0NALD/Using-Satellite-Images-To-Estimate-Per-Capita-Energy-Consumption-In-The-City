import tensorflow as tf
import numpy as np

# Loading classification model
model =  tf.keras.models.load_model('model.h5')
# Loading image path of sample image
image_path = 'Freeetown_testing1.png' 

def preprocess(image_path):
    # Load path
    img = tf.keras.preprocessing.image.load_img(image_path,target_size=(224,224))
    # Convert image to array
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    # Preprocess image array using VVG16 default preprocessing function 
    preprocessed_img = tf.keras.applications.vgg16.preprocess_input(img_array)
    # Expand image dimensions
    array = np.expand_dims(preprocessed_img,axis=0)
    # Return aray
    return array

def predict(array):
    # Make model prediction on input array and store it
    prediction = model.predict(array)
    # Obtain max of prediction array
    results = np.argmax(prediction)
    # Using max output of results to categorize image
    if results == 0:
        # Commercial Area
        output = print('Commercial Area')
    elif results == 1:
        # Industrial Area
        output = print('Industrial Area')
    elif results == 2:
        # Residential Area
        output = print('Residential Area')
    # Return predicted area    
    return output

# Preprocessing image path and performing prediction
predict(preprocess(image_path))
