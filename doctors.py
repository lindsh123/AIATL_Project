from pymongo import MongoClient
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

PASSWORD = os.getenv("PASSWORD")
CONNECTION_STRING = f"mongodb+srv://stevenzdragons:{PASSWORD}@aiatl.zehxy.mongodb.net/?retryWrites=true&w=majority&appName=AIAtl"

client = MongoClient(CONNECTION_STRING)  # Connect to MongoDB Atlas through Steven's key
db = client.myDatabase  # Create or get the user database

doctors_collection = db["doctors"]


def register_doctor(user, doctor_first, doctor_last, email, field):
    doctor_info = {
        "user":user,
        "first_name": doctor_first,
        "last_name": doctor_last,
        "email":email,
        "field":field
    }
    doctors_collection.insert_one(doctor_info)

def remove_doctor(user, field):
    result = doctors_collection.delete_one({"user":user, "field":field})
        
        # Check if a document was deleted
    if result.deleted_count > 0:
        return "Document deleted successfully."
    else:
        return "No document found matching the criteria."

def find_doctor(user, field):
    doc = doctors_collection.find({"user": user, "field":field})
    for doc1 in doc:
        if not doc1:
            return f"You don't have a {field} doctor currently registered."
        else:
            return [doc1["last_name"], doc1["email"]]

#print(find_doctor("a","General"))
#register_doctor("a","Steven", "Zhou", "szhou390@gatech.edu", "General")
