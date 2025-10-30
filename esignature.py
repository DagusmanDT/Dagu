import streamlit as st
from PIL import Image, ImageDraw

def create_signature():
    st.write("Draw your signature:")
    st.write("Click and drag to draw, press 'R' to reset")
    drawing_canvas = st.canvas()
    signature = drawing_canvas.get_signature()
    return signature

st.title("E-Signature Application")
if st.button("Create Signature"):
    signature = create_signature()
    if signature:
        st.write("Signature:")
        st.image(signature)
