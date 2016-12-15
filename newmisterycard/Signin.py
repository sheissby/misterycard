# encoding:utf-8
from Login import *


def getAward():
    url = host + '/user.php?do=GetUserinfo&OpenCardChip=1&v=1002&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    data = 'pvpNewVersion=1'

    url1 = host + '/user.php?do=AwardSalary&v=1523&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    data1 = ''

    jsonresponse = connectionuntilsuccess(url, data)
    print id[0], 'GetUserinfo success'
    jsonresponse = connectionuntilsuccess(url1, data1)
    print id[0], 'AwardSalary success'


def GetUserMapStages():
    url = host + '/mapstage.php?do=GetUserMapStages&v=7002&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    jsonresponse = connectionuntilsuccess(url, data='')
    data = jsonresponse['data']
    if data:
        arr = [i for i in data if int(data[i]['CounterAttackTime']) != 0]
        return arr
    else:
        return GetUserMapStages()


def EditUserMapStages(arr):
    url = host + '/mapstage.php?do=EditUserMapStages&v=7003&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    for i in arr:
        data = 'isManual=0&MapStageDetailId=' + i
        jsonresponse = connectionuntilsuccess(url, data)


def Worship():
    url = host + '/worship.php?do=Worship&v=8123&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    for type in ['1', '2', '3']:
        data = 'Type=' + type
        jsonresponse = connectionuntilsuccess(url, data)

ids = Amid()

for id in ids:
    if verification(id) == 1:
        getAward()
        arr = GetUserMapStages()
        print arr
        if arr:
            EditUserMapStages(arr)
        Worship()
