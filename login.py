# encoding:utf-8
import ConfigParser
from con_log import *
from id import *
from verification import verification

config = ConfigParser.ConfigParser()
config.read('init.conf')
isverification = config.get('verification', 'login')


def getAward():
    url = host + '/user.php?do=GetUserinfo&OpenCardChip=1&v=1522&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    data = 'pvpNewVersion=1'
    url1 = host + '/user.php?do=AwardSalary&v=1523&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    data1 = ''
    jsonresponse = connection(url, data)
    print id1[0], 'GetUserinfo sucess!'

    jsonresponse = connection(url1, data1)
    print id1[0], 'AwardSalaryres sucess!'

def GetUserMapStages():
    url = 'http://s1.xiaomi.mysticalcard.com/mapstage.php?do=GetUserMapStages&v=7002&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    data = ''
    # �õ����ֵ�����Ϣ
    jsonresponse = connection(url, data)
    data = jsonresponse.get('data', 0)
    arr = []
    for i in data:
        counterattacktime = data.get(i, 0).get('CounterAttackTime', 0)
        counterattacktime = int(counterattacktime)
        if counterattacktime != 0:
            arr.append(i)
    return arr


def EditUserMapStages(arr):
    url = 'http://s1.xiaomi.mysticalcard.com/mapstage.php?do=EditUserMapStages&v=7003&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    for i in arr:
        data = 'isManual=0&MapStageDetailId=' + i
        jsonresponse = connection(url, data)


def Worship(*id1):
    con_log(*id1)
    url = 'http://s1.xiaomi.mysticalcard.com/worship.php?do=Worship&v=6132&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    for type in ['1', '2', '3']:
        data = 'Type=' + type
        jsonresponse = connection(url, data)

id = id1()

for id1 in id:
    con_log(*id1)
    if isverification == 'true':
        isShengYu = verification()
        if isShengYu == 0:
            continue
    getAward()
    arr = GetUserMapStages()
    print arr
    if arr:
        EditUserMapStages(arr)
    Worship(*id1)
