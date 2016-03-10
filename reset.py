# encoding:GBK
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


def reset_tower(*id1):
    con_log(*id1)
    for tower_id in [8, 7, 6]:
        url = 'http://s1.xiaomi.mysticalcard.com/maze.php?do=Reset&v=6389&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
        data = "MapStageId=" + ('%d' % tower_id)
        jsonresponse = connection(url, data)
        if jsonresponse == 1:
            print id1[0], tower_id, 'reset fail'
        else:
            print id1[0], tower_id, 'reset success'

id = [
      ['鱼丸号旗舰','2013042910219954', '132168', 'hk8URzaHObkJbp0r'], ['鱼丸号巡洋舰','2013050510338482', '138002', 'hk8URzaHObkJbp0r'],
      ['鱼丸号驱逐舰','2013051110431066', '144222', 'hk8URzaHObkJbp0r'], ['鱼丸号护卫舰','2013072911496244', '213117', 'hk8URzaHObkJbp0r'],
      ['鱼丸号炮舰','2013072911496578', '213119', 'hk8URzaHObkJbp0r'], ['鱼丸号潜水艇','2013082111852712', '223399', 'hk8URzaHObkJbp0r'],
      ['鱼丸洲际导弹','2013110613340617', '244513', 'hk8URzaHObkJbp0r'], ['鱼丸舰队五纵队','2013112813880389', '249308', 'hk8URzaHObkJbp0r'],
      ['鱼丸舰队四纵队','2013112813880397', '249307', 'hk8URzaHObkJbp0r'], ['鱼丸舰队三纵队','2013112813880401', '249306', 'hk8URzaHObkJbp0r'],
      ['鱼丸舰队二纵队','2013112813880408', '249303', 'hk8URzaHObkJbp0r'], ['鱼丸舰队一纵队','2013112813880415', '249301', 'hk8URzaHObkJbp0r'],
      ['鱼丸舰队七纵队','2013112813880453', '249274', 'hk8URzaHObkJbp0r'], ['鱼丸号战列舰','2013112813880485', '249258', 'hk8URzaHObkJbp0r'],
      ['鱼丸舰队六纵队','2013112813892037', '249363', 'hk8URzaHObkJbp0r']
     ]
for id1 in id:
    reset_tower(*id1)
    time.sleep(1)
raw_input('End')
