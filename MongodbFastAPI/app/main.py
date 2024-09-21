from typing import Union, List
from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
from dotenv import find_dotenv
#from routes import controller, routes
import os

config = find_dotenv(".env")

# Load environment variables
load_dotenv()

# MongoDB connection parameters
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")
cluster_uri = os.getenv("CLUSTER_URI")
collection_name = os.getenv("MONGODB_COLLECTION")
database_name = os.getenv("MONGODB_DATABASE")

username1 = ""
password1 = ""
cluster_uri1 = ""
collection_name1 = ""
database_name1 = ""


app = FastAPI()


@app.get("/")
def read_root():
    """
    Get details of all data from MongoDB.

    Returns:
        List[dict]: A list of records retrieved from MongoDB as JSON objects.
    """
    
    # Connect to MongoDB
    client = MongoClient(cluster_uri1)
    db = client[database_name1]
    collection = db[collection_name1]

    # Query the database to retrieve all records
    records = list(collection.find({}))
    # Convert ObjectId to string for serialization
    for record in records:
        record["_id"] = str(record["_id"])

    # Close the MongoDB client connection
    client.close()
    return records

#app.include_router(routes.router)

