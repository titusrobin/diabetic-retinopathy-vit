from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image, UnidentifiedImageError
from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
import pandas as pd
import logging
import os

# Initialize Flask app
app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load model and processor
processor = AutoImageProcessor.from_pretrained(
    "rafalosa/diabetic-retinopathy-224-procnorm-vit"
)
model = AutoModelForImageClassification.from_pretrained(
    "rafalosa/diabetic-retinopathy-224-procnorm-vit"
)


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            logging.error("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            logging.error("No selected file")
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            return redirect(url_for("predict", filename=filename))
    return render_template("upload.html")


@app.route("/predict/<filename>")
def predict(filename):
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    try:
        # Open the image file
        image = Image.open(filepath)

        # Use the image processor to convert the image to a PyTorch tensor
        inputs = processor(images=image, return_tensors="pt")

        # Perform inference
        outputs = model(**inputs)

        # Get the predicted class probabilities
        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=-1)
        categories = ["Mild", "Moderate", "Healthy", "Severe", "Proliferative"]
        probabilities_list = probabilities.tolist()[0]  # Example list of probabilities

        # Logging
        logging.info("Prediction completed successfully.")

        # Check if the retina is healthy
        health_probability = probabilities_list[categories.index("Healthy")]
        is_healthy = health_probability > 0.5
        health_message = "This retina is healthy !!!" if is_healthy else ""

        return render_template(
            "prediction.html",
            categories=categories,
            probabilities=probabilities_list,
            image_url=url_for("static", filename="uploads/" + filename),
            health_message=health_message,
        )

    except UnidentifiedImageError:
        return render_template(
            "error.html", error="This is not a standard retinopathy picture"
        )
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return render_template("error.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)

