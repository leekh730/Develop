from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3
import time

base_url = "https://movie.naver.com/movie/point/af/list.nhn?&page={}"
# headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

# start_pg = int(input("Start p.g : "))
# end_pg = int(input("End p.g : "))

# for page in range(start_pg,end_pg+1):
# for page in range(1,3):
#     url = base_url.format(page)
#     res = requests.get(url=url, headers=headers)
#     res.raise_for_status() # status_code가 200이 아니면 바로 실행 취소
#     soup = BeautifulSoup(res.text, "lxml")
#     table = soup.find("table", attrs={"class":"list_netizen"})
#     li_num = table.select(selector="td[class]")
#     li_num1 = li_num[0].get_text()
#     print(li_num1)

    # new_table=[]
    # for tbody in table.find_all('tr')[1:]:
    #     columns = tbody.find_all('td')
    #     new_table.append([column.get_text() for column in columns])

    # print("="*200)

    # df = pd.DataFrame(new_table, columns=['No', 'Comment', 'Writer'])
    # df['Comment'] = df['Comment'].str.replace('\n','')
    # df['Comment'] = df['Comment'].str.replace('\t','')
    # print(df)

# Connect to SQLite3 DB 

# https://yceffort.kr/2018/11/05/web-crwaling-for-naver-movie/ => 네이버리뷰 스크래핑 참고


url = base_url.format(1)
res = requests.get(url=url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 번호만 출력
listnum = soup.find_all("td", attrs={"class":"ac num"})
# for i in listnum:
#     print(i.get_text()) 

# 감상평에 영화제목만 출력
listtitle = soup.find_all("td", attrs={"class":"title"})
# for i in listtitle:
#     title = i.find("a", attrs={"class":"movie color_b"}).get_text()
#     print(title) 

# 별점만 출력
liststar = soup.find_all("div", attrs={"class":"list_netizen_score"})
# for i in liststar:
#     print(i.get_text())

# 댓글만 출력
listreview = soup.find_all("a", attrs={"class":"report"})
# for i in listreview:
#     a = i.get('href').split(',')[2]
#     print(a)

# 영화제목, 별점, 댓글 출력
listtext = soup.find_all("td", attrs={"class":"title"})
# print(listtext[0].get_text())
# for i in listtext:
#     text = i.get_text()
#     a = text.strip()
#     b = a.replace("신고","")
#     c = b.strip()
#     print(c)
#     time.sleep(5)

# 글쓴이+날짜 출력
listauthor = soup.find_all("td", attrs={"class":"num"})
# for i in listauthor[1::2]:
#    print(i.get_text())