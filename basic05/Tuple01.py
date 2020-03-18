'''
군집자료형 : str, list, tuple, dict, set
*** 튜플 Tuple ***
list : []
tuple : (,)
튜플은 요소의 값을 수정할 수가 없다. imutable
데이터가 한개일 때는 쉼표를 반드시 기술
데이터 여러개일때는, 소가로 생략 가능 (쉼표로 구분)

'''
# 빈 튜플
t1 = ()
print(t1)
print(type(t1))

# 한개의 요소만 대입할 경우
t2 = (10)
print(t2)
print(type(t2))

t3 = (10,)
print(t3)
print(type(t3))

# 여러개의 요소를 대입할 경우
t4 = 1,2,3,4,5,6
print(t4)
print(type(t4))

print(t4[2:4])
print(len(t4))