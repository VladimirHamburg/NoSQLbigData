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
my_db = db.my_db
for line in fileData:
    jsonData = json.loads(line)
    my_db.insert(line)


print(client.name)


