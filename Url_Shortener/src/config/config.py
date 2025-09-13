from pymongo import MongoClient

#confg
URI = 'mongodb://localhost:27017/'
DB_NAME = 'url_shortener'
COLLECTION_NAME = 'urls'

# config connection
client = MongoClient(URI)
db = client[DB_NAME]
url_collection = db[COLLECTION_NAME] #the table that keeps all short and long link
