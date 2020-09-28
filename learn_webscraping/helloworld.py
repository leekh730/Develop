from selenium import webdriver
import os

#print(os.getcwd()) # 절대 경로 찾는 방법
driver = webdriver.Chrome(executable_path='/home/rapa/Documents/Develop/chromedriver')
print(type(driver), driver)

driver.get(url='https://www.google.com') # 크롬드라이버로 구글 브라우저 열기
print(type(driver.page_source), driver.page_source)
driver.quit() # 드라이버 종료