'''
Created on 25.05.2015

@author: marilena
'''
import pymongo
import json

client = pymongo.MongoClient("141.22.29.77",27017)
  
fileData = open('plz.data','r')

def getCityByZip(com):
    for item in client.my_db.find({ _id: com }):
        print item
        
