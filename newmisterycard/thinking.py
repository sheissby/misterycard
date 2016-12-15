# encoding:utf-8
from Login import *

# 获取npc的值
def getNPC():
    url = host + '/meditation.php?do=Info&v=6378&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    data = ''
    jsonresponse = connection(url, data)

    # 获得npc列表的最后一个值
    npc = jsonresponse.get('data', 0).get('NpcList', 0)[-1]
    return npc

def thinking():
    num = 0
    npc = getNPC()
    url = host + '/meditation.php?do=Npc&v=6382&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    data = 'NpcId=' + str(npc)
    jsonresponse = connection(url, data)
    Type = jsonresponse.get('data', 0).get('AwardItem', 0).get('Type', 0)
    value = jsonresponse.get('data', 0).get('AwardItem', 0).get('Value', 0)
    # 获得金色碎片
    if Type == 1 and int(value) == 5:
        num = num + 1
        return num
    else:
        return num

def clear():
    url = host + '/meditation.php?do=Deal&v=6384&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    data = ''
    jsonresponse = connection(url, data)

ids = [
    ['Csus4', '2013121714341555', '254543', 'LnQ6qpKCyY95nIrg'],
    ['Dsus4', '2013122514488598', '290176', 'LnQ6qpKCyY95nIrg'],
      ]

i = input('输入循环次数：')
for id in ids:
    jinsenum = 0
    for times in range(1, i+1):
        print times
        if verification(id) == 1:
            for count in range(1, 11):
                Num = thinking()
                jinsenum = jinsenum + Num
            clear()
        else:
            break
    print id[0], '获得金色碎片 '+ str(jinsenum) +'个'
