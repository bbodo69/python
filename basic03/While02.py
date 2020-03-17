# 무한적으로 숫자를 입력받아 출력하는 while문 만들어보자.
# 단, 숫자 9를 입력하면 while문 종료

# while True:
#     num = int(input("숫자를 입력"))
#     print("num = %d" %num)
#     if num==9:
#         break
#
# import time
# while True:
#     print("엔터를 눌러주세요")
#     input()
#     print("게임 시작")
#     time.sleep(3)
#     print("게임 종료")
#     break

# 문제 1.
'''
메뉴 출력하고, 주문을 계속 받는 프로그램
종료를 선택하면 프로그램 종료하고 총 합계를 출력하시오.
menu
    *** 글로벌 카페 ***
    1. 아메리카노   2000원
    2. 카페라뗴     3000원
    3. 자바침       4500원
    4. 모카라떼     4000원
    5. 종료
'''

print('menu\n*** 글로벌 카페 ***\n1. 아메리카노   2000원\n2. 카페라뗴     3000원\n3. 자바침       4500원\n4. 모카라떼     4000원\n5. 종료')

total = 0 ;
while True:
    num = int(input("메뉴 번호 눌러주세요"))
    if num==5:
        break
    elif num==1:
        total +=2000
    elif num==2:
        total +=3000
    elif num==3:
        total +=4500
    elif num==4:
        total +=4000
print("총 금액은 %d원 입니다." %total)

# 문제2. 커피 자판기
'''
커피는 10잔만 존재
1. 돈을 입력받는다. (커피값 : 300원 고정)
2. 300원 이상 입력, "거스름돈은 ??원 입니다." 출력
3. 300원 이하, "돈이 부족합니다."
4. 300원 입력, "맛커" 출력
커피 10 잔이 다 소진되면 프로그램 종료
'''

coffee_amout = 10;

while coffee_amout != 0:
    money = int(input("금액을 입력"))
    if money > 300:
        print("거스름 돈은 %d원 입니다" %(money-300))
        coffee_amout -= 1
    elif money == 300:
        print("맛커")
        coffee_amout -= 1
    elif money < 300:
        print("%d 원 모자릅니다." %(300-money))