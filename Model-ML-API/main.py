from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import json

# initialize flask
app = Flask(__name__)

# load model
model = load_model('my_model.keras')
class_indices = {
    "Ear Mites": 0, "Eyelid Lump": 1, "Flea Allergy": 2, "Keratosis": 3, 
    "Nasal Discharge": 4, "Ringworm": 5, "Scabies": 6,
}

# load disease information from JSON file
with open('disease_info.json', 'r') as f:
    disease_info = json.load(f)

# function for image processing
def preprocess_image(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

# function for prediction with threshold
def predict_with_threshold(img_path, model, class_indices, threshold=0.65):
    img_array = preprocess_image(img_path)
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    confidence = prediction[0][predicted_class_index]

    if confidence < threshold:
        predicted_class = "Sorry, disease cannot be detected"
        disease_data = None
    else:
        predicted_class = list(class_indices.keys())[predicted_class_index]
        disease_data = disease_info.get(predicted_class, None)
    
    return predicted_class, disease_data

# main route
@app.route('/')
def home():
    return render_template('index.html') 

# endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    filepath = os.path.join('uploads', file.filename)
    file.save(filepath)

    threshold = 0.65
    predicted_class, disease_data = predict_with_threshold(filepath, model, class_indices, threshold)

    os.remove(filepath)

    result = {
        "predicted_class": predicted_class,
        "disease_info": disease_data
    }
    return jsonify(result)

# run the flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)