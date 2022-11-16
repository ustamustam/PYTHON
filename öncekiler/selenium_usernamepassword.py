import requests
from bs4 import BeautifulSoup
url = "C:\Users\user\PycharmProjects\OpenandReadfFile\cloudcomuting.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
print(soup)