#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 12:38:39 2023

@author: moorthymnair
"""

import requests
import pandas as pd
import numpy as np
import json
from datetime import datetime as dt
import math
from tabulate import tabulate


"""
The AQI information retreived from the 'World AQI' Platoform is estimatd using the USEPA scale. 
This needs to be converted to India AQI scale to comply with National Ambient Air Quality Standards (NAAQS), GoI

"""

## First let us Convert pollution specific AQI at US scale to pollution concentration

def poll_conc(data, list_of_poll):
    critical_poll = ['pm10', 'pm25', 'so2','no2', 'o3','co']
    poll_conc =[]

    for i in critical_poll:
        if i in list_of_poll:
            val = data['iaqi'][i]['v']
            sheet = pd.read_excel('inputs/AQI_breakpoint.xlsx', sheet_name=i+'_US')
            req_row = sheet.loc[(sheet['Lower AQI']<= val) & (sheet['Upper AQI']>= val),:].reset_index()
            ## Let us convert AQI to Pollution concentration
            step_1 = (req_row['Upper AQI'][0] - req_row['Lower AQI'][0])/ (req_row['Upper Conc'][0] - req_row['Lower Conc'][0])
            step_2 = (int(val) - req_row['Lower AQI'][0])/step_1
            actual_conc = (step_2+ req_row['Lower Conc'][0]) *req_row['Conversion_const'][0]
            poll_conc.append(actual_conc)
        else:
            poll_conc.append('No Information available')
    poll_outs = {'poll_conc': poll_conc, 'critical_poll': critical_poll}
    return poll_outs

## Now calculate the AQI as per the India scale
    
def aqi(poll_outs):
    AQI = []
    
    for poll, val in zip(poll_outs['critical_poll'], poll_outs['poll_conc']):
        if val !='No Information available':
            sheet = pd.read_excel('inputs/AQI_breakpoint.xlsx', sheet_name=poll+'_IND')
            ## Ceiling the value just not to missed out the intermediate values (eg: PM10 =50.5,101.6 ug/m3,... etc )
            ciel_val = math.ceil(val)
            req_row = sheet.loc[(sheet['Lower Conc']<= ciel_val) & (sheet['Upper Conc']>= ciel_val),:].reset_index()
            ## Let us now get the AQI at India scale for the pollutant
            step_1 = (req_row['Upper AQI'][0] - req_row['Lower AQI'][0])/ (req_row['Upper Conc'][0] - req_row['Lower Conc'][0])
            step_2 = step_1 * (val - req_row['Lower Conc'][0])
            AQI_vals = step_2+ req_row['Lower AQI'][0]
            AQI.append(AQI_vals)
            
        else:
            AQI.append('No Information available')
    aqi_outs = {'aqi':AQI}
    return aqi_outs
    
    """
    Let us get the AQI category for the individual pollutants
    
    """
def category(AQI, critical_poll,poll_conc):
    
    AQI_int_index = [AQI.index(i) for i in AQI if i !='No Information available']
    
    AQI_int_filtered = [AQI[i] for i in AQI_int_index]    
    
   # poll_conc_filtered =[poll_conc[i] for i in AQI_int_index]   
    
    critical_poll_filtered = [critical_poll[i] for i in AQI_int_index] 
    
    AQI_sheet = pd.read_excel('inputs/AQI_breakpoint.xlsx', sheet_name='AQI_IND')
    
    category=[]
    
    catg_dummy = []
    
    for i in range(len(critical_poll)):
        poll = critical_poll[i]
        if poll in critical_poll_filtered:
            req_row = AQI_sheet.loc[(AQI_sheet['Lower AQI']<= AQI[i]) & (AQI_sheet['Upper AQI']>= AQI[i]),:].reset_index()
            category.append(req_row['Category'][0])
            catg_dummy.append(req_row['Category'][0])
        else:
            category.append('No Information Available')
            
    
    """
    Now that we have all the required information let us print that
    
    """   
    
    max_AQI = max(AQI_int_filtered)
    critical_pollutant = critical_poll_filtered[AQI_int_filtered.index(max(AQI_int_filtered))]
    cat = catg_dummy[AQI_int_filtered.index(max(AQI_int_filtered))]
    ##units = []
    
    concatenate =[]
    
    for poll, conc, aqi, catg in zip(critical_poll,poll_conc,AQI,category):
        if aqi !='No Information available':
            info = [poll.upper(), conc.round(2), math.ceil(aqi), catg.upper()]
            concatenate.append(info)
        else:
            info = [poll.upper(), conc.upper(), aqi.upper(), catg.upper()]
            concatenate.append(info)
            
    cat_outs = {'max_aqi':max_AQI, 'critical_pollutant':critical_pollutant, 'cat':cat,'concatenate':concatenate, 'category':category}
    return cat_outs
    
"""
Display the results
    
"""
    
def display(output,output2,distance,health):
    print()
    print('-*-'*28)  
    print()
    print('Findings collected on '+ output['time_of_retreival']+' from the CAAQMS located at '+output['nearest_station'].center(20))  
    print('The CAAQMS and the Point of Interest are '+ str(distance[0].round(2))+' meters apart'.center(10))
    print('**Information is specific to the retreived date & time**'.center(20))
    print()
    print('1. AQI of '+str(math.ceil(output2['max_aqi']))+' has been observed')
    print()
    print('2. '+output2['critical_pollutant'].upper()+' is the critical pollutant')
    print()
    print('3. The air quality is '+output2['cat'].upper()+ ' and may possess "'+health+'"')
    print()
    print('Summary Table'.center(30))
    print(tabulate(output2['concatenate'], headers = ['Pollutants', 'Concentration', 'AQI','Category'], tablefmt ='grid'))
    print('Note: The unit for CO is milligrams per cubicmeters and rest are in micrograms per cubicmeters')
    print()
    print('Disclaimer: There may be ±5% variation from the actual data due to conversion/rounding errors')
    print()
    print('-*-'*28)
    
    
        