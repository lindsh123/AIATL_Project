from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://stevenzdragons:hALALGUYS@aiatl.zehxy.mongodb.net/?retryWrites=true&w=majority&appName=AIAtl"

client = MongoClient(CONNECTION_STRING)  # Connect to MongoDB Atlas through Steven's key
db = client.myDatabase  # Create or get the user database

users_collection = db["users"]


def register_user(username, password, email, phone_number):
    user_info = {
        "user":username,
        "password":password,
        "email":email,
        "phone":phone_number
    }
    users_collection.insert_one(user_info)
}