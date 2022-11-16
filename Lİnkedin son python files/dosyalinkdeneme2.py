import urllib3
import requests
from bs4 import BeautifulSoup
f = open('alınacaksertifikalar3.txt', 'r')
lines = f.readlines()
f.close()
list1=[]
list2=[]
#print (lines)
for a in lines:
         b = a.find("<")
         c = a.find(">")
         d = a[b+1:c]
         list1.append(d)
for u in list1:
    response = requests.get(u)
    soup = BeautifulSoup(response.text, "lxml")
#print (soup)
    hrefler = soup.find_all('a',class_='base-card base-card--link base-main-card base-main-card--link',href=True)
    for a in hrefler:
         satir=a['href']
         list2.append(satir)
         print (satir)
with open('dosyalinkdeneme4.txt', 'w') as filehandle:
    for listitem in list2:
        filehandle.write('\n'+ listitem)
#print (hrefler)
#print(hrefler[1]['href'])

#class="base-card base-card--link base-main-card base-main-card--link"