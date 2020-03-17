from tkinter import *

window = Tk()

def test():
    print("확인 버튼 누름")

b1 = Button(window, text="확인", fg="blue", command=test)
b2 = Button(window, text="종료", fg="blue", command=window.quit)

b1.pack()
b2.pack()

window.mainloop()