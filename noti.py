import sys
import telepot
from pprint import pprint
import urllib
from urllib.request import urlopen
import traceback
from xml.etree import ElementTree
from xml.dom.minidom import parseString

key = '8b7e606c85b44ac2bbd02d70fcbc135d'
TOKEN = '5557473516:AAEHL1QHM6rfclxZtm-R1Epo1PvOV7NX1Dc'
MAX_MSG_LENGTH = 300
baseurl='https://openapi.gg.go.kr/PublicTrainingFacilityBasebal?KEY='+key+'&Type=xml&pSize=1000&pIndex=1'
bot = telepot.Bot(TOKEN)

def getData(loc_param):
    res_list = []
    url = baseurl+'&SIGUN_CD='+loc_param

    request = urllib.request.Request(url)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')

    tree = ElementTree.fromstring(response_body)

    items = tree.iter("row")
    for item in items:
        build = item.find("FACLT_NM").text
        name = item.find("SIGUN_NM").text
        row=build + ',' + name
        res_list.append(row)
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user,msg)
    except:
        traceback.print_exception(*sys.exc_info(),file=sys.stdout)