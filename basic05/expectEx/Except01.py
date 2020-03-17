'''
*** 예외 처리 ***
IOError : 파일 오픈할 수 없을 때 발생
IndexError
ImportError
ValueError
ZerodivisionError
FileNotFoundError
SyntaxError
EOFError : End of File 더이상 읽어올 내용이 없을때 발생

구조:
    try:
        # 예외 발생할 것 같은 코드...
    except 발생에러 as 에러메세지 받을 변수명:
        # 예외 발생시 처리할 코드...


'''

# print("시작")
#
# while True:
#     try:
#         num = input("정수 : ")
#         int(num)    # ValueError
#         print(num)
#     except ValueError:
#         print("ValueError 발생했다")
#
# print("종료")

lst = [1,2,3]

# try:
#     idx = int(input("정수 번호 입력 : "))
#     print(3/idx)        # 0 -> ZerodivisionError
#     print(lst[idx])     # 0 -> IndexError
# # except IndexError:
# #     print("인덱스 번호 에러")
# # except ZeroDivisionError:
# #     print("0으로 나눌 수 없다")
# except Exception:
#     print("모든 예외 처리")
# finally:
#     print("에외 발생 여부와 무관하게 실행되는 부분")

# def func():
#     num = int(input("1 ~ 5 사이의 정수 입력 : "))
#     if num > 5 or num < 1:
#         print("에러")
#         raise   # 강제 예외 발생 키워드
#     else:
#         print(num)
# #---------------------------------------------------
# try:
#     func()
# except:
#     print("예외 발생")

try:
    age = int(input("나이 입력: "))
    if age < 0:
        raise ValueError("나이가 음수")
except ValueError as e:
    print(e)
    

