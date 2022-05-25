#------------------------------------------------------------------------------
# ScriptLanguage Project
# By SeokJu
#------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
from tkinter import font
import tkinter.ttk as myTtk
from tokenize import cookie_re
from data import *
from send_email import sendMail
from email.mime.text import MIMEText
from image import ImageButton
from mapview import Map

curList = []
info_str = []
BGCOLOR = '#87CEEB'

sportsText = {BASEBALL:"Baseball", SOCCER:"Soccer", TENNIS:"Tennis", SWIM:"Swim", BALLGYM:"BallGym"}
sportsNow = BASEBALL

popup = inputEmail = btnEmail = None
addrEmail = None

curName = ''
curPos = []

# 그래프를 그려봅시다
def drawGraph(canvas, canvasWidth, canvasHeight):
    canvas.delete('grim')

    if not myData[curName] :
        canvas.create_text(canvasWidth/2, canvasHeight/2, text='No Data', tags='grim')
        return
    
    nData = len(myData[curName])
    nMax = max(myData[curName].values())
    nMin = min(myData[curName].values())
    
    canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill='white',tag='grim')

    rectWidth = canvasWidth // nData
    bottom = canvasHeight - 20
    maxheight = canvasHeight-40
    for i, (k, v) in enumerate(myData[curName].items()):
        if nMax == v:color='red'
        elif nMin == v:color='blue'
        else:color='grey'

        curHeight = maxheight*v/nMax
        top = bottom - curHeight
        left = i * rectWidth
        right = (i + 1) * rectWidth
        canvas.create_rectangle(left,top,right,bottom,fill=color,tag='grim',activefill='yellow')
    
        canvas.create_text((left+right)//2, top-10,text=v,tags='grim')
        canvas.create_text((left+right)//2, bottom+10, text=sportsText[k], tags='grim')

# 지도를 띄워봅시다
def makeMap():
    if len(curPos) == 0:
        messagebox.showinfo("검색 불가능", "지도 정보가 없습니다.")
        return
    if curPos[0] == '':
        messagebox.showinfo("검색 불가능", "지도 정보가 없습니다")
        return
    newMap = Map(window, float(curPos[0]), float(curPos[1]), curName)

def onEmailInput():
    global addrEmail
    addrEmail = inputEmail.get()
    send(addrEmail)
    popup.destroy() # popup 내리기

def onEmailPopup():
    global window, addrEmail, popup
    addrEmail = None
    popup = Toplevel(window, bg=BGCOLOR) # popup 띄우기
    popup.geometry("300x150")
    popup.title("받을 이메일 주소 입력")
    
    global inputEmail, btnEmail
    inputEmail = Entry(popup, width = 200)
    inputEmail.pack(fill='x', padx=10, expand=True)
   
    btnEmail = Button(popup, text="확인", command=onEmailInput)
    btnEmail.pack(anchor="s", padx=10, pady=10)


# 버튼 클릭시
#------------------------------------------------------------------------------
def buttonClick(num):
    global sportsNow
    sportsNow = num
    global combo
    for k, v in sportsButton.items():
        if k == sportsNow:
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
    global curName
    global curPos

    curPos = []

    global info_str
    info_str = []
    info.delete(1.0, END)

    sels = listBox.curselection()
    iIndex = 0 if len(sels) == 0 else listBox.curselection()[0]
    
    if sportsNow == BASEBALL:
        tree = ElementTree.fromstring(baseball)
    elif sportsNow == SOCCER:
        tree = ElementTree.fromstring(soccer)
    elif sportsNow == TENNIS:
        tree = ElementTree.fromstring(tennis)
    elif sportsNow == SWIM:
        tree = ElementTree.fromstring(swim)
    elif sportsNow == BALLGYM:
        tree = ElementTree.fromstring(ballGym)
    elements = tree.iter('row')

    for item in elements:
        part_el = item.find('FACLT_NM')
        if curList[iIndex] == part_el.text:
            info_str.append(getStr(item.find('SIGUN_NM').text)+'\n')
            info_str.append(getStr(item.find('FACLT_NM').text)+'\n')
            info_str.append("준공연도: "+getStr(item.find('COMPLTN_YY').text)+'\n')
            info_str.append("주소: "+getStr(item.find('REFINE_LOTNO_ADDR').text)+'\n')
            if sportsNow == BASEBALL:
                info_str.append("면적: "+getStr(item.find('AR').text)+'m^2\n')
                info_str.append("내야바닥: "+getStr(item.find('INFLD_BOTM_MATRL_NM').text)+'\n')
                info_str.append("외야바닥: "+getStr(item.find('OUTFLD_BOTM_MATRL_NM').text)+'\n')
                info_str.append("중앙길이: "+getStr(item.find('CENTER_LENG').text)+'m\n')
                info_str.append("1-3루길이: "+getStr(item.find('F_THDBASE_LENG').text)+'m\n')
            elif sportsNow == SOCCER:
                info_str.append("면적: "+getStr(item.find('AR').text)+'m^2\n')
                info_str.append("바닥: "+getStr(item.find('BOTM_MATRL_NM').text)+'\n')
                info_str.append("폭: "+getStr(item.find('BT').text)+'m\n')
                info_str.append("길이: "+getStr(item.find('LENG').text)+'m\n')
            elif sportsNow == TENNIS:
                info_str.append("면적: "+getStr(item.find('AR').text)+'m^2\n')
                info_str.append("바닥: "+getStr(item.find('BOTM_MATRL_NM').text)+'\n')
                info_str.append("코트 면 수: "+getStr(item.find('COURT_PLANE_CNT').text)+'\n')
            elif sportsNow == SWIM:
                info_str.append("정규 경영장 길이: "+getStr(item.find('REGULR_RELYSWIMPL_LENG').text)+'m\n')
                info_str.append("정규 경영장 폭: "+getStr(item.find('REGULR_RELYSWIMPL_BT').text)+'m\n')
                info_str.append("정규 경영장 레인 수: "+getStr(item.find('REGULR_RELYSWIMPL_LANE_CNT').text)+'\n')
                info_str.append("비정규 경영장 길이: "+getStr(item.find('IRREGULR_RELYSWIMPL_LENG').text)+'m\n')
                info_str.append("비정규 경영장 폭: "+getStr(item.find('IRREGULR_RELYSWIMPL_BT').text)+'m\n')
                info_str.append("비정규 경영장 레인 수: "+getStr(item.find('IRREGULR_RELYSWIMPL_LANE_CNT').text)+'\n')
                info_str.append("지도 검색 불가능")
                break        
            elif sportsNow == BALLGYM:
                info_str.append("가능 종목: "+getStr(item.find('POSBL_ITEM_NM').text)+'\n')
                info_str.append("바닥: "+getStr(item.find('BOTM_MATRL_NM').text)+'\n')
                info_str.append("면적: "+getStr(item.find('AR').text)+'m^2\n')
                info_str.append("높이: "+getStr(item.find('HG').text)+'m\n')
                info_str.append("길이: "+getStr(item.find('LENG').text)+'m\n')
                info_str.append("폭: "+getStr(item.find('BT').text)+'m\n')
                pass
            curName = part_el.text
            curPos.append(getStr(item.find('REFINE_WGS84_LAT').text))
            curPos.append(getStr(item.find('REFINE_WGS84_LOGT').text))
            if curPos[0] == '':
                info_str.append("지도 검색 불가능")
            else:
                info_str.append("지도 검색 가능")
            break
    for i in range(len(info_str)):
        info.insert(float(i + 1), info_str[i])

# 리스트 박스에 항목들을 추가해주는 함수
#------------------------------------------------------------------------------
def SearchLibrary():
    from xml.etree import ElementTree

    global listBox
    listBox.delete(0, listBox.size())

    if sportsNow == BASEBALL:
        tree = ElementTree.fromstring(baseball)
    elif sportsNow == SOCCER:
        tree = ElementTree.fromstring(soccer)
    elif sportsNow == TENNIS:
        tree = ElementTree.fromstring(tennis)
    elif sportsNow == SWIM:
        tree = ElementTree.fromstring(swim)
    elif sportsNow == BALLGYM:
        tree = ElementTree.fromstring(ballGym)

    elements = tree.iter('row')

    global curList, curName
    curList = []
    curName = combo.get()
    global graph
    drawGraph(graph, 300, 100)
    
    i = 1
    for item in elements:
        part_el = item.find('SIGUN_NM')

        if getStr(item.find('FACLT_NM').text) not in curList:
            if combo.get() == part_el.text:
                _text = "["+getStr(item.find('FACLT_NM').text)+"]"
                listBox.insert(i - 1, _text)
                i = i + 1  
                curList.append(getStr(item.find('FACLT_NM').text))

# 이메일 보내기!
##------------------------------------------------------------------------------
def send(recipientAddr):
    if len(info_str) == 0:
        return

    senderAddr = 'cheese04@tukorea.ac.kr'
    # recipientAddr = 'asa4163@naver.com'

    sendText = ''
    for str in info_str:
        sendText += str

    msg = MIMEText(sendText)
    msg['Subject'] = "경기도 공공시설체육 정보입니다."
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    sendMail(senderAddr,recipientAddr,msg)

# 윈도우 생성
window = Tk()
window.title("HSJ")
window.geometry("800x600")
window.configure(bg=BGCOLOR)
window.resizable(width=False, height=False)

# 폰트 설정
fontTitle = font.Font(window,size=18,weight='bold',family='휴먼둥근헤드라인')
fontNormal = font.Font(window, size=15, family='휴먼매직체')

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
frameB.pack(side='bottom',expand=True,fill='both')


# GUI 배치
#------------------------------------------------------------------------------
# 제목
MainText = Label(frameTitle,font=fontTitle,text='경기도 공공체육시설 찾기',bg=BGCOLOR, fg='white')
MainText.pack(anchor='center',fill='both')

# 종목 선택 버튼
buttonBaseball = ImageButton(frameMenu)
buttonBaseball.setImage('images/baseball.png')
buttonBaseball.configure(bg=BGCOLOR, bd=5)
buttonBaseball.grid(row=0,column=0,sticky='ew',padx=5)
buttonBaseball['command']=lambda:buttonClick(BASEBALL)

buttonSoccer = ImageButton(frameMenu)
buttonSoccer.setImage('images/soccer.png')
buttonSoccer.configure(bg=BGCOLOR, bd=5)
buttonSoccer.grid(row=0,column=1,sticky='ew',padx=5)
buttonSoccer['command']=lambda:buttonClick(SOCCER)

buttonTennis = ImageButton(frameMenu)
buttonTennis.setImage('images/tennis.png')
buttonTennis.configure(bg=BGCOLOR, bd=5)
buttonTennis.grid(row=0,column=2,sticky='ew',padx=5)
buttonTennis['command']=lambda:buttonClick(TENNIS)

buttonBall = ImageButton(frameMenu)
buttonBall.setImage('images/ballgym.png')
buttonBall.configure(bg=BGCOLOR, bd=5)
buttonBall.grid(row=0,column=4,sticky='ew',padx=5)
buttonBall['command']=lambda:buttonClick(BALLGYM)

buttonSwim = ImageButton(frameMenu)
buttonSwim.setImage('images/swim.png')
buttonSwim.configure(bg=BGCOLOR, bd=5)
buttonSwim.grid(row=0,column=3,sticky='ew',padx=5)
buttonSwim['command']=lambda:buttonClick(SWIM)

sportsButton = {BASEBALL:buttonBaseball, SOCCER:buttonSoccer, TENNIS:buttonTennis, BALLGYM:buttonBall, SWIM:buttonSwim, }


# 시군 콤보박스
LBScrollbar = Scrollbar(frameCombo)
SearchListBox = Listbox(frameCombo,font=fontNormal,activestyle='none',width=10,
height=1,borderwidth=12,relief='ridge',yscrollcommand=LBScrollbar.set)
sigun_list = makeLists()
combo  = myTtk.Combobox(frameCombo, values=sigun_list)
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
listBox.pack(side='left',anchor='n',expand=True,fill='both')
LBScrollbar.pack(side='right',expand=True,fill='y')
LBScrollbar.config(command=listBox.yview)

info = Text(infoframe,font=fontNormal,width=50, height=10)
info.pack(side='left', fill='both')

# 메일, 지도 버튼
mailButton = ImageButton(frameB)
mailButton.setImage('images/gmail.png')
mailButton.configure(padx=5, bg=BGCOLOR, bd=0)
mapButton = ImageButton(frameB)
mapButton.setImage('images/map.png')
mapButton.configure(padx=5, bg=BGCOLOR, bd=0)
mapButton['command'] = makeMap
mailButton['command'] = onEmailPopup
mailButton.pack(side='left')
mapButton.pack(side='right')
graph = Canvas(frameB, width=300, height=100, bg=BGCOLOR)
graph.place(relx=.5, rely=.5, anchor=CENTER)
drawGraph(graph, 300, 100)

# 그래프 그리기

# 메인루프
#------------------------------------------------------------------------------
window.mainloop()
