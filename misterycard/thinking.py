# encoding:utf-8
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
                else:
                    print message
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
    url = 'http://s1.xiaomi.mysticalcard.com/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
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
    url = 'http://s1.xiaomi.mysticalcard.com/login.php?do=mpLogin&v=1521&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
    jsonresponse = connection(url, conlog_data)
    # print id1[0], 'con_log success!'

# 获取npc的值
def getNPC():
    url = 'http://s1.xiaomi.mysticalcard.com/meditation.php?do=Info&v=6378&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1'
    data = ''
    jsonresponse = connection(url, data)

    # 获得npc列表的最后一个值
    npc = jsonresponse.get('data', 0).get('NpcList', 0)[-1]
    # print 'getNPC', npc
    return npc

def thinking():
    num = 0
    npc = getNPC()
    url = 'http://s1.xiaomi.mysticalcard.com/meditation.php?do=Npc&v=6382&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1'
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
    url = 'http://s1.xiaomi.mysticalcard.com/meditation.php?do=Deal&v=6384&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1'
    data = ''
    jsonresponse = connection(url, data)

id = [
    # ['Am', '1592626', '279696', 'IggFdDB5eE6uERXL'],
 ['Bm', '2016030615546648', '304592', 'IggFdDB5eE6uERXL'],
 #    ['Bm7', '2013072511431198', '209850', 'jlOxpE5vIdZCRceQ'],
 #    ['Cm7', '2013072511431214', '209852', 'jlOxpE5vIdZCRceQ'],
      ]

i = input('输入循环次数：')
for id1 in id:
    jinsenum = 0
    for times in range(1, i+1):
        print times
        con_log(*id1)
        for count in range(1, 11):
            Num = thinking()
            jinsenum = jinsenum + Num
            # print jinsenum
        clear()
        # print 'clear'
    print id1[0], '获得金色碎片 '+ str(jinsenum) +'个'
