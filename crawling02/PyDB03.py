from crawling02 import PyDB02 as dao
import datetime
# 전체 조회
# dao.selectAll()

# 회원 한명 조회
dao.selectOne(('java2',)) # 인자는 튜플 형태로

# 회원 추가
# dao.insertUser(('pytest01', '1234', 10, datetime.datetime.now()))

# 회원삭제
dao.deleteUser(('pytest01',))