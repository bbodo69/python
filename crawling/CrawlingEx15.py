import requests
from bs4 import BeautifulSoup
from pprint import pprint

# 네이버 웹툰 제목 가져오기
url = 'https://comic.naver.com/webtoon/weekday.nhn?order=StarScore'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
res.close()
# 커넥션 끊기
# 요일 한 기둥
# #content > div.list_area.daily_all > div.col.col_selected > div.col_inner
div = soup.find_all('div',{'class':'col_inner'}) # 첫번째 col_inner div 태그만 가져옴
titles = div.find_all('a', 'title')     # 첫번째 요일기둥에서 a.title 태그만 가져오기

title_list = []

for t in titles:
    title_list.append(t.text) # a태그의 text만 뽑아서 리스트에 저장

pprint(title_list)

t_list = [t.text for t in titles]

print("================================")

div = soup.find_all('div',{'class':'col_inner'})

week_list = []
for d in div:
    # 하나의 요일에서 제목 영역 추출
    titles = d.find_all('a', 'title')
    title_list = [t.text for t in titles]
    week_list.append(title_list)

pprint(week_list)







