# 문제1. sum() 함수를 구현하기 : my_sum()
# 문제2. max() 함수를 직접 구현하기 : my_max()
# 문제3. min() 함수를 직접 구현하기 : my_min()
# 문제4. index() 함수를 직접 구현하기 : my_index()
# 문제5. count() 함수를 직접 구현하기 : my_count()
# 문제6. (심화) replace() 함수 구현하기

# 문제1. sum() 함수를 구현하기 : my_sum()

def my_sum(*num):
        total = 0
        for i in num:
            total +=i
        print(total)

my_sum(22,6,7,8)

# 문제2. max() 함수를 직접 구현하기 : my_max()

def my_max(*num):

    index = 0
    lst = []

    for i in num:
        lst.append(i)
        index += 1

    i = 0
    count = len(lst) - 1
    print("count = ", count)

    while True:

        if lst[i] < lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            i += 1
            count = len(lst) -1
            if i == len(lst)-1:
                i = 0
        else:
            i += 1
            if i == len(lst)-1:
                i = 0
            count -= 1
            if count == 0:
                break

    print(lst[0])

my_max(4,55,9,6,4,2,8,4,23,232,55,3,2,2,66,98,45,2,2,34)

# 문제3. min() 함수를 직접 구현하기 : my_min()

def my_min(*num):
    index = 0
    lst = []

    for i in num:
        lst.append(i)
        index += 1

    i = 0
    count = len(lst) - 1
    print("count = ", count)

    while True:

        if lst[i] < lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i += 1
            count = len(lst) - 1
            if i == len(lst) - 1:
                i = 0
        else:
            i += 1
            if i == len(lst) - 1:
                i = 0
            count -= 1
            if count == 0:
                break

    print(lst[len(lst)-1])


my_min(4, 55, 9, 6, 4, 2, 8, 4, 23, 232, 55, 3, 2, 2, 66, 98, 45, 2, 2, 34)

# 문제4. index() 함수를 직접 구현하기 : my_index()

lst = [1,5,3,5,7,8,3,5,76,23,46,568,86,54,234,32,1,23,2,2]

def my_index(lst, num):
    count = 0
    check = 0
    for i in lst:
        if i == num:
            print(count)
            check = 1
            break
        count +=1
    if check==0:
        print("일치하는 값이 없습니다.")

my_index(lst, 234)

# 문제5. count() 함수를 직접 구현하기 : my_count()

str = "apple pineapple melon application app"

i = 0
while i <= len(str):
    print(str[i:i+1])
    i += 1


def my_count(str1, str2):
    return 0

# 문제6. (심화) replace() 함수 구현하기


