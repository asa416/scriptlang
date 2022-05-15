from urllib import response
from urllib.request import urlopen
#from urllib.parase import
from urllib.parse import urlencode,unquote,quote_plus,quote
import urllib

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

from xml.dom.minidom import parseString
from xml.etree import ElementTree
tree = ElementTree.fromstring(response_body)

itemElements = tree.iter("row")
for item in itemElements:
    isbn = item.find("SIGUN_NM")
    title = item.find("SIGUN_CD")
    if title.text == "41190":
        print ("ISBN:", isbn.text, "S", title.text)