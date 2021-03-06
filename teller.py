import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
import re
from datetime import date, datetime

BASEBALL, SOCCER, TENNIS, SWIM, BALLGYM = range(5)

import noti

NOTICE = '''모르는 명령어입니다.\n
명령어를 보시려면 help를 입력해주세요.
'''

HELP = '''명령어 도움말\n
야구 [지역번호], 축구 [지역번호], 테니스 [지역번호], 수영 [지역번호], 구기 [지역번호]
\n지역번호 [가평군 : 41820, 고양시 : 41280, 과천시 : 41290,
광명시 : 41210, 광주시 : 41610,구리시 : 41310, 군포시 : 41410,
김포시 : 41570, 남양주시 : 41360, 동두천시 : 41250, 부천시 : 41190,
성남시 : 41130, 수원시 : 41110, 시흥시 : 41390, 안산시 : 41270,
안성시 : 41550, 안양시 : 41170, 양주시 : 41630, 양평군 : 41830,
여주시 : 41670, 연천군 : 41800, 오산시 : 41370, 용인시 : 41460,
의왕시 : 41430, 의정부시 : 41150, 이천시 : 41500, 파주시 : 41480,
평택시 : 41220, 포천시 : 41650, 하남시 : 41450, 화성시 : 41590]
'''

def replyAptData(user,loc_param, sport):
    print(user, loc_param)
    res_list = noti.getData(loc_param, sport)

    msg =''
    for r in res_list:
        print(str(datetime.now()).split('.')[0],r)
        if len(r+msg)+1>noti.MAX_MSG_LENGTH:
            noti.sendMessage(user, msg)
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        noti.sendMessage(user,msg)
    else:
        noti.sendMessage(user,'해당하는 데이터가 없습니다.')

def save(user, loc_param):
    conn = sqlite3.connect('users.db')
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(user TEXT,location TEXT,PRIMARY KEY(user,location))')
    try:
        cursor.execute('INSERT INTO users(user,location) VALUES("%s","%s")'%(user,loc_param))
    except sqlite3.IntegrityError:
        noti.sendMessage(user,'이미 해당 정보가 저장되어 있습니다.')
        return
    else:
        noti.sendMessage(user,'저장되었습니다.')
        conn.commit()

def check( user ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT,PRIMARY KEY(user, location) )')
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall():
        row = 'id:' + str(data[0]) + ', location:' + data[1]
        noti.sendMessage( user, row )

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id,'난 텍스트 이외의 메시지는 처리하지 못해요.')
        return
    text=msg['text']
    args=text.split(' ')
    if text.startswith('야구') and len(args)>1:
        replyAptData( chat_id, args[1], BASEBALL)
    elif text.startswith('축구') and len(args)>1:
        replyAptData( chat_id, args[1], SOCCER)
    elif text.startswith('테니스') and len(args)>1:
        replyAptData( chat_id, args[1], TENNIS)
    elif text.startswith('수영') and len(args)>1:
        replyAptData( chat_id, args[1], SWIM)
    elif text.startswith('구기') and len(args)>1:
        replyAptData( chat_id, args[1], BALLGYM)
    else:
        noti.sendMessage(chat_id, HELP)

today = date.today()
print('[',today,']received token:', noti.TOKEN)

from noti import bot
pprint(bot.getMe())

bot.message_loop(handle)

print('Listening...')

while 1:
    time.sleep(10)