from bs4 import BeautifulSoup

path = 'datas/sample01.html' # from File
with open(path) as fp:       # Safe Return Resource
    soup = BeautifulSoup(fp, features='lxml')
    print(type(soup),soup)
# <class 'bs4.BeautifulSoup'><html><body><p>a web page</p></body></html>

import requests # from URL
res = requests.get('https://google.com/')
print(res.status_code, res._content)
soup = BeautifulSoup(res.content, features='lxml')
print(type(soup), soup.prettify())
# 200b'<!doctype html><html itemscope=""itemtype="http://schema.org/..."
# <class 'bs4.BeautifulSoup'><html><body><p>a web page</p></body></html>
# Create instance From URL (at least 3site) and share source with google Doc
