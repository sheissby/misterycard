# encoding:utf-8
import requests
import json
import time
from id import *

header = {'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5'}

host = 'http://s1.xiaomi.mysticalcard.com'

def connection(url, data):
    while 1:
        try:
            r = requests.post(url, data=data, headers=header)
            response = json.loads(r.content)
            status = response['status']
            if status == 0:
                message = response['message']
                if message == '':
                    print '登录失败'
                    time.sleep(1)
                else:
                    return 0, response
            return 1, response
        except requests.ConnectionError or requests.HTTPError, e:
            print e
            time.sleep(1)


def con(uid, sessionid):
    con_data = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + '&uid=' + uid + '&sessionid=' + sessionid
    url = 'http://s1.xiaomi.mysticalcard.com/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
    while 1:
        flg, jsonresponse = connection(url, con_data)
        if flg != 0:
            return jsonresponse
        else:
            print jsonresponse


def con_log(*id1):
    uid = id1[1]
    Muid = id1[2]
    sessionid = id1[3]
    y = con(uid, sessionid)
    ppsign = y.get('data', 0).get('uinfo', 0).get('ppsign', 0)
    sign = y.get('data', 0).get('uinfo', 0).get('sign', 0)
    times = '%d' % y.get('data', 0).get('uinfo', 0).get('time', 0)
    a = '&ppsign=' + ppsign
    b = '&sign=' + sign
    c = '&time=' + times
    d = '&MUid=' + Muid
    e = '&uin=' + uid
    f = '&nick=' + uid
    conlog_data = "access%5Ftoken=&plat=ANDROID%5FXIAOMI&newguide=1&Devicetoken=&Origin=xiaomi&IDFA=&Udid=64%3A09%3A80%3AD3%3AF3%3A0E" + d + e + f + c + b + a
    url = 'http://s1.xiaomi.mysticalcard.com/login.php?do=mpLogin&v=1521&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
    flg, jsonresponse = connection(url, conlog_data)
    # print id1[0], 'con_log success!'



def getAward():
    url = host + '/user.php?do=GetUserinfo&OpenCardChip=1&v=1522&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    data = 'pvpNewVersion=1'
    url1 = host + '/user.php?do=AwardSalary&v=1523&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    data1 = ''
    flg = 0
    while flg == 0:
        flg, jsonresponse = connection(url, data)
        if flg != 0:
            print id1[0], 'GetUserinfo sucess!'
        else:
            print id1[0], 'GetUserinfo failed!', jsonresponse
    flg = 0
    while flg == 0:
        flg, jsonresponse = connection(url1, data1)
        if flg != 0:
            print id1[0], 'AwardSalary sucess!'
        else:
            print id1[0], 'AwardSalary failed!', jsonresponse

def GetUserMapStages():
    url = 'http://s1.xiaomi.mysticalcard.com/mapstage.php?do=GetUserMapStages&v=7002&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    while 1:
        flg, jsonresponse = connection(url, data='')
        if flg != 0:
            data = jsonresponse['data']
            break
        else:
            print id1[0], 'GetUserMapStages failed!', jsonresponse
    if data:
        arr = [i for i in data if int(data[i]['CounterAttackTime']) != 0]
        return arr
    else:
        return GetUserMapStages()


def EditUserMapStages(arr):
    url = 'http://s1.xiaomi.mysticalcard.com/mapstage.php?do=EditUserMapStages&v=7003&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    for i in arr:
        data = 'isManual=0&MapStageDetailId=' + i
        flg, jsonresponse = connection(url, data)


def Worship(*id1):
    con_log(*id1)
    url = 'http://s1.xiaomi.mysticalcard.com/worship.php?do=Worship&v=6132&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    for type in ['1', '2', '3']:
        data = 'Type=' + type
        flg, jsonresponse = connection(url, data)

id = loginid()

for id1 in id:
    con_log(*id1)
    # if isverification == 'true':
    #     isShengYu = verification()
    #     if isShengYu == 0:
    #         continue
    getAward()
    arr = GetUserMapStages()
    print arr
    if arr:
        EditUserMapStages(arr)
    Worship(*id1)
    # time.sleep(10)

