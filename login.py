# encoding:GBK
import httplib
import json
import StringIO
import gzip
import time


def con(uid, sessionid):
    header1 = {'Host': 'master.xiaomi.mysticalcard.com', 'Cookie': '_sid=57t4jueeikn507j59png1gq7q1',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    uid1 = '&uid=' + uid
    sessionid1 = '&sessionid=' + sessionid
    param0 = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + uid1 + sessionid1
    con_status = 0
    conn = httplib.HTTPConnection("master.xiaomi.mysticalcard.com")
    while con_status == 0:
        conn.request("POST",
                     "/mpassport.php?do=plogin&v=1520&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
                     param0, header1)
        res = conn.getresponse()
        x = res.read()
        if len(x) != 0:
            y = json.loads(x)
            con_status = y.get('status', 0)
        else:
            con_status = 0
    print id1[0], 'con success!'
    ppsign = y.get('data', 0).get('uinfo', 0).get('ppsign', 0)
    sign = y.get('data', 0).get('uinfo', 0).get('sign', 0)
    times = y.get('data', 0).get('uinfo', 0).get('time', 0)
    return y
    conn.close()


def con_log(*id1):
    uid = id1[1]
    Muid = id1[2]
    sessionid = id1[3]
    y = con(uid, sessionid)
    ppsign = y.get('data', 0).get('uinfo', 0).get('ppsign', 0)
    sign = y.get('data', 0).get('uinfo', 0).get('sign', 0)
    times = '%d' % y.get('data', 0).get('uinfo', 0).get('time', 0)
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
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
    param0 = "access%5Ftoken=&plat=ANDROID%5FXIAOMI&newguide=1&Devicetoken=&Origin=xiaomi&IDFA=&Udid=64%3A09%3A80%3AD3%3AF3%3A0E" + d + e + f + c + b + a
    param1 = ''
    param2 = 'pvpNewVersion=1'
    con_log_status = 0
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    while con_log_status == 0:
        conn.request("POST",
                     "/login.php?do=mpLogin&v=1521&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
                     param0, header1)
        res = conn.getresponse()
        x = res.read()
        if len(x) != 0:
            y = json.loads(x)
            con_log_status = y.get('status', 0)
        else:
            con_log_status = 0
    print id1[0], 'con_log success!'

#    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    GetUserinfo_status = 0
    while GetUserinfo_status == 0:
        conn.request("POST",
                     "/user.php?do=GetUserinfo&OpenCardChip=1&v=1522&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                     param2, header1)
        GetUserinfo = conn.getresponse()
        x = GetUserinfo.read()
#        print len(x)
        if len(x) < 900:
            y = json.loads(x)
            GetUserinfo_status = y.get('status', 0)
        else:
            break
    print id1[0], 'GetUserinfo sucess!'
#    conn.close()


    AwardSalary_status = 0
#    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    while AwardSalary_status == 0:
        conn.request("POST",
                     "/user.php?do=AwardSalary&v=1523&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                     param1, header1)
        AwardSalaryres = conn.getresponse()
        x = AwardSalaryres.read()
        if len(x) != 0:
            y = json.loads(x)
            AwardSalary_status = y.get('status', 0)
        else:
            AwardSalary_status = 0
    conn.close()
    print id1[0], 'AwardSalaryres sucess!'


def GetUserMapStages(*id1):
    con_log(*id1)
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    param0 = ''
    status = 0
    # 得到入侵盗贼信息
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    while status == 0:
        conn.request("POST",
                     "/mapstage.php?do=GetUserMapStages&v=7002&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                     param0, header1)
        returnstr = conn.getresponse()
        responseheader = returnstr.getheaders()
        isgzipped = responseheader[0]
        if isgzipped[1] == 'gzip':
            compresseddata = returnstr.read()
            compressedstream = StringIO.StringIO(compresseddata)
            gzipper = gzip.GzipFile(fileobj=compressedstream)
            data = gzipper.read()
            y = json.loads(data)
            status = y.get('status', 0)
        else:
            data = returnstr.read()
            y = json.loads(data)
            status = y.get('status', 0)
    conn.close()
    data = y.get('data', 0)
    arr = []
    for i in data:
        counterattacktime = data.get(i, 0).get('CounterAttackTime', 0)
        counterattacktime = int(counterattacktime)
        if counterattacktime != 0:
            arr.append(i)
    return arr


def EditUserMapStages(arr):
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    for i in arr:
        param0 = 'isManual=0&MapStageDetailId=' + i
        conn.request("POST",
                     "/mapstage.php?do=EditUserMapStages&v=7003&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                     param0, header1)
        resstr = conn.getresponse()
        resstr.read()

        # returnstr = conn.getresponse()
        # responseheader = returnstr.getheaders()
        # isgzipped = responseheader[0]
        # if isgzipped[1] == 'gzip':
        #     compresseddata = returnstr.read()
        #     compressedstream = StringIO.StringIO(compresseddata)
        #     gzipper = gzip.GzipFile(fileobj=compressedstream)
        #     data = gzipper.read()
        #     y = json.loads(data)
        #     print y
        #     status = y.get('status', 0)
        # else:
        #     data = returnstr.read()
        #     y = json.loads(data)
        #     print y
        #     status = y.get('status', 0)
    conn.close()


def Worship(*id1):
    con_log(*id1)
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    for type in ['1', '2', '3']:
        param0 = 'Type=' + type
        conn.request("POST",
                     "/worship.php?do=Worship&v=6132&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                     param0, header1)
        resstr = conn.getresponse()
        x = resstr.read()



id = [['Am', '1592626', '279696', 'ILjEr8jamXWQSf4v'], ['#Cm', '2014092692358474', '285154', 'ILjEr8jamXWQSf4v'],
      ['Em', '2014121327096245', '288121', 'ILjEr8jamXWQSf4v'], ['#Fm', '2015031960117052', '294557', 'ILjEr8jamXWQSf4v'],
      ['樱木', '5047214', '198633', '0jOBCWaqFzYqZsNi'], ['利佐伊', '2013072511431198', '209850', '0jOBCWaqFzYqZsNi'],
      ['雷贝拉', '2013072511431214', '209852', '0jOBCWaqFzYqZsNi'],
      # ['赤刀', '26402923', '283622', 'jAKPM8ITjIyHr5At'],
      # ['骷髅大王', '2014082282360039', '283647', 'jAKPM8ITjIyHr5At'], ['獠牙', '2014082382723128', '283732', 'jAKPM8ITjIyHr5At'],
      # ['血刃', '2014082382762366', '283739', 'jAKPM8ITjIyHr5At'], ['军刺', '2014082382896209', '283757', 'jAKPM8ITjIyHr5At'],
      # ['袖箭', '2014082382896212', '283765', 'jAKPM8ITjIyHr5At'],
      ['杰尼龟','2014041855227765','273122', 'rUP529O9fB7ZKX38'],
      ['小火龙','2014042155811563','273419', 'rUP529O9fB7ZKX38'], ['妙蛙种子','2014052561883286','278956', 'rUP529O9fB7ZKX38'],
      ['绿毛虫','2014061766465489','278958', 'rUP529O9fB7ZKX38'], ['大针蜂','2014061866519659','278984', 'rUP529O9fB7ZKX38'],
      ['比比鸟','2014061866519756','278986', 'rUP529O9fB7ZKX38'], ['超音蝠','2014061866528941','279006', 'rUP529O9fB7ZKX38'],
      ['隆隆岩','2014061866529032','279007', 'rUP529O9fB7ZKX38'], ['大岩蛇','2014061866529097','279009', 'rUP529O9fB7ZKX38'],
      ['乘龙','2014061866529223','279045', 'rUP529O9fB7ZKX38'], ['耿鬼','2014061866529231','279049', 'rUP529O9fB7ZKX38'],
      ['烈焰马','2014061866529288','279053', 'rUP529O9fB7ZKX38'], ['吸盘魔偶','2014061866529337','279054', 'rUP529O9fB7ZKX38'],
      ['胖丁','2014061866529346','279080', 'rUP529O9fB7ZKX38'], ['阿柏蛇','2014061866529379','279081', 'rUP529O9fB7ZKX38'],
      ['椰蛋树','2014061866529407','279083', 'rUP529O9fB7ZKX38'], ['火爆猴','2014061866529462','279085', 'rUP529O9fB7ZKX38'],
      ['派拉斯','2014061866529470','279086', 'rUP529O9fB7ZKX38'], ['比雕','2014061866529500','279117', 'rUP529O9fB7ZKX38'],
      ['雷精灵','2014061866529554','279119', 'rUP529O9fB7ZKX38'], ['皮卡西','2014061866529628','279122', 'rUP529O9fB7ZKX38'],
      ['水精灵','2014061866529641','279131', 'rUP529O9fB7ZKX38'], ['火精灵','2014061866529643','279137', 'rUP529O9fB7ZKX38'],
      ['胡地','2014061866529675','279164', 'rUP529O9fB7ZKX38'], ['风速狗','2014061866529735','279165', 'rUP529O9fB7ZKX38'],
      ['喷火龙','2014061866529744','279166', 'rUP529O9fB7ZKX38'], ['钢板', '3586030', '212385', 'fgTUvLEu1B3rVcUk'],
      ['木板', '2013082711940981', '225069', 'fgTUvLEu1B3rVcUk'], ['石板', '2013083112015559', '226603', 'fgTUvLEu1B3rVcUk']
      ]

for id1 in id:
    arr = GetUserMapStages(*id1)
    print arr
    if arr:
        EditUserMapStages(arr)
    Worship(*id1)
    time.sleep(0.1)
