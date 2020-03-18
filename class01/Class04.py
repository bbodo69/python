# 클래스 변수 vs 인스턴스 변수
# 클래스 변수 : 객체들의 공통점, 객체들이 공용으로 사용할 때 만든다.
#               메서드 밖 선언
# 인스턴스 변수 : 객체에 데이터를 저장하고 싶을때 만든다.
#               메서드 안 선언

#전역변수
test = 0

class Starbucks:
    # 클래스 
    shape = ""

    def say(self):
        # 메서드안 -> 인스턴스변수(self.변수명) or 지역변수(변수명)
        
        self.msg = "안녕하세요 스타벅스 입니다"
        print(self.msg)
############################################################################
s1 = Starbucks()    # 1호점
s2 = Starbucks()    # 2호점

print(s1.say())

print(s1.shape)
print(s2.shape)
print("==========")
# 클래스 변수 : 클래스명.변수명, 인스턴스명.변수명
Starbucks.shape = "Star"
print(Starbucks.shape)
# 인스턴스변수 : 인스턴스명.변수명
# -> 인스턴스명.변수명으로 값대입을 안해주면 클래스변수를 참조한다.
print(s1.shape)
print(s2.shape)
print("==========")
s1.shape = "Square"
print(Starbucks.shape)
print(s1.shape)
print(s2.shape)







