from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/home/rapa/Documents/Develop/chromedriver')
driver.get(url='https://www.google.com')
driver.find_element(By.NAME, 'q').send_keys('webdriver'+Keys.ENTER)

SearchInput = driver.find_element(By.NAME, 'q')
time.sleep(5)
SearchInput.clear()

SearchInput.send_keys('selenium')

elements = driver.find_elements(By.XPATH, '//a[@href]')
for e in elements:
    if e != None:
        print(type(e.text), repr(e.text))

SearchInput.clear()
time.sleep(10)
driver.quit()
