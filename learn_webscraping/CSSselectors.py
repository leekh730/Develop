import requests
from bs4 import BeautifulSoup
res = requests.get('https://news.daum.net/economic/')
#print(res.status_code, res.content)

soup = BeautifulSoup(res.content, 'lxml')
links = soup.select(selector='a[href]') # list type
for link in links:
    print(type(links), links)
    break