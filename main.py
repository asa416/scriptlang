#------------------------------------------------------------------------------
# ScriptLanguage Project
# By SeokJu
#------------------------------------------------------------------------------
from tkinter import *
from tkinter import font
# import tkinter.ttk as myTtk

def InitScreen():
    fontTitle = font.Font(window,size=18,weight='bold',family='바탕체')
    fontNormal = font.Font(window, size=15, weight='bold')

    frameTitle=Frame(window, padx=10,pady=10,bg="red")
    frameTitle.pack(side='top',fill='x')
    frameCombo = Frame(window,pady=10,bg='green')
    frameCombo.pack(side='top',fill='x')
    frameEntry=Frame(window,pady=10,bg='blue')
    frameEntry.pack(side='top',fill='x')
    frameList=Frame(window,padx=10,pady=10,bg='yellow')
    frameList.pack(side='bottom',fill='both',expand=True)

    MainText = Label(frameTitle,font=fontTitle,text='경기도 공공체육시설 찾기')
    MainText.pack(anchor='center',fill='both')

    global SearchListBox
    LBScrollbar = Scrollbar(frameCombo)
    SearchListBox = Listbox(frameCombo,font=fontNormal,activestyle='none',width=10,
    height=1,borderwidth=12,relief='ridge',yscrollcommand=LBScrollbar.set)
    slist=['가평군', '고양시', '광명시', '구리시', '김포시', '남양주시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '양평군', '여주시', '연천군', '용인시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']
    for i, s in enumerate(slist):
        SearchListBox.insert(i,s)
    SearchListBox.pack(side='left',padx=10,expand=True,fill='both')

    LBScrollbar.pack(side='left')
    LBScrollbar.config(command=SearchListBox.yview)

    sendEmailButton=Button(frameCombo,font=fontNormal,text='검색')
    sendEmailButton.pack(side='right',padx=10,fill='y')

    global InputLabel
    InputLabel = Entry(frameEntry, font=fontNormal,width=26,borderwidth=12,relief='ridge')
    InputLabel.pack(side='left',padx=10,expand=True)

    SearchButton = Button(frameEntry,font=fontNormal,text='검색')
    SearchButton.pack(side='right',padx=10,expand=True,fill='both')

    global listBox
    LBScrollbar=Scrollbar(frameList)
    listBox=Listbox(frameList, selectmode='extended',font=fontNormal,width=10,height=15,borderwidth=12,relief='ridge',yscrollcommand=LBScrollbar.set)
    # listBox.bind('<<ListBoxSelect>>',event_for_listbox)
    listBox.pack(side='left',anchor='n',expand=True,fill='x')
    LBScrollbar.pack(side='right',fill='y')
    LBScrollbar.config(command=listBox.yview)

window = Tk()
window.geometry("400x600+300+100")

InitScreen()
window.mainloop()


url = "https://openapi.gg.go.kr/PublicTrainingFacilityBasebal?Key=8b7e606c85b44ac2bbd02d70fcbc135d&Type=xml&pIndex=1&pSize=100"

