import requests
from bs4 import BeautifulSoup
url = "https://www.linkedin.com/learning/topics/technology?entityType=COURSE"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
print(soup)
url2="https://www.linkedin.com/learning-api/searchV2?categorySlugs=List(technology)&facets=List(entityType^%^3DCOURSE)&q=categorySlugs&searchRequestId=1qkx5oXYTSWKkwbPyqRKLQ^%^3D^%^3D&sortBy=RELEVANCE&start=[1-70]0"
response2 = requests.get(url2)
soup2= BeautifulSoup(response.text, "lxml")
print("baslaiki")
print(soup2)

#print(soup)
#hrefler = soup.find_all('a',href=True)
#for a in hrefler:
#    print (a['href'])

#print(hrefler['href'])
#for a in hrefler:
#    print (a['href'])

