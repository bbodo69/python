# 문자열 함수

# 문자열 바꾸기 : replace()
str = "apple tree"
print(str)
str = str.replace("apple", "lemon")
print(str)

# 문자열 나누기 : split()

a,b,c,d,e="1 2 3 4 5".split() # 구분자 저장안하면 공백을 기준으로 분할
print(a)
print(b)
print(c)
print(d)
print(e)

str1 = "Global:Institute"
a, b = str1.split(':') # 구분자 지정
print(a)
print(b)

# 문자열 길이 : len()
str2 = "aksdafdjhaspkffjhaskdfasdashdjkas"
print(len(str2))

# 문자 개수 구하기 : count('문자')
print(str2.count('f'))

# 문자의 위치 알려주는(1) : find() # 찾는 값이 -1 로 리턴
print(str2.find('f'))
# 문자의 위치 알려주는(2) : index() # 찾는 값이 없으면 에러 발생
print(str2.index('f'))

str = "Apple Tree"
# 소문자를 대문자로 바꿔주는 : upper()
print(str.upper())
# 대문자를 소문자로 바꿔주는 : lower()
print(str.lower())
# 공백 지우기 : strip(), lstrip(), rstrip()

stripEx = "         p                    y       th               o n "
print(stripEx)
print(stripEx.strip())
print(stripEx.lstrip())
print(stripEx.rstrip())


