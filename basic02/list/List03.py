# 문재1. 5개의 요소를 가지고 있는 리스트를 하나 만들고,
#       인덱스번호 2개를 입력받고, 해당 인덱스 번호에 자리한 값을 교환해보자

lst0 = [1,2,3,4,5]
print("현재 리스트에 있는 번호 ", lst0)
num = input("바꿀 인덱스 번호 2개 입력")
index1=int(num[0])
index2=int(num[1])
num1 = lst0[index1]
num2 = lst0[index2]
print(num1)
print(num2)
lst0.pop(index1)
lst0.insert(index1, num2)
lst0.pop(index2)
lst0.insert(index2, num1)
print(lst0)

# 문제2. 리스트가 가지고 있는 다양한 함수를 이용해보자
lst1 = [1,3,5,4,2]
#[5,4,3,2,1]로 만들어 보자.
lst1.sort(reverse=True)
print(lst1)


# 문제3. 아래 리스트르르 활용하여 주어진 요소를 출력해보자
lst2 = ["Global", ["IT", [1,3,5,7,9], ["Even", [0,2,4,6,8]]]]
# "Global" 출력
# 숫자3 출력
# 숫자8 출력
print(lst2[0])
print(lst2[1][1][1])
# 문제4. 아래와 같이 출력해보자.
'''
==========================
        파이썬
==========================
자료형 *
제어문 ***
입출력 ****
클래스 ******
'''