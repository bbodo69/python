import requests
from bs4 import BeautifulSoup

# 네이버 실시간 검색어 가져오기

# 간혹 크롤링이 안될 때 밑에 헤더를 만들어 보면 될 때도 있다.
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

url = "https://datalab.naver.com/keyword/realtimeList.naver?age=30s&where=main"
res = requests.get(url, headers=headers)
print(res)
soup = BeautifulSoup(res.content, 'html.parser')

content02 = soup.find_all('span', 'item_title')
print(content02)
for i in content02:
    print(i.text)

# content01 = soup.find_all(class_="item_title")
# print(content01)
# print(type(content01))



# copy element : class 속성값
# <span class="item_title">김미균</span>
# <span class="item_title">미스터트롯 진</span>

# ======================================================================================================== 여기까지 공통점
#content > div > div.selection_area > div.selection_content > div.field_list > div > div > ul:nth-child(1) > li:nth-child(1) > div > span.item_title_wrap > span
#content > div > div.selection_area > div.selection_content > div.field_list > div > div > ul:nth-child(1) > li:nth-child(6) > div > span.item_title_wrap > span

