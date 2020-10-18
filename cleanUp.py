# OwlHacks 2020
# Athan Kim

# Program first removes all elements from given list that have a rating less than 3.5
# Then removes all elements from given list that contain blacklisted words

import urllib.request, json

def tooBad(request_url): # returns true or false if the rating is less than or greater than 3.5
    with urllib.request.urlopen(request_url) as url:
        data = json.loads(url.read())
        rating = data["result"].get("rating")
        if rating < 3.5:
            return 0
        else:
            return 1

def noBadRatings(place_id_list):
    for i in range(len(place_id_list)):
        with urllib.request.urlopen(place_id_list[i]) as url:
            data = json.loads(url.read())
            rating = data["result"].get("rating")
            print()
            print(rating)
            print()
            print(i)
            print()
            if rating < 4:
                deadUrl = place_id_list[i]
                place_id_list.remove(deadUrl)
                i = i - 1
    return place_id_list

testList = ['https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJM5LjuzqwxokRf4fN-q4FkI8&key=AIzaSyCR4FS2rFxzokjyDe5nkDOF9TKYcNBvAZs&fields=name,website,rating','https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJH_t6dDDGxokRgS5Jwy5zf8k&key=AIzaSyCR4FS2rFxzokjyDe5nkDOF9TKYcNBvAZs&fields=name,website,rating','https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJyfcTbMnBxokR_syntaa6Nso&key=AIzaSyCR4FS2rFxzokjyDe5nkDOF9TKYcNBvAZs&fields=name,website,rating']
print(testList)
print()
print(noBadRatings(testList))
