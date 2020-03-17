# 객체의 구조화
class Person:
    def __init__(self, name, age):
        # 인스턴스 변수
        self.name = name
        self.age = age

    def walk(self):
        print("걷자!")
    def eat(self):
        pass
#-----------------------------------------

p1 = Person('홍길동', 10)
print(p1.name)
print(p1.age)

#------------------------------------------
class Postman(Person):
    # 생성자 오버라이딩
    def __init__(self, name, age, *args, **kwargs):
        super().__init__(name,age)
        # **kwargs 가 키=벨류 형태의 인자들을 한번에 모두 받아서
        # item() 함수를 이용하여 키=벨류 형태의 값들을 모두 꺼내고
        # 반복문을 통해 i, j에 각각 키, 벨류로 반복할때마다 데이터를 담고
        self.data = []              # self 를 붙이면서 post1 이 갖고 다니는 인스턴스 변수화
        for i in args:              # 키=밸류 값이 아닌 불특정 인자를 배열로 받아준다.
            self.data.append(i)
        for i, j in kwargs.items():
            # setattr() 라는 함수를 이용하여 인스턴스 변수를 만들어준다.
            # 이때 self 는 생성자를 호출하는 객체가 되고
            # i, j 는 순서대로 i =key값 = 변수명, j = value = 변수의 값으로
            # 인스턴스 변수로 생성된다.
            setattr(self, i, j)

#-------------------------------------------
post1 = Postman("누구", 20, 1,2,3,4,5,6,'이것도 되나?', gender="f", section="B")
print(post1.name)
print(post1.age)
print(post1.gender)
print(post1.section)
print(post1.data)
#--------------------------------------------

dic = dict()
for i in range(3):

    lst = list()
    for j in range(50):
        lst.append(Postman("postman"+str(j+1), 20+j, section="A", worktime="8hours"))
    dic.update({"monster"+str(i+1):lst})

print(lst[30].name)

print(lst[30].age)
print(lst[30].section)
print(lst[30].worktime)
print(lst[5].walk())

print(dic["monster1"][10].name)