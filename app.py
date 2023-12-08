import streamlit as st
from PIL import Image
# from transformers import AutoImageProcessor, AutoModelForImageClassification
# import torch

## Load model and processor
# processor = AutoImageProcessor.from_pretrained("rafalosa/diabetic-retinopathy-224-procnorm-vit")
# model = AutoModelForImageClassification.from_pretrained("rafalosa/diabetic-retinopathy-224-procnorm-vit")

# Streamlit app
st.title("Image Classification App")

# Upload image through Streamlit
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file is not None:
    # Open the image file
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Predict button
    if st.button("Predict"):
        # Use the image processor to convert the image to a PyTorch tensor
        # inputs = processor(images=image, return_tensors="pt")

        # # Perform inference
        # outputs = model(**inputs)

        # # Get the predicted class probabilities
        # logits = outputs.logits
        # probabilities = torch.nn.functional.softmax(logits, dim=-1)

        # # Get the predicted label
        # predicted_label = torch.argmax(probabilities, dim=-1).item()

        # Display prediction results
        st.write(f"Predicted Label: {predicted_label}")
        st.write(f"Class Probabilities: {probabilities.tolist()[0]}")
