from bs4 import BeautifulSoup

with open('datas/sample02.html')as fp:
    soup = BeautifulSoup(fp, features='lxml')
    print(type(soup.title),soup.title)
    # <class 'bs4.element.Tag'><title>The Dormouse's story</title>

    print(type(soup.title.string), soup.title.string)
    # <class 'bs4.element.NavigableString'>The Dormouse's story

    print(type(soup.p), soup.p)
    # <class 'bs4.element.Tag'><p class="title"><b>The Dormouse's story</b></p>
    
    elementTag = soup.p
    print(type(elementTag.b), elementTag.b)
    # <class'bs4.element.Tag'><b>The Dormouse's story</b>

    print(type(soup.a), soup.a)
    # <a class="sister" href="http://examplet.com/elsie" id="link1">Elsie</a>

    print(type(soup.p['class']), soup.p['class'])
    # <class 'list'>['title']