from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com/search?q=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&oq=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&aqs=chrome..69i57.1167j0j7&sourceid=chrome&ie=UTF-8'
res = requests.get(url=url)
soup = BeautifulSoup(res.content, 'html.parser')
soupa = soup.find_all('a')
print(type(soupa), soupa)

