import urllib3
from bs4 import BeautifulSoup
import csv
http=urllib3.PoolManager()

data = open('webdevelopmentcourses3.txt', 'r')

#print(hrefler)
liste=[]
liste2=[]
#print(liste)

for a in data:
    satir = a.rstrip()

#    print(satir)
    liste.append("'"+satir+"',")
print(liste)
with open('webdevelopmentcourses4.txt', 'w') as filehandle:
    for listitem in liste:
        filehandle.write('%s\n' % listitem)

