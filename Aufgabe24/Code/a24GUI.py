'''
Created on 13.05.2015

@author: Vladimir/Marilena
'''
import redis
import sys
import time

redisDB = redis.StrictRedis(host='localhost', port=6379, db=0)
fileData = open('log.log','a')

def writeToFile(s):
    fileData.write(str(s) + '\n')

def getZIP(com):
    start = time.time()
    if redisDB.hexists(com, 'zips'):#Es wird geprueft ob die DB solche Stadt kennt
        stop = time.time()
        writeToFile('hexists: ' + str(stop-start))
        start = time.time()
        #
        zips = redisDB.hget(com, 'zips').decode("utf-8")
        #
        stop = time.time()
        writeToFile('hget: ' + str(stop-start))
        
        listZIPS = zips.split(';')
        print('ES WURDEN FOLGENDEN PLZs GEFUNDEN: ') 
        for i in listZIPS:
            print(i)
    else:
        print('ES WURDEN KEINE PLZs GEFUNDEN')
        
def getCityState(com):
    start = time.time()
    if redisDB.hexists(com, 'city'):#Es wird geprueft ob die DB solche PLZ kennt
        stop = time.time()
        writeToFile('hexists: ' + str(stop-start))
        start = time.time()
        #
        city = redisDB.hget(com, 'city').decode("utf-8") #Abfrage der Stadtname
        #
        stop = time.time()
        writeToFile('hget: ' + str(stop-start))
        start = time.time()
        #
        state = redisDB.hget(com, 'state').decode("utf-8")#Abfrage der Staatsname
        #
        stop = time.time()
        writeToFile('hget: ' + str(stop-start))
        out = 'Es ist '+ str(city) + ' in ' + str(state)
        print(out)
    else:
        print('PLZ NICHT VORHANDEN')   

wFlag = True

#Die GUI ist eine einfache EIngabe per Konsole
#Es wird zwischen 4 Zustaenden unetrschieden
#    ZIP -> Suche mit PLZ nach Stadt- und Staatsname
#    CITY -> Suche mit Stadtname nach PLZs
#    EXIT -> Programm wird beendet
#    Alles andere wird als "EINGABE NICHT ERKANNT" dem Nutzer gemeldet
def work():
    com = input('WONACH SOLL GESUCHT WERDEN? [ZIP/CITY] ')
    if com == 'ZIP':
        com = input('BITTE ZIP-NUMMER EINGEBEN: ')
        getCityState(com)
        print()
    elif com == 'CITY':
        com = input('BITTE EINEN STADT ANGEBEN: ')
        getZIP(com)
    elif com == 'EXIT':
        sys.exit()
    else:
        print('EINGABE NICHT ERKANNT')
        print()
        
while wFlag:
    work()  