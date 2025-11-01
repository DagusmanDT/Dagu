import streamlit as st
from streamlit_draw import st_canvas

def create_signature():
    st.write("Draw your signature:")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=5,
        stroke_color="#000000",
        background_color="#ffffff",
        height=200,
        width=400,
        drawing_mode="freedraw",
        key="canvas",
    )
    return canvas_result

signature = create_signature()
