'''
*** 함수 function ***
def 함수명():
    실행문들....
----------------------
def 함수명(매개변수1, 매개변수2, ...):
    실행문들....
    return 값
----------------------
변수 = 함수명(인자1, 인자2...)

## 함수의 종류
# 사용자 정의 함수 : 개발자가 직접 작성한 함수
# 내장 함수 (builtins.py)
    print(), input(), len(), range()....
# 메서드 : 클래스 안에 있는 함수를 부르는 이름

'''

def showInfo():
    print('출력문 함수')

showInfo()

def getNum():
    print("리턴 값 보유")
    return 10

num = getNum()
print(num)

def showName(name):
         print("당신의 이름은 %s 입니다." %name)

showName("욘사마")

def my_sum(num1, num2):
    result = num1 + num2
    return result

sum = my_sum(5,7)
print(sum)

# my_sub : 빼기
# my_mul : 곱하기
# my_div : 나누기

def my_sub(num1, num2):
    result = num1-num2
    return result
fun_sub = my_sub(1,5)
print(fun_sub)

def my_mul(num1, num2):
    result = num1*num2
    return result
fun_mul = my_mul(2,5)
print(fun_mul)

def my_div(num1, num2):
    result = num1/num2
    return result
fun_div = my_div(1,5)
print(fun_div)