from pymongo import MongoClient

try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['business']
    collection = db['businessdb1']
    print("Connected to MongoDB successfully!")
    print("Documents in collection:", collection.count_documents({}))
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")