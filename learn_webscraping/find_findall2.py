from bs4 import BeautifulSoup
import re

with open('datas/sample02.html')as fp:
    soup = BeautifulSoup(fp, features='lxml')

result = soup.find_all(name=re.compile("^b")) # regular express
print(type(result), result)

for tag in result:
    print(type(tag), tag, type(tag.name), tag.name)

gettag = result[0].find_all('a')
print(type(gettag), gettag)
