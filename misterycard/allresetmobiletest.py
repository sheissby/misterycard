# encoding:UTF-8
import requests
import json
import time

header = {'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5'}


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
                    return message
        except requests.ConnectionError, e:
            print e
            status = 0
            time.sleep(1)
        except requests.HTTPError, e:
            print e
            status = 0
            time.sleep(1)
    return jsonresponse


def con(uid, sessionid):
    con_data = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + '&uid=' + uid + '&sessionid=' + sessionid
    url = 'http://s1.xiaomi.mysticalcard.com/mpassport.php?do=plogin&v=3468&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
    jsonresponse = connection(url, con_data)
    return jsonresponse


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
    url = 'http://s1.xiaomi.mysticalcard.com/login.php?do=mpLogin&v=3469&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
    jsonresponse = connection(url, conlog_data)


def reset_tower(*id1):
    con_log(*id1)
    for tower_id in [8, 7, 6, 5, 4, 3, 2]:
        url = 'http://s1.xiaomi.mysticalcard.com/maze.php?do=Reset&v=993&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
        data = 'MapStageId=' + str(tower_id)
        jsonresponse = connection(url, data)
        if jsonresponse == 1:
            print id1[0], tower_id, 'reset fail'
        else:
            print id1[0], tower_id, 'reset success'


def resetWithNoCost(*id1):
    con_log(*id1)
    for tower_id in [8, 7, 6, 5, 4, 3, 2]:
        url = 'http://s1.xiaomi.mysticalcard.com/maze.php?do=Reset&v=993&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
        data = 'MapStageId=' + str(tower_id)
        show='http://s1.xiaomi.mysticalcard.com/maze.php?do=Show&v=3470&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
        response=connection(show,data)
        if isinstance(response,unicode):
            print response
            continue
        else:
            whetherReset=response.get('data').get('FreeReset')
            if int(whetherReset)==1:
                jsonresponse=connection(url,data)
                if jsonresponse == 1:
                    print id1[0], tower_id, 'reset fail'
                else:
                    print id1[0], tower_id, 'reset success'
            else:
                print 'tower'+str(tower_id)+'reseted today'
            
        

id = [['小火龙', '2014042155811563', '273419', 'QcGtd5Hmsy3g7dS9'],
      ]
      
for id1 in id:
    choose=input('是否消耗晶钻重置：1.否；2.是')
    print type(choose)
    if int(choose)==1 or choose=='':
        resetWithNoCost(*id1)
    if int(choose)==2:
        reset_tower(*id1)
    time.sleep(1)
raw_input('End')
