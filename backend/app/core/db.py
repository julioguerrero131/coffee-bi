from pymongo import MongoClient
from app.core.config import settings

# Create a global MongoDB client
client = MongoClient(settings.MONGO_URI)

# Select the database dynamically using the environment variable
db = client[settings.MONGO_DB]