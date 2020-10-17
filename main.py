# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:23:21 2020

@author: alexl
"""
from makeURL import *


def main():
    key = getKey();
    lat = getLati();
    long = getLongi();
    rad = getRadius();
    
    generatePlaceSearchCall(key, lati, long, rad);
    

if __name__== "__main__":
    main()