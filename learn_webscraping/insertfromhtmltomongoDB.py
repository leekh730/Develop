from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests

path = 'datas/sample03.html'
db_url = 'mongodb://192.168.219.112:27017/' 
# 192.168.219.112는 개인 IP => linux terminal에 ip address show 치면 나오는 내용 중 inet이라는 글자 뒤에 나오는 IP가 개인 IP

with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    links = soup.select('p[id]')
    with MongoClient(db_url) as client:
        sampledb = client['sample03db']
        title = ''
        link = ''
        for link in links:
            title = str.strip(link.get_text())
            link = link['id']
            data = {'title':title, 'id':link}
            infor = sampledb.sampleCollection.insert_one(data)