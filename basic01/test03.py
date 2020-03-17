'''
자료형(data type)
1) 숫자형
    1. 정수 : int (integer)
            파이썬 2.x : int, long
            파이썬 3.x : int
    2. 실수 : float
            파이썬 2.x : 5000 / 3 = 1666
            파이썬 3.x : 5000 / 3 = 1666.6666

2) 참/거짓형 : bool (boolean)
            True / False (첫글자 대문자)

3) 군집자료형
    1. 문자열형 : str (string)
    2. 리스트 : list
    3. 튜플 : tuple
    4. 딕셔너리 : dict (dictionary) / 자바의 hashmap 같은것
    5. 집합 : set / 자바의 keyset 같은것 중복되는것 걸러줌.

*** 변수 variable ***
    데이터타입 기술 X (동적언어)

    type() : 데이터 타입을 돌려주는 함수

    변수 명명규칙
    num != Num
    n1um(0) 1num(X)
    특수문자 _ 만 허용해줌
'''
num = 10
num2 = 10
s1 = "hello"
print(num)
print(type(num))
print(type(num2))
print(type(s1))
print(id(num))
print(id(num2))
print(id(s1))

'''
입력함수 : input()
    변수 = input("콘솔에 띄워줄 메세지")
'''
'''
name = input("이름을 입력하세요")
print(name)
'''

'''
형변환 casting, convert

    문자 ---> 정수
        int (문자)
    문자 ---> 실수
        float (문자)
    정수/실수 ---> 문자
        str (정수/실수)
'''
num3 = '10'
print(type(num3))
num4 = int(num3)
print(type(num4))
'''
age = int(input("나이 입력 : "))
'''
print("당신의 내년 나이는 %d살 이네요" %(age+1))
'''
a = int(input("국어 점수 입력"))
b = int(input("수학 점수 입력"))
c = int(input("영어 점수 입력"))

total = a+b+c
avg = total /3

print("국어점수는 %d 점, 수학점수는 %d 점, 영어점수는 %d 점 이다" %(a,b,c))
print("총점은 %d, 평균은 %d 이다" %(total,avg))
'''





