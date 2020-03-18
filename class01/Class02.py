class Person:
    # 변수
    name = ""
    age = 0
    gender = ""
    blood = ""

    # 메서드
    def speak(self):
        print("말하다")

    def eat(self):
        print("먹다")

    def showInfo(self):
        print("이름 : %s" % self.name)

person = Person()

print(person.speak())
person.name = "휴머노이드"
person.age = 1
print(person.showInfo())
