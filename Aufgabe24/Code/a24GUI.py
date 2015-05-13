'''
Created on 13.05.2015

@author: Vladimir
'''
import redis
import sys

redisDB = redis.StrictRedis(host='localhost', port=6379, db=0)

def getZIP(com):
    if redisDB.hexists(com, 'zips'):#Es wird geprüft ob die DB solche Stadt kennt
        zips = redisDB.hget(com, 'zips').decode("utf-8")
        listZIPS = zips.split(';')
        print('ES WURDEN FOLGENDEN PLZs GEFUNDEN: ') 
        for i in listZIPS:
            print(i)
    else:
        print('ES WURDEN KEINE PLZs GEFUNDEN')
        
def getCityState(com):
    if redisDB.hexists(com, 'city'):#Es wird geprüft ob die DB solche PLZ kennt
        city = redisDB.hget(com, 'city').decode("utf-8") #Abfrage der Stadtname
        state = redisDB.hget(com, 'state').decode("utf-8")#Abfrage der Staatsname
        out = 'Es ist '+ str(city) + ' in ' + str(state)
        print(out)
    else:
        print('PLZ NICHT VORHANDEN')   

wFlag = True

#Die GUI ist eine einfache EIngabe per Konsole
#Es wird zwischen 4 Zuständen unetrschieden
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