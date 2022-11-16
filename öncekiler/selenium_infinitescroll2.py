import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromrdriver = "c:\windows\chromedriver"
os.environ["webdriver.chrome.driver"] = chromrdriver
driver = webdriver.Chrome(chromrdriver)
driver.get("https://www.linkedin.com/learning/topics/data-science?entityType=COURSE")

ScrollNumber = 60
for i in range(1,ScrollNumber):
    driver.execute_script("window.scrollTo(1,50000)")
    time.sleep(1)

file = open('datascience.html', 'w')
file.write(driver.page_source)
file.close()
driver.close()