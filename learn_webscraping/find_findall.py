from bs4 import BeautifulSoup

with open('datas/sample02.html')as fp:
    soup = BeautifulSoup(fp, features='lxml')

print(type(soup.find(id="link3")), soup.find(id="link3"))
# <class 'bs4.element.Tag'> <a class="sister" href="http://example03.com/tillie" id="link3">Tillie</a>

print(type(soup.find_all(name='a')), soup.find_all(name='a'))
# <class 'bs4.element.ResultSet'> [<a class="sister" href="http://example01.com/elsie" id="link1">
#     Elsie
#    </a>, <a class="sister" href="http://example02.com/lacie" id="link2">
#     Lacie
#    </a>, <a class="sister" href="http://example03.com/tillie" id="link3">
#     Tillie
#    </a>]

print(type(soup.find_all(name='b')), soup.find_all(name='b'))
# <class 'bs4.element.ResultSet'> [<b>The Dormouse's story</b>]

print(type(soup.find_all(name=["a","b"])), soup.find_all(name=["a","b"]))
# <class 'bs4.element.ResultSet'> [<b>
#     The Dormouse's story
#    </b>, <a class="sister" href="http://example01.com/elsie" id="link1">
#     Elsie
#    </a>, <a class="sister" href="http://example02.com/lacie" id="link2">
#     Lacie
#    </a>, <a class="sister" href="http://example03.com/tillie" id="link3">
#     Tillie
#    </a>]

print(type(soup.find_all(id=True)), soup.find_all(id=True))
# <class 'bs4.element.ResultSet'> [<a class="sister" href="http://example01.com/elsie" id="link1">
#     Elsie
#    </a>, <a class="sister" href="http://example02.com/lacie" id="link2">
#     Lacie
#    </a>, <a class="sister" href="http://example03.com/tillie" id="link3">
#     Tillie
#    </a>]

find_attrs = soup.find_all(name='a', attrs={"href":True})
print(type(find_attrs), find_attrs)
# <class 'bs4.element.ResultSet'> [<a class="sister" href="http://example01.com/elsie" id="link1">
#     Elsie
#    </a>, <a class="sister" href="http://example02.com/lacie" id="link2">
#     Lacie
#    </a>, <a class="sister" href="http://example03.com/tillie" id="link3">
#     Tillie
#    </a>]

find_attrs = soup.find_all(name='a', attrs={'class':'sister', 'id':['link2','link3']})
print(type(find_attrs), find_attrs)
# <class 'bs4.element.ResultSet'> [<a class="sister" href="http://example02.com/lacie" id="link2">
#     Lacie
#    </a>, <a class="sister" href="http://example03.com/tillie" id="link3">
#     Tillie
#    </a>]