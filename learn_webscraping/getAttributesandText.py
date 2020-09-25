from bs4 import BeautifulSoup

with open('datas/sample03.html', 'r', encoding='UTF8')as fp:
    soup = BeautifulSoup(fp, features='lxml')
    title_data = soup.find('h1')                # tag로 검색
    print(type(title_data), '|', title_data,'|', title_data.string)
    print("-"*100)

    title_data = soup.find_all(id='h1_id_name') # id로 검색
    print(type(title_data), '|', title_data, '|', title_data[0].get_text())
    print("-"*100)
    
    title_data = soup.find_all('p',class_='public_class_name') # tag와 class로 검색
    print(type(title_data), '|', title_data, '|', title_data[0].attrs)
    print("-"*100)

    title_data = soup.find_all('p', attrs = {'align':'center'}) # 속성값으로 검색
    print(title_data, '|', title_data[0].string)
    print("-"*100)

    title_data = soup.find_all('a', href=True) # 속성 존재 여부 검색
    print(title_data, '|', title_data[0].string)
    print("-"*100)
