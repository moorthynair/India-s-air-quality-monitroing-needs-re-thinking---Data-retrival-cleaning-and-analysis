#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:37:01 2023

@author: moorthymnair
"""

from shapely.geometry import Point
import geopandas as gpd


def distancer(Latitude, Longitude, nearest_st_geo_retreived):
    poi = gpd.GeoSeries(Point(Longitude,Latitude), crs='epsg:4326')
    nearest_st_geo = gpd.GeoSeries(Point(nearest_st_geo_retreived[1], nearest_st_geo_retreived[0]), crs='epsg:4326')
    
    poi_reprojected = poi.to_crs('epsg:32645')
    nearest_st_geo_reprojected = nearest_st_geo.to_crs('epsg:32645')
    
    dist = poi_reprojected.distance(nearest_st_geo_reprojected)
    
    return dist