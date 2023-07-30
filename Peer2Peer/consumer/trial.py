import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Peer2Peer"]
Cart = mydb["Container"]

Cart.delete_many({})