import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=469&aid=0000476992"
res = requests.get(url)
print(url)

soup = BeautifulSoup(res.content, 'html.parser')
title = soup.find_all("title")
title1 = soup.find("title")
print(title)
print(type(title))
print(title1.text)
print(type(title1.text))

content = soup.find_all(class_="_article_body_contents")
print(content)

content2 = soup.find(class_="_article_body_contents")
print(content2)