"""

Created on Sat Oct 17

Parameters:
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
def webScraper(siteDict):
    returnDict = {}
    words = []
    
    with open('salePhrases.csv', 'r') as f:
        words.append(list(f))
    with open('salePhrases.csv', 'r') as f: # Gets rid of \n in list elements
        words = [line.rstrip('\n') for line in f]
    
    print(words)    
    
    # siteDict is a dictionary of URLs with attached names
    for link in siteDict:
        # Check if the key word appears in the html of a website
        page = urlopen(link)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        print("Searching url: " + link)
        for word in words:
            # print("Searching for '" + word + "' at url: " + link)
            print("for word: " + word)
            # print(soup.get_text())
            # print(soup.find_all(string=re.compile(word)))
            match = soup.find(string=re.compile(word))
            
            # If there's at least one match for the words, add the website and move to the next
            if(match != None): 
                print("Found")
                returnDict[link] = siteDict.get(link)
                break      
    return returnDict



    

