# 인스타그램
from selenium import webdriver
import urllib
import time

keyword = input("검색어 입력 : ")
keyword = urllib.parse.quote(keyword)
url = "https://www.instagram.com/explore/tags/"+str(keyword)+"/"


driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
driver.implicitly_wait(3)

instar_tags = []

# 이미지 클릭 > 해쉬태그 긁기 > ">" 눌러서 다음 포스트로 가서 해쉬태그 긁기
driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()
driver.implicitly_wait(3)
for i in range (10):
    # 해쉬태그들 긁기
    time.sleep(1)
    tags = driver.find_elements_by_css_selector('a.xil3i')
    for t in tags:                  # 해쉬태그들 반복해서 각각 접근
        raw = t.text
        raw = raw.replace('#','') # 해쉬태그 기호 삭제
        instar_tags.append(raw)    # 리스트에 추가
    # 다음 포스트로 넘어가기 클릭
    driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()
    time.sleep(3)       # 너무 빨리 돌아가면 가저오기 전에 넘어가기 때문에 쉬는 타임 넣어줌

print(instar_tags)

# 단어 제거
stop_word = ['스타벅스', '스벅', 'starbucks']
instargram_tag = [word for word in instar_tags if word not in stop_word]

# 워드 클라우드(word cloud) 만들기
import matplotlib.pyplot as pyplot  # 워드 클라우드 뷰어
from wordcloud import WordCloud

wordcloud = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf',
                      background_color='white', max_words=1000).generate(' '.join(instargram_tag))
pyplot.imshow(wordcloud, interpolation='bilinear')
pyplot.axis("off") # x, y 축을 없앰.
pyplot.show()
