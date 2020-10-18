# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:12:05 2020

@author: 17sgi
"""
from makeURL import getKey

# Takes a list of place_IDs
# Returns a list of API calls for Google's Place Details API
def makePlaceDetailsAPICalls(placeIdList):
    
    """
    
    Sample API call:
    https://maps.googleapis.com/maps/api/place/details/output?parameters
    Need an API key
    Requires parameters:
      key
      place_id
    Output is either json or xml, here let's use json
    
    
    """
    print(placeIdList)
    
    apiKey = getKey()
    
    apiCallList = []
    
    # Goes through the provided dictionary of place_IDs
    for i in placeIdList:
        
        # apiCall is a specific API call given the place ID   
        apiCall = "https://maps.googleapis.com/maps/api/place/details/json?"    
        
        apiCall += "place_id=" + i + "&"
        apiCall += "key=" + apiKey + "&"
        # fields: website, rating
        apiCall += "fields=" + "website,rating"
        
        apiCallList.append(apiCall)
    
    return apiCallList
        
    
    
        
    
    
    
    
    
    