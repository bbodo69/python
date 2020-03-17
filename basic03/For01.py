'''
*** for문 ***
for 변수 in "문자열"/리스트/튜풀/딕셔너리:
    실행문.....
for 변수 in range(숫자):
    실행문.....
'''

for i in "hello":
    print(i)

print("")

lst = [1,2,3,4,5]
for i in lst:
    print(i)

print("")

score = [40, 70, 34, 97, 68]
# 시험 점수가 60 점 이상이면 합격 그렇지 않으면 불합격 출력
# for문으로 만들어보자

for i in score:
    if i >= 60:
        print("%d 점 으로 합격" %i)
    else:
        print("%d 점 으로 불합격" %i)

# 0 ~ 10 까지 출력
for i in range(10):
    print(i)

# 건너뛰면서 출력
for i in range(1, 11, 2):
    print(i)






