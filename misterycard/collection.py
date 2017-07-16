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
                    print '��¼ʧ��'
                    time.sleep(1)
                else:
                    return 1
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
    url = 'http://master.xiaomi.mysticalcard.com/mpassport.php?do=plogin&v=3468&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
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
 
def collection(): 
    url = 'http://s1.xiaomi.mysticalcard.com/collectCard.php?do=Exchange&v=1919&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
    for ActivityId in ['336']:
        data='ActivityId='+ActivityId
        jsonresponse = connection(url, data)
        print jsonresponse






id = [ ['#Cm', '2014092692358474', '285154', 'ZmeyMlMTIaQoo1vn'],
        ['Em', '2014121327096245', '288121', 'ZmeyMlMTIaQoo1vn'],
        ['#Fm', '2015031960117052', '294557', 'ZmeyMlMTIaQoo1vn'],
        ['Bm', '2016030615546648', '304592', 'ZmeyMlMTIaQoo1vn'],
        ['Asus4', '6437079', '226322', 'LnQ6qpKCyY95nIrg'],
        ['Bsus4', '2013120213991947', '250246', 'LnQ6qpKCyY95nIrg'],
        ['Csus4', '2013121714341555', '254543', 'LnQ6qpKCyY95nIrg'],
        ['Dsus4', '2013122514488598', '290176', 'LnQ6qpKCyY95nIrg'],

        ['Aadd9', '10550637', '250398', 'QcGtd5Hmsy3g7dS9'],
        ['Badd9', '2014041855227765', '273122', 'QcGtd5Hmsy3g7dS9'],
        ['Cadd9', '2014042155811563', '273419', 'QcGtd5Hmsy3g7dS9'],
        ['Dadd9', '2014052561883286', '278956', 'QcGtd5Hmsy3g7dS9'],
        ['Eadd9', '2014061766465489', '278958', 'QcGtd5Hmsy3g7dS9'],
        ['Fadd9', '2014061866529032', '279007', 'QcGtd5Hmsy3g7dS9'],
      ]

for id1 in id: 
    con_log(*id1)
    print id1[0], 'cllection start'
    collection()
    print id1[0], 'cllection end'
    # time.sleep(10)


