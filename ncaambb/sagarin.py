# small script to collect the week's Sagarin ranking directly from his website
# AP 25 poll is at
# https://www.ncaa.com/rankings/basketball-men/d1/associated-press
from bs4 import BeautifulSoup
import requests
import re

import pandas as pd

sagarin = 'http://sagarin.com/sports/cbsend.htm'
def souper(url):
    try:
        response = requests.get(url).content
        return BeautifulSoup(response, 'html5lib')
    except:
        return
    
# webmaster splits the content of the page into <pre> tags. The second one
# contains the info we want
webtext = souper(sagarin).find_all('pre')[1].text

# printing first 800 characters to make sure we're scraping the right data
print(webtext[300:800])

# now to do some regex to clean our data
# pattern is integer space schoolname space equalsign space rating
# (which has two decimal places)
stat = re.compile(r'[\d]{1,3}[\s]+[\D]+[=]{1}[\s]+[\d]+.{1}[\d]{2}')
# list that should contain all schools
stats = re.findall(stat, webtext)
print(len(stats)) # should be 353
stats = [re.sub(r'[\s]{2,}[=]', ' =',x) for x in stats]
stats = [re.sub(r'^[\d]{1,3}[\s]+', '',x) for x in stats]
# turning into dictionary
stats = [re.split(r'=',x) for x in stats]
statsnames = [ re.sub(r'\s$', '',x[0]) for x in stats]
statsranks = [ float(re.sub(r'\s+', '',x[1])) for x in stats]
statsdict = dict(zip(statsnames, statsranks))
# tuning into data frame
mydf = pd.DataFrame(list(zip(statsnames, statsranks)), columns = ["Team", "Ranking"]
