import os

from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = os.environ.get('MONGO')
uri = "mongodb+srv://Shivam:AshTreeko123@cluster0.fgsaetf.mongodb.net/?retryWrites=true&w=majority"
myclient = MongoClient(uri, server_api=ServerApi('1'))
mydb = myclient["Peer2Peer"]