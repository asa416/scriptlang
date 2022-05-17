import math
from tkinter import * # Import tkinter
from random import randint

NOT_FINSIHED, CORRECT, WRONG = range(3)

class Hangman:
    def __init__(self):
        self.setWorld()
        self.draw()

    def draw(self):
        # 한꺼번에 지울 요소들을 "hangman" tag로 묶어뒀다가 일괄 삭제.
        canvas.delete("hangman")

        # 인자 : (x1,y1)=topleft, (x2,y2)=bottomright, start=오른쪽이 0도(반시계방향), extent=start부터 몇도까지인지
        #    style='pieslice'|'chord'|'arc'
        canvas.create_arc(20, 200, 100, 240, start = 0, extent = 180, style='chord', tags = "hangman") # Draw the base
        canvas.create_line(60, 200, 60, 20, tags = "hangman")  # Draw the pole
        canvas.create_line(60, 20, 160, 20, tags = "hangman") # Draw the hanger
        
        str2 = None
        if self.finished == NOT_FINSIHED:
            str = "단어 추측:"+''.join(self.guessWord)
            if self.nMissChar != 0:
                str2 = "틀린 글자:"+''.join(self.nMissedLetters)
        elif self.finished == CORRECT:
            str = ''.join(self.guessWord)+' 맞았습니다'
            str2 = "게임을 계속하려면 ENTER를 누르세요"
        elif self.finished == WRONG:
            str = "정답:"+self.hiddenWord
            str2 = "게임을 계속하려면 ENTER를 누르세요"
        canvas.create_text(200, 190, text=str, tags='hangman')
        canvas.create_text(200, 210, text=str2, tags='hangman')

        if self.nMissChar < 1:
            return
        radius = 20 # 반지름
        canvas.create_line(160, 20, 160, 40, tags = "hangman") # Draw the hanger
        

        if self.nMissChar < 2:
            return
        # Draw the circle
        canvas.create_oval(140, 40, 180, 80, tags = "hangman") # Draw the hanger

        if self.nMissChar < 3:
            return
        # Draw the left arm (중심(160,60)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
        x1 = 160 - radius * math.cos(math.radians(45))
        y1 = 60 + radius * math.sin(math.radians(45))
        x2 = 160 - (radius+60) * math.cos(math.radians(45))
        y2 = 60 + (radius+60) * math.sin(math.radians(45))

        canvas.create_line(x1, y1, x2, y2, tags = "hangman")
        
        if self.nMissChar < 4:
            return
        # Draw the right arm
        x1 = 160 + radius * math.cos(math.radians(45))
        y1 = 60 + radius * math.sin(math.radians(45))
        x2 = 160 + (radius + 60) * math.cos(math.radians(45))
        y2 = 60 + (radius + 60) * math.sin(math.radians(45))
        canvas.create_line(x1, y1, x2, y2, tags='hangman')

        if self.nMissChar < 5:
            return
        # Draw the body
        canvas.create_line(160, 80, 160, 140, tags='hangman')

        if self.nMissChar < 6:
            return
        # Draw the left leg
        x1 = 160
        y1 = 140
        x2 = 160 - (radius+60) * math.cos(math.radians(45))
        y2 = 140 + (radius+60) * math.sin(math.radians(45))
        canvas.create_line(x1, y1, x2, y2, tags='hangman')

        if self.nMissChar < 7:
            return
        # Draw the right leg
        x1 = 160
        y1 = 140
        x2 = 160 + (radius + 60) * math.cos(math.radians(45))
        y2 = 140 + (radius + 60) * math.sin(math.radians(45))
        canvas.create_line(x1, y1, x2, y2, tags='hangman')

    def setWorld(self):
        i = randint(0, len(words) - 1)
        self.hiddenWord = words[i]
        self.guessWord = []
        for _ in range(len(self.hiddenWord)):
            self.guessWord.append('*')
        self.nCorrectChar = 0
        self.nMissChar = 0
        self.nMissedLetters = []
        self.finished = NOT_FINSIHED

    def guess(self, letter):
        import re
        i = 0
        if self.hiddenWord.find(letter) == -1:
            self.nMissChar += 1
            self.nMissedLetters.append(letter)
        else:
            while True:
                p = self.hiddenWord.find(letter,i)
                if p == -1:
                    break
                if self.guessWord[p] == '*':
                    self.guessWord[p] = letter
                    self.nCorrectChar += 1
                i = p + 1
        self.checking()
        self.draw()

    def checking(self):
        if self.nMissChar == 7:
            self.finished = WRONG
        elif self.nCorrectChar == len(self.hiddenWord):
            self.finished = CORRECT

    def reset(self):
        self.setWorld()
        self.draw()           

# Initialize words, get the words from a file
infile = open("Games\hangman.txt", "r")
words = infile.read().split()

window = Tk() # Create a window
window.title("행맨") # Set a title

def processKeyEvent(event):  
    global hangman
    if event.char >= 'a' and event.char <= 'z':
        if hangman.finished == NOT_FINSIHED:
            hangman.guess(event.char)
    elif event.keycode == 13:
        if hangman.finished == CORRECT or hangman.finished == WRONG:
            hangman.reset()
    
width = 400
height = 280    
# 선, 다각형, 원등을 그리기 위한 캔버스를 생성
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

hangman = Hangman()

# Bind with <Key> event
canvas.bind("<Key>", processKeyEvent)
# key 입력 받기 위해 canvas가 focus 가지도록 함.
canvas.focus_set()

window.mainloop() # Create an event loop
