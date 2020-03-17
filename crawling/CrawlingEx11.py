'''

'''

import requests
from bs4 import BeautifulSoup

## 네이터 속보 가져오기

for i in range(1,6):
    url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date=20200316&page="+str(i)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    content2 = soup.select('ul.type06_headline > li > dl > dt:nth-child(2) > a')



    content = soup.find_all(class_="nclicks(fls.list)")
    # print(content)

    for a in content:
        print(type(a))
        print(a.text.strip())       # 텍스트만 뽑아주기, strip() - 공백 없애주기

