from tkinter import *

win = Tk()

r2d2 = PhotoImage(file = "r2d2.gif")

# 레이블, 이미지 같은 것을 클릭 버튼으로 만들때

lab1 = Label(win, image=r2d2).pack(side="right")

memo = '''
이미지는 gif와 ppm/pgm포맷만 사용 가능
특정 모듈을 import하면, 다른 포맷의 이미지도 사용 가능하다.
'''
lab2 = Label(win, text=memo, padx=10).pack(side="left")

win.mainloop()

