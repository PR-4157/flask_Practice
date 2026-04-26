from pymongo import MongoClient

client = MongoClient("mongodb+srv://rahul_3077:*********@rahulmongodb.zh7l1fq.mongodb.net/")

try:
    client.admin.command('ping')
    print("MongoDB Connected Successfully!")
except Exception as e:
    print("Connection Failed:", e)
