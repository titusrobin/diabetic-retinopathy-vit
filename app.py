import streamlit as st
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load model and processor
processor = AutoImageProcessor.from_pretrained("rafalosa/diabetic-retinopathy-224-procnorm-vit")
model = AutoModelForImageClassification.from_pretrained("rafalosa/diabetic-retinopathy-224-procnorm-vit")

# Streamlit app
st.title("RetinaScope")

# Upload image through Streamlit
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file is not None:
    logging.info("Image uploaded successfully.")

    # Open the image file
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Predict button
    if st.button("Predict"):
        logging.info("Starting prediction.")
        
        try:
            # Use the image processor to convert the image to a PyTorch tensor
            inputs = processor(images=image, return_tensors="pt")

            # Perform inference
            outputs = model(**inputs)

            # Get the predicted class probabilities
            logits = outputs.logits
            probabilities = torch.nn.functional.softmax(logits, dim=-1)

            # Your other code remains the same...

            # Assuming probabilities_list contains the probabilities for each category
            categories = ["Mild", "Moderate", "Healthy", "Severe", "Proliferative"]
            probabilities_list = probabilities.tolist()[0]  # Example list of probabilities
            data = pd.DataFrame(
                probabilities_list, index=categories, columns=["probability"]
            )

            # Use Streamlit to create a bar chart
            st.bar_chart(data)

            logging.info("Prediction completed successfully.")
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            st.error("An error occurred during prediction.")

# Complete
