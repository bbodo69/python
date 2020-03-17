import requests
from bs4 import BeautifulSoup
'''
# 영화명

#old_content > table > tbody > tr:nth-child(1) > td.title > a.movie.color_b
#old_content > table > tbody > tr:nth-child(2) > td.title > a.movie.color_b

# 평점

#old_content > table > tbody > tr:nth-child(1) > td.title > div > em
#old_content > table > tbody > tr:nth-child(2) > td.title > div > em

# 리뷰

'''

url = 'https://movie.naver.com/movie/point/af/list.nhn?&page=1'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')


# title = soup.find_all(class_='movie color_b')
# point = soup.find_all('em', class_='list_netizen_score')
# content = soup.find_all('br', class_='title')

title = soup.select('td.title > a.movie.color_b')
point = soup.select('td.title > div > em')
content = soup.select('td.title > br')

for i in range (1,6):
     print("제목 : ", title[i].text.strip(), "    점수 : ", point[i].text.strip()), "        내용 : ", content[i].next_sibling.strip()

'''
# BeautifulSoup 파싱한 데이터(soup)에서 추출
# 함수 : find(), find_all(). select()
# 태그 : soup.태그명
# 자식태그 : contents, children
        soup.p.contents : 자식태그들을 list로 가져옴.
        soup.p.children : 이터레이터 object 반환
# 부모태그 : parent, parents
# 형제태그 : next_sibling ( 밑에 있는 것을) , previous_sibling (위에 있는것을 ) (한개)
             next_siblings, previous_siblings (전체)
# 다음, 이전 요소 : next_element(s), previous_element(s) (단수/복수)             
'''

print("===================================================")

html = '''<html>
<head><title>타이틀</title></head>
<body><p><span>1111</span><span>2222</span></p></body>
</html>
'''
soup = BeautifulSoup(html, 'html.parser')
p_contents = soup.p.contents
print(p_contents)

p_children = soup.p.children
for child in p_children:
    print(child)




