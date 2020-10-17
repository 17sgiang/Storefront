# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:57:04 2020
Takes in html request url for use in Google Place Search API and generates a dictionary containing place_id's for 
use by Google Place Details API'
@author: alexl
"""


import urllib.request, json, requests, sys
from bs4 import BeautifulSoup

def locationParse(request_url):
    places = requests.get(request_url)
    results = BeautifulSoup(places.content, 'html.parser')
    
    place_id_dict = {}
    
    for result in results:
        id = result.find('place_id')
        place_id_dict.update(id)
    
    #testing
    print (place_id_dict)
    
    return (place_id_dict)
    
        