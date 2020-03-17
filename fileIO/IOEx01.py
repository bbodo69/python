'''
*** 파일 입출력 i/o ***
1) 파일 생성하기
    open("파일이름", "파일열기 모드")
2) 파일 열기 모드
    r : 읽기모드 (read)
    w : 쓰기모드 (write)
        - 파일이 존재하지 않을경우, 새로운 파일 생성
        - 파일이 존재할 경우, 기존 내용을 지우고 새로 작성,
    a : 추가모드(append)
3) 파일 닫기
    객체이름.close() : 열려있는 파일 객체 닫기.
'''
# 1. 파일 객체 생성 (파일이름, 모드)
f = open("newFile01.txt", 'w')
# 2. 파일에 저장할 텍스트 입력
f.write("쓰기\n")
f.write("쓰기\n")
f.write("쓰기\n")
f.write("hello\n")
f.write("hello1")
f.write("hello2\n")

# 3. 작성후 파일 객체 닫기
# f.close()

import codecs

f = codecs.open("newFile02.txt.", 'w', "utf-8")
f.write("욜로욜로\n")
f.write("모냐이거\n")
f.write("그러게 모냐이거\n")

f.close()