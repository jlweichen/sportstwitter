import tweepy
import sqlite3

# making/creating database as file on disk
db = sqlite3.connect('twitter.db')
cur = db.cursor()
# creating the table
# only run this line if table doesn't exist

cur.execute('''CREATE TABLE tweets(text TEXT, author TEXT, 
                                 time TEXT)''')

# API authorization                        

consumer_key = #consumer key
consumer_secret = #consumer secret

access_key = #access key
access_secret = #access secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


#empty list of filter terms
#in this case, the team names of the second week of NFL 2018 playoffs

topicList = ['eagles', 'falcons', 'saints', 'patriots', 'titans', 'steelers', 'vikings', 'jaguars']
print(topicList)


class myStreamListener(tweepy.StreamListener):
    
    def on_status(self, status):
        entries = (str(status.text), str(status.user.screen_name), str(status.created_at))
        cur.execute('INSERT INTO tweets VALUES(?, ?, ?)', entries)
        db.commit()
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
db.close()
print('done!')
