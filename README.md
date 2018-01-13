# Sports Twitter
Using Twitter, Python and R to analyze sentiment before, during, and/or after a sports event
## Step 1: Python script using the Tweepy library to stream tweets to a Sqlite database
This is done using twitterpysqlite.py.
## Step 2: Connecting the database to R and separating into data frames, one per team
This is done with an R script.
## Step 3: Filtering out irrelevant tweets
Right now this is done with filtering common irrelevant terms. Long-term I hope to build an algorithm that can determine if the tweet is relevant to football.
## Step 4: Sentiment analysis of each team's tweets
This is done with tidytext and tm.
