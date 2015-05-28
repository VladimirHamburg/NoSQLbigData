'''
Created on 22.05.2015

@author: Vladimir
@author: Marilena
'''
import json
import pymongo


try:
    client = pymongo.MongoClient("141.22.29.77",27017)
    print ("Connected")
except (pymongo.errors.ConnectionFailure):
    print ("ERROR")
    
fileData = open('plz.data','r')
db = client.test_db
collection = db.test_collection
for line in fileData:
    jsonData = json.loads(line)
    collection.insert(line)


print(client.name)


