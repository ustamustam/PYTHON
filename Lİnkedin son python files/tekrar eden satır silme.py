import urllib3
import requests
from bs4 import BeautifulSoup

f = open('alınacaksertifikalar3.txt', 'r')
lines = f.readlines()
f.close()
list1 = []
list2 = []
for a in lines:
    if a.find('path'):
        list1.append(a)
    else:
        list2.append(a)
with open('list1.txt', 'w') as filehandle:
    for listitem in list1:
        filehandle.write('\n' + listitem)
with open('list2.txt', 'w') as filehandle:
    for listitem2 in list2:
        filehandle.write('\n' + listitem2)
