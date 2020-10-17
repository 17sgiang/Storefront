# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:23:21 2020

@author: alexl
"""
from makeURL import *
from locationParse import locationParse
from makePlaceDetailsAPICalls import makePlaceDetailsAPICalls

##philly lat long is 39.952583, -75.165222

def main():
    key = getKey();
    lat = getLati();
    long = getLongi();
    rad = getRadius();
    
    place_search_call = generatePlaceSearchCall(key, lat, long, rad)
    
    
    place_id_dict = print(locationParse(place_search_call))
    
    print(makePlaceDetailsAPICalls(place_id_dict))

if __name__== "__main__":
    main()