'''
*** 파이썬 -Oracle DB 연동
# 라이브러리
    cx-Oracle(pycharm)
    cx_Oracle(pip)
'''
import cx_Oracle

# 1. 회원 전체 조회
def selectAll():
    connection = cx_Oracle.connect("java13/java13@nullmaster.iptime.org:3000/orcl")
    cursor = connection.cursor()

    sql = "select * from test"
    cursor.execute(sql)

    for record in cursor:
        print(record)

    cursor.close()
    connection.close()

# 회원 조회
def selectOne(tup):
    connection = cx_Oracle.connect("java13/java13@nullmaster.iptime.org:3000/orcl")
    cursor = connection.cursor()

    sql = "select * from test where id=:1"
    cursor.execute(sql, tup)
    print(cursor.fetchone())
    cursor.close()
    connection.close()

# 2. 회원 추가
import datetime # 시간삽입을 위해

def insertUser(tup):    # 매개변수를 튜플 형태로 받을것

    connection = cx_Oracle.connect("java13/java13@nullmaster.iptime.org:3000/orcl")
    cursor = connection.cursor()
    sql = "insert into test values(:1, :2, :3, :4)" # 쿼리문자 : place-holder ": 숫자"
    cursor.execute(sql, tup)
    cursor.close()
    connection.commit() # 수동 커밋
    connection.close()

# 회원 비번 수정
def updatePw(tup):
    connection = cx_Oracle.connect("java13/java13@nullmaster.iptime.org:3000/orcl")
    cursor = connection.cursor()
    sql = "update test set pw=:1 where id=:2"
    cursor.execute(sql, tup)
    cursor.close()
    connection.commit()  # 수동 커밋
    connection.close()

#  회원 삭제
def deleteUser(tup):
    connection = cx_Oracle.connect("java13/java13@nullmaster.iptime.org:3000/orcl")
    cursor = connection.cursor()

    sql = "delete from test where id=:1"
    cursor.execute(sql, tup)
    cursor.close()
    connection.commit()
    connection.close()
