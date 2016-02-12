# encoding: GBK
import httplib
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
        try:
            conn = httplib.HTTPConnection("master.xiaomi.mysticalcard.com")
            conn.request("POST",
                         "/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
                         param0, header1)
            res = conn.getresponse()
            x = res.read()
            y = json.loads(x)
            con_status = y.get('status', 0)
        except Exception:
            print 'login failed, try again'
            con_status = 0
    # print id1[0], 'con success'
    ppsign = y.get('data', 0).get('uinfo', 0).get('ppsign', 0)
    sign = y.get('data', 0).get('uinfo', 0).get('sign', 0)
    times = y.get('data', 0).get('uinfo', 0).get('time', 0)
    conn.close()
    return y


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
        try:
            conn.request("POST",
                         "/login.php?do=mpLogin&v=3338&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
                         param0, header1)
            res = conn.getresponse()
            x = res.read()
            y = json.loads(x)
            con_log_status = y.get('status', 0)
        except Exception:
            print 'con_log failed, try again'
            con_log_status = 0
    print id1[0], 'con_log success'
    conn.close()


def play_tower(*id1):
    for map_id in [8, 7, 6]:
        for layer in range(1, 6):
            con_log(*id1)
            layerinfostatus = 0
            header = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
                           'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
                           'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
                           'x-flash-version': '18,0,0,161',
                           'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache',
                           'Referer': 'app:/assets/CardMain.swf', 'Content-Type': 'application/x-www-form-urlencoded'
                           }
            param = "Layer=" + ('%d' % layer) + '&MapStageId=' + ('%d' % map_id)
            conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")

            # ���ÿ����Ϣ
            while layerinfostatus == 0:
                try:
                    conn.request("POST",
                                 "/maze.php?do=Info&v=8995&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",
                                  param, header)
                    res = conn.getresponse()
                    layerinfo = res.read()
                    layerinfojson = json.loads(layerinfo)
                    layerinfostatus = layerinfojson.get('status', 0)
                    if layerinfostatus == 0:
                        message = layerinfojson.get('message', 0)
                        print message
                        break
                except Exception:
                    print '���ÿ����Ϣ����'
                    layerinfostatus = 0
            if len(layerinfo) == 62:
                print map_id, 'end'
                break
            else:
                y = json.loads(layerinfo)
                items = y.get('data', 0).get('Map', 0).get('Items', 0)  # ���и��ӵ���Ϣ
                item = []   # ��Ҫ�����ĸ��Ӽ���
                count = 0   # ������Ӻ�
                for cords in items:                            # ѭ�����и��ӣ������Ҫ��������Ϣ
                    cords = int(cords)
                    if cords == 2 or cords == 3 or cords == 5:
                       item.append(count)                       # ��Ӹ��Ӻŵ���������
                    count = count + 1                           # ������Ҫ�����ĸ��Ӻ�

                # ��ʼ����
                battlestatus = 0
                for cord in item:
                    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
                               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
                               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
                               'x-flash-version': '18,0,0,161',
                               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache',
                               'Referer': 'app:/assets/CardMain.swf', 'Content-Type': 'application/x-www-form-urlencoded'
                               }
                    param0 = "Layer=" + ('%d' % layer) + "&ItemIndex=" + (
                    '%d' % cord) + "&manual=0&OpenCardChip=1" + "&MapStageId=" + ('%d' % map_id)
                    print param0
                    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
                    # while battlestatus == 0:
                        # try:
                    conn.request("POST",
                                 "/maze.php?do=Battle&v=8996&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",param0, header1)
                    res = conn.getresponse()
                    battleinfo = res.read()
                    # print battleinfo
                    # battlejson = json.loads(battleinfo)
                            # battlestatus = battlejson.get('status', 0)
                        # except Exception:
                        #     print 'battle error, try again'
                        #     battlestatus = 0
                    if len(battleinfo) == 196:
                        print ('out of power!')
                        return
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
      ['R5','2015072214675611', '297876', 'ekyOlt6j4VLipThy'], ['СС��','59079768', '289074', 'lVMmfvcdVHKt1OeA']
      ]
for id1 in id:
    play_tower(*id1)
raw_input('The End')
