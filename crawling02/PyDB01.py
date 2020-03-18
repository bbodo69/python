'''
*** 파이썬 -Oracle DB 연동
# 라이브러리
    cx-Oracle(pycharm)
    cx_Oracle(pip)



'''
import cx_Oracle

# 1. 전체 데이터 조회
# connection = cx_Oracle.connect("java13/java13@nullmaster.iptime.org:3000/orcl")
# cursor = connection.cursor()
#
# sql = "select * from test"
# cursor.execute(sql)
#
# for record in cursor:
#     print(record)
#
# cursor.close()
# connection.close()

# 2. 1개 데이터 삽입
import datetime # 시간삽입을 위해
connection = cx_Oracle.connect("java13/java13@nullmaster.iptime.org:3000/orcl")
cursor = connection.cursor()
# data = ('python_id', 'python_pw', 1, datetime.datetime.now())   # 매핑시킬데이터는 튜플로
# cursor.execute(sql, data)

# 여러개 데이터 삽입
# 튜플형태의 레코드들을 리스트로 묶어서 데이터 통으로 준비
users = [
    ('python_id1', 'python_pw', 1, datetime.datetime.now()),
    ('python_id2', 'python_pw', 1, datetime.datetime.now()),
    ('python_id3', 'python_pw', 1, datetime.datetime.now()),
    ('python_id4', 'python_pw', 1, datetime.datetime.now())
]

sql = "insert into test values(:1, :2, :3, :4)" # 쿼리문자 : place-holder ": 숫자"

# 1번째 방법 : for 문으로 execute 반복시키기
# for i in users:
#     cursor.execute(sql, i)

# 2번째 방법 :
# cursor.arraysize = len(users) # 리스트로 묶은 레코드의 개수 지정
# cursor.executemany(sql, users) # 한번에 저장 시키기

cursor.close()
connection.commit() # 수동 커밋
connection.close()

# 3. 데이터 개수 조회
connection = cx_Oracle.connect("java13/java13@nullmaster.iptime.org:3000/orcl")
cursor = connection.cursor()

# sql = "select count(*) from test"
# cursor.execute(sql)
#
# count = cursor.fetchone()
# print(type(count))
# print("회원수 :", count[0])

cursor.close()
connection.close()

# 4. 데이터 수정하기
connection = cx_Oracle.connect("java13/java13@nullmaster.iptime.org:3000/orcl")
cursor = connection.cursor()

# sql = "update test set pw='1' where id='java1'"
# cursor.execute(sql)

# id = input("아이디 입력")
# new_pw = input("새 비밀번호 입력")
# sql = "update test set pw=:1 where id=:2"
# data = (new_pw, id) # 튜플형태로 데이터 합치기
# cursor.execute(sql, data)

cursor.close()
connection.commit()
connection.close()

# 5. 데이터 삭제
connection = cx_Oracle.connect("java13/java13@nullmaster.iptime.org:3000/orcl")
cursor = connection.cursor()

sql = "delete from test where id='java1'"
cursor.execute(sql)
cursor.close()
connection.commit()
connection.close()

