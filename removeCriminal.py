import os
from loadFunctions import images

def remove_convict():
    convict_name = str(input("What is the name of the convict?")).capitalize()

    for i in images:
        if str(convict_name) in i:
            os.remove(i)

remove_convict()
