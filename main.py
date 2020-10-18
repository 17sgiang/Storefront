# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:23:21 2020

@author: alexl
"""
from makeURL import *
from locationParse import locationParse
from makePlaceDetailsAPICalls import makePlaceDetailsAPICalls
from cleanUp import *

##philly lat long is 39.952583, -75.165222

def main():
    key = getKey();
    lat = getLati();
    long = getLongi();
    rad = getRadius();
    
    place_search_call = generatePlaceSearchCall(key, lat, long, rad)
    
    
    place_id_dict = print(locationParse(place_search_call))
    
    api_call_list = makePlaceDetailsAPICalls(place_id_dict)

    rateFilteredList = noBadRatings(api_call_list)
    
if __name__== "__main__":
    main()