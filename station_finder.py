#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 09:56:21 2023

@author: moorthymnair
"""

import requests
import json


def stationlocator(API, Latitude, Longitude):
    dt = requests.get('https://api.waqi.info/feed/geo:'+str(Latitude)+';'+str(Longitude)+'/?token='+API)
    doc = dt.text
    j = json.loads(doc)
    data = j['data']
    nearest_station = data['city']['name']
    geo_loc = data['city']['geo']
    time_of_retreival = data['time']['s']
    list_of_poll = list(data['iaqi'].keys())
    station_details = {'data':data, 'nearest_station':nearest_station, 'time_of_retreival':time_of_retreival,'list_of_poll':list_of_poll, 'geo':geo_loc}
    print()
    print('Information successfully fetched from the nearest station')
    return station_details
     
