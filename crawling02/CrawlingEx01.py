'''
(학원 컴퓨터 기준 Win7)
사전필요
.NET Framework 최신버전 (lxml, oracle...)
VS build tool

# lxml 설치 방법 2가지. (설치 시 컴퓨터 환경에 따라 설치가 잘 되지 않음. , 환경 변수가 설치 안됬을시에도)

    # 1. cmd > pip install lxml
    %APPDATA% 검색 후 C:\Users\pc\AppData\Local\Programs\Python\Python38\Lib\site-packages 에서 lxml, lxml-4.5.0.dist-info 설치 되있는지 확인.
    있는데도 실행 안되면 파이참에 직접 venv > lib > site-packages 에 붙여 넣기.

    #2. FIle > setting > 추가해서 lxml 추가 하기, 안되면 위에 처럼

# 파이썬 오라클
cx_Oracle
링크 : https://www.oracle.com/kr/database/technologies/instant-client/downloads.html

## 동적 크롤링
# selenium


'''

import requests
from pprint import pprint
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn?order=StarScore'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'lxml')

div = soup.find_all('div', {'class':'col_inner'})
# pprint(div)

li_list = []
for d in div:
    li_list.extend(d.find_all('li'))

# pprint(li_list)

for li in li_list:
    img = li.find('img')
    title = img['title']
    src = img['src']
    print(title)