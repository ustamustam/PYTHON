import requests
from bs4 import BeautifulSoup
url = "https://www.linkedin.com/learning/python-for-students/getting-set-up-on-a-pc-using-windows"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
hrefler = soup.find_all('a',class_='video__link',href=True)
#print(hrefler['href'])
list1=[]
for a in hrefler:
    list1.append(a['href'])
    print(list1)

#    print (a['href'])


#quotes = soup.find_all('a', class_='video__link')
#quotes = soup.find_all('span', class_='text')
#for i in range(0,len(quotes)):
#print(quotes)