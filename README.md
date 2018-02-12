# Sports Twitter
Using Twitter, Python and R to analyze sentiment before, during, and/or after a sports event
## Overarching Goals
1. To build a machine learning algorithm that detects sports-related tweets
2. To perform sentiment analysis on said tweets to determine the general public's confidence in a team or athlete
3. To perform quantitative analysis to determine a team's general popularity
## Sentiment Analysis
### Step 1: Use Python and the Tweepy library to stream tweets to a series of CSV files
This is done using the Tweepy, CSV, and OS libraries from PyPi. I wrote specific functions contained in buildingcsv.py, which are imported into twitterpymain.py, to write each tweet's username, time, and content into a CSV file. The twitterpymain.py script prompts the user to choose a prefix file name and the number of CSVs created. Each CSV is limited to 15 mb of data.
### Step 2: Upload the CSV files to R and separate into data frames, one per team
This is done with an R script.
### Step 3: Filtering out irrelevant tweets
Right now this is done with filtering common irrelevant terms. Long-term I hope to build an algorithm that can determine if the tweet is relevant to the sport. For instance, filtering for 'patriots' culls not just tweets related to the NFL's New England Patriots, but also many irrelevant political tweets. I am building a dictionary of sports terms and hashtags using what is trending, searching the term on Twitter, and noting to what sport and team each term refers.
### Step 4: Sentiment analysis of each team's tweets
This is done with tidytext and tm. One interesting tweak that needs to be made to the sentiment lexicon is that the word "madden", which has negative connotations on its own, is also the surname of beloved NFL coach, commentator, and video game namesake John Madden.
