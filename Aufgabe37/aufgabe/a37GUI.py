'''
Created on 25.05.2015

@author: marilena
'''
import pymongo
import json
import time

client = pymongo.MongoClient("141.22.29.77",27017)

fileData = open('log.log','a')

def writeToFile(s):
    fileData.write(str(s) + '\n')
    
def getZipByCity(com):
    start = time.time()
    for item in client.plz_db.plz_collection.find( { "city" : com } ):
        stop = time.time()
        writeToFile('find_city: ' + str(stop-start))
        print (item.get('_id'))
        
def getCityStateByZip(com):
    start = time.time()
    for item in client.plz_db.plz_collection.find({"_id": com}):
        stop = time.time()
        writeToFile('find_plz: ' + str(stop-start))
        print(item.get('city') +', '+item.get('state'))
            
wFlag = True        
          
def work():
    com = input('WONACH SOLL GESUCHT WERDEN? [ZIP/CITY] ')
    if com == 'ZIP':
        com = input('BITTE ZIP-NUMMER EINGEBEN: ')
        getCityStateByZip(com)
        print()
    elif com == 'CITY':
        com = input('BITTE EINEN STADT ANGEBEN: ')
        getZipByCity(com)
   
        
while wFlag:
    work()  