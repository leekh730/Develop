import requests, json
import pandas as pd


url = 'https://openapi.naver.com/v1/search/news.json?query=스마트'
headers = {'X-Naver-Client-Id':'uITSoiE2UkJrXzFoSDoB','X-Naver-Client-Secret':'HKHnXjUbh9'}
response = requests.get(url=url, headers=headers)
response.raise_for_status()

rt_dict = json.loads(response.content)
print(rt_dict.keys())

print(pd.DataFrame(rt_dict['items']))