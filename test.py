#------------------------------------------------------------------------------
# 실험용 시군명 리스트 만들기
#------------------------------------------------------------------------------
from xml.etree import ElementTree

SigunList = []

with open('공공체육시설현황(야구).xml','rb') as f:
    strXml = f.read().decode('UTF-8')
parseData = ElementTree.fromstring(strXml)
elements=parseData.iter('row')

i = 1
for item in elements:
    part_el = item.find('SIGUN_NM')

    if part_el.text not in SigunList:
        SigunList.append(part_el.text)

SigunList.remove("시군명")

print(SigunList)

