'''
*** selenium ***                    동적인 페이지에서는 셀레늄을 사용. 새로운 작업이 실행될때마다 데이터를 받음.
# 셀레늄 설치+사용
1. 크롬 브라우저 버전 정보
2. 크롬 드라이버 다운
3. 작업하는 파이썬 파일과 동일한 폴더에 압축해제한 크롬드라이버.exe 파일 놓기
'''

# 라이브러리 임포트
from selenium import webdriver
import time

#1. 브라우저 띄우기
driver = webdriver.Chrome('chromedriver.exe')
url = "http://www.google.com/maps/"
driver.get(url)
# driver.implicitly_wait(3)
time.sleep(5)

# 지도 검색
driver.find_element_by_id('searchboxinput').send_keys('서울대입구 맛집')
driver.find_element_by_id('searchbox-searchbutton').click()
time.sleep(5)

# # 한번 클릭
# box = driver.find_element_by_xpath('//div[@role="listbox"]/div[@data-result-index="1"]').click()
# time.sleep(5)
#
# # title = driver.find_element_by_xpath('//div[@class="section-hero-header-title-desc')
# # print(title.text)
# add = driver.find_element_by_xpath('//div[@data-section-id="ad"]')
# print("주소:", add.text)
# phone = driver.find_element_by_xpath(('//div[@data-section-id="pn0"]'))
# # 뒤로가기
# driver.back()

for i in range(1,21):
    driver.implicitly_wait(3)
    box = driver.find_element_by_xpath('//div[@role="listbox"]/div[@data-result-index="%d"]' %i).click()
    time.sleep(3)

    # 썸네일 정보
    try:
        title = driver.find_element_by_xpath('//div[@class="section-hero-header-title-description"]')
        print(title.text)
    except Exception:
        pass
    # 주소
    try:
        add = driver.find_element_by_xpath('//div[@data-section-id="ad"]')
        print("주소:", add.text)
    except Exception:
        pass
    # 전화번호
    try:
        phone = driver.find_element_by_xpath(('//div[@data-section-id="pn0"]'))
        print("전화번호 : ", phone.text)
    except Exception:
        pass

    # 브라우저 뒤로 돌아가기
    back_btn = driver.find_element_by_xpath('//button[@jsaction="pane.place.backToList"]')
    driver.implicitly_wait(3)
    back_btn.click()

    # 뒤로가기
    # driver.back()