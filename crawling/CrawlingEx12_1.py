import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20200315'

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

content = soup.find_all(class_="tit5")
point01 = soup.find_all(class_="point")

titles = soup.find_all('td', 'title')
point = soup.find_all('td','point')

for i in range(len(titles)):
    print("제목 : ", titles[i].text.strip(), "    점수 : " , point[i].text.strip())

print("========================")

for i in range(len(content)):
    print("제목 : ", content[i].text.strip(), "    점수 : " , point01[i].text.strip())