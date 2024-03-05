import streamlit as st
from PIL import Image, ImageOps, ImageEnhance

# Function to posterize an image
def posterize_image(image, bits):
    return ImageOps.posterize(image, bits)

# Function to save processed image
def save_image(image, filename):
    image.save(filename)

# Main UI
st.title('Image Toolbox App')

# File uploader allows user to add their own image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "bmp"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Posterize settings
    st.subheader("Posterize")
    bits = st.slider('Select bit depth:', 1, 8, 4)
    if st.button('Apply Posterize'):
        processed_image = posterize_image(image, bits)
        st.image(processed_image, caption='Posterized Image', use_column_width=True)

