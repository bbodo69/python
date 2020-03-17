'''
파일 읽기
r : 읽기 모드 : open()에 파ㅣㅇㄹ 모드 지정안하면 기본값 r 로 처리
'''

f = open("data.txt")

# # 1. read(byte) : 바이트수 만큼 읽기
# rea = f.read(5)
# print(rea)
#
# # 2. read() : 전체 읽기
# rea = f.read()
# print(rea)

# # 3. seek(byte)
# f.seek(0) # 0 == 처음
# rea = f.read(20)
# print(rea)

# 4. readLine()
f.seek(0)
lines = f.readlines()
print(len(lines))
print(lines)

# 작성한 글자 거꾸로 출력
for line in lines:
    print(line[::-1])

f.close()

with open("data.txt", 'r', encoding="utf-8") as f:
    line = f.readline()
    print(line, " = lineeeeeeeee")