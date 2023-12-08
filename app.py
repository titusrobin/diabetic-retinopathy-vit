from fastapi import FastAPI
from PIL import Image

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get('predict')
def predict():
    # Load model directly
    from transformers import AutoImageProcessor, AutoModelForImageClassification
    
    processor = AutoImageProcessor.from_pretrained("rafalosa/diabetic-retinopathy-224-procnorm-vit")
    model = AutoModelForImageClassification.from_pretrained("rafalosa/diabetic-retinopathy-224-procnorm-vit")

    # Specify the path to your image
    image_path = "path/to/your/image.jpeg"
    
    # Open the image file
    image = Image.open(image_path)
    print(f"Dimensions of the image is {image.shape}")

    print(model.predict(image))

    return model.predict(image)
