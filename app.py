import os
import cv2
import numpy as np
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from keras.models import load_model

# Initialize Flask app
app = Flask(__name__)

# Path to the model
MODEL_PATH = './pneumonia_model.h5'

# Load the trained model
try:
    model = load_model(MODEL_PATH)
    print("✅ Model loaded successfully!")
    print("🔍 Model expected input shape:", model.input_shape)
except Exception as e:
    print("❌ Error loading model:", e)
    exit(1)  # Exit if model fails to load

# Function to process and predict
def model_predict(img_path, model):
    img_size = 150
    img_arr = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if img_arr is None:
        raise ValueError(f"❌ Error loading image: {img_path}")

    resized_arr = cv2.resize(img_arr, (img_size, img_size))

    # Normalize image (VERY IMPORTANT FIX)
    resized_arr = resized_arr.astype('float32') / 255.0

    resized_arr = np.expand_dims(resized_arr, axis=-1)  # Add channel dimension
    resized_arr = np.expand_dims(resized_arr, axis=0)   # Add batch dimension

    # Debugging: Print final input shape and pixel values
    print("📊 Final input shape:", resized_arr.shape)  # Should be (1, 150, 150, 1)
    print("🔢 Sample pixel values:", resized_arr[0, :, :, 0].flatten()[:10])  # Print some pixel values

    preds = model.predict(resized_arr)
    print("📈 Model Prediction:", preds)  # Debugging output to see raw model output

    return preds

# Home route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return '❌ No file part in the request'

    file = request.files['file']
    if file.filename == '':
        return '❌ No selected file'

    if file:
        basepath = os.path.dirname(__file__)
        upload_folder = os.path.join(basepath, 'uploads')
        os.makedirs(upload_folder, exist_ok=True)  # Ensure uploads folder exists

        file_path = os.path.join(upload_folder, secure_filename(file.filename))
        file.save(file_path)

        preds = model_predict(file_path, model)

        os.remove(file_path)  # Remove file after processing

        # Debugging: Print model prediction value
        print("🔍 Raw Prediction Value:", preds[0][0])

        # Adjust threshold if necessary
        if preds[0][0] < 0.5:  # FIX: Changed from 0.96 to 0.5
            result_text = '🚨 Pneumonia Detected'
            color_class = "alert-danger"  # Red for Pneumonia
        else:
            result_text = '✅ No Signs of Pneumonia'
            color_class = "alert-success"  # Green for Normal

        return render_template('results.html', filename=file.filename, result=result_text, color_class=color_class)

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
    
