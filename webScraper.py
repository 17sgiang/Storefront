"""

Created on Sat Oct 17

Parameters:
    list of words (to scrape for)
    Directory. Website link is the key, and name is the value.

Returns:
    Directory that is essentially the parameter but filtered 
    
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
    return type is a dictionary
    {
     {"link": "name"}
    }        
    
    
"""

# Takes a directory where website URLs are keys paired with the store name
# Returns a filtered version of that based on searched keywords
def webScraper(words, siteDict):
    returnDict = {}
    
    # siteDict is a dictionary of URLs with attached names
    for link in siteDict:
        # isFound = 0
        # Check if the key word appears in the html of a website
        for word in words:
            print("Searching for '" + word + "' at url: " + link)
            page = urlopen(link)
            
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            # print(soup.get_text())
            # print(soup.find_all(string=re.compile(word)))
            matchList = soup.find_all(string=re.compile(word))
            
            # If there's at least one match for the words, add the website and move to the next
            if(len(matchList) > 0): 
                # found = 1
                returnDict[link] = returnDict.get(link)
                break      
    return returnDict


    

