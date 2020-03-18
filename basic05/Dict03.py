# **kwargs : *args와 비슷한 개념의 파라미터
#       1. 함수 호출시, 몇개가 될지 모르는 키=벨루의 쌍의 형태의 인자를
#          받아주기 위한 파라미터
#          여러개의 데이터를 동시에 받아주기 때문에, for문과 items() 함수를 통해
#          key 와 value로 값을 분리시켜 사용하는 공식이 필요
#       2. 작성위치 : 파라미터 뒷부분에 위치, 초기값파라미터 앞.
#          일반파라미터 -> *파라미터 -> **파라미터 -> 초기값 파라미터

#packing : 낱개로 던저주는 키=밸루 형태의 데이터들을
#            딕셔너리로 패킹해서 받아주는 형
def packer(name = None,**kwargs):

    print(name)
    print(kwargs.keys())
    print(kwargs.values())
    for i,j in kwargs.items():
        print("%s 는 %s 입니다." %(i, j))

packer(name="가오리", age="30", mob="010-1111-1111", city="seoul")

# unpacking : 딕셔너리를 던져주면 변수에 unpacking 해서 받는 형태
def unpacker(name=None, score=None):
    if name and score:
        print("안녕하세요, %s님의 점수는 %d 입니다." % (name, score))
    else:
        print("이름 또는 점수가 없습니다.")
    print(name)
    print(score)


unpacker(**{"name" : "피카츄", "score" : 30})
unpacker(**{"name" : "피카츄"})
unpacker(**{"score" : 30})


