# small script to collect the current NCAA NET ranking
# NCAA NET replaced RPI
# https://www.ncaa.com/rankings/basketball-men/d1/ncaa-mens-basketball-net-rankings
from bs4 import BeautifulSoup
import requests
import re
import time

import pandas as pd

neturl = 'https://www.ncaa.com/rankings/basketball-men/d1/ncaa-mens-basketball-net-rankings'
def souper(url):
    try:
        response = requests.get(url).content
        return BeautifulSoup(response, 'html5lib')
    except:
        return
    
# webmaster splits the content of the page into <pre> tags. The second one
# contains the info we want
webtext = souper(neturl).find("article", class_ ="rankings-content overflowable-table-region layout--content-left")
webtext = webtext.find("tbody").find_all("tr")
# each row is one school
listing = [x.find_all("td") for x in webtext]
# have to extract rank and school name
rank = [int(x[0].text) for x in listing]
name = [x[2].text for x in listing]
# getting date of last update

datemade = souper(neturl).find("figure", class_ ="rankings-last-updated").text
datemade = re.sub(r'\n[\s]+Through Games ', '', datemade)
datemade = re.sub(r'\n', '', datemade)

#putting it together into a dataframe

mydf = pd.DataFrame(data = list(zip(rank, name)), columns = ["Rank", "School"])
mydf['Date'] = pd.to_datetime(datemade)
