from pymongo import MongoClient
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

PASSWORD = os.getenv("PASSWORD")
CONNECTION_STRING = f"mongodb+srv://stevenzdragons:{PASSWORD}@aiatl.zehxy.mongodb.net/?retryWrites=true&w=majority&appName=AIAtl"

client = MongoClient(CONNECTION_STRING)  # Connect to MongoDB Atlas through Steven's key
db = client.myDatabase  # Create or get the user database

users_collection = db["users"]


def register_user(username, firstname, lastname, password, email, phone_number, identity, age, race, gender):
    user_info = {
        "user":username,
        "first_name":firstname,
        "last_name":lastname,
        "password":password,
        "email":email,
        "phone":phone_number,
        "identity":identity,
        "age":age,
        "race":race,
        "gender":gender
    }
    users_collection.insert_one(user_info)

db2 = client.myDatabase

symptoms_collection = db2["symptoms"]

def register_symptoms(symptoms):
    symptoms_info = {
        "symptoms":symptoms
    }
    symptoms_collection.insert_one(symptoms_info)
