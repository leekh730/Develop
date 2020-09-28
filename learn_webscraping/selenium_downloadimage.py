import wget
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/home/rapa/Documents/Develop/chromedriver')
url = 'https://www.coupang.com/np/search?q=컴퓨터'
driver.get(url=url)

elements = driver.find_elements(By.XPATH,'//img[@class="search-product-wrap-img"]')
down_path = 'Pictures/'
for element in elements:
    src = element.get_attribute('src')
    img_txt = src.split('/')[-1]
    image_name = down_path+img_txt
    
    #first way
    wget.download(url=src, out=image_name)

    #second way
    # with urllib.request.urlopen(src)as response, open(image_name,'wb')as out_file:
    #     data = response.read()
    #     out_file.write(data)