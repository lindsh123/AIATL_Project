# utils/helpers.py

import streamlit as st
from PIL import Image
import os
from datetime import datetime
import uuid
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = "mongodb+srv://stevenzdragons:hALALGUYS@aiatl.zehxy.mongodb.net/?retryWrites=true&w=majority&appName=AIAtl"


def load_css(file_name):
    css_path = os.path.join("assets", file_name)
    try:
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file `{file_name}` not found.")


def display_header():
    col1, col2 = st.columns([1, 3])
    with col1:
        logo_path = os.path.join("assets", "logo.png")
        try:
            logo = Image.open(logo_path)
            st.image(logo, width=100)
        except FileNotFoundError:
            st.warning("Logo image not found.")
    with col2:
        st.title("Healthcare Management System")


def get_current_timestamp():
    return datetime.utcnow().isoformat()


def get_mongo_client():
    try:
        client = MongoClient(MONGODB_URI)
        return client
    except Exception as e:
        st.error(f"Failed to connect to MongoDB: {e}")
        return None
