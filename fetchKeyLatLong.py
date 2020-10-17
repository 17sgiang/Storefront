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

# Tests
print("Key: " , getKey()) 
lati = getLati()
longi = getLongi()
print("Latitude: " , lati , "Longitude: " , longi)
