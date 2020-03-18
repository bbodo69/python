class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print("부모클라스")
        print("이름 : ", self.name)
        print("나이 : ", self.age)

#=========================================

class Student(Person):
    pass
    # 메서드 오버라이딩
    def __init__(self, name, age, num):
        super().__init__(name, age) #부모가 가진 생성자를 호출
        self.num = num

    # 메서드 오버라이딩딩
    def showInfo(self):
        print("자식클라스")
        super().showInfo()
        print("숫자 : ", self.num)

#=========================================
s = Student("학생", 10, 2020)
s.showInfo()