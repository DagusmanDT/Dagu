import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import streamlit.components.v1 as components
def add_watermark(image, watermark_text):
    img = Image.open(image)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((10, 10), watermark_text, font=font)
    return img
  def create_signature():
    html_code = """
    <canvas id="canvas" width="400" height="200"></canvas>
    <script>
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');
    var drawing = false;
    ctx.lineWidth = 5;
    
    canvas.addEventListener('mousedown', (e) => {
    drawing = true;
    ctx.beginPath();
    ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    });
    
    canvas.addEventListener('mousemove', (e) => {
    if (drawing) {
    ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    ctx.stroke();
    }
    });
    
    canvas.addEventListener('mouseup', () => {
    drawing = false;
    });
    </script>
    """
    components.html(html_code, height=250)
    st.title("Document Editor")
tab1, tab2 = st.tabs(["Watermark", "E-Signature"])

with tab1:
    image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if image:
        watermark_text = st.text_input("Enter watermark text")
        if st.button("Add Watermark"):
            img = add_watermark(image, watermark_text)
            st.image(img)

with tab2:
    st.write("Draw your signature:")
    create_signature()
    
