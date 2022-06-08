import sys
import telepot
from pprint import pprint
from urllib.request import urlopen
import traceback
from xml.etree import ElementTree
from xml.dom.minidom import parseString

from data import *

TOKEN = '5562382017:AAHih7vbGfToXnLS0179qLDm_pvMvEP4-lg'
MAX_MSG_LENGTH = 300
bot = telepot.Bot(TOKEN)

def getAddress(s):
    return '주소 없음'if not s else s

def getData(loc_param, sport):
    res_list = []

    if sport == BASEBALL:
        xmlData = getDataBaseball(loc_param)
    elif sport == SOCCER:
        xmlData = getDataSoccer(loc_param)
    elif sport == TENNIS:
        xmlData = getDataTennis(loc_param)
    elif sport == SWIM:
        xmlData = getDataSwim(loc_param)
    elif sport == BALLGYM:
        xmlData = getDataBall(loc_param)

    tree = ElementTree.fromstring(xmlData)

    items = tree.iter("row")
    for item in items:
        sigun = item.find('SIGUN_NM').text
        name = item.find("FACLT_NM").text
        address = item.find("REFINE_LOTNO_ADDR").text
        row=name + '(' + getAddress(address) + ')'
        res_list.append(row)
    if sport == TENNIS:
        res_list = list(set(res_list))
    res_list.insert(0, sigun)
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user,msg)
    except:
        traceback.print_exception(*sys.exc_info(),file=sys.stdout)