# 파라미터와 인자의 개수, 순서가 일치해야 한다.
# 파라미터 순서가 바뀌어도 가능한 방법
# 인자 기입시, 파라미터명=값

def signup(username, pw, name, gender, email, nation): # 초기값 지정, 항상 끝에 와야한다.
    print(username)
    print(pw)
    print(name)
    print(gender)
    print(email)
    print(nation)

signup(pw='1',username='3',nation='4',email='5',gender='6',name='7')