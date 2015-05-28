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
    for item in client.vereine_db.fussball.find({"$and": {'nike' : 'j', 'farben': {"$in": ['schwarz']}}}):    
        print(item)
        
#alle Nike-Vereine, welche weiss und gruen als Vereinsfarbe haben
def  nikeWeissGruen():
    for item in client.vereine_db.fussball.find({"$and": {'nike' : 'j', "$and":[{'farben' : 'weiss'}, {'farben':'gruen'}]}}):
        print(item)

# alle Nike-Vereine, welche weiss oder gruen als Vereinsfarbe haben       
def nikeWeissOrgruen():
    for item in client.vereine_db.fussball.find({"$and": {"nike": 'j', "$or": [{'farben' : 'weiss'}, {'farben' : 'gruen'}]}}):
        print(item)
        
#den Verein mit dem hoechsten Tabellenplatz
def highestPlace():
    for item in client.vereine_db.fussball.find({"$max": {"$Tabellenplatz"}}):
        print(item)

#alle Vereine, die nicht auf einem Abstiegsplatz stehen        
def keinAbstieg():
    for item in client.vereine_db.fussball.find({"$not": {'Tabellenplatz' : 17}}):
        print(item)