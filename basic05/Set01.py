'''
*** set 집합 ***
dict에서 value를 버리고 key만 남은 형태와 비슷
1. set 키워드 사용
2. 중복을 허용하지 않는다.
3. 순서가 없다.
4. 2.3 버전부터 지원
5. set : 어떤것이 존재하는지 여부만 판단하기 위해서 주로 사용
    dict : 키에 어떤 정보를 첨부하여 결과를 얻거나 저장을 위해 주로 사용
6. 교집합 intersection 합집합 union 차집합 difference
7. 변수명 = set()  # 빈 set 생성
    변수명 = set(리스트, 문자열, 튜플, 딕셔너리)
        * 중복된 값을 버리고 남은 값들을 담는다.
'''

s1 = set([1,1,1,2,3,4,5,6,7,8])
print(s1)
s2 = set([3,6,8,9])
print(s2)

# 교집합 : &
print(s1 & s2)
print(s1.intersection(s2))

# 합집합 : |
print(s1 | s2)
print(s1.union(s2))

# 차집합 : -
print(s1 - s2)
print(s1.difference(s2))

# 추가하기 : add()
s3 = set([1,2,3])
print(s3)
s3.add(4)
print(s3)

# 삭제하기 : remove()
s3.remove(4)
print(s3)

'''
변수 자료형
    숫자 : int float
    참거짓 : bool
    문자/열 : str
    리스트 list
    튜플 tuple
    딕셔너리 dict
    집합 set

연산자
제어문 : if / for / while
함수 : def

기초 문법 ^
----------------------------
클래스
예외처리
입출력
(gui)

파이썬 문법 ^
----------------------------
크롤링 

    
    
'''