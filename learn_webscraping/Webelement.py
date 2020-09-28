from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/home/rapa/Documents/Develop/chromedriver')
driver.get(url="https://www.google.com")
search_form = driver.find_element(By.TAG_NAME,'form')
print(type(search_form),search_form)

# search_box = search_form.find_element(By.NAME, 'q')
# search_box.send_keys("webdriver")

searching = search_form.find_element_by_name('q')
searching.send_keys("에놀라 홈즈")

time.sleep(2)
searching.send_keys(Keys.RETURN)

time.sleep(3)
driver.quit()