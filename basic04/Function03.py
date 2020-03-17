'''
문제1. 계산기
사칙연산을 모두 수행하여 결과를 보여주는 프로그램 만들기
단, 사용자에게 종료여부를 물어서 y를 입력하면 프로그램 종료, n을 입력하면 계속 계산

콘솔 출력예)
정수1 입력:     10
정루2 입력:     20
덧셈 : 30
뺄셈 : -10
곱셈 : 200
나눗셈 : 0.5

종료하시겠습니다? y/n
n 선택시

정수1 입력:     10
정루2 입력:     20
덧셈 : 30
뺄셈 : -10
곱셈 : 200
나눗셈 : 0.5
종료하시겠습니다? y/n
y 선택시
프로그램 종료.

'''

def cal(num1, num2):
    plus = num1 + num2
    minus = num1 - num2
    mul = num1 * num2
    div = num1 / num2

    print("덧셈 : %d" %plus)
    print("뺼셈 : %d" %minus)
    print("곱셈 : %d" %mul)
    print("나누셈 : %d" % div)

while True:
    num1 = int(input("1 번째 정수 입력"))
    num2 = int(input("2 번째 정수 입력"))
    cal(num1, num2)
    select = input("종료하시겠습니까? (y/n)")
    if select.upper()=='Y':
        break

'''
문제2. 로그인 프로그램 : login()
사용자로부터 id와 pw 를 입력받아
로그인 메세지 출력
id가 다르면. "??는 존재하지 않는 id입니다."
pw가 다르면, "비밀번호가 다릅니다."
둘다 일치하면, "?? 님 환영합니다." 출력하기
'''

db_id="python"
db_pw="1234"

def login():
    while True:
        id = input("id 입력")
        pw = input("pw 입력")

        if db_id != id:
            print("%s 는 존재하지 않는 id 입니다" %id)
        elif db_id == id and db_pw != pw:
            print("비밀번호가 다릅니다")
        elif db_id == id and db_pw == pw:
            print("%s 님 환영합니다." %id)
            break

login()