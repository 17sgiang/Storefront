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

def noBadRatings(api_call_list):
    newList = []
    for i in api_call_list:
        with urllib.request.urlopen(i) as url:
            data = json.loads(url.read())
            rating = data["result"].get("rating")
            if rating >= 4:
                newList.append(i)
    return newList

def onlyElectronics(api_call_list):
    blackList = []
    newList1 = []
    with open('blacklist.csv', 'r') as f:
        blackList.append(list(f))
    with open('blacklist.csv', 'r') as f: # Gets rid of \n in list elements
        blackList = [line.rstrip('\n') for line in f] 
    for i in api_call_list:
        with urllib.request.urlopen(i) as url:
            data = json.loads(url.read())
            name = data["result"].get("name")
            if name not in blackList:
                newList1.append(i)
    return newList1
    
def desiredURLs(api_call_list):
    newDict = {}
    for i in api_call_list:
        with urllib.request.urlopen(i) as url:
            data = json.loads(url.read())
            name = data["result"].get("name")
            link = data["result"].get("website")
            newDict[link] = name
    return newDict
