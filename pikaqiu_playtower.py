import httplib
import time
import json


def con(uid):
    header1 = {'Host': 'master.xiaomi.mysticalcard.com', 'Cookie': '_sid=57t4jueeikn507j59png1gq7q1',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    uid1 = '&uid=' + uid
    param0 = "sessionid=rUP529O9fB7ZKX38&Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + uid1
    con_status = 0
    while con_status == 0:
        conn = httplib.HTTPConnection("master.xiaomi.mysticalcard.com")
        conn.request("POST",
                     "/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
                     param0, header1)
        res = conn.getresponse()
        x = res.read()
        if len(x) != 0:
            y = json.loads(x)
            con_status = y.get('status', 0)
        else:
            con_status = 0
    print id1[0], 'con success'
    ppsign = y.get('data', 0).get('uinfo', 0).get('ppsign', 0)
    sign = y.get('data', 0).get('uinfo', 0).get('sign', 0)
    times = y.get('data', 0).get('uinfo', 0).get('time', 0)
    return y
    conn.close()


def con_log(*id1):
    uid = id1[1]
    Muid = id1[2]
    y = con(uid)
    ppsign = y.get('data', 0).get('uinfo', 0).get('ppsign', 0)
    sign = y.get('data', 0).get('uinfo', 0).get('sign', 0)
    times = '%d' % y.get('data', 0).get('uinfo', 0).get('time', 0)
    header1 = {'Host': 's2.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    a = '&ppsign=' + ppsign
    b = '&sign=' + sign
    c = '&time=' + times
    d = '&MUid=' + Muid
    e = '&uin=' + uid
    f = '&nick=' + uid
    con_log_status = 0
    param0 = "access%5Ftoken=&plat=ANDROID%5FXIAOMI&newguide=1&Devicetoken=&Origin=xiaomi&IDFA=&Udid=64%3A09%3A80%3AD3%3AF3%3A0E" + d + e + f + c + b + a
    conn = httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
    while con_log_status == 0:
        conn.request("POST",
                     "/login.php?do=mpLogin&v=3338&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
                     param0, header1)
        res = conn.getresponse()
        x = res.read()
        if len(x) != 0:
            y = json.loads(x)
            con_log_status = y.get('status', 0)
        else:
            con_log_status = 0
    print id1[0], 'con_log success'
    conn.close()


def play_tower(*id1):
    for map_id in [8, 7, 6]:
        for layer in range(1, 6):
            con_log(*id1)
            header = {'Host': 's2.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
                           'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
                           'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
                           'x-flash-version': '18,0,0,161',
                           'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache',
                           'Referer': 'app:/assets/CardMain.swf', 'Content-Type': 'application/x-www-form-urlencoded'
                           }
            param = "Layer=" + ('%d' % layer) + '&MapStageId=' + ('%d' % map_id)
            conn = httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
            conn.request("POST",
                         "/maze.php?do=Info&v=8995&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",
                          param, header)
            res = conn.getresponse()
            layerinfo = res.read()
            y = json.loads(layerinfo)
            if len(layerinfo) == 62:
                print map_id, 'end'
                break
            else:
                y = json.loads(layerinfo)
                items = y.get('data', 0).get('Map', 0).get('Items', 0)
                item = []
                count = 0
                for cords in items:
                    cords = int(cords)
                    if cords == 2 or cords == 3 or cords == 5:
                       item.append(count)
                    count = count + 1
                for cord in item:
                    header1 = {'Host': 's2.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
                               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
                               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
                               'x-flash-version': '18,0,0,161',
                               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache',
                               'Referer': 'app:/assets/CardMain.swf', 'Content-Type': 'application/x-www-form-urlencoded'
                               }
                    param0 = "Layer=" + ('%d' % layer) + "&ItemIndex=" + (
                    '%d' % cord) + "&manual=0&OpenCardChip=1" + "&MapStageId=" + ('%d' % map_id)
                    print param0
                    conn = httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
                    conn.request("POST",
                                 "/maze.php?do=Battle&v=8996&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",param0, header1)
                    res = conn.getresponse()
                    y = res.read()
                    if len(y) == 196:
                        print ('out of power!')
                        return
                    conn.close()
                time.sleep(0.1)


id = [['No.1', '2014041855227765', '273122'], ['No.2', '2014061866519756', '278986'], ['No.3', '2014042155811563', '273419'],
      ['No.4', '2014052561883286', '278956'], ['No.5', '2014061766465489', '278958'], ['No.6', '2014061866519659', '278984'],
      ['No.7', '2014061866528941', '279006'], ['No.8', '2014061866529032', '279007'], ['No.9', '2014061866529097', '279009'],
      ['No.10', '2014061866529223', '279045'], ['No.11', '2014061866529231', '279049'], ['No.12', '2014061866529288', '279053'],
      ['No.13', '2014061866529337', '279054'], ['No.14', '2014061866529346', '279080'], ['No.15', '2014061866529379', '279081'],
      ['No.16', '2014061866529407', '279083'], ['No.17', '2014061866529462', '279085'], ['No.18', '2014061866529470', '279086'],
      ['No.19', '2014061866529500', '279117'], ['No.20', '2014061866529554', '279119'], ['No.21', '2014061866529628', '279122'],
      ['No.22', '2014061866529641', '279131'], ['No.23', '2014061866529643', '279137'], ['No.24', '2014061866529675', '279164'],
      ['No.25', '2014061866529735', '279165'], ['No.26', '2014061866529744', '279166']]
for id1 in id:
    play_tower(*id1)
raw_input('The End')
