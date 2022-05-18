#------------------------------------------------------------------------------
# ScriptLanguage Project
# By SeokJu
#------------------------------------------------------------------------------
from tkinter import *
from tkinter import font
import tkinter.ttk as myTtk
from tokenize import cookie_re
from data import *

curList = []
info_str = []
BGCOLOR = '#87CEEB'

# 버튼 클릭시
#------------------------------------------------------------------------------
def buttonClick(num):
    for k, v in sportsButton.items():
        if k == sportsList[num]:
            v['relief']='sunken'
        else:
            v['relief']='raised'             

def getStr(s):
    return ''if not s else s

# info에 info 출력 해주는 함수
#------------------------------------------------------------------------------
def showInfo(event):
    from xml.etree import ElementTree
    global listBox

    global info_str
    info_str = []
    info.delete(1.0, END)

    sels = listBox.curselection()
    iIndex = 0 if len(sels) == 0 else listBox.curselection()[0]
    
    tree = ElementTree.fromstring(baseball)
    elements = tree.iter('row')

    for item in elements:
        part_el = item.find('FACLT_NM')
        if curList[iIndex] == part_el.text:
            info_str.append(getStr(item.find('SIGUN_NM').text)+'\n')
            info_str.append(getStr(item.find('FACLT_NM').text)+'\n')
            info_str.append("준공연도: "+getStr(item.find('COMPLTN_YY').text)+'\n')
            info_str.append("주소: "+getStr(item.find('REFINE_LOTNO_ADDR').text)+'\n')
            break
    for i in range(len(info_str)):
        info.insert(float(i + 1), info_str[i])

# 리스트 박스에 항목들을 추가해주는 함수
#------------------------------------------------------------------------------
def SearchLibrary():
    from xml.etree import ElementTree

    global listBox
    listBox.delete(0, listBox.size())

    tree = ElementTree.fromstring(baseball)
    elements = tree.iter('row')

    global curList
    curList = []

    i = 1
    for item in elements:
        part_el = item.find('SIGUN_NM')

        if combo.get() == part_el.text:
            _text = "["+getStr(item.find('FACLT_NM').text)+"]"
            listBox.insert(i - 1, _text)
            i = i + 1  
            curList.append(getStr(item.find('FACLT_NM').text))

# 윈도우 생성
window = Tk()
window.title("HSJ")
window.geometry("800x600")
window.configure(bg=BGCOLOR)
window.resizable(width=False, height=False)

# 폰트 설정
fontTitle = font.Font(window,size=18,weight='bold',family='바탕체')
fontNormal = font.Font(window, size=15, weight='bold')

# 프레임 설정
#------------------------------------------------------------------------------
# 타이틀 출력 프레임
frameTitle=Frame(window, padx=10,pady=5,bg=BGCOLOR)
frameTitle.pack(side='top',fill='x')

# 종목 고르기 프레임
frameMenu = Frame(window, padx=10, pady=5, bg=BGCOLOR)
frameMenu.pack(side='top', fill='both')

# 검색 출력 프레임
frameCombo = Frame(window,padx=10,pady=5,bg=BGCOLOR)
frameCombo.pack(side='top',fill='x')

# 리스트, 정보 출력 프레임  
frameList=Frame(window,padx=10,pady=5,bg=BGCOLOR)
frameList.pack(side='top',expand=True,fill='both')

# 메일, 지도 버튼 프레임
frameB = Frame(window, padx=10, pady =5, bg=BGCOLOR)
frameB.pack(side='bottom',fill='x')


# GUI 배치
#------------------------------------------------------------------------------
# 제목
MainText = Label(frameTitle,font=fontTitle,text='경기도 공공체육시설 찾기',bg=BGCOLOR)
MainText.pack(anchor='center',fill='both')

# 종목 선택 버튼
buttonBaseball=Button(frameMenu, relief='sunken', padx=5, width=10, height=3, text='야구')
buttonBaseball.grid(row=0,column=0,sticky='ew',padx=5)
buttonSoccer=Button(frameMenu, relief='raised', padx=5, width=10, height=3, text='축구')
buttonSoccer.grid(row=0,column=1,sticky='ew', padx=5)
buttonTennis=Button(frameMenu, relief='raised', padx=5, width=10, height=3, text='테니스')
buttonTennis.grid(row=0,column=2,sticky='ew', padx=5)
sportsButton = {'Baseball': buttonBaseball, 'Soccer':buttonSoccer, 'Tennis':buttonTennis}
buttonBaseball['command']=lambda:buttonClick(0)
buttonSoccer['command']=lambda:buttonClick(1)
buttonTennis['command']=lambda:buttonClick(2)

# 시군 콤보박스
LBScrollbar = Scrollbar(frameCombo)
SearchListBox = Listbox(frameCombo,font=fontNormal,activestyle='none',width=10,
height=1,borderwidth=12,relief='ridge',yscrollcommand=LBScrollbar.set)
sigun_list = makeList()
combo  = myTtk.Combobox(frameCombo, values=sigun_list[0])
combo.pack(side=LEFT, expand=True, fill='both')
combo.set('시군 선택')

searchButton=Button(frameCombo,font=fontNormal,text='검색',command=SearchLibrary)
searchButton.pack(side='right',padx=10,fill='y')

# 리스트, 정보 출력
sigunList=Frame(frameList, bg=BGCOLOR)
sigunList.pack(side='left', fill='both',padx=5)
infoframe=Frame(frameList, bg=BGCOLOR)
infoframe.pack(side='right', fill='both',padx=5)

LBScrollbar=Scrollbar(sigunList)
listBox=Listbox(sigunList, selectmode='extended',font=fontNormal,width=20,height=14,borderwidth=10,relief='ridge',yscrollcommand=LBScrollbar.set)
listBox.bind('<Double-1>',showInfo)
listBox.pack(side='left',anchor='n',expand=True,fill='x')
LBScrollbar.pack(side='right',expand=True,fill='y')
LBScrollbar.config(command=listBox.yview)

info = Text(infoframe,font=fontNormal,width=50, height=15)
info.pack(side='left', fill='both')

# 메일, 지도 버튼
mailButton = Button(frameB, padx=5, width = 10, height = 3,text='Mail')
mapButton = Button(frameB, padx=5, width=10, height=3,text='Map')
mailButton.pack(side='left')
mapButton.pack(side='right')



# 메인루프
#------------------------------------------------------------------------------
window.mainloop()


url = "https://openapi.gg.go.kr/PublicTrainingFacilityBasebal?Key=8b7e606c85b44ac2bbd02d70fcbc135d&Type=xml&pIndex=1&pSize=100"

