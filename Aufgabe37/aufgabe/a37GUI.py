'''
Created on 25.05.2015

@author: marilena
'''
import pymongo
import json

client = pymongo.MongoClient("141.22.29.77",27017)
  
fileData = open('plz.data','r')

def getZipByCity(com):
    for item in client.my_db.find( { "city" : "com" } )
        print item
        
wFlag = True        
        
def work():
    com = input('Bitte Stadt eingeben:')
        getZipByCity(com)
        print()
    
        
while wFlag:
    work()  