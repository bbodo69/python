'''
*** list 리스트 ***
여러개의 값을 하나로 묶어서 저장할 수 있는 데이터 타입
구조 :
    변수명 = [요소1, 요소2, 요소3,....]
특징 :
    다양한 데이터 타입을 섞어서 하나로 묶을 수 있다.
    수정가능 (mutable)
    크기 제한 없다.
구분기호 : []
'''
nums = [1,2,3,4,5,6]

# 빈 리스트
a = []
b = list()
print(a)
print(b)
print(nums)
c = ['apple', 0, 'all', 1000]
print(c)
print(c[2])
print(c[-3])

num2 = [ [1,2,3], [4,5,6], [7,8,9]]
print(num2[0][2])

num3 = [1,2,3,[4,5,6],7]
# 숫자 4 출력
print(num3[3][0])
# 숫자 3 출력
print(num3[2])
# 숫자 7 출력
print(num3[4])

num4 = [1,2,3,['a','b','c'],4,5]
#[3,['a','b','c'],4] 출력
#['a','b'] 출력
list1 = [num4[2],num4[3],num4[4]]
list2 = [num4[3][0], num4[3][1]]
print(list1)
print(list2)
print(num4[2:5])
print(num4[3][:2])

lst = [1,2,3]
lst[0] = 10
print(lst)
# 인덱스 번호 1번의 요소를 'a', 'b', 'c'로 바꿔보자
lst[1] = 'a','b','c' # 큐플, 수정이 불가능한 리스트 형태
print(lst)
lst[1] = ['a','b','c']
print(lst)
lst[1:2] = ['a','b','c']
print(lst)