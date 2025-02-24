# 🩺 Pneumonia Detection Flask App  

This is a **Flask-based web application** that uses a **custom deep learning model** trained on top of VGG-16 to predict whether an uploaded chest X-ray image shows signs of **pneumonia**.  

The model is trained using **NIH's Chest X-ray Dataset**: [NIH Chest X-ray Dataset](https://cloud.google.com/healthcare-api/docs/resources/public-datasets/nih-chest).

---

## 📌 Features
- 🌐 **Web-based UI**
- 🧠 Uses a pre-trained **CNN model** for pneumonia detection  
- 📸 **Image Processing** – Automatically resizes & normalizes images before prediction  
- 🎨 **Color-coded Results** – Pneumonia (Red) 🔴 | Normal (Green) 🟢  
- ⚡ **Accuracy: 92.6%**

---

## 🚀 Installation & Setup  
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/chirag-bhardwaj/xray-app.git
cd xray-app
```

### **2️⃣ Create a Virtual Environment (Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the Flask App**
```sh
python app.py
```
✔️ Open **http://127.0.0.1:5000/** in your browser to upload an X-ray image.

---

## 📂 Project Structure
```
xray-app/
│── pneumonia_model.h5    # Trained deep learning model
│── app.py                # Main Flask application
│── requirements.txt      
│── README.md            
│── templates/
│   ├── index.html        # Upload page
│   ├── results.html      # Results page (with red/green alerts)
│   ├── styles.css        
│   ├── script.js         
```

---

## 📊 Example Predictions  
<table> 
  <tr> 
    <td align="center"> 
      <img src="https://github.com/user-attachments/assets/e44aca71-c666-47d0-93b9-36fdfee3bd49" width="100"> 
      <br> ✅ No Pneumonia
    </td> 
    <td align="center"> 
      <img src="https://github.com/user-attachments/assets/19355d73-137c-4030-8638-7d005ede697a" width="100"> 
      <br> 🚨 Pneumonia Detected 
    </td> 
  </tr> 
</table>

---

## 🛠 Dependencies  
- **Python 3.10**  
- **Flask**  
- **TensorFlow 2.9**  
- **Keras 2.9**  
- **OpenCV (cv2)**  
- **NumPy 1.23.5**  

---

## 🤝 Contributing  
💡 Have ideas for improvement? **Feel free to open an issue or submit a pull request!**  

---

### **📢 If you found this useful, give it a ⭐ on GitHub!**  
