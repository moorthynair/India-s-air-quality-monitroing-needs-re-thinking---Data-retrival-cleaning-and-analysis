#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 08:55:29 2023

@author: moorthymnair
"""

from datetime import datetime as dt

def header():
    print("-*-" * 28)
    print()
    print("Near Real Time AQI Finder".center(70))
    print(f"Fetches AQI and Pollutant concentrations from the nearest CAAQMS".center(70))
    print()
    print(f"Date & Time of Run:     {dt.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("Contact:                morthymnair@yahoo.in")
    print("Acknolwedgement:        World Air Quality Index (https://waqi.info/)")
    print("                        Central Pollution Control Board (https://cpcb.nic.in/)")                       
    print()
    print("-*-" * 28)
    print()
    print("Fetching details........")