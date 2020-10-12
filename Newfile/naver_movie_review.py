from bs4 import BeautifulSoup
import requests
import time

base_url = "https://movie.naver.com/movie/point/af/list.nhn?&page={}"
# headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

start_pg = int(input("Start p.g : ")) # 시작 페이지 선택
end_pg = int(input("End p.g : ")) # 끝 페이지 선택

for page in range(start_pg,end_pg+1):
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
    
    for a,b,c,d,e in zip(listnum, listtitle, liststar, listtext, listauthor_date):
        num = a.get_text() # 번호만 출력
        title = b.get_text() # 감상평에 영화제목만 출력
        star = c.get_text() # 별점만 출력
        text = d.get('href').split(',')[2] # 댓글만 출력
        author_date = e.get_text() # 글쓴이+날짜 출력
        print(num, title, star, text, author_date)
        time.sleep(3)
