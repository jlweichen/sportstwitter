# Sports Twitter
Using Twitter, Python and R to analyze sentiment before, during, and/or after a sports event
### Step 1: Use Python and the Tweepy library to stream tweets to a series of CSV files
This is done using twitterpymain.py.
### Step 2: Upload the CSV files to R and separate into data frames, one per team
This is done with an R script.
### Step 3: Filtering out irrelevant tweets
Right now this is done with filtering common irrelevant terms. Long-term I hope to build an algorithm that can determine if the tweet is relevant to football. I am building a dictionary of sports terms and hashtags using what is trending, searching the term on Twitter, and noting to what sport and team each term refers.
### Step 4: Sentiment analysis of each team's tweets
This is done with tidytext and tm.
