'''
# 제어문
    1) 조건문 : if
    2) 반복문 : while, for
    3) 보조제어문 : break, continue

1) 조건문 : if
    구조
        if 조건문:
            실행문들....
        ------------------
        if 조건문,
            실행문들....
        else:
            실행문들....
        ------------------
        if 조건문,
            실행문들....
        elif 조건문,
            실행문들....
        elif 조건문,
            실행문들....
        else:
            실행문들....
        ------------------
        # 들여쓰기 : indentation
            spacebar 4번 == tab키 1번
'''

score = 70
if score >= 60:
    print("합격")
elif score < 60:
    print("불합격")

# result :1, false: 0
result = int(score/60)
if result:
    print("result 합격")
else:
    print("result 불합격")

# 문제. 정수 1개를 입력받아, 그 수가 '양수' 인지 '음수'인지 출력해보자.
# 문제. 정수 1개를 입력받아, 그 수가 '짝수' 인지' '홀수'인지 출력해보자.
# 문제. id와 pw 입력받아 모두 일치하면 "(id)님이 로그인 되었습니다" 출력
#       불일치면 " 아이디와 비밀번호 확인해주세요" 출력
db_id = "python"
db_pw = "1234"

num1 = int(input("num1 정수 입력"))

if num1>=0:
    print("num1은 양수 입니다.")
else: 
    print("num1은 음수 입니다.")

num2 = int(input("num2 정수 입력"))
if num2%2==0:
    print("num2 값은 짝수이다.")
else:    
    print("num2 값은 홀수이다.")

input_id = input("아이디 입력")
input_pw = input("비밀번호 입력")

if db_id == input_id and db_pw == input_pw:
    print("로그인 성공")
else:
    print("아이디와 비밀번호 확인해주세요")
    
# 문제. 주민번호를 입력받아 "여성" / "남성"을 출력해보자

id_number = input("주민번호를 입력")

if len(id_number)==13:
    if id_number[6] == "1":
        print("남성")
    else:
        print("여성")
else:
    print("주민번호 잘못 입력")



# 문제 .사용자로부터 키를 입력받아, 키가 150이상이면 "놀이기구 이용가능" 150 미만이면 "부모님 여부 질문 후 답변 yes, no 로 받아서
# yes 시 이용 가능, no 시 이용 불가능 출력

heigh = int(input("키 입력해주세요"))
if heigh >=150:
    print("이용가능")
else:
    ans = input("부모님 같이 왔니?")
    if ans.upper()=="YES":
        print("이용가능")
    else:
        print("불가능")

# 문제. 학점처리 프로그램
'''
이름과 국어, 영어, 수학 3과목에 대한 점수를 입력받아
총점, 평균, 학점(평균으로 적용)을 구해보세요
단, 평균은 소수점 이하 한자리까지 표현
학점 기준 : 90 점이상 A
            80 점 이상 B
            70 점 이상 c
            60 점 이상 d
            그 이하 f

'''
language = int(input("국어점수 입력"))
math = int(input("수학점수 입력"))
english = int(input("영어점수 입력"))
total = language + math + english
avg = total / 3
if avg >= 90:
    grade = "A"
elif 80 <= avg < 90:
    grade = "B"
elif 70 <= avg < 80:
    grade = "C"
elif 60 <= avg < 70:
    grade = "D"
else:
    grade = "F"

print("총점은 %d 이고 평균은 %0.1f 이고 학점은 %s 이다" %(total, avg, grade))