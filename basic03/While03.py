# ATM 기계

'''
*** 글로벌 은행 ATM ***
1. 입금
2. 출금
3. 잔액 조회
4. 계좌 이체
5. 종료
'''
# 1단계 : 메뉴 번호 선택하면, 메뉴 이름 출력
# 2단계 : 메뉴별 기능 구현하기
# 3단계 : 아이디와 패스워드 입력받아서 로그인하면 서비스 이용가능하게 만들기
# 4단계 : 아이디와 패스워드 3회 오류시 프로그램 강제 종료

my_money = 100000
id = 'python'
pw = '1234'

print("로그인 해주세요.")
while True:
    input_id = input("아이디 입력, 0입력시 끝")
    if input_id == '0':
        break
    input_pw = input("비밀번호 입력, 0입력시 끝")
    if input_pw == '0':
        break
    elif id==input_id and pw==input_pw:
        print("로그인 성공")
        while True:
            print('*** 글로벌 은행 ATM ***\n1. 입금\n2. 출금\n3. 잔액 조회\n4. 계좌 이체\n5. 종료')
            selector = input("메뉴 숫자를 입력하세요.")
            if selector=='1':
                amount = int(input("입금 금액을 입력하세요"))
                my_money += amount
                print('%d 원을 입금하셨습니다. 잔액은 %d 입니다.' %(amount, my_money))
            elif selector=='2':
                amount = int(input("출금 금액을 입력하세요"))
                if my_money - amount >= 0:
                    my_money -= amount
                    print('%d 원을 출금하셨습니다. 잔액은 %d 원 입니다.' % (amount, my_money))
                else:
                    print('잔액이 부족합니다. 잔액은 %d 원, 희망출금 금액은 %d 입니다' %(my_money, amount))
            elif selector=='3':
                print('잔액은 %d 입니다' %my_money)
            elif selector=='4':
                transit_number = input("이체할 계좌를 입력하세요.")
                amount = int(input("이체할 금액을 입력하세요"))
                if my_money - amount >= 0:
                    my_money -= amount
                    print('%d 원을 출금하셨습니다. 잔액은 %d 원 입니다.' % (amount, my_money))
                else:
                    print('잔액이 부족합니다. 잔액은 %d 원, 희망출금 금액은 %d 입니다' % (my_money, amount))
            elif selector=='5':
                break
    else:
        print("아이디와 비밀번호를 확인해주세요.")



# Up, Down 게임
'''
컴퓨터로 부터 1 ~ 100 사이의 임의의 숫자를 입력받고,
숫자를 맞춰보자
기회는 10번, 기회를 모두 소진하면 종료.
숫자를 맞췄을 경우 "축하합니다." 종료
기회가 끊났을 경우 "실패..." 종료
'''
import random

random_num = random.randint(1,100)
chance = 7;

while True:
    if chance == 0:
        print("10번안에 못 맞춤. 생성된 번호는 %d 입니다" %random_num)
        break
    while True:
        input_num = int(input("1 ~ 100 사이의 숫자 입력"))
        if input_num > 100 or input_num < 1:
            print("1 ~ 100 사이의 값 입력 바람. 입력한 값 %d" %input_num)
        if 1 <= input_num <= 100:
            break

    if input_num == random_num:
        print("정답입니다. 랜덤으로 생선된 번호는 %d 입니다." %random_num)
        break
    elif input_num > random_num:
        print("입력값이 큽니다.")
        chance -= 1
    elif input_num < random_num:
        print("입력값이 작습니다.")
        chance -= 1








