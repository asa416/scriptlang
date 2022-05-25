from urllib import response
from urllib.request import urlopen
#from urllib.parase import
from urllib.parse import urlencode,unquote,quote_plus,quote
import urllib
from collections import defaultdict

sigun_list = []

BASEBALL, SOCCER, TENNIS, SWIM, BALLGYM = range(5)


myData = defaultdict(lambda:defaultdict(int))

def getDataBaseball():
    url = 'https://openapi.gg.go.kr/PublicTrainingFacilityBasebal'

    queryParams = '?' + urlencode({ quote_plus('KEY') : '8b7e606c85b44ac2bbd02d70fcbc135d',
    quote_plus('Type'):'xml',
    quote_plus('pSize'):'1000',
    quote_plus('pIndex'):'1'
    })

    request = urllib.request.Request(url+unquote(queryParams))
    # print ('Your Request:\n'+url+queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    return response_body

def getDataSoccer():
    url = 'https://openapi.gg.go.kr/PublicTrainingFacilitySoccer'

    queryParams = '?' + urlencode({ quote_plus('KEY') : 'cc3702232f9d4e70a663bc53279486e1',
    quote_plus('Type'):'xml',
    quote_plus('pSize'):'1000',
    quote_plus('pIndex'):'1'
    })

    request = urllib.request.Request(url+unquote(queryParams))
    # print ('Your Request:\n'+url+queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    return response_body

def getDataTennis():
    url = 'https://openapi.gg.go.kr/PublicTennis'

    queryParams = '?' + urlencode({ quote_plus('KEY') : 'ff5245121c4440f59a365a2d57e923d0',
    quote_plus('Type'):'xml',
    quote_plus('pSize'):'1000',
    quote_plus('pIndex'):'1'
    })

    request = urllib.request.Request(url+unquote(queryParams))
    # print ('Your Request:\n'+url+queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    return response_body

def getDataSwim():
    url = 'https://openapi.gg.go.kr/PublicSwimmingPool'

    queryParams = '?' + urlencode({ quote_plus('KEY') : '53976cb9ccc8418e97a1e06da922d0a0',
    quote_plus('Type'):'xml',
    quote_plus('pSize'):'1000',
    quote_plus('pIndex'):'1'
    })

    request = urllib.request.Request(url+unquote(queryParams))
    # print ('Your Request:\n'+url+queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    return response_body

def getDataBall():
    url = 'https://openapi.gg.go.kr/PublicGameOfBallGymnasium'

    queryParams = '?' + urlencode({ quote_plus('KEY') : 'c5d4e782fc8c4037b2f3051f7c82b46b',
    quote_plus('Type'):'xml',
    quote_plus('pSize'):'1000',
    quote_plus('pIndex'):'1'
    })

    request = urllib.request.Request(url+unquote(queryParams))
    # print ('Your Request:\n'+url+queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    return response_body

def makeList(sport):
    from xml.etree import ElementTree

    global sigun_list
    global myData

    tree = ElementTree.fromstring(sport)
    itemElements = tree.iter('row')
    for item in itemElements:
        sigun = item.find("SIGUN_NM")
        myData[sigun.text][sports[sport]] += 1    
        if sigun.text not in sigun_list:
            sigun_list.append(sigun.text)
            

def makeLists():
    
    global baseball, soccer, tennis, swim, ballGym

    makeList(baseball)
    makeList(soccer)
    makeList(tennis)
    makeList(swim)
    makeList(ballGym)

    # 임시방편입니다
    # 왜 테니스만 2개씩 들어가는지 모르겠어요...
    global myData
    for d in myData.values():
        d[TENNIS] //= 2

    return sigun_list

baseball = getDataBaseball()
soccer = getDataSoccer()
tennis = getDataTennis()
swim = getDataSwim()
ballGym = getDataBall()

sports = {baseball:BASEBALL, soccer:SOCCER, tennis:TENNIS, swim:SWIM, ballGym:BALLGYM}