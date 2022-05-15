#------------------------------------------------------------------------------
# ScriptLanguage Project
# By SeokJu
#------------------------------------------------------------------------------
from tkinter import *
from tkinter import font
import tkinter.ttk as myTtk

def InitScreen():
    fontTitle = font.Font(window,size=18,weight='bold',family='바탕체')
    fontNormal = font.Font(window, size=15, weight='bold')

# 타이틀 출력 프레임
    frameTitle=Frame(window, padx=10,pady=10,bg="#87CEEB")
    frameTitle.pack(side='top',fill='x')

# 종목 고르기 프레임
    frameMenu = Frame(window, padx=5, pady=10, bg='#87CEEB')
    frameMenu.pack(side='top', fill='both')

# 검색 출력 프레임
    frameCombo = Frame(window,padx=10,pady=10,bg='#87CEEB')
    frameCombo.pack(side='top',fill='x')

# 리스트, 정보 출력 프레임  
    frameList=Frame(window,padx=10,pady=10,bg='#87CEEB')
    frameList.pack(side='bottom',fill='both',expand=True)

    sigunList=Frame(frameList, bg='#87CEEB')
    sigunList.pack(side='left', fill='both', expand=True, padx=5)
    infoframe=Frame(frameList, bg='#87CEEB')
    infoframe.pack(side='right',fill='both', expand=True, padx=5)

    MainText = Label(frameTitle,font=fontTitle,text='경기도 공공체육시설 찾기',bg="#87CEEB")
    MainText.pack(anchor='center',fill='both')

    buttonBaseball=Button(frameMenu, relief='groove', padx=5, width=10, height=5, bg='red')
    buttonBaseball.grid(row=0,column=0,sticky='news',padx=5)
    buttonSoccer=Button(frameMenu, relief='groove', padx=5, width=10, height=5, bg='blue')
    buttonSoccer.grid(row=0,column=1,sticky='news', padx=5)
    buttonTennis=Button(frameMenu, relief='groove', padx=5, width=10, height=5, bg='green')
    buttonTennis.grid(row=0,column=2,sticky='news', padx=5)


    global SearchListBox
    LBScrollbar = Scrollbar(frameCombo)
    SearchListBox = Listbox(frameCombo,font=fontNormal,activestyle='none',width=10,
    height=1,borderwidth=12,relief='ridge',yscrollcommand=LBScrollbar.set)
    sigun_list=['가평군', '고양시', '광명시', '구리시', '김포시', '남양주시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '양평군', '여주시', '연천군', '용인시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']
    combo  = myTtk.Combobox(frameCombo, values=sigun_list)
    combo.pack(side=LEFT, expand=True, fill='both')
    combo.set('시군 선택')
    
    sendEmailButton=Button(frameCombo,font=fontNormal,text='검색')
    sendEmailButton.pack(side='right',padx=10,fill='y')

    global listBox
    LBScrollbar=Scrollbar(sigunList)
    listBox=Listbox(sigunList, selectmode='extended',font=fontNormal,width=10,height=15,borderwidth=12,relief='ridge',yscrollcommand=LBScrollbar.set)
    # listBox.bind('<<ListBoxSelect>>',event_for_listbox)
    listBox.pack(side='left',anchor='n',expand=True,fill='both')
    LBScrollbar.pack(side='right',fill='y')
    LBScrollbar.config(command=listBox.yview)

    info = Entry(infoframe,font=fontNormal)
    info.pack(side='right', expand=True,fill='both')

window = Tk()
window.geometry("600x800+300+100")
window.configure(bg='blue')
window.resizable(width=False, height=False)
InitScreen()
window.mainloop()


url = "https://openapi.gg.go.kr/PublicTrainingFacilityBasebal?Key=8b7e606c85b44ac2bbd02d70fcbc135d&Type=xml&pIndex=1&pSize=100"

