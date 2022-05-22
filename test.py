from tkinter import *

window = Tk()
window.title("TEST")
window.geometry("800x600")
window.resizable(width=False, height=False)

test_image = PhotoImage(file='image/baseball.png').subsample(20)

bnt = Button(window,image=test_image)
bnt.pack()

window.mainloop()