# OwlHacks 2020
# Athan Kim

# Program takes dict and writes it to a .txt file
import os

def dictToTxt(dictInput):
    # Before calling open(), do cleanup so there's no other output.txt
    if os.path.exists("output.txt"):
        os.remove("output.txt")    
    
    file = open('output.txt', 'wt')
    
    # Iterate over the dictionary to print line by line for formatting
    for key, value in dictInput.items():
        file.write(value + ' : ' + key + '\n')
    
    # file.write(str(dictInput))
    file.close()
