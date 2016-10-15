# encoding:utf-8
import requests
import json
import time
import ConfigParser
from id import *
header = {'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5'}
config = ConfigParser.ConfigParser()
config.read('init.conf')
# host = config.get('Host', 'host')


# 成功返回1和response信息，失败返回0和失败信息
def connection(url, data):
    status = 0
    while status == 0:
        try:
            response = requests.post(url, data=data, headers=header)
            jsonresponse = json.loads(response.content)
            status = jsonresponse.get('status', 0)
            if status == 0:
                message = jsonresponse.get('message', 0)
                if message == '':
                    print '登录失败'
                    time.sleep(1)
                else:
                    return 0, message
        except requests.ConnectionError, e:
            print e
            status = 0
            time.sleep(1)
        except requests.HTTPError, e:
            print e
            status = 0
            time.sleep(1)
        except Exception, e:
            print e
            status = 0
            time.sleep(1)
    return 1, jsonresponse


def con(uid, sessionid):
    con_data = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + '&uid=' + uid + '&sessionid=' + sessionid
    url = 'http://s1.xiaomi.mysticalcard.com/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
    flag, jsonresponse = connection(url, con_data)
    return jsonresponse


def con_log(id):
    uid = id[1]
    Muid = id[2]
    sessionid = id[3]
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
    flag, jsonresponse = connection(url, conlog_data)
    # print id1[0], jsonresponse

# def getmapid():
#     MapStageId =[]    #3星地图id集合
#     MapStageIdAll =[] #所有已开地图集合
#     flg = 0
#     url = host + '/mapstage.php?do=GetUserMapStages&v=3885&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
#     jsonresponse = connection(url, data='')
#     mapinfoall = jsonresponse.get('data')
#     print mapinfoall
#
# def getwanneng():
#     url = 'http://s1.xiaomi.mysticalcard.com/cardchip.php?do=CompositeChip&v=6413&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
#     data = 'ChipId=6003&IsSuper=0'
#     json = connection(url, data)
#     print json


if __name__ == '__main__':
    ids =[
        # ['R0', '59079768', '289074', 'rgHAKkH6roUMGmeY'],
        ['#Cm', '2014092692358474', '285154', 'ZmeyMlMTIaQoo1vn'],
        ['Em', '2014121327096245', '288121', 'ZmeyMlMTIaQoo1vn'],
    ]

    for id in ids:
        con_log(id)
        # getmapid()