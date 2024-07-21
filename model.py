import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load your trained model
model = load_model('trained.h5')

def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(140, 140))  # adjust target size as per your model's input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # normalize if required

    predictions = model.predict(img_array)
    
    # Ensure the class order matches the training labels
    classes = ['Normal', 'Lung_Opacity', 'COVID', 'Viral Pneumonia']
    
    predicted_class = classes[np.argmax(predictions)]

    return predicted_class