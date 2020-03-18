'''
*** 상속 inheritance ***
class A:            # 부모 클래스
    변수, 메서드
class B(A):         # 자손 클래스
    pass

# 파이썬은 다중상속을 허용 -> 족보가 꼬이기 쉬움.
# 메서드 오버라ㅣㅇ딩
    상속관계에서 성립
'''

class Student1:
    def python(self):
        print("재밌어 파이썬")

class Student2:
    def c(self):
        print("재밌어 c")

class Student3:
    def java(self):
        print("재밌어 자바")

class Name1(Student1, Student2, Student3):
    pass

#======================================================

name = Name1()
name.c()