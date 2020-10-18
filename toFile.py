# OwlHacks 2020
# Athan Kim

# Program takes dict and writes it to a .txt file

def dictToTxt(dictInput):
    file = open('output.txt', 'wt')
    file.write(str(dictInput))
    file.close()
