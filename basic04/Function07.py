# 예상할 수 없는 함수
'''
def 함수명(*파라미터):
    실행문들....
'''

# 숫자를 원하는 만큼 인자로 입력해 함수를 호출하면 모든 숫자를 더해서 총 합계를 돌려주는 함수 만들기
def sum(*num):
    tot = 0
    for i in num:
        tot += i
    return tot

print(sum(10,20))

# op : 연산자 기호, *num : 연산하고 싶은 숫자들
# 파라미터 작성 순서 : 일반파라미터 -> *파라미터 -> 초기값 있는 파라미터
# 초기값 있는 파라미터에 보내줄 인자는 파라미터명 = 값 로 지정해서 보내줘야한다.
def calc(op, *num, age=0): # 초기값 있는것은 뒤에 나와야함
    if op == 'sum':
        tot = 0
        for i in num:
            tot += i
    elif op == 'minus':
        tot = num[0]
        for i in num:
            tot -= i
    elif op == 'mul':
        tot = num[0]
        for i in num:
            tot *= i
    elif op == 'div':
        tot = num[0]
        for i in num:
            tot /= i
    print(age,' = age')
    return tot

print(calc('mul', 1,2,3,4,5,6,age=10))