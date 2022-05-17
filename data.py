from urllib import response
from urllib.request import urlopen
#from urllib.parase import
from urllib.parse import urlencode,unquote,quote_plus,quote
import urllib

def getDataBaseball():
    url = 'https://openapi.gg.go.kr/PublicTrainingFacilityBasebal'

    queryParams = '?' + urlencode({ quote_plus('KEY') : '8b7e606c85b44ac2bbd02d70fcbc135d',
    quote_plus('Type'):'xml',
    quote_plus('pSize'):'300',
    quote_plus('pIndex'):'1'
    })

    request = urllib.request.Request(url+unquote(queryParams))
    print ('Your Request:\n'+url+queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    return response_body

def getDataSoccer():
    url = 'https://openapi.gg.go.kr/PublicTrainingFacilitySoccer'

    queryParams = '?' + urlencode({ quote_plus('KEY') : 'cc3702232f9d4e70a663bc53279486e1',
    quote_plus('Type'):'xml',
    quote_plus('pSize'):'300',
    quote_plus('pIndex'):'1'
    })

    request = urllib.request.Request(url+unquote(queryParams))
    print ('Your Request:\n'+url+queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    return response_body

sportsList = ['Baseball', 'Soccer', 'Tennis']

def makeList():
    from xml.dom.minidom import parseString
    from xml.etree import ElementTree

    global baseball, soccer


    tree = ElementTree.fromstring(baseball)

    sigunListBaseball =[]

    itemElements = tree.iter("row")
    for item in itemElements:
        sigun = item.find("SIGUN_NM")
        if sigun.text not in sigunListBaseball:
            sigunListBaseball.append(sigun.text)

    tree2 = ElementTree.fromstring(soccer)

    sigunListSoccer =[]

    itemElements = tree2.iter("row")
    for item in itemElements:
        sigun = item.find("SIGUN_NM")
        if sigun.text not in sigunListSoccer:
            sigunListSoccer.append(sigun.text)


    return sigunListBaseball, sigunListSoccer

baseball = getDataBaseball()
soccer = getDataSoccer()