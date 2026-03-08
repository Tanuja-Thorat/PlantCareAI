# 🌿 PlantCareAI – Plant Disease Detection System

PlantCareAI is an AI-powered web application that detects plant diseases from leaf images using deep learning.  
Users can upload a plant leaf image, and the system predicts the disease and provides detailed information such as symptoms, causes, prevention, and treatment.

This project uses a Convolutional Neural Network (CNN) model trained on the PlantVillage dataset and is deployed using a Flask web application.

---

## 🚀 Features

- 🌱 Upload plant leaf images for disease detection
- 🤖 Deep learning model for accurate prediction
- 📊 Displays disease name and confidence score
- 📖 Shows symptoms, causes, prevention, and treatments
- 🌐 Simple and user-friendly web interface

---

## 🧠 Tech Stack

**Backend**
- Python
- Flask

**Machine Learning**
- TensorFlow
- Keras
- MobileNetV2 (Transfer Learning)

**Frontend**
- HTML
- CSS
- JavaScript
- Font Awesome

**Dataset**
- PlantVillage Dataset

---

## 📂 Project Structure


PlantCareAI
│
├── app.py # Flask web application
├── train.py # Model training script
├── plant_model.h5 # Trained model
├── templates/ # HTML templates
│ └── index.html
│
├── static/ # CSS, JS, images
│
└── dataset/ # Training dataset (not uploaded to GitHub)


---

## ⚙️ Installation

1. Clone the repository


git clone https://github.com/Tanuja-Thorat/PlantCareAI.git


2. Go to project directory


cd PlantCareAI


3. Install dependencies


pip install -r requirements.txt


4. Run the Flask app


python app.py


5. Open in browser


http://127.0.0.1:5000


---

## 📸 How It Works

1. User uploads a plant leaf image  
2. Image is preprocessed for the model  
3. CNN model predicts the plant disease  
4. The system displays disease information and treatment suggestions

---

## 📊 Model Details

- Architecture: MobileNetV2 (Transfer Learning)
- Image Size: 224 × 224
- Dataset: PlantVillage
- Number of Classes: 15 plant disease categories

---

## ⚠️ Note

Due to GitHub file size limitations, the dataset and trained model file are not included in this repository.

---

## 👩‍💻 Author

**Tanuja Thorat**

AI / Machine Learning Project
