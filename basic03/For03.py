# 문제10. 별찍기
print("\n\n문제10")

for i in range(1,6):
    print("%d행 : ***" %i)

print()

for i in range(1,6):
    print("*"*i)

print()

for i in range(5, 0, -1):
    print("*" * i)

print()

for j in range(1,6):
    for i in range(j, j+5):
        print(i,end="")
    print()

print()

for j in range(5,0,-1):
    for i in range(j, j+5):
        print(i,end="")
    print()

print()

for i in range(1,6):
    print("*"*i)
for i in range(4, 0, -1):
    print("*" * i)



for i in range(5,-1,-1):
    print(" "*i,end="")
    print("*"*(5-i))

print()

for i in range(0,5):
    print(" "*i,end="")
    print("*"*(5-i))

for i in range(6,-1,-1):
    print(" "*i,end="")
    print("*"*(6-i))
for i in range(1,6):
    print(" "*i,end="")
    print("*"*(6-i))

print()

for i in range(4, -1, -1):
    print(" "*i,end="")
    print("*"*(5-i),end="")
    print("*"*(4-i),end="")
    print(" "*i, end="")
    print()

print()

for i in range(0, 5):
    print(" "*i,end="")
    print("*"*(5-i),end="")
    print("*"*(4-i),end="")
    print(" "*i, end="")
    print()

print()

for i in range(5, 0, -1):
    print("*" * i)
for i in range(1,6):
    print("*"*i)

print()


for i in range(0,4):
    print("*"*(4-i), end="")
    print(" " * i, end="")
    print(" ", end="")
    print(" "*i, end="")
    print("*" * (4 - i), end="")
    print()
print()
for i in range(1,5):
    print("*"*(i), end="")
    print(" "*(4-i), end="")
    print(" ", end="")
    print(" "*(4-i), end="")
    print("*"*(i), end="")
    print(" ", end="")
    print()

print()

i = 1
while i<6:
    print("*"*i)
    i+=1






