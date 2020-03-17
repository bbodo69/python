def writeThings(things):
    with open("data.txt", "a") as f:
        f.write(things+"\n")
        # f 객체변수가 해당 with open 블럭에서만 존재하고
        # 블럭실행이 종료되면 소멸된다.
        # --> f.close()해줄 필요가 없다.

if __name__ == '__main__':
    writeThings(input("저장할 것 작성 : "))