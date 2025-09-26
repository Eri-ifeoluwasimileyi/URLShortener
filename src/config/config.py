from pymongo import MongoClient


URI = 'mongodb://localhost:27017/'
DB_NAME = 'url_shortener'
COLLECTION_NAME = 'urls'

client = MongoClient(URI)
db = client[DB_NAME]
url_collection = db[COLLECTION_NAME]
