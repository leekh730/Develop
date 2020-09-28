from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path='/home/rapa/Documents/Develop/chromedriver')
driver.get(url="https://www.google.com")
search_form = driver.find_element(By.TAG_NAME,'form')
search_box = search_form.find_element(By.NAME, 'q')
time.sleep(3)
search_box.send_keys("webdriver")
time.sleep(3)
search_box.send_keys(Keys.RETURN)
elements = driver.find_elements(By.XPATH, '//a[@href]')
for e in elements:
    if e != None:
        print(type(e.text), repr(e.text))

# 해보기
# driver = webdriver.Chrome(executable_path='/home/rapa/Documents/Develop/chromedriver')
# driver.get(url="https://www.daum.net")
# #searching_form = driver.find_element(By.TAG_NAME, 'fieldset') # 이것도 가능
# searching_form = driver.find_element_by_class_name("box_search") # 이것도 가능
# searching_box = searching_form.find_element(By.NAME, "q")
# time.sleep(5)
# searching_box.send_keys("딥러닝")
# time.sleep(5)
# searching_box.send_keys(Keys.RETURN)
# print(...)
