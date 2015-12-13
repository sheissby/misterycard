# encoding:utf-8
import httplib, urllib, urllib2, re, time, json, requests


def con(uid):
    header1 = {'Host': 'master.xiaomi.mysticalcard.com', 'Cookie': '_sid=d3kv2cgc086bs71ujmg746qqd3',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css'
                         ', image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9,'
                         ' flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, '
                         '*/*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    uid1 = '&uid=' + uid
    param0 = "sessionid=tbmXwubvxzvP4nHa&Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + uid1
    conn = httplib.HTTPConnection("master.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0"
                 "&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
                 param0, header1)
    mpassport = conn.getresponse()
    x = mpassport.read()
    print 'con response:',x
    y = json.loads(x)
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
    header1 = {'Host': 's2.xiaomi.mysticalcard.com', 'Cookie': '_sid=d3kv2cgc086bs71ujmg746qqd3',
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
    conn = httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/login.php?do=mpLogin&v=3338&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
                 param0, header1)
    x = conn.getresponse()
    print 'con_log response:', x.read()
    conn.close()


def mapstage(*id1):
    con_log(*id1)
    header1 = {'Host': 's2.xiaomi.mysticalcard.com', 'Cookie': '_sid=d3kv2cgc086bs71ujmg746qqd3',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, '
                         'text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;'
                         'q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application'
                         '/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '16,0,0,276',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    param0 = "MapStageDetailId=30"
    conn = httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/mapstage.php?do=Explore&v=4581&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1"
                 "&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                 param0, header1)
    returnstr = conn.getresponse()
    lenth = returnstr.read()
    print 'mapstage response:', lenth
    y = json.loads(lenth)
    status = y.get('status', 0)
    conn.close()
    list = lenth, status
    return list


def thievesfight(userthievesid):
    header1 = {'Host': 's2.xiaomi.mysticalcard.com', 'Cookie': '_sid=d3kv2cgc086bs71ujmg746qqd3',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, '
                         'text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;'
                         'q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application'
                         '/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '16,0,0,276',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    # 将userthievesid转为string类型
    struserthievesid = str(userthievesid)
    thievesid = '&UserThievesId=' + struserthievesid
    param0 = 'OpenCardChip=1' + thievesid
    conn = httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/arena.php?do=ThievesFight&v=9785&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1"
                 "&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                 param0, header1)
    conn.close()


# 账户列表
id = [['#Cm', '2014092692358474', '285154'], ['Em', '2014121327096245', '288121'], ['#Fm', '2015031960117052', '294557']]


for id1 in id:
    lenth1 = ''
    status1 = 1
    while len(lenth1) < 400 and status1 == 1:
        lenth1, status1 = mapstage(*id1)
        if status1 == 0:  # status=0表示探索失败，跳出本次循环
            break
        else:
            #  返回值长度大于400，表示有盗贼
            if len(lenth1) > 400:
                y = json.loads(lenth1)
                # 获得盗贼血量
                HPCount = y.get('data', 0).get('ThievesInfo', 0).get('HPCount', 0)
                userthievesid = y.get('data', 0).get('ThievesInfo', 0).get('UserThievesId', 0)
                if HPCount > 40000:
                    print id1[0], '出现精英盗贼'
                    # 出现精英盗贼自动攻击
                    thievesfight(userthievesid)
                else:
                    print id1[0], '出现普通盗贼'
                break
raw_input('End')
