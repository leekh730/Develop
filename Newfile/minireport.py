from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3
import time

base_url = "https://movie.naver.com/movie/point/af/list.nhn?&page={}"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

# start_pg = int(input("Start p.g : "))
# end_pg = int(input("End p.g : "))

# for page in range(start_pg,end_pg+1):
for page in range(1,3):
    url = base_url.format(page)
    res = requests.get(url=url, headers=headers)
    res.raise_for_status() # status_code가 200이 아니면 바로 실행 취소
    soup = BeautifulSoup(res.text, "lxml")
    table = soup.find("table", attrs={"class":"list_netizen"})
    li_num = table.select(selector="td[class]")
    li_num1 = li_num[0].get_text()
    print(li_num1)

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