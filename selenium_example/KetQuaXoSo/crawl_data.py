import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import date, datetime

driver = webdriver.Chrome("D:\\UpW\\Python_Script\\chromedriver.exe")
url = 'https://www.thantai.net/so-ket-qua'
status_code = driver.get(url)
time.sleep(1)

if status_code == 200:
    driver.close()
    exit()

#Set date
date_element = driver.find_element_by_id('end')
date_element.clear()
date_element.send_keys("{0}-{1}-{2}".format('10','05','2022'))
time.sleep(2)

button_300_counts_element = driver.find_element_by_xpath('//*[@id="skq"]/form/div[2]/div/button[9]')
button_300_counts_element.click()
time.sleep(3)

# Get date and specific result

page_source = BeautifulSoup(driver.page_source, 'html.parser')
print(page_source)

