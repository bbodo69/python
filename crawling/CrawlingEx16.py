from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup
from pprint import pprint

# 썸네일 가져오기
url = 'https://comic.naver.com/webtoon/weekday.nhn?order=StarScore'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# 요일별로 웹툰 영역 추출
data = soup.find_all('div', {'class':'col_inner'})
# pprint(data)
# 전체 웹툰 리스트
li_list = []
for d in data:
    li_list.extend(d.find_all('li'))    # li 태그들을 찾아 li_list 에 풀어서 담기

# pprint(li_list)


'''
# 썸네일 이미지 저장
# 라이브러리 추가
from urllib.request import urlretrieve

# 저장할 폴더 생성
os 패키지 기본제공 -> import
'''
import os, errno, re

try:
    if not (os.path.isdir('image')):        # 이미 같은이름의 폴더가 있는지 확인
        os.makedirs(os.path.join('image'))
        # 폴더생성 현재경로를 계산해서 입력한 이름("image") 텍스트를 합쳐 새로운 경로를 생성
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더생성 실패!!!")
        exit()

# 제목과 이미지 링크
for li in li_list:
    img = li.find('img')    # 이미지 태그 추출
    title = img['title']    # 이미지 태그에서 title 속성값(웹툰제목) 추출
    img_src = img['src']    # 이미지 태그에서 image 링크 추출
    print(title, img_src)
    # 제목 글귀 정규표현식으로 수정
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '',title)
    # title에 있는 문자들중 숫자, 영대소문, 한글을 제외한 모든 글자는 
    # 삭제하고 다시 title에 담겠다.
    # 저장
    # urlretrieve(img_src, 'image/'+title+'.jpg')



'''
하나의 요일 구조
<div class="col">
    <div class="col_inner">
        <h4>...월요웹툰</h4>
        <ul>
            <li></li>       // 요일의 한개의 썸네일
            <li></li>       // 요일의 한개의 썸네일
            <li></li>       // 요일의 한개의 썸네일
            ....
        </ul>
    </div>
</div>

리스트 한개 구조 : 한 요일의 한개의 웹툰
<li>
    <div class="thumb">
        <a href="/webtoon/list.nhn?titleId=723414&amp;weekday=sun" onclick="nclk_v2(event,'thm*S.img','','31')">
            <img alt="속삭이는 e로맨스" height="90" onerror="this.src='https://ssl.pstatic.net/static/comic/images/migration/common/blank.gif'" src="https://shared-comic.pstatic.net/thumb/webtoon/723414/thumbnail/thumbnail_IMAG10_9085b8b9-d7ac-4cee-be86-b104cd2fa72e.jpg" title="속삭이는 e로맨스" width="83"/><span class="mask"></span>
        </a>
    </div>
    <a class="title" href="/webtoon/list.nhn?titleId=723414&amp;weekday=sun" onclick="nclk_v2(event,'thm*S.tit','','31')" title="속삭이는 e로맨스">속삭이는 e로맨스</a>
</li>
'''
