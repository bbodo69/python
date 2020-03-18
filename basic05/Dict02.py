# 성적처리 프로그램
'''
*** 글로벌 학원 ***
1. 학생정보 출력 (학생전체)
2. 학생정보 입력 (학생추가)
3. 학생정보 수정 
4. 학생정보 삭제 
5. 학생정보 검색 
6. 총점, 평균 
7. 종료 
'''

scores = {"name1":100, "name2":70, "name3":80, "name4":95, "name5":75}

def list_student():
    for i,j in scores.items():
        print("%s 학생의 점수는 %d 입니다" %(i,j))

def add_student(name, score):
    scores[name] = score
    print("현재 학생 / 점수 리스트")
    print(scores)
    print()

def update_student(name, score):
    if name in scores:
        score_before = scores[name]
        scores[name] = score
        print("%s 학생의 점수가 %d -> %d 점으로 변경 되었습니다. " %(name, score_before, score))
    else:
        print("없는 학생입니다.")

def delete_student(name):
    if name in scores:
        scores.__delitem__(name)
        print("학생 %s 가 삭제 되었습니다" %name)
    else:
        print("없는 학생입니다.")

def search_student(name):
    if name in scores:
        print("%s의 점수는 %d 입니다." %(name, scores[name]))
    else:
        print("없는 학생입니다.")

def total_avg():
    total = sum(scores.values())
    avg = total/len(scores)
    print("총 학생수는 %d 명, 학생들의 총 합은 %d, 평균은 %d 입니다" %(len(scores), total, avg))


while True:
    print("*** 글로벌 학원 ***\n1. 학생정보 출력 (학생전체)\n2. 학생정보 입력 (학생추가)\n3. 학생정보 수정\n4. 학생정보 삭제\n5. 학생정보 검색\n6. 총점, 평균\n7. 종료 ")
    print()
    print("현재 학생 / 점수 리스트")
    print(scores)
    print()
    selector = int(input("메뉴를 선택해주세요."))
    print()
    if selector==1:
        list_student()

    elif selector==2:
        name = input("학생의 이름을 입력해주세요")
        score = int(input("점수를 입력해주세요."))
        add_student(name, score)

    elif selector==3:
        name = input("수정할 학생을 입력해주세요")
        score = int(input("수정할 점수를 입력해주세요."))
        update_student(name, score)

    elif selector==4:
        name = input("삭제할 학생을 입력해주세요")
        delete_student(name)

    elif selector==5:
        name = input("검색할 학생을 입력해주세요")
        search_student(name)

    elif selector==6:
        total_avg()

    elif selector==7:
        break
    print()
