# for i in range() 이용해서 풀기
# 문제1. 60점 이상 합격, 미만 불합격 출력
print("문제1")
score = [90, 45, 66, 10, 49]

for i in score:
    if i >= 60:
        print("%d 점으로 합격" %i)
    else:
        print("%d 점으로 불합격" %i)

# 문제2. 1 ~ 10 까지 수중 홀수만 출력
print("\n\n문제2")
for i in range(1,10,2):
    print(i, end=" ")

# 문제3. 10 ~ 100 까지의 수중 짝수의 합만 출력
print("\n\n문제3")
total = 0;
for i in range(10,101,2):
    total += i
print(total)

# 문제4. 0 ~ 100 까지의 수중 10 단위로 출력
print("\n\n문제4")
for i in range(0, 101, 10):
    print(i, end=" ")

# 문제5. 구구단 2단 출력
print("\n\n문제5")
for i in range(2,2*10,2):
    print(i, end=" ")

# 문제6. 구구단 수 입력받아 해당 단수 출력
print("\n\n문제6")
num = int(input("구구단 숫자 입력"))
for i in range(num, num*10, num):
    print("%d x %d = %d" %(num,i/num,i), end="\n")

# 문제7. 구구단 전체 출력
print("\n\n문제7")
i = 2
while i<10:
    print("구구단 %d 단" %i)
    for j in range(i,i*10,i):
        print("%d x %d = %d" %(i,j/i,j), end="\n")
    print("\n")
    i += 1

# 문제8. 양의 개수와 음의 개수 출력
print("\n\n문제8")
lst = [-1, -20, -34, 78, -40]
plus_cnt = 0
minus_cnt= 0

for i in lst:
    if i > 0:
        plus_cnt += 1
    elif i < 0:
        minus_cnt += 1
print("양의 갯수는 %d개, 음의 갯수는 %d 개"%(plus_cnt, minus_cnt))
# 문제9. 은행 이자 계산 프로그램
print("\n\n문제9")
'''
은행에 n원을 입금했다.
그리고 은행은 하루에 이자가 10원씩 붙는다.
n일 후에 잔액은 얼마가 되어있을까?
원금, 예치일 수를 입력받아 처리하자.
'''

money=int(input("원금을 입력하세요"))
period=int(input("예치일을 입력하세요"))


for total in range(money, money+10+period*10,10):
    total = total
print(total)

