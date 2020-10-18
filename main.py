# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:23:21 2020

@author: alexl
"""
from makeURL import *
from locationParse import locationParse
from makePlaceDetailsAPICalls import makePlaceDetailsAPICalls
from cleanUp import *
from webScraper import *

##philly lat long is 39.952583, -75.165222

def main():
    key = getKey();
    lat = getLati();
    long = getLongi();
    rad = getRadius();
    
    # 0 API calls
    place_search_call = generatePlaceSearchCall(key, lat, long, rad)
    
    # 1 API call
    place_id_list = locationParse(place_search_call)
    
    # 0 Calls
    api_call_list = (makePlaceDetailsAPICalls(place_id_list))
    
    # n Calls
    URL_name_dict = applyRatingFilterAndBlacklist(api_call_list)

    print(URL_name_dict)
    
    # n Calls to read HTML
    sites_with_sale = webScraper(URL_name_dict)
    
    print(sites_with_sale)
    
if __name__== "__main__":
    main()