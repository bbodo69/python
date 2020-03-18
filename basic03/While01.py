'''
반복문 : while , for

*** while ***
구조
    #1. 반복횟수를 알때 지정
    while 조건식:
        실행문...
        증감식
    #2. 무한반복
    while True:
        실행문...
        // 종료시점
        if 조건문:
            break
'''

# 10 회 반복
i = 0;
while i < 10:
    print("hello",i)
    i = i + 1

# 문제1. 0 ~ 3 까지 출력
i  = 0 ;
while i < 4:
    print(i)
    i += 1

# 문제2. 1 ~ 10 사이의 홀수 출력
i = 0;
while i<10:
    if i % 2 == 1:
        print(i)
    i += 1

# 문제3. 0 ~ 100 사이의 수중 10단위로 출력
i = 0 ;
while i <= 100:
    if(i % 10 == 0):
        print(i)
    i += 1

# 문제4. 1 ~ 10 까지의 모든 수를 더한 합을 출력
i = 1 ;
total = 0;
while i <= 10:
    total += i;
    i += 1
print(total)

# 문제5. 1 ~ 20 사이의 짝수를 모두 더한 값 출력
i = 1;
total = 0;
while i <= 20:
    if(i % 2 == 0):
        total = total + i;
    i += 1
print(total)

# 문제6. 숫자를 5번 입력받고, 입력받은 수를 모두 더한 값을 출력

i = 0;
total = 0;
while i<5:
    num = int(input("%d 번째 숫자 입력" %(i+1)))
    total += num;
    i += 1;
print(total)

