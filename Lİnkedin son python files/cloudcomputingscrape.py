import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromrdriver = "c:\windows\chromedriver"
os.environ["webdriver.chrome.driver"] = chromrdriver
driver = webdriver.Chrome(chromrdriver)
driver.get("https://www.linkedin.com/learning/topics/cloud-computing-5?entityType=COURSE")

ScrollNumber = 200
for i in range(1,ScrollNumber):
    driver.execute_script("window.scrollTo(1,10000000)")
    time.sleep(1)

file = open('cloudcomputingcourses.txt', 'w')
file.write(driver.page_source)
file.close()
driver.close()