import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import streamlit.components.v1 as components

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
