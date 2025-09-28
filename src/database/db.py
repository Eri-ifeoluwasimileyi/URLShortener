from pymongo import MongoClient
from pymongo.synchronous.database import Database

from src.configuration.config import Config

client: MongoClient = None
db: Database = None


def connect_db():
    global client, db
    client = MongoClient(Config.DATABASE_URI)
    print("Connected to MongoDB", client)
    db = client.get_database(Config.DATABASE_NAME)
    print("Connected to MongoDB", db)


def get_db():
    global db
    if db is None:
        raise RuntimeError("Database not initialized.")
    return db

connect_db()
print(get_db())

