# encoding:GBK
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
    # ӣľ
    #param0 = "sessionid=0niwv4OngcXD5tXg&Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + uid1
    # Am
   # param0 = "sessionid=tbmXwubvxzvP4nHa&Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + uid1
    # �൶
    param0 = "sessionid=jAKPM8ITjIyHr5At&Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + uid1
    # Ƥ����
   # param0 = "sessionid=0niwv4OngcXD5tXg&Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + uid1
    conn = httplib.HTTPConnection("master.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0"
                 "&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
                 param0, header1)
    mpassport = conn.getresponse()
    x = mpassport.read()
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
    params = urllib.urlencode(
        {'access%5Ftoken': '', 'plat': 'ANDROID%5FXIAOMI', 'nick': '2015031960117052', 'newguide': '1',
         'time': times, 'ppsign': ppsign, 'sign': sign, 'MUid': '294557', 'Devicetoken': '', 'Origin': 'xiaomi',
         'IDFA': '', 'uin': '2015031960117052', 'Udid': '64%3A09%3A80%3AD3%3AF3%3A0E'})
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
    param0 = "MapStageDetailId=70"
    conn = httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/mapstage.php?do=Explore&v=4581&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1"
                 "&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                 param0, header1)
    returnstr = conn.getresponse()
    lenth = returnstr.read()
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
    # ��userthievesidתΪstring����
    struserthievesid = str(userthievesid)
    thievesid = '&UserThievesId=' + struserthievesid
    print thievesid
    param0 = 'OpenCardChip=1' + thievesid
    conn = httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/arena.php?do=ThievesFight&v=9785&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1"
                 "&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                 param0, header1)


# �˻��б�
id = [['�൶', '26402923', '283622'], ['���ô���', '2014082282360039', '283647'] , ['���', '2014082382723128', '283732'],
  ['Ѫ��', '2014082382762366', '283739'], ['����', '2014082382896209', '283757'], ['���', '2014082382896212', '283765']]

# [['#Cm', '2014092692358474', '285154'], ['Em', '2014121327096245', '288121'],
#  ['#Fm', '2015031960117052', '294557']]

#  ['�൶', '26402923', '283622'], ['���ô���', '2014082282360039', '283647'] , ['���', '2014082382723128', '283732'],
#  ['Ѫ��', '2014082382762366', '283739'], ['����', '2014082382896209', '283757'], ['���', '2014082382896212', '283765']

#  ['ӣľ', '5047214', '198633'], ['������', '2013072511431198', '209850']


for id1 in id:
    lenth1 = ''
    status1 = 1
    while len(lenth1) < 400 and status1 == 1:
        lenth1, status1 = mapstage(*id1)
        if status1 == 0:  # status=0��ʾ̽��ʧ�ܣ���������ѭ��
            break
        else:
            #  ����ֵ���ȴ���400����ʾ�е���
            if len(lenth1) > 400:
                y = json.loads(lenth1)
                # ��õ���Ѫ��
                HPCount = y.get('data', 0).get('ThievesInfo', 0).get('HPCount', 0)
                userthievesid = y.get('data', 0).get('ThievesInfo', 0).get('UserThievesId', 0)
                if HPCount > 40000:
                    print id1[0], '���־�Ӣ����'
                    # ���־�Ӣ�����Զ�����
                    thievesfight(userthievesid)
                else:
                    print id1[0], '������ͨ����'
                break
raw_input('End')
