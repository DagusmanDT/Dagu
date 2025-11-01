import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("E-Signature Application")

if st.button("Create Signature"):
    with st.form("signature_form"):
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
        submitted = st.form_submit_button("Submit Signature")
        if submitted and canvas_result.image_data is not None:
            st.write("Signature:")
            st.image(canvas_result.image_data)
