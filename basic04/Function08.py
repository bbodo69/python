# ATM 기계
# 함수로 바꿔서 만들어보기.

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
login_check = 0




def login():
    while True:
        global login_check
        input_id = input("아이디 입력 바람")
        input_pw = input("패스워드 입력 바람")

        if id != input_id:
            print("존재하지 않는 아이디 입니다.")
        elif id==input_id and pw != input_pw:
            print("비밀번호를 확인해주세요")
        elif id==input_id and pw == input_pw:
            print("로그인 성공")
            login_check = 1
            break

def deposit(amount):
    global my_money
    my_money += amount
    print("입금금액은 %d, 잔액은 %d 입니다" %(amount, my_money))


def withrow(amount):
    global my_money
    if my_money >= amount:
        my_money -= amount
        print("출금금액은 %d, 잔액은 %d 입니다" %(amount, my_money))
    elif my_money < amount:
        print("잔액이 부족합니다. 잔액은 %d원, 요청 금액은 %d원 입니다." %(my_money, amount))

def checking():
    print("현재 잔액은 %d 원 입니다." %my_money)

def transit(amount, transit_number):
    global my_money
    if my_money >= amount:
        my_money -= amount
        print("%s 로 %d원 이체 완료, 잔액은 %d 입니다" %(transit_number, amount, my_money))
    elif my_money < amount:
        print("잔액이 부족합니다. 잔액은 %d원, 요청 금액은 %d원 입니다." %(my_money, amount))

def service():
    while True:
        print('*** 글로벌 은행 ATM ***\n1. 입금\n2. 출금\n3. 잔액 조회\n4. 계좌 이체\n5. 종료')
        selector = input("서비스 할 번호를 눌러주세요.")
        if selector=='1':
            amount = int(input("입금할 금액을 입력하세요"))
            deposit(amount)
        elif selector=='2':
            amount = int(input("출금할 금액을 입력하세요"))
            withrow(amount)
        elif selector=='3':
            checking()
        elif selector=='4':
            transit_number = input("이체 할 번호를 적어주세요.")
            amount = int(input("입금할 금액을 입력하세요"))
            transit(amount, transit_number)
        elif selector=='5':
            print("종료합니다")
            break

print("로그인 해주세요.")
login()
if login_check==1:
    service()