'''
# 파이선 다중상속 주의점
파이썬은 클래스/메서드 탐색 순서는 MRO(Method Resolution Order)를 따른다
다중상속 시, 부모 클래스 나열할때 우선순위 왼쪽 -> 오른쪽
동일 메서드가 둘 이상의 부모에 존재하면 왼쪽 클래스의 메서드가 실행
클래스명.rmo()를 통해 순서 확인 가능
MRO 가 꼬이도록 클래스를 정의하면
TypeError : ..................(MRO) 에러 메세지 발생
'''

class A:
    pass

print(A.mro())  # A

class B(A):
    pass

print(B.mro()) # B -> A

class C(A):
    pass

print(C.mro()) # C -> A

class D(B, C):
    pass

print(D.mro()) # D -> B -> C -> A

class E(C, B):
    pass

print(E.mro())

class F(D, E):
    pass

print(F.mro())