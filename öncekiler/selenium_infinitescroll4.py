import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromrdriver = "c:\windows\chromedriver"
os.environ["webdriver.chrome.driver"] = chromrdriver
driver = webdriver.Chrome(chromrdriver)
driver.get("https://www.linkedin.com/learning/topics/technology?entityType=COURSE&sortBy=POPULARITY")

ScrollNumber = 1000
for i in range(1,ScrollNumber):
    driver.execute_script("window.scrollTo(1,100000000)")
    time.sleep(1)

file = open('Technologycourses.txt', 'w')
file.write(driver.page_source)
file.close()
driver.close()