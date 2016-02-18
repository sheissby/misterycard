# encoding:GBK
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
    sessionid = '&sessionid=' + id1[3]
    param0 = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + uid1 + sessionid
    con_status = 0
    while con_status == 0:
        conn = httplib.HTTPConnection("master.xiaomi.mysticalcard.com")
        conn.request("POST",
                     "/mpassport.php?do=plogin&v=1522&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
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
    con_log_status = 0
    param0 = "access%5Ftoken=&plat=ANDROID%5FXIAOMI&newguide=1&Devicetoken=&Origin=xiaomi&IDFA=&Udid=64%3A09%3A80%3AD3%3AF3%3A0E" + d + e + f + c + b + a
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    while con_log_status == 0:
        conn.request("POST",
                     "/login.php?do=mpLogin&v=1523&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
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


def reset_tower(*id1):
    con_log(*id1)
    for tower_id in [8, 7, 6]:
        header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
                   'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
                   'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
                   'x-flash-version': '18,0,0,161',
                   'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        param0 = "MapStageId=" + ('%d' % tower_id)
        towerstatus = 0
        while towerstatus == 0:
            conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
            conn.request("POST",
                         "/maze.php?do=Reset&v=6389&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                         param0, header1)
            res = conn.getresponse()
            x = res.read()
            if len(x) != 0:
                y = json.loads(x)
                towerstatus = y.get('status', 0)
                if towerstatus == 1:
                    print id1[0], '  ', tower_id, 'reset success'
            else:
                towerstatus = 0
            conn.close()


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
      ['R5','2015072214675611', '297876', 'ekyOlt6j4VLipThy'], ['СС��','59079768', '289074', 'lVMmfvcdVHKt1OeA'],

      ['������콢','2013042910219954', '132168', 'wALTg8x1Axg8FNIi'], ['�����Ѳ��','2013050510338482', '138002', 'wALTg8x1Axg8FNIi'],
      ['���������','2013051110431066', '144222', 'wALTg8x1Axg8FNIi'], ['����Ż�����','2013072911496244', '213117', 'wALTg8x1Axg8FNIi'],
      ['������ڽ�','2013072911496578', '213119', 'wALTg8x1Axg8FNIi'], ['�����Ǳˮͧ','2013082111852712', '223399', 'wALTg8x1Axg8FNIi'],
      ['�����޼ʵ���','2013110613340617', '244513', 'wALTg8x1Axg8FNIi'], ['���轢�����ݶ�','2013112813880389', '249308', 'wALTg8x1Axg8FNIi'],
      ['���轢�����ݶ�','2013112813880397', '249307', 'wALTg8x1Axg8FNIi'], ['���轢�����ݶ�','2013112813880401', '249306', 'wALTg8x1Axg8FNIi'],
      ['���轢�Ӷ��ݶ�','2013112813880408', '249303', 'wALTg8x1Axg8FNIi'], ['���轢��һ�ݶ�','2013112813880415', '249301', 'wALTg8x1Axg8FNIi'],
      ['���轢�����ݶ�','2013112813880453', '249274', 'wALTg8x1Axg8FNIi'], ['�����ս�н�','2013112813880485', '249258', 'wALTg8x1Axg8FNIi'],
      ['���轢�����ݶ�','2013112813892037', '249363', 'wALTg8x1Axg8FNIi']
      ]
for id1 in id:
    reset_tower(*id1)
