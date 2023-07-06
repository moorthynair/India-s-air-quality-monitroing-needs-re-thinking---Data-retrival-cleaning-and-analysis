#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:03:37 2023

@author: moorthymnair
"""

import pandas as pd
import numpy as np

def health_impact(AQI_category):
    sheet = pd.read_excel('inputs/AQI_breakpoint.xlsx', sheet_name='AQI_IND')
    impact = sheet.loc[sheet['Category']==AQI_category, 'Health Impacts'].reset_index(drop=True)
    return impact[0]
