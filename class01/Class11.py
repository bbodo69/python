'''
특수 메서드
1) __init__() : 생성자
2) __del__() : 소멸자
                del 명령어로 객체를 삭제하겠다고 명령하면,
                해당 객체의 레퍼런스카운트가 -1 이 되고
                래퍼런스 카운트가 0 이 될 때 이 소멸자가 자동 호출
3) __call__() : 객체 호출 시 실행되ㅏ는 메서드
4) __getitem__() : 딕셔너리 데이터 찾듯이 객체['키']
'''

class Character:
    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print("player가 생성되었습니다")

    def __call__(self, *args, **kwargs):
        print("hp : %d, attack: %d, defence: %d" % (self.hp, self.attack, self.defence))

    # def showInfo(self):
    #     print("hp : %d, attack: %d, defence: %d" %(self.hp, self.attack, self.defence))
    #
    # def __del__(self):
    #     print("player가 죽었")

    def __getitem__(self, item):
        print(item)
        if item == "hp":
            return self.hp
        elif item == "attack":
            return self.attack
        elif item == "defence":
            return self.defence
        else:
            return "존재하지 않는 변수입니다."

#-============================================
import sys

print("ref = " ,sys.getrefcount(Character))
a = Character(10,20,30)
b = Character(10,20,30)
c = Character(10,20,30)
# a.showInfo()
# print("ref = " ,sys.getrefcount(Character))
# del a
# del b
# print("ref = " ,sys.getrefcount(Character))

print("====================")
#1. call
a()
b()

#2. getitem
print("a[hp] = " , a["hp"])