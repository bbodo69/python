'''
*** 딕셔너리 Dict ***
1. key와 value 로 구성된다.
2. key값은 고유한 값으로, 하나만 적용되고 나머지는 제외된다. (중복x)
3. 수정가능 mutable
4. 변수명 = {key:value, key:value, key:value....}
5. 구분기호 : { : }
6. key 는 불변하므로 list, dict, set 같이 수정가능한 타입은 적용x
7. 딕셔너리는 순서가 없다. 구분은 key
8. **kwargs : *args와 비슷한 개념의 파라미터
'''

# 빈 딕셔너리 만들기
dic = {}
print(dic)
print(type(dic))

dic = {"글로벌": "IT", "서울": "코리아", "A클래스": "겁나잘함"}
print(dic["글로벌"])

# key를 꺼내오는 함수 : keys()
key_list = dic.keys()
print(key_list)
print(type(key_list))

# value를 꺼내오는 함수 : values()
value_list = dic.values()
print(value_list)
print(type(value_list))

# key와 value를 쌍으로 꺼내오는 함수 : item()
item = dic.items()
print(item)
print(type(item))

info = {"mob": "010-0000-0000", "age": 20, "name": "홍길동"}

# key 값을 이용해서 value를 꺼내오는 함수 : get()
mob = info.get("mob")
# 없는 값의 경우 결과값을 null 로 표시
city = info.get("city")
print(mob)
print(city)

mob1 = info["mob"]
# 없는 값의 경우 에러발생
# city1 = info["city"]
print(mob1)
# print(city1)

# 딕셔너리에 해당 키값이 존재하는지 알아보기 : in
result = "age" in info
print(result)

# 딕셔너리에 요소 처리하기 : update()
info.update({"city": "seoul"})
print(info)

# 기존의 키 값이 존재하면 value 값만 변경해 준다.
info.update({"city": "busan"})
print(info)

info["gender"] = "female"
print(info)
info["gender"] = "male"
print(info)

# 요소 제거하기 : _delitem_(키값)
info.__delitem__("gender")
print(info)

