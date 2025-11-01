import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("E-Signature Application")

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=5,
    stroke_color="#000000",
    background_color="#ffffff",
    height=400,
    width=600,
    drawing_mode="freedraw",
    key="canvas",
)

# Display the canvas
if canvas_result.image_data is not None:
    st.write("Signature:")
    st.image(canvas_result.image_data)
