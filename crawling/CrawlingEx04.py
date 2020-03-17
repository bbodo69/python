'''
기상청 RSS 서비스 정보 가져오기
http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
파라미터 stnId : 지역 파라미터명
전국 108, 서울/경기 109, 강원 105 등등
'''
# 라이브러리 임포트
import urllib.request as request
import urllib.parse

# 주소담기
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 요청할때 넘겨줄 파라미터를 딕셔너리 타입으로 처리할 경우
values = {"stnId" : "108"}
params = urllib.parse.urlencode(values)

# 요청 url 완성
url = API + "?" + params
print(url)

# 요청하고 read()로 html 가져오기
data = request.urlopen(url).read()
text = data.decode("utf-8")
print(text)