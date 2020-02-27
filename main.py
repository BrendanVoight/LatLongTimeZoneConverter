# Author: Brendan Voight
# Initial Create Date: 2/26/2020
# This will take in a list of latitude and longitude pairs and return a list of corresponding time zones
# License: MIT
# Copyright 2020 Brendan Voight
# For this code to work you will need a free api key from here: https://timezonedb.com/
import requests

def main(locations):
    keyfile = open("APIKey.txt", "rt")
    key = keyfile.readline()
    keyfile.close()
    timezones = []
    for latlong in locations:
        lat = latlong[0]
        long = latlong[1]
        r = requests.get('http://api.timezonedb.com/v2.1/get-time-zone?key='+str(key)+'&format=json&by=position&lat='+str(lat)+'&lng='+str(long))
        body = r.json()
        abbv = body['abbreviation']
        timezones.append(abbv)

    export = open('exportFile.txt', "w")
    for i in range(len(timezones)):
        export.write(timezones[i]+'\n')
x = [(40.689247,-74.044502), (65.74051,-154.61156)]
main(x)
