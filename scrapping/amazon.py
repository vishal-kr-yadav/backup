import urllib2
from bs4 import BeautifulSoup
import requests
import pandas as pd
import unicodedata
import re

dict={}
counter=0

res = requests.get("https://www.amazon.in/Apple-iPhone-Space-Grey-256GB/dp/B072LNNSQN/ref=sr_1_4?s=electronics&ie=UTF8&qid=1519143645&sr=1-4&keywords=iphone+x&dpID=41wUnHPGFBL&preST=_SY300_QL70_&dpSrc=srch")
soup = BeautifulSoup(res.content, 'lxml')
for each in soup.find_all('div',attrs={'class':'a-section review'}):
    # table = pd.DataFrame(
    #     {"Date": each.text
    #      },index=[0]
    # )
    # print(table)
    key='Review'+str(counter)
    dict[key]=unicodedata.normalize('NFKD', re.sub('\s+',' ',each.text)).encode('ascii', 'ignore')
    counter+=1
    break
print(dict)