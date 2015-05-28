'''
Created on 28.05.2015

@author: marilena
'''
import pymongo
import bson
from bson.json_util import loads

try:
    client = pymongo.MongoClient("141.22.29.77",27017)
    print ("Connected")
except (pymongo.errors.ConnectionFailure):
    print ("ERROR")
    

db = client.vereine_db
db.fussball.drop()
fileData = open('sinndeslebens.data','r')
for line in fileData:
    print(line)
    jsonData = loads(line)
    db.fussball.insert_one(jsonData)

