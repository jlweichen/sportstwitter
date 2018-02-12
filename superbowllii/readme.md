### Super Bowl LII: Revenge of the Birds
I used my Python scripts to follow Twitter during the Super Bowl on February 4, 2018. My goal is to perform sentiment analysis on the tweets posted during this historic game in which the Philadelphia Eagles clinched their first Lombardi Trophy over the favored New England Patriots.
#### The CSVs
Over the course of the day, I saved twenty CSV files worth of tweets, each file being 15 mb in size. I did not filter for language, though most of the tweets are in English. Each CSV contains over 100,000 tweets, containing username, tweet, and timestamp. I filtered the streaming API with the footballterms.py list of terms. The team name, head coach surname, and starting quarterback surname for each team was included. The remaining terms were the names of other players, team cheers, the stadium name, and the phrase 'super bowl'.
#### The Teams
The first analysis of tweets simply divided along team lines: I sorted the tweets between those mentioning the Eagles, and those mentioning the Patriots. Tweets mentioning both teams were included in both teams' analyses.
