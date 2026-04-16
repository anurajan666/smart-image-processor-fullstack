
from flask import Flask, request, send_file
from flask_cors import CORS
import cv2
import numpy as np
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/process", methods=["POST"])
def process_image():
    file = request.files["image"]
    operation = request.form.get("operation")

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(OUTPUT_FOLDER, "processed_" + file.filename)

    file.save(input_path)

    img = cv2.imread(input_path)

    if operation == "grayscale":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif operation == "blur":
        img = cv2.GaussianBlur(img, (15, 15), 0)
    elif operation == "edges":
        img = cv2.Canny(img, 100, 200)

    cv2.imwrite(output_path, img)

    return send_file(output_path, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True)
