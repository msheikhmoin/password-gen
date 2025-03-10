import streamlit as st
import random
import string
import os

# Page Config
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

# Custom Styling with Glassmorphism, Neon Effect & Blue Gradient Shade
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #000000 30%, #002366 100%) !important;
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            color: #00ffff;
            text-shadow: 0px 0px 15px rgba(0, 255, 255, 0.8);
        }
        /* Blue Slider */
        .stSlider > div > div > div {
            background: linear-gradient(90deg, #0066ff, #00ccff) !important;
            border-radius: 8px;
        }
        /* Blue Gradient Button */
        .stButton > button {
            background: linear-gradient(90deg, #002366, #0052cc);
            color: white;
            font-size: 20px;
            padding: 12px 24px;
            border-radius: 12px;
            border: none;
            cursor: pointer;
            box-shadow: 0px 5px 20px rgba(0, 82, 204, 0.6);
            transition: all 0.3s ease-in-out;
        }
        .stButton > button:hover {
            transform: scale(1.1);
            box-shadow: 0px 8px 25px rgba(0, 82, 204, 0.8);
        }
        .password-box {
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            padding: 15px;
            border-radius: 15px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #00ff99;
            text-shadow: 0px 0px 10px rgba(0, 255, 153, 0.8);
            box-shadow: 0px 5px 20px rgba(0, 255, 153, 0.6);
        }
        /* Blue Radio Buttons */
        div[data-testid="stRadio"] label {
            color: #00ccff !important;
            font-size: 18px !important;
            font-weight: bold !important;
        }
        div[data-testid="stRadio"] div[role="radiogroup"] > label > div {
            background: linear-gradient(90deg, #0066ff, #00ccff) !important;
            border-radius: 50%;
        }
        /* Transparent Footer with Gradient Text */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            padding: 10px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            background: transparent;
        }
        .footer-text {
            background: linear-gradient(90deg, #0000ff, #0099ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
            text-shadow: 0px 0px 15px rgba(255, 255, 255, 0.8);
        }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<p class='title'>🔐 Password Generator</p>", unsafe_allow_html=True)

# ✅ Image Path Handling
current_dir = os.path.dirname(os.path.abspath(__file__))  
image_path = os.path.join(current_dir, "images", "galax.gif")  

# ✅ Show Image
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.warning(f"⚠️ Image '{image_path}' not found! Make sure it exists.")

# Password Length
length = st.slider("Select Password Length", min_value=6, max_value=20, value=12)

# Password Type
password_type = st.radio("Select Password Type", ("Digits Only", "Digits + Special Characters"))

# ✅ Password Generation Function
def generate_password(length, use_special_chars):
    characters = string.digits + (string.punctuation if use_special_chars else "")
    return ''.join(random.choice(characters) for _ in range(length))

# ✅ Generate Password Button
if st.button("Generate Password"):
    password = generate_password(length, password_type == "Digits + Special Characters")
    st.markdown(f"<p class='password-box'>🔑 {password}</p>", unsafe_allow_html=True)

# ✅ Transparent Footer with Gradient Text
st.markdown("<div class='footer'><span class='footer-text'> Made by Moin Sheikh</span></div>", unsafe_allow_html=True)