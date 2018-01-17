# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 19:52:53 2018

@author: jw
"""
import csv
import os

def pathFile(n = 1, prefix='tweets', path="/home/jw/Documents/twitterpython/data/"):    
    myPath = os.path.join(path, (prefix + str(n) + '.csv'))
    return(myPath)

def makeFile(myPath):
    csvFile = open(myPath, 'a')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['author', 'time', 'text'])
    return csvFile


def inputList():
    topicList = []
    topic = 'e'
    while topic != 'done':
        topic = str(input("Give a filter term, or type 'done':"))
        if topic != 'done':
            topicList.append(topic)
    return(topicList)



