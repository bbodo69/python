import requests
from bs4 import BeautifulSoup
'''
# 웨에서 데이터 가져오는 순서
- reuquests.get() 이요ㅕㅇ하여 웹 페이지 가져오기
- BS 으로 파싱
- find() find_all() 이용하여 필요한 데이터 검색
'''

url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=005&aid=0001298986"
res = requests.get(url)
print(res)
# print(res.content)

#2. BS 파싱
soup = BeautifulSoup(res.content, 'html.parser')
title = soup.find("title")
print(title.text)

# select() : 필요한 데이터 검색 (선택자)
# soup.select_one (선택자)
# soup.select(선택자) <p class="img" ></p>
imgs = soup.select('.img')
print(imgs)
news_title = soup.select('#articleTitle')
print(news_title[0].text)


print("==================================================================")
print(soup.find_all(class_='media_end_summary'))
print(soup.find_all(class_='tts_head'))
