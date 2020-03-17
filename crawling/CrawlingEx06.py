'''
BeautifulSoup 파밍 모듈
'''
from bs4 import BeautifulSoup
html = """"""

'''
# 파서 parser : 원시코드만 순수 문자열 객체를 해석할 수 있도록 분석하는 것
                파이썬에서 사용되는 파서는 lxml, html5lib, html.parser
# 파서 종류
    lxml (HTML parser)
        BeautifulSoup(html, 'lxml')
        c언어로 구현되어 있어 매우 빠름, 별도로 라이브러리 추가 필요
    lxml (XML parser)
        BeautifulSoup(html, 'lxml-xml')
        매우빠름, 유일하게 지원되는 xml parser
    html5lib
        웹브라우저 형태로 HTML 분석하고 관리
        라이브러리 설치 필요
        매우 느림
    html.parser
        적당한 속도, 라이브러리 추가없이 바로 사용가능    
'''
html = """<p>test</p>"""
html1 = ""
print(html)
print(type(html))
soup = BeautifulSoup(html, 'html.parser')
print(soup)
print(soup.prettify())
print(type(soup))

# res = requests.get(url) -> res.text 또는 res.content 뽑아낸 형태
html = """<html>
<head><title>test title</title></head>
<body> <p>haha</p> <p>haha2</p> </body>
</html>"""

soup = BeautifulSoup(html, 'html.parser')

### 태그명으로 가져오기 : soup.태그명 : 첫번째로 등장하는 태그만 가져옴.
title_tag = soup.title
print(soup.title)
print(type(soup.title))
# text : 태그 내부의 텍스트 : 내부의 하위 태그들도 모두 가져온다.
print(title_tag.text)
print(type(title_tag.text))
# string " 태그 내부의 텍스트 : 정확하게 해당 태그에 대한 한 값만 가져온다.
print(title_tag.string)
print(type(title_tag.string))

# 2. 태그의 속성으로 접근하기
html = """<html>
<head><title class="t" id="tid">test title</title></head>
<body> <p>haha</p><p>haha2</p> </body>
</html>"""

soup = BeautifulSoup(html, 'html.parser')
p_tag = soup.p
print(p_tag)

# 타이틀 태그만 가져오기
title_tag = soup.title
print(title_tag.attrs)
print(title_tag['class'])
print(title_tag['id'])


html = """<html>
<head><title class="t" id="tid">test title</title></head>
<body> <p><span>haha</span><span>haha2</span></p> </body>
</html>"""

soup = BeautifulSoup(html, 'html.parser')
p_tag = soup.p
print(p_tag)

text_data = p_tag.text
string_data = p_tag.string

print("text : ", text_data)
print("string : ", p_tag.string_data)
print("string : ", p_tag.span.string)

# 원하는 요소 정확히 접근하기
html = """<html>
<head><title class="t" id="tid">test title</title></head>
<body> <p id = "a" class="a">haha</p><p>haha2</p> </body>
</html>"""
soup = BeautifulSoup(html, 'html.parser')
# find_all() : 원하는 태그들을 리스트 형태로 얻어 올 수 있다.
# 1. 태그명으로 가져오기
print(soup.find_all('title'))
print(soup.find_all('p'))
print(soup.find_all(id='a'))

#2. id 속성으로 가져오기
print(soup.find_all)
#3. 속성 존재 여부로 가져오기
print(soup.find_all(id=True))
#print(soup.prettify().find_all(id=True))
print(soup.find_all(id=False))

#4. 태그, id 속성값 두개 지정해서 찾기
print(soup.find_all('title', class_='t'))
# 두번째 매개변수인 class_ 속성은 속성명
print(soup.find_all('p','a'))
# print(soup.find_all('a', href='http://www.naver.com'))
# print(soup.find_all('image', href='http://www.naver.com/.png'))
print(soup.find_all('p', text='haha'))

# 검색양 제한 주기 : limit
print(soup.find_all('p', limit=1))
print(soup.find_all())
print(soup.find_all(['title', 'p']))

print("==========================================================")

# 응용 : 두번 거르기
body_tag = soup.find_all('body')    # 리스트로 반환
print(body_tag)
p_tag = body_tag[0].find_all("p")   # 리스트 방번호 접근해서 find_all()
print(p_tag)









# import requests
#
# url = "http://naver.com"
# res = requests.get(url)
# soup = BeautifulSoup(res, 'url.parser')
# print(soup)
