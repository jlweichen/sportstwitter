import tweepy
import csv

consumer_key = #key
consumer_secret = #secret

access_key = #access key
access_secret = #access secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# prompt user to name the csv

fileName = input("Name the file you're saving data to: ")

#empty list of filter terms
topicList = []

topic = ""

while topic != 'done':
    topic = str(input("Give a filter term, or type 'done':"))
    topicList.append(topic)

print(topicList)

csvFile = open(fileName +'.csv', 'a')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['author', 'time', 'text'])
fileName = fileName+'.csv'


class myStreamListener(tweepy.StreamListener):
    
    def on_status(self, status):
        csvWriter.writerow([status.user.screen_name, status.created_at, status.text])
        return True

    def on_error(self, status_code):
        print('Encountered error with status code:' + status_code)
        if status_code == 420:
            return False
        return True
    
    def on_timeout(self):
        print('Timeout...')
        return True

streamingAPI = tweepy.streaming.Stream(auth, myStreamListener())

streamingAPI.filter(track=topicList, languages=['en'])
