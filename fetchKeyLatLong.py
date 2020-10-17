# OwlHacks 2020
# Athan Kim
# Program takes in two user inputs as the Latitude and Longitude of the location to be used
# Also takes in the API key

def getKey(): # Fetches the key and returns the value
    file = open(r"C:\Users\Athan-PC\Storefront\.gitignore\key.txt")
    key1 = file.read()
    file.close()
    return key1


print("Key: " , getKey()) # Prints the key
lati = input("Enter the desired latitude value (N): ") # Takes in latitude and stores it in lati
longi = input("Enter the desired longitude value (W): "); # Takes in longitude and stores it in longi
print("Latitude: " , lati , "Longitude" , longi)

key = getKey()