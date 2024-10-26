from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://stevenzdragons:hALALGUYS@aiatl.zehxy.mongodb.net/?retryWrites=true&w=majority&appName=AIAtl"

client = MongoClient(CONNECTION_STRING)  # Connect to MongoDB Atlas through Steven's key
db = client.myDatabase  # Create or get the user database

doctors_collection = db["doctors"]


def register_doctor(user, doctor_first, doctor_last, email, field):
    doctor_info = {
        "patient":user,
        "first_name": doctor_first,
        "last_name": doctor_last,
        "email":email,
        "field":field
    }
    doctors_collection.insert_one(doctor_info)

def remove_doctor(user, field):
    result = doctors_collection.delete_one({"patient":user, "field":field})
        
        # Check if a document was deleted
    if result.deleted_count > 0:
        return "Document deleted successfully."
    else:
        return "No document found matching the criteria."

def find_doctor(user, field):
    doc = doctors_collection.find({"user": user, "field":field})
    if not doc:
        return f"You don't have a {field} doctor currently registered."
    else:
        return doc["email"]
