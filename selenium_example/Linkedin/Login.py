import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome("D:\\UpW\\Python_Script\\chromedriver.exe")
url = 'https://www.linkedin.com/login'
driver.get(url)

time.sleep(3)
username = ''
password = ''

with open('pass.txt','r') as file:
    lines = file.readlines()
    username = lines[0]
    password = lines[1]

# Login Enter text in text box
email_element = driver.find_element_by_id('username')
email_element.send_keys(username)
time.sleep(3)
pass_element = driver.find_element_by_id('password')
pass_element.send_keys(password)
time.sleep(2)
# Click button
login_button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
login_button.click()

time.sleep(4)
# Completed login search 'software engineer people'
search_element = driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input')
search_element.send_keys('software engineer people')
time.sleep(2)
search_element.send_keys(Keys.ENTER)
time.sleep(2)

# Scrape all URLs of the profile.
# Load a page source 
page_source = BeautifulSoup(driver.page_source)
time.sleep(2)
#profiles = page_source.find_all('a', class_ = #)

