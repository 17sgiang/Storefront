# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:20:41 2020

@author: alexl
"""
import urllib.request, json, requests, sys
from bs4 import BeautifulSoup

def makeWebsiteDict(place_details_http_dict):
    website_dict = []
    
    for place_details in place_details_http_dict:
        #if statements with criteria
        