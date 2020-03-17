'''
*** 문자열 str ***
    '문자열' "문자열" """여러줄 문자열""" (홑따옴표도 여러줄 문자열 가능)

    문자열 indexing
    0 1 2 3 4
    h e l l o

'''
print("hello python")
print('''hello


python''')

memo = """안녕하세요
저는 아무래 입니다
나이는 10 살 입니다."""
print(memo)

first = "python"
secont = " is easy"
third = first + secont
print(third)

str1 = "Global IT"
print(str1[0],str1[1])

# hello 믄지열을 변수에 저장하고거꾸로 출력해 보자
hello = "hello"

hello0 = hello[0]
hello1 = hello[1]
hello2 = hello[2]
hello3 = hello[3]
hello4 = hello[4]

print(hello4+hello3+hello2+hello1+hello0)

# 문자열 수정 불가능
# 문자열 슬라이싱(slicing)
# 변수명[시작번호:끝번호+1]
helloSlicing1 = hello[0:5]
helloSlicing2 = hello[0:4]
helloSlicing3 = hello[:5]
print(helloSlicing1)
print(helloSlicing2)
print(helloSlicing3)

str4 = "prigraming"
# programming 수정하기

str4Pri = str4[0:2]
str4Gram = str4[3:6]
str4ing = str4[6:]
str4Programing = str4Pri + "o" +str4Gram + "m" + str4ing
str4 = str4Pri + "o" +str4Gram + "m" + str4ing
print(str4Programing)
print(str4)

# 날짜 잘라보기
import datetime

date = str(datetime.date.today())
print(date)

year = date[:4]
month =  date[5:7]
day = date[8:]

print(date)
print(year)
print(month)
print(day)

print ("내 생일은 %s 년 %s 월 %s일 입니다" %(year, month, day))

