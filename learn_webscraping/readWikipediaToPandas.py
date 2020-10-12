import requests
import pandas as pd
from bs4 import BeautifulSoup

wikipage = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)"
result = requests.get(wikipage)

if result.status_code == 200:
    soup = BeautifulSoup(result.content, 'lxml')

table = soup.find('table', {'class':'wikitable sortable'})

new_table = []
new_table2 = []
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    new_table.append([column.get_text() for column in columns])
    #[column.get_text() for column in columns]
    # listtmp=[]
    # for column in columns:
    #     result = column.get_text()
    #     listtmp.append(column.get_text())
    # #new_table.append()
    # new_table2.append(listtmp)

# for row in table.find_all('tr')[1:]:
#     columns = row.find_all('td')
#     new_table.append(columns)
#     for column in columns:
#         column.get_text()



df = pd.DataFrame(new_table, columns=['ContinentCode', 'Alpha2', 'Alpha3', 'PhoneCode', 'Name'])
df['Name'] = df['Name'].str.replace('\n','')
print(df)

df.to_csv("Wikipedia_example.csv", mode='w') # csv파일로 저장, mode'w'는 작성, 'a'는 추가

call = pd.read_csv("Wikipedia_example.csv", index_col=0) # csv파일 불러오기, index_col=0은 인덱스 column을 0번째 줄로 정하겠다는 의미
print(call)
