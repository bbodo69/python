class A:
    def hello(self):
        print("AAAAAA")

class B(A):
    # 오버라이딩
    def hello(self):
        print("BBBBB")

class C(A):
    def hello(self):
        print("CCCCCCCCCCCC")

class D(B, C):
    # pass
    # 부모를 지정해서 메서드를 호출 할 수 있다.
    #이 때 MRO를 정확히 알아야 어떤것의 부모를 호출할지 알 수 있다.
    def hello(self):
        # super(D, self).hello() # BBB
        # super(C, self).hello() # AAA
        super(B, self).hello() # CCC
#==================================================

x = D()
print(D.mro())
x.hello()