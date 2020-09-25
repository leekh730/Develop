from bs4 import BeautifulSoup

with open('datas/sample02.html')as fp:
    soup = BeautifulSoup(fp, features='lxml')

# Going sideways -.next_sibling and .next_siblings
link = soup.a
print(type(link), link)
print(type(link.next_sibling), link.next_sibling)
# <class 'bs4.element.NavigableString'>'/n'

print(type(link.next_sibling.next_sibling), link.next_sibling.next_sibling)
# <class 'bs4.element.Tag'><a class="sister" href="http://..."id="link2">Lacie</a>

# .next_sibling and .previous_siblings
for sibling in soup.a.next_siblings:
    print(type(sibling), repr(sibling)) # returns a printable representation
    # <class 'bs4.element.NavigableString'>'/n'
    # <class 'bs4.element.Tag'><a class="sister" href="http:/..."id="link2">Lacie</a>
    # ...
    # <class 'bs4.element.NavigableString'>'and they lived at the bottom of a well.'