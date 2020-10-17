"""

Created on Sat Oct 17
Takes in a target word to scrape for and a website's URL to scrape.
Returns
@author: steveng

"""


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# Class def

# Use BeautifulSoup library to scrape a web page for a target word
# Later I'll decide whether the return value is true/false or hit count
# Currently returns the number of times a url contains the target word
def webScraper(word, targetUrl):
    
    print("Searching for '" + word + "' at url: " + targetUrl)
    page = urlopen(targetUrl)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.get_text())
    # print(soup.find_all(string=re.compile(word)))
    matchList = soup.find_all(string=re.compile(word))
    hitCount = 0
    
    for i in matchList:
        hitCount += 1
        
    return hitCount    

# Test case
print("hitCount: " + str(webScraper("RegEx", "http://w3schools.com/python/python_regex.asp")))

    

