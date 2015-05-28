'''
Created on 28.05.2015

@author: marilena
'''
import pymongo
from bson.json_util import loads

client = pymongo.MongoClient("141.22.29.77",27017)

def augsburg():
    for item in client.vereine_db.fussball.find({'name': "Augsburg"}):
        print(item)
    
#alle Nike-Vereine, welche schwarz als mindestens eine Vereinsfarbe haben
def nikeSchwarz():
    for item in client.vereine_db.fussball.find( {"nike" : 'j', "farben": {"$in": ['schwarz']}}):    
        print(item)
        
#alle Nike-Vereine, welche weiss und gruen als Vereinsfarbe haben
def  nikeWeissGruen():
    for item in client.vereine_db.fussball.find( {'nike' : 'j', "$and":[{'farben' : 'weiss'}, {'farben':'gruen'}]}):
        print(item)

# alle Nike-Vereine, welche weiss oder gruen als Vereinsfarbe haben       
def nikeWeissOrgruen():
    for item in client.vereine_db.fussball.find({"nike": 'j', "$or": [{'farben' : 'weiss'}, {'farben' : 'gruen'}]}):
        print(item)
        
#den Verein mit dem hoechsten Tabellenplatz
def highestPlace():
        print(client.vereine_db.fussball.find_one(sort=[("tabellenplatz",+1)]))

#alle Vereine, die nicht auf einem Abstiegsplatz stehen        
def keinAbstieg():
    for item in client.vereine_db.fussball.find({"tabellenplatz": {'$not' : {"$gt": 15}}}):
        print(item)

def beliebigeAnfrage():
    print(client.vereine_db.fussball.find_one({'name': "HSV"},{'_id': False}))

def anderung():
    print(client.vereine_db.fussball.update({'name':"Augsburg"}, {'tabellenplatz' : 1}))


def rettung():
    fileData = open('sinndeslebens.data','r')
    for line in fileData:
        jsonData = loads(line)
        if(jsonData["name"] == 'Augsburg'):
            client.vereine_db.fussball.update({'tabellenplatz' : 1},jsonData)
    
print('Anfrage 1')
augsburg()
print('Anfrage 2')
nikeSchwarz()
print('Anfrage 3')
nikeWeissGruen()
print('Anfrage 4')
nikeWeissOrgruen()
print('Anfrage 5')
highestPlace()
print('Anfrage 6')
keinAbstieg()
print('Anfrage 7')
beliebigeAnfrage()
print('Aenderung')
anderung()
print('Rettung')
rettung()


for item in client.vereine_db.fussball.find():
    print(item)