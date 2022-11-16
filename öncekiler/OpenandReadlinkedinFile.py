import urllib3
from bs4 import BeautifulSoup
import csv

http=urllib3.PoolManager()
data = open('cloudcomuting.txt', 'r')
soup = BeautifulSoup(data, 'html.parser')
hrefler = soup.find_all('a',class_='ember-view entity-link',href=True)
#print(hrefler)
liste=[]
liste2=[]
print(liste)
for a in hrefler:
    satir=a['href']
    if satir not in liste:
        linksatir="https://www.linkedin.com"+satir
        liste.append(satir)
        liste2.append(linksatir)
with open('listfile2.txt', 'w') as filehandle:
    for listitem in liste2:
        filehandle.write('%s\n' % listitem)

