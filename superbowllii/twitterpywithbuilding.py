import tweepy
import os
import csv
import buildingcsv
import footballterms
from http.client import IncompleteRead
from urllib3.response import ReadTimeoutError

consumer_key =  #consumer key
consumer_secret = #consumer secret

access_key = #access key
access_secret = #access secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# prompt user to name the csv
pref = str(input("Give a word to name the csv files:"))
count = int(input("How many files to make:"))

# prompt user to make list of terms being followed
#list = buildingcsv.inputList()
list = footballterms.termlist

class myStreamListener(tweepy.StreamListener):
    
    def on_status(self, status):
        for i in range(count):
            myPathName = buildingcsv.pathFile(n=(i+1), prefix = pref)
            if (os.path.isfile(myPathName)) == False:
                buildingcsv.makeFile(myPathName)
            if (os.stat(myPathName)).st_size < 15000000:
                csvWriter = csv.writer(open(myPathName, 'a'))
                csvWriter.writerow([str(status.user.screen_name), str(status.created_at), str(status.text)])
                return True
        return True


    def on_error(self, status_code):
        print('Encountered error with status code:' + status_code)
        if status_code == 420:
            return False
        return True
    
    def on_timeout(self):
        print('Timeout...')
        return True

while True:
    try:
        streamingAPI = tweepy.streaming.Stream(auth, myStreamListener())
        streamingAPI.filter(track=list)
    except IncompleteRead:
        continue
    except ReadTimeoutError:
        continue
    
