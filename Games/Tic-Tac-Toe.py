from tkinter import *

def winOrLose(token):
    if (cells[0][0].token == token and cells[0][1].token == token and cells[0][2].token == token) or\
        (cells[1][0].token == token and cells[1][1].token == token and cells[1][2].token == token) or\
        (cells[2][0].token == token and cells[2][1].token == token and cells[2][2].token == token) or\
        (cells[0][0].token == token and cells[1][0].token == token and cells[2][0].token == token) or\
        (cells[0][1].token == token and cells[1][1].token == token and cells[2][1].token == token) or\
        (cells[0][2].token == token and cells[1][2].token == token and cells[2][2].token == token) or\
        (cells[0][0].token == token and cells[1][1].token == token and cells[2][2].token == token) or\
        (cells[0][2].token == token and cells[1][1].token == token and cells[2][0].token == token):
        global running
        running = False
        return True        
    return False

def isFull():
    for i, row in enumerate(cells):
        for c, cell in enumerate(row):
            if cell.token == '':
                return False
    global running
    running = False
    return True

def cellReset(event):
    global currentToken
    global running
    running = True
    for i, row in enumerate(cells):
        for c, cell in enumerate(row):
            cell.token = ''
            cell["image"]=images[cell.token]
    currentToken = 'O'
    str.set(currentToken+" 차례")

def endGame(event):
    window.destroy()

class Cell(Label):
    def __init__(self, *args, img):
        self.token = ''
        Label.__init__(self, *args, image=img)
        self.bind("<Button-1>", self.flip)

    def flip(self, event):
        global currentToken
        global str
        if running == False:
            return
        if self.token != '':
            return
        self.token = currentToken
        if currentToken == 'O':
            currentToken = 'X'
        else:
            currentToken = 'O'
        if winOrLose(self.token):
            str.set(self.token+"승리! 게임이 끝났습니다")
        elif isFull():
            str.set("비김! 게임이 끝났습니다")
        else:
            str.set(currentToken+" 차례")
        self["image"]=images[self.token]



window = Tk()
window.title("Tic-Tac-Toe")

img_O = PhotoImage(file='image/o.gif')
img_X = PhotoImage(file='image/x.gif')
img_empty = PhotoImage(file='image/empty.gif')

images = {'':img_empty,'O':img_O,'X':img_X}

running = True

GameFrame=Frame(window)
GameFrame.pack(side='top',expand=True,fill='both')

currentToken = 'O'

cells = [[Cell(GameFrame, img = images['']) for _ in range(3)] for _ in range(3)]

for r, row in enumerate(cells):
    for c, cell in enumerate(row):
        cell.grid(row=r,column=c,padx=5,pady=5)

str = StringVar()
str.set(currentToken+" 차례")

statusFrame=Frame(window)
statusFrame.pack(expand=True,fill='both')
statusLabel = Label(statusFrame,textvariable=str).pack(expand=True)

EndFrame = Frame(window)
EndFrame.pack(expand=True,fill='both')

restartButton = Button(EndFrame, text="재시작")
exitButton = Button(EndFrame, text="종료")

restartButton.pack(side="left", expand=True, fill='both',padx=5, pady=5)
restartButton.bind("<Button-1>", cellReset)
exitButton.pack(side="right", expand=True, fill='both',padx=5, pady=5)
exitButton.bind("<Button-1>", endGame)

window.mainloop()