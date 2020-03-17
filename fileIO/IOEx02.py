'''
# 쓰기
1. open file
2. write
3. close file
# 더 쉬운 방법
with 키워드 이용해서 context manager 만들기
하나의 open 블럭을 만들고, 블럭안의 변수는 일정기간 동안(블록이 실행될때)만
존재하게 함.
'''

def writeThings(things):
    f = open("date.txt", 'w') # 덮어쓰기 모드
    # f = open("data.txt", 'a') # 추가 모드
    f.write(things + "\n")
    f.close()

if __name__ == '__main__':
    writeThings(input("저장할것 작성 : "))