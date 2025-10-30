import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def add_watermark(image, watermark_text):
    img = Image.open(image)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((10, 10), watermark_text, font=font)
    return img

st.title("Watermark Application")
image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if image:
    watermark_text = st.text_input("Enter watermark text")
    if st.button("Add Watermark"):
        img = add_watermark(image, watermark_text)
        st.image(img)
