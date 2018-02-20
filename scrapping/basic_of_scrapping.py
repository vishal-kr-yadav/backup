# import urllib2
# from bs4 import BeautifulSoup
#
# #url given for scrapping of a websites
# website_url="https://www.bloomberg.com/quote/SPX:IND"
#
# #with the help of urllib2,url opening
# page=urllib2.urlopen(website_url)
#
# #parsing the html page and storing in a variable
# soup=BeautifulSoup(page,"html.parser")
#
# #fetching some result based on tag and class
# print(soup.find('h1',attrs={'class':'name'}).text)
# print(soup.find('div',attrs={'class':'price'}).text)



# #As a json from a table
# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
#
# res = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
# soup = BeautifulSoup(res.content,'lxml')
# table = soup.find_all('table')[0]
# df = pd.read_html(str(table))
# # print(df[0].to_json(orient='records'))


# #Pretty print pandas dataframe
#
# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# from tabulate import tabulate
#
# res = requests.get("https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20180121&end=20180220")
# soup = BeautifulSoup(res.content, 'lxml')
# table = soup.find_all('table')[0]
# df = pd.read_html(str(table))
# print(tabulate(df[0], headers='keys', tablefmt='psql'))


#creating data frame for only two columns
import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get("https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20180121&end=20180220")
soup = BeautifulSoup(res.content, 'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))[0]
Date = df["Date"].tolist()
ETH_Close = df["Close"].tolist()
table=pd.DataFrame(
    {"Date":Date,
     "Close":ETH_Close}
)
print(table)