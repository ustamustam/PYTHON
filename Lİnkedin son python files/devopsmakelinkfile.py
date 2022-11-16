import urllib3
from bs4 import BeautifulSoup
import csv

http=urllib3.PoolManager()
data = open('Devops.txt', 'r')
soup = BeautifulSoup(data, 'html.parser')
hrefler = soup.find_all('a',class_='ember-view entity-link',href=True)
#print(hrefler)
liste=[]
liste2=[]
#print(liste)

for a in hrefler:
    satir=a['href']
    if satir not in liste:
        linksatir="https://www.linkedin.com"+satir
        d=0
        for b in linksatir:
            if b=="/":
                d=d+1
       # print(d)
        liste.append(satir)
        if d==4:
            liste2.append(linksatir)

with open('Devops2.txt', 'w') as filehandle:
    for listitem in liste2:
        filehandle.write('%s\n' % listitem)

