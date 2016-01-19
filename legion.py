# encoding:GBK
import httplib
import json


def con(uid):
    header1 = {'Host': 'master.xiaomi.mysticalcard.com', 'Cookie': '_sid=d3kv2cgc086bs71ujmg746qqd3',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    uid1 = '&uid=' + uid
    sessionid = '&sessionid=' + id1[3]
    param0 = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + uid1 + sessionid
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
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=d3kv2cgc086bs71ujmg746qqd3',
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
    while con_log_status == 0:
        conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
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
    conn.close()


def legionattack(*id1):
    con_log(*id1)
    legionId = str(legionid)
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=d3kv2cgc086bs71ujmg746qqd3',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '16,0,0,276',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    param0 = '&Type=1&Id='+ legionId
    param1 = '&Type=2&Id='+ legionId

    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    conn.request("POST",
                     "/legionattack.php?do=join&v=3339&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                     param0, header1)
    res = conn.getresponse()

    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    conn.request("POST",
                     "/legionattack.php?do=exit&v=3340&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                     param1, header1)
    res = conn.getresponse()
    conn.close()



id = [['Am', '1592626', '279696', 'tbmXwubvxzvP4nHa'],
      ['#Cm', '2014092692358474', '285154', 'tbmXwubvxzvP4nHa'],
      ['Em', '2014121327096245', '288121', 'tbmXwubvxzvP4nHa'],
      ['#Fm', '2015031960117052', '294557', 'tbmXwubvxzvP4nHa'],
      ['jinxiaoxi', '2014011514924154', '289074', 'TqctVYyZJmA6JrGC'],
      ['jinxiaoxiaoxi', '2014021715652853', '265008', 'TqctVYyZJmA6JrGC'],
      ['jinxiaoxiaoxiaoxi', '2015010132895122', '289017', 'TqctVYyZJmA6JrGC'],
      ['jinxixi', '2015011837740716', '289647', 'TqctVYyZJmA6JrGC'],
      ['jinxiaoxixi', '2015013142224275', '290057', 'TqctVYyZJmA6JrGC'],
      ['hong', '2015052882084219', '296351', 'TqctVYyZJmA6JrGC'],
      ['cong', '2015052882088503', '296352', 'TqctVYyZJmA6JrGC'],
      ['feng', '2015052882090943', '296354', 'TqctVYyZJmA6JrGC'],
      ['yu', '2015052882090503', '296353', 'v1soiQ8I8RgIvg2p'],
      ['R1', '2014021515603023', '264491', 'ekyOlt6j4VLipThy'],
      ['R2', '2014040452624347', '289393', 'ekyOlt6j4VLipThy'],
      ['XiaoXiaoZhu', '59079768', '289074', 'lVMmfvcdVHKt1OeA'],
      ['妙蛙种子', '2014052561883286', '278956', '6ANyAXvi6sC76fNP'],
      ['绿毛虫', '2014061766465489', '278958', '6ANyAXvi6sC76fNP'],
      ['大针蜂', '2014061866519659', '278984', '6ANyAXvi6sC76fNP'],
      ['比比鸟', '2014061866519756', '278986', '6ANyAXvi6sC76fNP'],
      ['超音蝠', '2014061866528941', '279006', '6ANyAXvi6sC76fNP'],
      # ['隆隆岩', '2014061866529032', '279007', '6ANyAXvi6sC76fNP'],
      # ['大岩蛇', '2014061866529097', '279009', '6ANyAXvi6sC76fNP'],
      # ['乘龙', '2014061866529223', '279045', '6ANyAXvi6sC76fNP'],
      # ['耿鬼', '2014061866529231', '279049', '6ANyAXvi6sC76fNP'],
      # ['烈焰马', '2014061866529288', '279053', '6ANyAXvi6sC76fNP'],
      # ['吸盘魔偶', '2014061866529337', '279054', '6ANyAXvi6sC76fNP'],
      # ['胖丁', '2014061866529346', '279080', '6ANyAXvi6sC76fNP'],
      # ['阿柏蛇', '2014061866529379', '279081', '6ANyAXvi6sC76fNP'],
      # ['椰蛋树', '2014061866529407', '279083', '6ANyAXvi6sC76fNP'],
      # ['火爆猴', '2014061866529462', '279085', '6ANyAXvi6sC76fNP'],
      # ['派拉斯', '2014061866529470', '279086', '6ANyAXvi6sC76fNP'],
      # ['比雕', '2014061866529500', '279117', '6ANyAXvi6sC76fNP'],
      # ['雷精灵', '2014061866529554', '279119', '6ANyAXvi6sC76fNP'],
      # ['皮卡西', '2014061866529628', '279122', '6ANyAXvi6sC76fNP'],
      # ['水精灵', '2014061866529641', '279131', '6ANyAXvi6sC76fNP'],
      # ['火精灵', '2014061866529643', '279137', '6ANyAXvi6sC76fNP'],
      # ['胡地', '2014061866529675', '279164', '6ANyAXvi6sC76fNP'],
      # ['风速狗', '2014061866529735', '279165', '6ANyAXvi6sC76fNP'],
      # ['喷火龙', '2014061866529744', '279166', '6ANyAXvi6sC76fNP']
      ]


global legionid
print '1.试炼森林'
print '2.落日荒原'
print '3.西风岛'
print '4.翡翠森林'
print '5.燃烧平原'
print '6.乌木地下城'
print '7.末日峡谷'
print '8.天上界'
print '9.海龟岛'
print '10.海底界'
legionid = raw_input('选择战场：')
if legionid.strip() == '' or not legionid.isdigit():
    print 'error'
else:
    for id1 in id:
        legionattack(*id1)
raw_input('The End')
