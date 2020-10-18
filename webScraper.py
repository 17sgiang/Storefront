"""

Created on Sat Oct 17

Parameters:
    list of words (to scrape for)
    list of dictionaries. Each dictionary is a site
    Site items:
        "name": common name for the location
        "website": url for the corresponding site

Returns:
    list of dictionaries, where each dictionary is a site.
    This list is a filtered version of the parameter list. 
    
Potentially an issue of the search range being too broad.
Currently, if the scraper finds one instance of a key word in the html, the entire
site is added, which might result in too many sites being added.
Uses BeautifulSoup library.

@author: steveng

"""


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

"""
    return type is a list of dictionaries
    [
     {name:"",website:""}
     {name:"",website:""}
     ]        
    
    
"""

# Takes a list of dictionaries where names are coupled with website URLs
# Returns a filtered version of that based on searched keywords
def webScraper(words, websiteList):
    returnList = []
    
    # websiteList is a list of dictionaries
    # siteDict should be a dictionary
    for siteDict in websiteList:
        # isFound = 0
        # Check if the key word appears in the html of a website
        for word in words:
            print("Searching for '" + word + "' at url: " + siteDict["website"])
            page = urlopen(siteDict["website"])
            
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            # print(soup.get_text())
            # print(soup.find_all(string=re.compile(word)))
            matchList = soup.find_all(string=re.compile(word))
            
            # If there's at least one match for the words, add the website and move to the next
            if(len(matchList) > 0): 
                # found = 1
                obj = {"name":siteDict["name"],"website":siteDict["website"]}
                returnList.append(obj)
                break
            
    return returnList


    

