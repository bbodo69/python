from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20200315'

res = urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
content = soup.find_all(class_="tit5")

titles = soup.find_all('td', 'title')
point = soup.find_all('td','point')
for i in range(len(titles)):
    print("제목 : ", titles[i].text.strip(), "    점수 : " , point[i].text.strip())


print(content.text.strip())