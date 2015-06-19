'''
Created on 22.05.2015

@author: Vladimir
@author: Marilena
'''

import bson
from bson.json_util import loads
import pymongo
import time

try:
    client = pymongo.MongoClient("141.22.29.77",27017)
    print ("Connected")
except (pymongo.errors.ConnectionFailure):
    print ("ERROR")
    
fileData = open('plz.data','r')
logData = open('log.log','a')

def writeToFile(s):
    logData.write(str(s) + '\n')
    
db = client.plz_db
collection = db.plz_collection
collection.drop()
for line in fileData:
    jsonData = loads(line)
    start = time.time()
    collection.insert_one(jsonData)
    stop = time.time()
    writeToFile('insert: ' + str(stop-start))

print(client.name)


