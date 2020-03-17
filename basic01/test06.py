"""
*** 연산자 operator ***
산술 연산자 : + - * / %
대입 연산자 : =
복합대입 연산자 : += -= *= /= %=
비교 연산자 : > >= <= == /=
논리 연산자 : True / False
멤버 연산자 : in / not in /
식별 연산자 : is / in not
"""

# 대입 연산자
x = 10;
y = 10;
z = 10;

x = y = z = 10 ;
print(x)
print(y)
print(z)

x, y, z = 10, '20', 30
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
"""
# 문제1. 분자, 분모 하나씩 입력받고 몫과 나머지를 출력하자

dinomirator = int(input("분모를 입력하세요"))
numerator = int(input("분자를 입력하세요"))
print("몫은 %d 이고 나머지는 %d 이다" %(numerator/dinomirator, numerator%dinomirator))

# 문제2. 1000초를 몇분 몇초로 나누어 출력하자. 출력 예) 27분 27초
minute = 1000/60
second = 1000%60
print("1000초는 %d분 %d초 이다." %(minute, second))
"""
# 복합대입 연산자
num1 = 10
num2 = 20

num1 = num1 + 10
num1 += 10
print(num1," = num1")

print(num1 > num2)

# 논리 연산자 : and or not
'''
a and b : a(바교연산식) 와 b 모두 조건에 맞아야 true
a or b : a와 b 중 둘중 하나가 조건에 맞으면 ture
not a : a가 거짓이어야 ture
'''

#문제3 아래의 식을 비교 연산자 번형하여 true 로 만들어 보기
a,b,c,d = 10,9,8,7
print(a == b and c > d)
print(a <= b or c < d)
print(not(a < b or c > d))

print(a >= b and c > d)
print(a <= b or c > d)
print(not(a < b or c < d))

# 문제 4 복합대입연산자를 이용해서 연결
a = "Python"
b = " is fun!!!"
c = "Java"
d = " is not fun !!!"
print(a+b+c+d)

# 문제2. 화폐매수 구하기
'''
금액을 입력받고 최소 화폐 매수를 구해서 출력하세요.
예) 67800원 입력받았을 경우 출력
5만원 : 1장
1만원 : 1장
5천원 : 1장
1천웑 : 2장
5백원 : 1개
1백원 : 3개
'''
amount = int(input("금액을 입력하세요"))

amount50000 = amount//50000;
amount10000 = (amount-amount50000*50000)//10000;
amount5000 = (amount-amount50000*50000-amount10000*10000)//5000;
amount1000 = (amount-amount50000*50000-amount10000*10000-amount5000*5000)//1000;
amount500 = (amount-amount50000*50000-amount10000*10000-amount5000*5000-amount1000*1000)//500;
amount100 = (amount-amount50000*50000-amount10000*10000-amount5000*5000-amount1000*1000-amount500*500)//100;
amount50 = (amount-amount50000*50000-amount10000*10000-amount5000*5000-amount1000*1000-amount500*500-amount100*100)//50;
amount10 = (amount-amount50000*50000-amount10000*10000-amount5000*5000-amount1000*1000-amount500*500-amount100*50-amount100*50)//10;

print("50000만원권 %d장" %amount50000)
print("10000만원권 %d장" %amount10000)
print("5000만원권 %d장" %amount5000)
print("1000만원권 %d장" %amount1000)
print("500만원권 %d개" %amount500)
print("100만원권 %d개" %amount100)
print("50만원권 %d개" %amount50)
print("10만원권 %d개" %amount10)
