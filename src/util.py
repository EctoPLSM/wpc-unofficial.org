#!/usr/bin/python
import os

def makedirs(path):
    try:
        os.makedirs(path)
    except OSError:
        pass

def readfile(path):
    with open(path, 'r', encoding="utf-8") as file:
        return file.read()

def writefile(path, content):
    with open(path, 'w', encoding="utf-8") as file:
        return file.write(content)
        
def copyfile(_from, to):
    # sry shutil
    writefile(to, readfile(_from))
        
def ordinal(number):
    if number != "11" and number[-1] == "1":
        return "st"
    elif number != "12" and number[-1] == "2":
        return "nd"
    elif number != "13" and number[-1] == "3":
        return "rd"
    else:
        return "th"