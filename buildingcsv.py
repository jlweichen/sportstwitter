# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 19:52:53 2018

@author: jw
"""
import csv
import os

def pathFile(n = 1, prefix = "tweets", path="/home/jw/Documents/twitterpython/data/"):
    myPath = os.path.join(path, (prefix + str(n) + '.csv'))
    return(myPath)

def makeFile(myPath):
    csvFile = open(myPath, 'a')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['author', 'time', 'text'])
    return True

def writeData(myPath, a, b, c):
    while (os.stat(myPath)).st_size < 2000:
        csvWriter = csv.writer(open(myPath, 'a'))
        csvWriter.writerow([str(a), str(b), str(c)])
    return True

def dataDump(a, b, c):
    i = 1
    myFile = pathFile(n = i)
    makeFile(myFile)
    while i < 30:
            myFile = pathFile(n = i)
            makeFile(myFile)
            writeData(myFile, a, b, c)
            i = i+1
    return True

def inputList():
    topicList = []
    topic = str(input("Give a filter term, or type 'done':"))
    while topic != 'done':
        topicList.append(topic)
    return(topicList)

