'''
*** 모듈과 패키지 ***
모듈
    1) 함수가 파이썬이 제공하는 내장 함수가 있듯이
        모듈 또한 파이썬이 제공하는 표준 모듈이 있다.
    2) 함수는 단순 명령문들의 집합이지만,
        모듈은 클래스, 함수, 변수 등으로 구성 된다.
    3) 함수는 사용자가 작성하는 프로그램파일 내에 존재하지만,
        모듈은 별도의 .py 파일로 존재한다.

모듈 사용법
    import 모듈명

    from basic04,guiEx import Gui01 as g

표쥰 모듈 Doc
    http://docs.python.org/ko/3/library.index.html

*** GUI (Graphic User Interface) ***
    1) 컨테이너
    2) 컴포넌트
    3) 배치관리자
    4) 이벤트

표준 라이브러리에 있는 tkinter 모듈 사용

# 배치관리자 3가지
    1) pack : 상하좌우로 컴포넌트(위젯)을 배치
    2) grid : 행과 열로 구획을 지어서 컴포넌트 배치
    3) place : 좌표를 지정해서 컴포넌트 배치

    #1. pack
        1) side : 위젯을 배치하는 시작점 설정
            TOP(기본값, 위), LEFT, RIGHT, BOTTOM
        2) fill : 위젯을 화면에 꽉차게 표시
                X(가로), Y(세로), BOTH(둘다)
        3) expand : 창 크기가 변하면, 위젯의 배치도 비율대로 변함
        4) padx : 좌우 여백 지정
        5) pady : 상하 여백 지정
        6) anchor : 위젯을 방위에 따라 배치
            E, W, S, W, SW, SE, NW, NE

    #2. grid
        1) row : 행 번호
        2) column : 열 번호
        3) rowspan : 행의 개수
        4) columnspan : 열의 개수

'''
from tkinter import * # tkinter 라는 모듈안에 모든값을 import 하겠다.

#1. 컨테이너
window = Tk()

#2. 컴포넌트
b1 = Button(window, text="one")
b2 = Button(window, text="two")
b3 = Button(window, text="three")
b4 = Button(window, text="병합을 수행")

#3. 배치관리자
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0, columnspan=3)

#4. 루프돌리기 : thread : 신호를 기다리면서 무한적으로 반복해서 화면 띄우기
window.mainloop()


