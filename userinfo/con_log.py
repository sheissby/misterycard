# encoding:utf-8
import requests
import json
import time
import ConfigParser
import sys

header = {'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5'}
curpath = sys.path[0]
initpath = curpath + '/init.conf'
config = ConfigParser.ConfigParser()
config.read(initpath)
host = config.get('Host', 'host')


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
    return 1, jsonresponse


def con(uid, sessionid):
    con_data = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + '&uid=' + uid + '&sessionid=' + sessionid
    url = 'http://s1.xiaomi.mysticalcard.com/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
    flg, jsonresponse = connection(url, con_data)
    if flg == 0:
        print jsonresponse
        return
    return jsonresponse


def con_log(*id1):
    uid = id1[1]
    Muid = id1[2]
    sessionid = id1[3]
    y = con(uid, sessionid)
    if y != None:
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
