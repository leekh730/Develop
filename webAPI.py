import requests
from bs4 import BeautifulSoup

info_url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'
response = requests.get(info_url)
soup = BeautifulSoup(response.content, 'lxml')

#locations = soup.find_all('location')
#print(type(locations))
# for location in locations:
#     print(location.find('city').get_text(), ":", location.find('wf').get_text())

loca = soup.select(selector='city') # list type
# for i in loca:
#     print(i.text) # text만 추출
wea = soup.select(selector='wf') 
lowea = dict(zip(loca, wea)) #list type을 Dict 타입으로 전환
#print(lowea)

loca_wea = soup.select('city+wf')
for i in loca_wea:
    print(i)