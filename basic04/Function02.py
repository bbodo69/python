'''
*** 변수의 scope ***
변수의 종류 (선언 위치에 따른)
    1. 전역변수 global variable
        선언위치 : 함수 밖
        유효범위 : 프로그램이 종료될때까지 유효
                    함수안에서 사용할 시 참조형으로만 사용가능.
                    함수내에서 변경 불가능
                * 함수내에서 전역변수 값을 변경하는 방법
                    #1. 리턴값 이용하기
                    #2. global 키워드 이용하기 (비추천)

    2. 지역변수 local variable
        선언위치 : 함수 안
        유효범위 : 함수안에서만, 함수가 종료될 시 소멸
                    함수 밖에서 사용 불가
'''



# num = 10
# print("전역 : ", num)
#
# def func(num):
#     # 전역 변수의 num을 호출
#     num = num + 1
#     print("함수안 num = ", num)
#     # 지역변수
#     hello = "hello"
#     print("지역변수 안 hello 변수 = ",hello)
#
# func(num)
# print("전역 변수 의 num = ", num)
#
# ######################
# # 전역 num 던져주고 func를 호출하면
# # 전역 num 에 1이 더해진 값을 갖게 하고 싶다
# def func(num1): # 지역(매개)변수
#     # num 지역변수
#     num1 = num1 + 1
#     print(num1)
#     return num1
# #######################
#
# # 함수에서 전역변수의 값 변경1. 리턴값
# num = func(num) # 전역변수 던지기
# print("전역 : ", num) # 전역변수 출력




num = 5
print("전역 num =  ", num)

def func1():
    global num # 전역 num 을 가르킴, 함수 안에서 변경 가능하게 선언함
    num = num+1 # 위에 global num 을 뺄시 에러 발생, 이유는 지역에서 전체 변수를 수정하려고 해서.
    print(num)

func1()

print(func1)
print("전역 num =  ", num)



