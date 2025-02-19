import cv2
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from keras.models import load_model
import numpy as np
import os

app = Flask(__name__)

MODEL_PATH = './pneumonia_model.h5'
model = load_model(MODEL_PATH)

def model_predict(img_path, model):
    img_size = 150
    img_arr = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    resized_arr = cv2.resize(img_arr, (img_size, img_size))
    resized_arr = resized_arr.reshape(-1, img_size, img_size, 1) / 255.0
    preds = model.predict(resized_arr)
    return preds

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(file.filename))
        file.save(file_path)

        preds = model_predict(file_path, model)
        os.remove(file_path)  # Clean up after prediction

        filename_without_ext = os.path.splitext(file.filename)[0]  # Remove file extension
        if preds[0][0] < 0.96:
            result_text = 'Pneumonia Detected'
        else:
            result_text = 'No Signs of Pneumonia'
        print(preds)
        return render_template('results.html', filename=filename_without_ext, result=result_text)

if __name__ == '__main__':
    app.run(debug=True)
