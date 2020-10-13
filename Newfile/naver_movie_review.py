from bs4 import BeautifulSoup
import requests
import time
from pymongo import MongoClient
import schedule

base_url = "https://movie.naver.com/movie/point/af/list.nhn?&page={}"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
#headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
db_url = 'mongodb://192.168.219.124:27017/' # ip는 계속 바뀐다. 그러므로 항상 ip주소를 재확인하자

# start_pg = int(input("Start p.g : ")) # 시작 페이지 선택
# end_pg = int(input("End p.g : ")) # 끝 페이지 선택

def job():
    #for page in range(start_pg,end_pg+1):
    for page in range(1,2):
        url = base_url.format(page)
        res = requests.get(url=url, headers=headers)
        res.raise_for_status() # status_code가 200이 아니면 바로 실행 취소
        soup = BeautifulSoup(res.text, 'lxml')
        # 번호
        listnum = soup.find_all("td", attrs={"class":"ac num"})

        # 영화제목
        listtitle = soup.find_all("a", attrs={"class":"movie color_b"})

        # 별점
        liststar = soup.find_all("div", attrs={"class":"list_netizen_score"})

        # 댓글
        listtext = soup.find_all("a", attrs={"class":"report"})

        # 글쓴이 + 날짜
        listauthor = soup.find_all("td", attrs={"class":"num"})
        listauthor_date = listauthor[1::2]

        with MongoClient(db_url) as client:
            moviedb = client['moviedb']

            for a,b,c,d,e in zip(listnum, listtitle, liststar, listtext, listauthor_date):
                num = a.get_text() # 번호만 출력
                title = b.get_text() # 감상평에 영화제목만 출력
                star = c.get_text() # 별점만 출력
                text = d.get('href').split(',')[2] # 댓글만 출력
                author_date = e.get_text() # 글쓴이+날짜 출력
                star = star.replace('\n','') # 별점에서 \n 제거
                #print(num, title, star, text, author_date)
                #time.sleep(1)

                dic = {'번호':num, '영화제목':title, '평점':star, '감상평':text, '글쓴이+날짜':author_date}
                moviedb.review.insert_one(dic)

    print("I'm working...")

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
