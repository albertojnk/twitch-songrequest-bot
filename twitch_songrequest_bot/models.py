import os
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

client = MongoClient(os.environ["DATABASE_URL"])
db=client['songrequestbot']
collection = db['songrequestbot']
