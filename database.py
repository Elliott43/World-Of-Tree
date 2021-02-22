# MongoDB username: epc
# MongoDB password: ul7AoWc4eGDH7pSY
# MongoDB app ID: tree-oooxv
# Connect code: mongodb+srv://epc:ul7AoWc4eGDH7pSY@testing.oborm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
import pymongo

client = pymongo.MongoClient("mongodb+srv://epc:ul7AoWc4eGDH7pSY@testing.oborm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["database"]

def save(key, data):
    global db
    cl = db[key]

    cl.inser_one(data)