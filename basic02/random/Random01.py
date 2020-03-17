"""
*** Random 난수 ***
*seed : 임의로 선택하는 것처럼 만들어주는 숫자

"""

import random

# (1) 숫자리스트 샘플링
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = random.sample(numlist, 3)
print(s)  # [1, 2, 8]

# (2) 튜플 샘플링
frutes = ('사과', '귤', '포도', '배')
s = random.sample(frutes, 2)
print(s)  # ['배', '사과']


# 문제1. 동전던지기. 앞면 (0), 뒷면 (1) 인지 출력

coin_side = random.randint(0, 1)
if coin_side == 0:
    print("앞면")
else:
    print("뒷면")


# 문제2. 가위(0), 바위(1), 보(2) 게임
'''
컴퓨터와 가위바위보 대결하기
컴퓨터는 임의의 값을 가지고,
플레이어는 입력을 하여 서로 비교한 후,
플레이어가 이겼는지, 비겼는지, 졌는지 출력
'''

rsp = ['가위', '바위', '보']
result_rsp = str(random.sample(rsp, 1))[2:-2]
player = input("가위, 바위, 보 입력")

if player == "가위" and result_rsp == "가위":
    print("플레이어 %s, 컴퓨터 %s 비겼습니다." %(player, result_rsp))
elif player == "가위" and result_rsp == "보":
    print("플레이어 %s, 컴퓨터 %s 이겼습니다." %(player, result_rsp))
elif player == "가위" and result_rsp == "바위":
    print("플레이어 %s, 컴퓨터 %s 졌습니다." %(player, result_rsp))
elif player == "바위" and result_rsp == "보":
    print("플레이어 %s, 컴퓨터 %s 졌습니다." %(player, result_rsp))
elif player == "바위" and result_rsp == "가위":
    print("플레이어 %s, 컴퓨터 %s 이겼습니다." %(player, result_rsp))
elif player == "바위" and result_rsp == "바위":
    print("플레이어 %s, 컴퓨터 %s 비겼습니다." %(player, result_rsp))
elif player == "보" and result_rsp == "가위":
    print("플레이어 %s, 컴퓨터 %s 졌습니다." %(player, result_rsp))
elif player == "보" and result_rsp == "바위":
    print("플레이어 %s, 컴퓨터 %s 이겼습니다." %(player, result_rsp))
elif player == "보" and result_rsp == "보":
    print("플레이어 %s, 컴퓨터 %s 비겼습니다." %(player, result_rsp))


