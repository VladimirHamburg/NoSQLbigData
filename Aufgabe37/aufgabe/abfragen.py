'''
Created on 28.05.2015

@author: marilena
'''
import pymongo

client = pymongo.MongoClient("141.22.29.77",27017)

def augsburg():
    for item in client.vereine_db.fussball.find({"name": augsburg}):
        print(item)
    
#alle Nike-Vereine, welche schwarz als mindestens eine Vereinsfarbe haben
def nikeSchwarz():
    for item in client.vereine_db.fussball.find({'nike' : 'j', 'farben' : 'schwarz'}):
        print(item)
        
#alle Nike-Vereine, welche weiss und gruuen als Vereinsfarbe haben
def  nikeWeissGruen():
    for item in client.vereine_db.fussball.find({'nike' : 'j', 'farben' : ['weiss', 'gruen']}):
        print(item)