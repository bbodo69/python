'''
## 웹 크롤러
    웹에 접속해서 데이터 받아오는 것
    1 - 웹페이지 요청 -> 요청 라이브러리 필요
    2 - 요청 결과를 파이썬에서 사용 가능한 형태로 파싱(변환) -> 라이브러리 필요
    
## 라이브러리
파이썬에서 표준으로 제공하는 urllib 라이브러리 사용해보자.
urllib : URL을 다루는 모듈을 모아 높은 패키지라 할 수 있다.
    이 라이브러리를 이용하여 HTTP, FTP 를 사용해 데이터 다운 가능.
    urllib.request 모듈은 웹 사이에 있는 데이터 접근하는 기능을 제공함.
    인증, 리다이렉트, 쿠키 같은 요청과 처리 지원
'''

# 1. 라이브러리 임포트
# urllib.request 모듈에 있는 Request 클래스와 urlopen
from urllib.request import Request, urlopen

url = "https://www.naver.com"

# 2. 요청
# url 주면서 요청 객체를 만들고
req = Request(url)
# 만들어진 요청 객체를 이용하여 페이지 요청 : urlopen()은 요청후 응답을 객체로 리턴
page = urlopen(url)

# 3. 응답 결과 객체 정보 출력
print(page)
print(page.code)    # 응답 코드
print(page.headers)
print(page.url)
print(page.info().get_content_charset())

# 4. html 꺼내기
print(page.read())

##########################################################################################
# 5. post 요청
# 5-1. post 요청시 보낼 데이터 만들기 : 데이터를 만들때에는 바이너리 형태로 인코딩해 보내야함.
import urllib
data = {"key1":"value1", "key2":"value2"}
data = urllib.parse.urlencode(data) # 딕셔너리를 쿼리스트링의 형태로 바꿔주기
data = data.encode("utf-8")         # 쿼리스트링처럼 표현된 문자열을 UTF-8 로 인코딩하여
                                    # 바이너리 형태로 바꿔준다.
print(data)

print("===========================================")
# 5-2 post 요청
# 요청객체 만들기 : url, 요청시 던져줄 데이터, header
req_post =  Request(url, data=data, headers={})
page = urlopen(req_post)

print(page)
print(page.headers)

print("===========================================")

# 6. GET 요청
# urllib의 Request 객체 생성시, 두번째 인자값이 존재하면 POST 요청
# 두번째인자가 None 이거나 생략하면 GET 요청함 ( 두쨰 인자의 유/무)
req_get = Request(url+"?key1=value1&key2=value2", None, headers={})
page = urlopen(req_get)
print(page)
print(page,url)
print("code", page.code)

# 7. 파일 다운로드
from urllib.request import urlretrieve
# 구글 로고 이미지 주소
url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"

# 저장할 이미지 경로 + 이름 만들기
name = "googleLogo.png"

# 이미지 다운로드 : 인자 : (다운받을 데이터 url, 저장할 파일 경로)
urlretrieve(url, name)