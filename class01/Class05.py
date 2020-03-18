class Person:

    def __init__(self, name, age):
        # 인스턴스변수 선언, name 매개변수의 값 대입
        self.name = name
        self.age = age
############################################################################

pika = Person("pikachu", 10)
print(pika.name)
print(pika.age)

class Character:
    count = 0 # 캐릭터 객체의 개수를 카운트할 변수

                        # name 은 매개변수(지역변수)
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        print("%s가 만들어지는 중..." % self.name)
        Character.count += 1

    def die(self):
        print("%s가 죽었습니다." %self.name)
        Character.count -= 1

    def showInfo(self):
        print("캐릭터의 개수는 %d이다." % Character.count)

elf1 = Character("엘프1")
elf2 = Character("엘프2")
elf3 = Character("엘프3")
elf1.showInfo()
elf2.die()
elf1.showInfo()
