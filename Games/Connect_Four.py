from tkinter import *

_MAXROW = 6
_MAXCOL = 7

Turn = 'red'

class Cell(Canvas):
    def __init__(self, parent, row, col, width = 20, height = 20):
        Canvas.__init__(self, parent, width = width,height=height,bg="blue",borderwidth=2)
        self.color = "white"
        self.row = row
        self.col = col
        self.create_oval(4,4,20,20,fill=self.color,tags='oval')
        self.bind("<Button-1>", self.clicked)

    def clicked(self, event):
        global Turn
        global cells
        global process_button
        if self.color != "white" or Turn == None:
            return
        if (self.row == _MAXROW - 1):    
            self.setColor(Turn)
            Turn = 'red' if Turn == 'yellow' else 'yellow'
            if self.__checkHorizontal() or self.__checkVertical() or self.__checkDiag1() or self.__checkDiag2():
                str = self.color + " 승리!"
                process_button["text"] = str
                Turn = None
                
        elif (cells[self.row + 1][self.col].color != "white"):
            self.setColor(Turn)
            Turn = 'red' if Turn == 'yellow' else 'yellow'
            if self.__checkHorizontal() or self.__checkVertical() or self.__checkDiag1() or self.__checkDiag2():
                str = self.color + " 승리!"
                process_button["text"] = str
                Turn = None

    def setColor(self, color):
        self.delete("oval")
        self.color = color
        self.create_oval(4,4,20,20,fill=self.color,tags='oval')

    def reset(self):
        self.color = "white"
        self.delete("oval")
        self.create_oval(4,4,20,20,fill=self.color,tags='oval')

    def __checkVertical(self):
        checkList = []
        checkRow = self.row
        global cells
        cnt = 0
        maxcnt = 0
        plag = False
        for j in range(_MAXCOL):
            if cells[checkRow][j].color == self.color:
                if plag == False:
                    plag = True
                cnt += 1
                checkList.append((checkRow,j))
            else:
                plag = False
                if cnt > maxcnt:
                    maxcnt = cnt
                    if maxcnt < 4:
                        checkList.clear()
                cnt = 0

        if cnt > maxcnt:
            maxcnt = cnt

        if maxcnt >= 4:
            for i, j in checkList:
                cells[i][j]["bg"] = self.color
            return True 
        return False          

    def __checkHorizontal(self):
        checkList = []
        checkCol = self.col
        global cells
        cnt = 0
        maxcnt = 0
        plag = False
        for i in range(_MAXROW):
            if cells[i][checkCol].color == self.color:
                if plag == False:
                    plag = True
                cnt += 1
                checkList.append((i,checkCol))
            else:
                plag = False
                if cnt > maxcnt:
                    maxcnt = cnt
                    if maxcnt < 4:
                        checkList.clear()
                cnt = 0

        if cnt > maxcnt:
            maxcnt = cnt

        if maxcnt >= 4:
            for i, j in checkList:
                cells[i][j]["bg"] = self.color
            return True 
        return False    

    def __checkDiag1(self):
        # / 방향 확인 row + 1 col - 1
        checkList=[]
        r, c = self.row, self.col
        while r < _MAXROW - 1 and c > 0:
            r += 1
            c -= 1
        cnt = 0
        maxcnt = 0
        plag = False
        while r > 0 and c < _MAXCOL:
            if cells[r][c].color == self.color:
                if plag == False:
                    plag = True
                cnt += 1
                checkList.append((r,c))
            else:
                plag = False
                if cnt > maxcnt:
                    maxcnt = cnt
                    if maxcnt < 4:
                        checkList.clear()
                cnt = 0
            r -= 1
            c += 1

        if cnt > maxcnt:
            maxcnt = cnt    

        if maxcnt >= 4:
            for i, j in checkList:
                cells[i][j]["bg"] = self.color
            return True 
        return False

    def __checkDiag2(self):
        # \ 방향 확인 row + 1 col + 1
        checkList = []
        r, c = self.row, self.col
        while r > 0 and c > 0:
            r -= 1
            c -= 1
        cnt = 0
        maxcnt = 0
        plag = False
        while r < _MAXROW and c < _MAXCOL:
            if cells[r][c].color == self.color:
                if plag == False:
                    plag = True
                cnt += 1
                checkList.append((r,c))
            else:
                plag = False
                if cnt > maxcnt:
                    maxcnt = cnt
                    if maxcnt < 4:
                        checkList.clear()
                cnt = 0
            r += 1
            c += 1
        if cnt > maxcnt:
            maxcnt = cnt

        if maxcnt >= 4:
            for i, j in checkList:
                cells[i][j]["bg"] = self.color
            return True 
        return False



def restart(event):
    global cells
    global Turn
    Turn = 'red'
    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            cell["bg"] = 'blue'
            cell.reset()             
    process_button["text"] = restart_text

window = Tk()
window.title('Connect Four')

frame1 = Frame(window)
frame1.pack()
cells = [[Cell(frame1, j, i, width=20,height=20) for i in range(_MAXCOL)] for j in range(_MAXROW)]
for i, row in enumerate(cells):
    for j, cell in enumerate(row):
        cell.grid(row=cell.row,column=cell.col)

frameButton = Frame(window)
frameButton.pack()

restart_text = "새로 시작"

process_button = Button(frameButton, text=restart_text)
process_button.bind("<Button-1>", restart)
process_button.pack()

window.mainloop()