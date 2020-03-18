'''
제품의 가격과 수량을 넘겨주면,
총 금액을 계산해 주는 프로그램을 만들어보자.
'''

class Cashier:
    # 공용변수
    count = 0       # 계산하는 제품 순서
    discount = 0.3  # 할인율

    # 생성자
    def __init__(self, price, number):
        self.price = price      # 제품 가격
        self.number = number    # 제품 수량
        Cashier.count += 1

    def calculator(self):
        # 정가로 지불해야 하는 금액
        self.pay = self.price * self.number
        self.dc_pay = self.pay - (self.pay * Cashier.discount)

    def display(self):
        print(Cashier.count, "번째 제품입니다.")
        print("정가 : ", self.price)
        print("수량 : ", self.number)
        print("가격 : ", self.pay)
        print("할인가격 : ", self.dc_pay)

    @staticmethod
    def message():
        print("어서오세요")
        print("할인중입니다.")

    @classmethod
    def update(cls, value):
        while value >= 1 or value <= 0:
            value = float(input("할인률을 다시 입력"))
        cls.discount = value

product1 = Cashier(1000,5)
product1.calculator()
product1.display()

product1.update(1.2)