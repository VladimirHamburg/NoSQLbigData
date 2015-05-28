'''
Created on 25.05.2015

@author: marilena
'''
import pymongo
import json

client = pymongo.MongoClient("141.22.29.77",27017)
  
fileData = open('plz.data','r')

def getZipByCity(com):
    for item in client.my_db.find( { "city" : com } ):
        print item
        
def getCityStateByZip(com):
            
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