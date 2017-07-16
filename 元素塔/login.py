# encoding: utf-8
import requests
import json
import time
import string
import random

##防止cookie冲突，随机分配一个cookie值
cookie_str = string.join(random.sample('abcdefghijklmnopqrstuvwxyz', 26)).replace(" ","")

header = {'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': '_sid='+cookie_str}


def connection(url, data):
    status = 0
    try_times = 0
    while status == 0:
        #if try_times>5:
            #print "瓒呰繃灏濊瘯娆℃暟,杩炴帴澶辫触"
            #return 0
        try:
            response = requests.post(url, data=data, headers=header)
            x = 0
            while x == 0:
                #if try_times>5:
                    #print "瓒呰繃灏濊瘯娆℃暟,杩炴帴澶辫触"
                    #return 0
                try:
                    jsonresponse = json.loads(response.content)
                    # logger.info(response.content)
                    x = 1
                except Exception:
                    x = 0
                    #try_times+=1
                    continue
            status = jsonresponse.get('status', 0)
            if status == 0:
                message = jsonresponse.get('message', 0)
                if message == '':
                    #try_times+=1
                    print '鐧诲綍澶辫触'
                    time.sleep(1)
                else:
                    #print message
                    return message
        except requests.ConnectionError, e:
            #try_times+=1
            #print e
            status = 0
            time.sleep(1)
        except requests.HTTPError, e:
            #try_times+=1
            #print e
            status = 0
            time.sleep(1)
    #print jsonresponse
    return jsonresponse


def con(*id):
    uid = id[0]
    Muid = id[1]
    session = id[2]
    name = id[3]
    #print uid,session,type(uid),type(session)
    con_data = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + '&uid=' + uid + '&sessionid='+session
    url = 'http://s1.xiaomi.mysticalcard.com/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
    jsonresponse = connection(url, con_data)
    #print jsonresponse
    return jsonresponse


def con_log(*id):
    uid = id[0]
    Muid = id[1]
    session = id[2]
    name = id[3]
    y=con(*id)
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


