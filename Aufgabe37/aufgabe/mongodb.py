'''
Created on 22.05.2015

@author: Vladimir
'''
import pymongo

try:
    client = pymongo.MongoClient("141.22.29.77",27017)
    print ("Connected")
except (pymongo.errors.ConnectionFailure):
    print ("ERROR")
    
fileData = open('plz.data','r')

print(client.test.name)