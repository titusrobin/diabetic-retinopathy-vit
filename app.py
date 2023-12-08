from fastapi import FastAPI
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get('/predict')
def predict():
    
    # Load model and processor
    processor = AutoImageProcessor.from_pretrained("rafalosa/diabetic-retinopathy-224-procnorm-vit")
    model = AutoModelForImageClassification.from_pretrained("rafalosa/diabetic-retinopathy-224-procnorm-vit")

    # Specify the path to your image
    image_path = "image.jpeg"

    # Open the image file
    image = Image.open(image_path)

    # Use the image processor to convert the image to a PyTorch tensor
    inputs = processor(images=image, return_tensors="pt")

    # Perform inference
    outputs = model(**inputs)

    # Get the predicted class probabilities
    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)

    # Get the predicted label
    predicted_label = torch.argmax(probabilities, dim=-1).item()

    return predicted_label, probabilities.tolist()[0]
