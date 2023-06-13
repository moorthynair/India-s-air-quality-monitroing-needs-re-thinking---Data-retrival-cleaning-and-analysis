#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 09:24:09 2023

@author: moorthymnair
"""

import argparse
import initialiser
import aqi_finder
import station_finder
import distance_finder

#API = 'dedb41dc*********f51fe'

if __name__ =='__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('API', help ='Enter the API generated from World AQI forun')
    parser.add_argument('Lat', help ='Enter the Latitude of the Point of Intrest')
    parser.add_argument('Lon', help ='Enter the Longitude of the Point of Intrest')
    
    args = parser.parse_args()
    
    ## Let us call the header from the initialiser module
    initialiser.header()
    
    ## Let us find the nearest station to the POI using the station_finder module
    
    st_details = station_finder.stationlocator(args.API, args.Lat, args.Lon)
    
    ## Let us now fetch the AQI and pollution details using the aqi_finder module
    
    pollution_con = aqi_finder.poll_conc(st_details['data'], st_details['list_of_poll'])
    
    aqi_values = aqi_finder.aqi(pollution_con)
    
    categorisation = aqi_finder.category(aqi_values['aqi'], pollution_con['critical_poll'], pollution_con['poll_conc'])
    
   ## Let us calculate the distance between the station and the POI using the distance_finder module
    
    dist = distance_finder.distancer(args.Lat, args.Lon, st_details['geo'])
   
   ## Let us now display the results
    
    aqi_finder.display(st_details,  categorisation, dist)
