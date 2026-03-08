import os
import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Upload folder setup
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load trained model
model = load_model("plant_model.h5")

# IMPORTANT:
# Make sure this order matches your dataset folder order
class_names = [
    "Potato Early Blight",
    "Potato Late Blight",
    "Potato Healthy",
    "Tomato Bacterial Spot",
    "Tomato Early Blight",
    "Tomato Late Blight",
    "Tomato Leaf Mold",
    "Tomato Powdery Mildew"
]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    img_path = None

    if request.method == "POST":
        file = request.files["file"]

        if file:
            # Secure filename (removes spaces & special chars)
            filename = secure_filename(file.filename)

            img_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(img_path)

            # Prepare image for prediction
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0

            # Predict
            predictions = model.predict(img_array)

            predicted_index = np.argmax(predictions)
            prediction = class_names[predicted_index]

            confidence = round(np.max(predictions) * 100, 2)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        img_path=img_path
    )

if __name__ == "__main__":
    app.run(debug=True)