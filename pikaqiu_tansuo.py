# encoding:GBK
import httplib
import json
import StringIO
import gzip
import time


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
    sessionid = '&sessionid=' + id1[3]
    param0 = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + uid1 + sessionid
    con_status = 0
    conn = httplib.HTTPConnection("master.xiaomi.mysticalcard.com")
    while con_status == 0:
        conn.request("POST",
                     "/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0"
                     "&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
                     param0, header1)
        res = conn.getresponse()
        x = res.read()
        if len(x) != 0:
            y = json.loads(x)
            con_status = y.get('status', 0)
        else:
            con_status = 0
    # print id1[0], 'con success'
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
    param0 = "access%5Ftoken=&plat=ANDROID%5FXIAOMI&newguide=1&Devicetoken=&Origin=xiaomi&IDFA=&Udid=64%3A09%3A80%3AD3%3AF3%3A0E" + d + e + f + c + b + a
    con_log_status = 0
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
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
    # print id1[0], 'con_log success'
    conn.close()


# �õ�������Ϣ
def GetThieves(*id1):
    con_log(*id1)
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=d3kv2cgc086bs71ujmg746qqd3',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, '
                         'text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;'
                         'q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application'
                         '/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '16,0,0,276',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    param0 = ""
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    GetThievesStatus = 0
    while GetThievesStatus == 0:
        conn.request("POST",
                     "/arena.php?do=GetThieves&v=8313&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
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
            GetThievesStatus = y.get('status', 0)
        else:
            data = returnstr.read()
            y = json.loads(data)
            GetThievesStatus = y.get('status', 0)
    return y
    conn.close()


# ����0��ʾû����������̽��������1��ʾ����������̽��
def ExistThief(thievesinfo):
    Thievesinfo = thievesinfo.get('data', 0).get('Thieves', 0)
    Countdown = thievesinfo.get('data', 0).get('Countdown', 0)
    currentuid = id1[0]
    currentuid = currentuid.decode('GBK')
    a = 0
    for a in Thievesinfo:
        thievesNickName = a.get('NickName', 0)
        thievesstatus = a.get('Status', 0)
        thievesfleetime = a.get('FleeTime', 0)
        thieveshpcurrent = a.get('HPCurrent', 0)
        # �ж�����δ��������δ�ܣ�����̽��
        if (thievesNickName == currentuid and thievesstatus == 1 and thieveshpcurrent > 0 and thievesfleetime > 0) \
                or (thievesNickName == currentuid and thievesstatus == 0 and thievesfleetime > 0):
            return 1, Countdown
    return 0, Countdown


# ����̽��
def mapstage(*id1):
    con_log(*id1)
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=d3kv2cgc086bs71ujmg746qqd3',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, '
                         'text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;'
                         'q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application'
                         '/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '16,0,0,276',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    param0 = "MapStageDetailId=25"
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/mapstage.php?do=Explore&v=4581&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1"
                 "&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                 param0, header1)
    returnstr = conn.getresponse()
    lenth = returnstr.read()
    # print 'mapstage response:', lenth
    y = json.loads(lenth)
    mapstagestatus = y.get('status', 0)
    conn.close()
    list = lenth, mapstagestatus
    return list


# ��������
def thievesfight(userthievesid):
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=d3kv2cgc086bs71ujmg746qqd3',
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
    param0 = 'OpenCardChip=1' + thievesid
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/arena.php?do=ThievesFight&v=9785&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1"
                 "&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                 param0, header1)
    conn.close()

# �˻��б�
id = [
      ['�����','2014041855227765','273122', 'd6YpW93AIdMBso3Z'],
      ['С����','2014042155811563','273419', 'd6YpW93AIdMBso3Z'], ['��������','2014052561883286','278956', 'd6YpW93AIdMBso3Z'],
      ['��ë��','2014061766465489','278958', 'd6YpW93AIdMBso3Z'], ['�����','2014061866519659','278984', 'd6YpW93AIdMBso3Z'],
      ['�ȱ���','2014061866519756','278986', 'd6YpW93AIdMBso3Z'], ['������','2014061866528941','279006', 'd6YpW93AIdMBso3Z'],
      ['¡¡��','2014061866529032','279007', 'd6YpW93AIdMBso3Z'], ['������','2014061866529097','279009', 'd6YpW93AIdMBso3Z'],
      ['����','2014061866529223','279045', 'd6YpW93AIdMBso3Z'], ['����','2014061866529231','279049', 'd6YpW93AIdMBso3Z'],
      ['������','2014061866529288','279053', 'd6YpW93AIdMBso3Z'], ['����ħż','2014061866529337','279054', 'd6YpW93AIdMBso3Z'],
      ['�ֶ�a','2014061866529346','279080', 'd6YpW93AIdMBso3Z'], ['������','2014061866529379','279081', 'd6YpW93AIdMBso3Z'],
      ['Ҭ����','2014061866529407','279083', 'd6YpW93AIdMBso3Z'], ['�𱬺�','2014061866529462','279085', 'd6YpW93AIdMBso3Z'],
      ['����˹','2014061866529470','279086', 'd6YpW93AIdMBso3Z'], ['�ȵ�','2014061866529500','279117', 'd6YpW93AIdMBso3Z'],
      ['�׾���','2014061866529554','279119', 'd6YpW93AIdMBso3Z'], ['Ƥ����','2014061866529628','279122', 'd6YpW93AIdMBso3Z'],
      ['ˮ����','2014061866529641','279131', 'd6YpW93AIdMBso3Z'], ['����','2014061866529643','279137', 'd6YpW93AIdMBso3Z'],
      ['����','2014061866529675','279164', 'd6YpW93AIdMBso3Z'], ['���ٹ�','2014061866529735','279165', 'd6YpW93AIdMBso3Z'],
      ['�����','2014061866529744','279166', 'd6YpW93AIdMBso3Z'],

      ['Reao1st','2014021515603023', '264491', 'ekyOlt6j4VLipThy'], ['Reao2nd','2014040452624347', '289393', 'ekyOlt6j4VLipThy'],
      ['R3','2015032863087404', '295303', 'ekyOlt6j4VLipThy'], ['R4','2015072214671030', '297875', 'ekyOlt6j4VLipThy'],
      ['R5','2015072214675611', '297876', 'ekyOlt6j4VLipThy'], ['СС��','59079768', '289074', 'lVMmfvcdVHKt1OeA']
      ]
for id1 in id:
    thievesinfo = GetThieves(*id1)
    thief = ExistThief(thievesinfo)
    thievesfightCD = thief[1]    #����cdʱ��
    if thief[0] == 1:
        # print id1[0],'����̽��'
        continue
    else:
        # print id1[0],'����̽��'
        lenth1 = ''
        status1 = 1
        while len(lenth1) < 400 and status1 == 1:
            lenth1, status1 = mapstage(*id1)
            if status1 == 0:  # status=0��ʾ̽��ʧ�ܣ���������ѭ��
                break
            else:
                if len(lenth1) > 400:    #  ����ֵ���ȴ���400����ʾ�е���
                    y = json.loads(lenth1)
                    # ��õ�������
                    Type = y.get('data', 0).get('ThievesInfo', 0).get('Type', 0)
                    userthievesid = y.get('data', 0).get('ThievesInfo', 0).get('UserThievesId', 0)
                    if Type == 2:
                        print id1[0], '���־�Ӣ����'
                        # if thievesfightCD <= 0:
                        #     thievesfight(userthievesid)    # ���־�Ӣ�����Զ�����
                        # else:
                        #     print id1[0], '����cd��......'
                    else:
                        print id1[0], '������ͨ����'
                        # if thievesfightCD <= 0:
                        #     thievesfight(userthievesid)
                        # else:
                        #     print id1[0], '����cd��......'
                    break


raw_input('End')
