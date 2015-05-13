'''
Created on 12.05.2015

@author: Vladimir
'''
import redis
import json

redisDB = redis.StrictRedis(host='localhost', port=6379, db=0)
fileData = open('plz.data','r')

redisDB.flushdb()

for line in fileData:
    jsonData = json.loads(line)
    #Die ZIP-Codes sind die keys alles andere values
    redisDB.hmset(jsonData['_id'], {'state':jsonData['state'],'city':jsonData['city'],'pop':jsonData['pop'],'loc':jsonData['loc']})
    #redisDB.sadd(jsonData['state'], jsonData['_id'])
    
    #Um ZIP-Codes einfacher zu finden, werden Stadtnamen als keys und ZIP-Codes als values verwendet. 
    #Dabei werden dies ZIP-Codes in einem String abgespeichert
    if redisDB.hexists(jsonData['city'], 'zips'): #Überprüfe ob es schon einen Eitrag gibt`s
        zips = redisDB.hget(jsonData['city'], 'zips').decode("utf-8") #Alte Daten werden geholt und in ein string umgewandelt
        zips += str(jsonData['_id'])
        zips += ';' #Trennzeichen um die einzellne ZIP-Codes zu unterscheiden
        redisDB.hmset(jsonData['city'], {'zips':zips}) #Neue Daten abspeichern
    else:
        zips = str(jsonData['_id'])
        zips += ';' #Trennzeichen um die einzellne ZIP-Codes zu unterscheiden
        redisDB.hmset(jsonData['city'], {'zips':zips}) #Neue Daten abspeichern
    
    
        