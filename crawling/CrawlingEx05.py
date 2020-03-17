'''
# requests(urllib.request와 비슷)
    파이썬에서 HTTP 요청을 보낼때 많이 사용되는 모듈
    request로 HTTP 요청을 하면 응답에 관련된 정보들을 함께 응답객체로 반환해줌
    라이브러리 추가 설치 필요함
# BeautifulSoup (bs4로 갬색해 설치)
    HTML의 태그를 파싱해서 필요한 데이터만 추출하는 함수를 제공하는 라이브러리
    * 파싱 : 문자열을 분석하여 의미있는 토큰으로 분해해서 파스 트리를 만드는 과정
            문자열을 일정한 퐴ㅅ에 맞게 구조화(변경) 해줌
        urllib = bs
        requests = bs

        CRUD : 클라이언트가 서버에 데이터를 요청할 때 크게 4가지 타입
        Create      -> POST : 데이터 추가 요청 메서드
        Read        -> GET : 서버에 데이터 요청할 때 사용하는 메서드
        Update      -> PUT :
        Delete      -> DELETE
'''
# 1. 라이브러리 임포트
import requests

url = "http://www.naver.com"

# 요청! 응답을 리턴해줌
res = requests.get(url)
print(res)
print(res.status_code)
print(res.headers)
print(res.cookies)
print(dict(res.cookies))
print(list(res.cookies))

#html 코드 보기
# print(res.text)
# print(res.content)
print(res.encoding)

# 요청시 데이터 보내는 방법
# GET : .get()
# 1-1. 쿼리 스트링 데이터 만들어 요청 1
res = requests.get(url, params=({"key1":"value1","key2":"value2"}))
print(res.url)
# 1-2. 쿼리 스트링 데이터 만들어 요청 2
url = "http://www.naver.com/?key1=value1%key2=value2"
requests.get(url)
print(res.url)
# POST : .post()
url = "http://www.naver.com/"
res = requests.post(url, data={"key1":"value1","key2":"value2"})
print(res.url)

# data = json 형태로 보내기
import json
res = requests.post(url, data=json.dumps({"key1":"value1"}))
print(res.url)

'''
request 예외
HTTPError
ConnectionError
ProxyError
SSLError    (https)
Timeout
ConnectionTimeout
URLRequired
TooMayRedirects
MissingSchema
InvalidURL
'''
try:
    url = "naver.com"
    response = requests.get(url)
    print(response.url)
except requests.exceptions.HTTPError:
    print("http 에러발생")
except requests.exceptions.Timeout:
    print("timeout 에러 발생")
except requests.exceptions.MissingSchema:
    print("missingSchema 에러 발생")

# 예외 처리




