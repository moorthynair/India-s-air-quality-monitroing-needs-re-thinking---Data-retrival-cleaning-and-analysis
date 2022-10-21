# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:30:24 2022

@author: USER
"""

import pandas as pd
from geopandas.tools import geocode
import numpy as np


data = pd.read_excel('C:/Users/USER/Downloads/all_sitestatus20221021184248.xlsx')

data = data.iloc[2:,np.r_[1:4]]
data.columns = data.iloc[0,]
data.drop(2, axis=0, inplace=True)


##Fill the missing state name
data['State'] = data['State'].fillna(method = 'ffill')

## Split and join the state name
data['Station Name'] = data['Station Name'].apply(lambda x:x.split('-')[0])
data['Station Name'] = data['Station Name']+','+data['State']
data['Station Name'] = data['Station Name'].apply(lambda x:"".join(x.split(' ')))


for index, i in data.iterrows():
    p = geocode(i['Station Name'], provider='arcgis', user_agent="xyz", timeout=5)
    data.loc[index, 'Longitude'] = p.geometry.x[0]
    data.loc[index, 'Latitude'] = p.geometry.y[0]
    print('{}: Completed'.format(index))

data.to_csv('CAAQMS.csv', index=False)
