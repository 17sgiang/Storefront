# OwlHacks 2020
# Athan Kim
# Program takes in two user inputs as the Latitude and Longitude of the location to be used
# Also takes in the API key

def getKey(): # Fetches the key and returns the value
    file = open(r"C:\Users\Athan-PC\Storefront\.gitignore\key.txt")
    key1 = file.read()
    file.close()
    return key1

def getLati(): # Takes in a user input of the latitude and returns the value
    lati = input("Enter the desired latitude value (N): ")
    return lati

def getLongi(): # Takes in a user input of the longitude and returns the value
    longi = input("Enter the desired longitude value (W): ");
    return longi

def getRadius(): # Takes in a user input of miles and converts it to meters and returns the value
    miles = input("Enter the desired mile radius: ")
    meters = float(miles) * 1609.34
    return meters

def makePlaceSearchCall(): # Takes all three methods and appends them to the URL
    return "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(getLati()) + "," + str(getLongi()) + "&radius=" + str(getRadius()) + "&type=electronics&keyword=gpu&key=" + str(getKey())

print(makePlaceSearchCall())
