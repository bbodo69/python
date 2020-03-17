'''
크롤링, 스크래핑
인터넷에 존재하는 다양한 데이터를 활용하기 위해
데이터를 다운로드 하여 용도에 맞게 가공하는 과정.
크롤링 : 웹사이트를 정기적으로 돌며 정보를 추출하는 기술
크롤러 : 알고리즘에 의해 인터넷을 탐색하는 프로글매
        스크래퍼, 봇, 스파이더, 지능에이전트

# 웹 구조
클라이언트
서버 : 서비스를 제공해주는 프로그램
    종류
            영상제공 : youtube 스트리밍방식으로 분할해서 전송
            파일 : P2P, 토렌트, 드라이브, FTP, SFTP 등
            도메인 : DNS
            채팅 및 음성, 게임, 전자우편, 웹 서버....

# 헤더
서버와 클라이언트 간에 데이터를 주고 받을때, 헤더라는 정보를 포함해서 보낸다.
요청헤더 : 클라이언트 -> 서버에 요청할 때 정보를 포함
            user-agent(브라우저 정보), method(요청 메서드), refered(요청 이전에 머물렀던 주소)
응담헤더 :  서버 -> 클라이언트에게 응답할 때 정보를 포함
일반헤더 : 클라이언트와 서버 양측 모두에서 사용되는 일반 정보를 포함한 헤더
    Content-Type(entity-body의 미디어 타입)

# 데이터 전송
리소스 경로 : REST API(모든 웹 경로를 이미지로)
쿼리스트링 : URI 에 ? 뒤에 보내는 것들
header body : Request mehtod POST 일때만 Body에 데이터가 존재
            크롬개발자도구 headers 부분에 Form Data 표현

# 웹 페이지
HTML : 웹 페이지 문서 구조, 내용물을 넣기 위한 언어
CSS : 문서에 디자인을 주기 위한 언어
Javascript : 웹 페이지에 기능을 주기위한 언어(동적효과)
    크롤링할 때,
    자바스크립트에서 가장 중요한 점은 HTML 코드를 만들수 있다는 점.
    이렇게 생성된 HTML 코드는 크롤러가 접근하기 힘들다.

'''