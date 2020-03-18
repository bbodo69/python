# 튜플의 unpacking
tup = ("피카츄", 20, "서울")
print(tup)
name, age, city = tup
print(name)
print(age)
print(city)

# name1, age1 = tup
# print(name1)
# print(age1)

# 값 변경 하는 방법
a, b = 10, 20
a,b = b,a

print(a)
print(b)

# 튜플 결합하기
t1 = (1,2,3)
t2 = ('a', 'b', 'c')
t3 = t1 + t2
print(t3)

# in 여산자
tup = (1,2,'a', 'b')
print('a' in tup)

tupList = [("피카츄", 100), ("꼬부기", 70), ("파이리", 45)]
for i,j in tupList:
    print("%s님의 점수는 %d 입니다" %(i, j))

# 인덱싱, 슬리이싱
tup = ("global", [1,2,3], (4,5,6))
print(tup[1][1:])