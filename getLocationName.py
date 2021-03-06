from urllib.request import urlopen
import pandas as pd
import csv
import json
import time

def getplace(lat, lon):
    url = "https://api.opencagedata.com/geocode/v1/json?key=8ebed16c3a09454e9a78de2a2f79a8bf&"
    url += "q=%s%%2C%s&pretty=1&no_annotations=1" % (lat, lon)
    v = urlopen(url)
    j = json.load(v)
    #components = j['results'][0]['address_components']
    #country = town = city = None
    #for c in components:
    #    if "country" in c['types']:
    #        country = c['long_name']
    #    if 'postal_town' in c['types']:
    #        town = c['long_name']
    #    if 'locality' in c['types']:
    #        city = c['long_name']
    #local = None
    #if city is None: # city has preference
    #    if town is None:
    #        local = None
    #    else:
    #        local = town
    #else:
    #    local = city
    #
    #    return "%s,%s" % (local, country)
    return j['results'][0]['formatted'] 

currlabel = -1
currLoc = ""
labeleddata = pd.read_csv('datawithlabel.csv', delimiter=',')

with open('locations.csv', 'w', newline='', encoding='utf-8') as csvfile:
    for i, row in labeleddata.iterrows():
        if row['label'] != currlabel and int(row['label']) != -1:
            currLoc = getplace(row['lat'], row['lon'])
            currlabel = row['label']
            print("%s|%s|%s" % (row['lat'], row['lon'], currLoc))
            locrow = str(int(currlabel))+"|"+currLoc+"\r\n"
            csvfile.write(locrow)
            time.sleep(1) # opencagedata free tier api limit
    
