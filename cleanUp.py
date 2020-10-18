# OwlHacks 2020
# Athan Kim

# Program first removes all elements from given list that have a rating less than 3.5
# Then removes all elements from given list that contain blacklisted words

import urllib.request, json, os

def tooBad(request_url): # returns true or false if the rating is less than or greater than 3.5
    with urllib.request.urlopen(request_url) as url:
        data = json.loads(url.read())
        rating = data["result"].get("rating")
        if rating < 3.5:
            return 0
        else:
            return 1

def applyRatingFilterAndBlacklist(api_call_list):
    filteredDict = {}
    blackList = []
    with open('blacklist.csv', 'r') as f:
        blackList.append(list(f))
    with open('blacklist.csv', 'r') as f: # Gets rid of \n in list elements
        blackList = [line.rstrip('\n') for line in f] 
        
    for i in api_call_list:
        with urllib.request.urlopen(i) as url:
            data = json.loads(url.read())
            rating = data["result"].get("rating")
            name = data["result"].get("name")
            link = data["result"].get("website")
            
            if(rating is not None):
                if (rating >= 4) & (name not in blackList):
                    filteredDict[link] = name
            else:
                if (name not in blackList):
                    filteredDict[link] = name
    return filteredDict

    

