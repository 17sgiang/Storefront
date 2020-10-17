# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:57:04 2020
Takes in html request url for use in Google Place Search API and generates a dictionary containing place_id's for 
use by Google Place Details API'
@author: alexl
"""


import urllib.request, json, requests, sys


def locationParse(request_url):
    #https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=39.952583,-75.165222&radius=30000&type=electronics_store&keyword=gpu&key=AIzaSyCR4FS2rFxzokjyDe5nkDOF9TKYcNBvAZs
    
    with urllib.request.urlopen(request_url) as url:
         data = json.loads(url.read())
         
         place_id_list = []
    
    for i in range(len(data['results'])):
        place_id = data['results'][i].get('place_id')
        place_id_list.append(place_id)
        
    return (place_id_list)
    
        