import redis
import json

redisDB = redis.StrictRedis(host='localhost', port=6379, db=0)
fileData = open('plz.data','r')

for line in fileData:
    jsonData = json.loads(line)
    redisDB.hmset(jsonData['_id'], {'state':jsonData['state'],'city':jsonData['city'],'pop':jsonData['pop'],'loc':jsonData['loc']})
    
    

    
    
        