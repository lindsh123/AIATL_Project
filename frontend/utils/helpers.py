# utils/helpers.py

import streamlit as st
from PIL import Image
import os
from datetime import datetime
import uuid
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError

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
            st.image(logo, width=150)
        except FileNotFoundError:
            st.warning("Logo image not found.")
    with col2:
        st.markdown(
    """
    <h1 style='text-align: right; font-size: 36px; font-weight: bold;'>
        medmap.ai
    </h1>
    """,
    unsafe_allow_html=True
)
        st.markdown("<div style='text-align: right; font-size: 20px;'>the one-stop shop for chronic illness management</div>", 
        unsafe_allow_html=True
        )


def get_current_timestamp():
    return datetime.utcnow().isoformat()

def get_doctor_specialty(username):

    client = get_mongo_client()
    if client:
        db = client["myDatabase"]
        users_collection = db["users"]
        try:
            user = users_collection.find_one({"username": username.lower(), "role": "doctor"})
            if user:
                return user.get("speciality", None)
            else:
                return None
        except Exception as e:
            st.error(f"An error occurred while fetching doctor's specialty: {e}")
            return None
    else:
        st.error("Failed to connect to the database.")
        return None
def get_username_by_full_name(full_name):
    if not full_name:
        st.error("Full name must be provided.")
        return None
    try:
        client = get_mongo_client()
        if not client:
            st.error("MongoDB client is not available.")
            return None
        db = client["myDatabase"]       # Replace with your actual database name
        users_collection = db["users"]     # Replace with your actual collection name

        # Query to find the user by full_name (case-insensitive)
        user = users_collection.find_one({"full_name": {"$regex": f"^{full_name}$", "$options": "i"}})

        if user:
            return user.get("username", None)
        else:
            st.warning(f"No user found with the full name: {full_name}")
            return None

    except PyMongoError as e:
        st.error(f"An error occurred while fetching the username: {e}")
        return None
def get_mongo_client():
    try:
        client = MongoClient(MONGODB_URI)
        return client
    except Exception as e:
        st.error(f"Failed to connect to MongoDB: {e}")
        return None
