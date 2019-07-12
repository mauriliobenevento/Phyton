# Algoritmo088.py
#
# Json com google maps # precisa rever a API do google maps
#
# By Maurilio Benevento - 11/07/2019

import urllib.request, urllib.parse, urllib.error
import json
import http
import sqlite3
import time
import ssl
import sys



api_key = ''

if api_key is False:
    serviceurl = "https://py4e-data.dr-chuck.net/geojson?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

http.client.HTTPConnection.debuglevel = 1

while True:
    address = input('Entre a sua localização: ')
    if len(address) < 1: break
    
    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data), 'carateres')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'Ok':
        print('=== Fail to retrieve ===')
        print(data)
        continue
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lat"]
    print('lat',lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
