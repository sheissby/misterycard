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
        try:
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
        except Exception, e:
            con_status == 0
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
def GetLilisi(*id1):
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
                     "/Journey.php?do=GetUserJourneysStatus&v=8313&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
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
    conn.close()
    return y



# ����0��ʾû��lls������̽��������1��ʾ��lls������̽��
def ExistLilisi(Lilisiinfo):
    Lilisiinfo = Lilisiinfo.get('data', 0).get('journeyList', 0).get('journeyList', 0)
    currentuid = id1[0]
    currentuid = currentuid.decode('GBK')
    for a in Lilisiinfo:
        llsNickName = a.get('NickName', 0)   #̽����
        llsstatus = a.get('Status', 0)       #lls״̬
        llsfleetime = a.get('FleeTime', 0)   #lls����ʱ��
        llshpcurrent = a.get('HPCurrent', 0) #lls��ǰѪ��
        llsgrade = a.get('Grade', 0)         #lls�Ѷ�
        llsid = a.get('UserJourneyId', 0)    #lls��id
        # �ж���llsδ����δ�ܣ�����̽��
        if (llsNickName == currentuid and llsstatus == 1 and llshpcurrent > 0 and llsfleetime > 0) \
                or (llsNickName == currentuid and llsstatus == 0 and llsfleetime > 0):
            return 1, llsgrade, llsid
    llsgrade = 0
    llsid = 0
    return 0, llsgrade, llsid


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
    param0 = "MapStageDetailId=53"
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/mapstage.php?do=Explore&v=4581&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1"
                 "&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                 param0, header1)
    returnstr = conn.getresponse()
    responseheader = returnstr.getheaders()
    isgzipped = responseheader[0]
    if isgzipped[1] == 'gzip':
        compresseddata = returnstr.read()
        compressedstream = StringIO.StringIO(compresseddata)
        gzipper = gzip.GzipFile(fileobj=compressedstream)
        data = gzipper.read()
    else:
        data = returnstr.read()
    return data


# ��������������0��ʾ����cd
def llsfight(llsid):
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
    strllsid = str(llsid)
    param0 = 'userJourneyId=' + strllsid
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/Journey.php?do=JourneyFight&v=9785&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1"
                 "&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                 param0, header1)
    returnfight = conn.getresponse()
    responseheader = returnfight.getheaders()
    isgzipped = responseheader[0]
    if isgzipped[1] == 'gzip':
        compresseddata = returnfight.read()
        compressedstream = StringIO.StringIO(compresseddata)
        gzipper = gzip.GzipFile(fileobj=compressedstream)
        fightdata = gzipper.read()
    else:
        fightdata = returnfight.read()
    # print fightdata
    if 'message' in fightdata:
        datajson = json.loads(fightdata)
        fightstatus = datajson.get('status', 0)
        fightmessage = datajson.get('message', 0)
        fightmessage = fightmessage.encode('utf-8')
        string = '��ȴʱ��δ���������ĵȴ�����Ҳ����ʹ�þ�������������ȴʱ�䣡'
        if fightstatus == 0 and cmp(fightmessage, string):
            print id1[0], 'cd��'
            return 0
    conn.close()

# �˻��б�
id = [['#Cm', '2014092692358474', '285154', 'tbmXwubvxzvP4nHa'],
      ['Em', '2014121327096245', '288121', 'tbmXwubvxzvP4nHa'],
      ['#Fm', '2015031960117052', '294557', 'tbmXwubvxzvP4nHa'],
      ['ӣľ����a', '5047214', '198633', '0jOBCWaqFzYqZsNi'],
      ['������', '2013072511431198', '209850', '0jOBCWaqFzYqZsNi'],
      ['�մ�����', '3586030', '212385', 'fgTUvLEu1B3rVcUk'],
      ['ľ��a', '2013082711940981', '225069', 'fgTUvLEu1B3rVcUk'],
      ['ʯ��', '2013083112015559', '226603', 'fgTUvLEu1B3rVcUk']
      ]
for id1 in id:
    # Lilisiinfo = GetLilisi(*id1)
    # isLilisi = ExistLilisi(Lilisiinfo)
    # thievesfightCD = thief[1]    #����cdʱ��
    mapstagestatus = 1
    isLilisi = 0
    while isLilisi == 0 and mapstagestatus == 1:
        Lilisiinfo = GetLilisi(*id1)
        isLilisi, llsgrade, llsid = ExistLilisi(Lilisiinfo)
        if isLilisi == 1:
            # print id1[0], '����̽��'
            if llsgrade == 1 or llsgrade == 2:
                fightresult = llsfight(llsid)
                if fightresult == 0:
                    break
                isLilisi = 0      #�����Ƿ����lls��ʶ���Ա����ѭ���ٴι���
            elif llsgrade == 3:
                print id1[0], '���ѵĴ򲻹�'
                break
            elif llsgrade == 4:
                print id1[0], 'ج�λ�û����'
                break
            elif llsgrade == 5:
                print id1[0], '����������'
                break
        else:
            data = mapstage(*id1)
            # print data
            if 'JourneyInfo' in data:
                isLilisi = 0
                datajson = json.loads(data)
                # mapstagestatus = y.get('status', 0)
                lilisiHP = datajson.get('data', 0).get('JourneyInfo', 0).get('HPCount', 0)
                llsid = datajson.get('data', 0).get('JourneyInfo', 0).get('UserJourneyId', 0)
                if lilisiHP > 150000:
                    if lilisiHP == 236520:
                        print id1[0], '�һ�ج��'
                        break
                    elif lilisiHP == 238980:
                        print id1[0], 'а��ج��'
                        break
                    elif lilisiHP == 232340:
                        print id1[0], '˫��ج��'
                        break
                    elif lilisiHP == 226540:
                        print id1[0], '����ج��'
                        break
                    elif lilisiHP == 241060:
                        print id1[0], '����ج��'
                        break
                    elif lilisiHP == 353600:
                        print id1[0], '��������������'
                        break
                    elif lilisiHP == 350450:
                        print id1[0], '�ͻ�����������������'
                        break
                    elif lilisiHP == 356800:
                        print id1[0], '��������������'
                        break
                    elif lilisiHP == 350275:
                        print id1[0], '�ܴ�����������'
                        break
                    elif lilisiHP == 352800:
                        print id1[0], 'а������������'
                        break
                    print id1[0], '���ֲ�������'
                    break
                else:
                    # print id1[0], '��������˿'
                    fightresult = llsfight(llsid)
                    if fightresult == 0:
                        break
            elif 'message' in data:
                isLilisi = 1
                datajson = json.loads(data)
                mapstagestatus = datajson.get('status', 0)
                message = datajson.get('message', 0)
                message = message.encode('utf-8')
                string = '�ж�������!ÿ10���ӿɻָ�1��!��Ҳ����ʹ�þ��깺���ж���Ŷ!'
                if mapstagestatus == 0 and cmp(message, string):
                    print id1[0], 'out of power'
                    break
        time.sleep(0.1)

raw_input('End')