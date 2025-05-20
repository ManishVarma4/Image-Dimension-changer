import streamlit as st
from PIL import Image
from io import BytesIO

def resize_image(image, new_width, new_height):
    return image.resize((new_width, new_height))

def convert_image_to_bytes(img):
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer
st.set_page_config(page_title="Image Resizer",layout="centered")
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>Image Resizer Tool</h1>", unsafe_allow_html=True)
st.write("Resize and download your image easily with custom dimensions.")
st.markdown("---")
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.subheader("Original Image")
    st.image(image, use_container_width=True)
    st.markdown("---")
    st.subheader("Resize Settings")

    col1, col2 = st.columns(2)
    with col1:
        new_width = st.number_input("New Width (px)", min_value=1, value=image.width)
    with col2:
        new_height = st.number_input("New Height (px)", min_value=1, value=image.height)
    st.write("")
    if st.button("🔄 Resize Image"):
        resized_img = resize_image(image, new_width, new_height)
        st.subheader("Resized Image")
        st.image(resized_img, use_container_width=True)
        img_bytes = convert_image_to_bytes(resized_img)
        st.download_button(
            label="💾 Download Resized Image",
            data=img_bytes,
            file_name="resized_image.png",
            mime="image/png"
        )
else:
    st.info("Please upload a JPG or PNG image file to begin.")
