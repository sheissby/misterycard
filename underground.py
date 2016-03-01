import httplib,json, StringIO, gzip


def con(uid, sessionid):
    header1 = {'Host': 'master.xiaomi.mysticalcard.com', 'Cookie': '_sid=qg675n070s5pdb9beaosuhdgo4',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    uid1 = '&uid=' + uid
    sessionid1 = '&sessionid=' + sessionid
    param0 = "Udid=58%3A44%3A98%3A53%3A03%3AAA&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + uid1 + sessionid1
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


def con_log(*id):
    uid = id1[0]
    Muid = id1[1]
    sessionid = id1[2]
    y = con(uid, sessionid)
    ppsign = y.get('data', 0).get('uinfo', 0).get('ppsign', 0)
    sign = y.get('data', 0).get('uinfo', 0).get('sign', 0)
    times = '%d' % y.get('data', 0).get('uinfo', 0).get('time', 0)
    ##    print ppsign,sign,times
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=s0ob55jn6kf8v36veh7vbqltk2',
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


def sweep(*id):
    con_log(*id)
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=s0ob55jn6kf8v36veh7vbqltk2',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/dungeon.php?do=Sweep&v=8889&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",
                 '', header1)
    x = conn.getresponse()
    ##print x.status,x.reason,x.read()
    conn.close()


def get_status(*id):
    con_log(*id)
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=s0ob55jn6kf8v36veh7vbqltk2',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    param0 = ''
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    conn.request("POST",
                 "/dungeon.php?do=GetUserDungeon&v=8890&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",
                 '', header1)
    getstatus = conn.getresponse()
    ##   print getstatus.status,getstatus.reason,getstatus.getheaders()
    ##   x=getstatus.read().decode("utf-8")
    buf = StringIO.StringIO(getstatus.read())
    x = gzip.GzipFile(fileobj=buf)
    y = json.loads(x.read())
    ##   print y
    conn.close()
    return y
    ## conn.close()


def fight(*id):
    sweep(*id)
    y = get_status()
    layer = y.get('data', 0).get('UserDungeon', 0).get('CurrentLayer', 0) + 1
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=s0ob55jn6kf8v36veh7vbqltk2',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    temp = con_log(*id)
    while 1:
        param0 = "Layer=" + ('%d' % layer) + "&isManual=0"
        ##     print param0
        conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
        conn.request("POST",
                     "/dungeon.php?do=Fight&v=8891&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",
                     param0, header1)
        getwin = conn.getresponse()
        y = get_status()
        if y.get('data', 0).get('UserDungeon', 0).get('CurrentLayer', 0) >= layer:
            layer += 1
        if y.get('data', 0).get('UserDungeon', 0).get('Resurrection', 0) <= -1:
            return 0
            ##     print x.status,x.reason,x.read()
        print layer
        conn.close()

#
id = [['2014092692358474', '285154', 'tbmXwubvxzvP4nHa'], ['2014121327096245', '288121', 'tbmXwubvxzvP4nHa'],
      ['2015031960117052', '294557', 'tbmXwubvxzvP4nHa'], ['5047214', '198633', 'jlOxpE5vIdZCRceQ'],
      # ['2014082282360039', '283647', 'jAKPM8ITjIyHr5At'],
      ['3586030', '212385', 'fgTUvLEu1B3rVcUk'],
      ['2014021515603023', '264491', 'ekyOlt6j4VLipThy'], ['2014040452624347', '289393', 'ekyOlt6j4VLipThy'],
      ['2015032863087404', '295303', 'ekyOlt6j4VLipThy'], ['2015072214671030', '297875', 'ekyOlt6j4VLipThy'],
      ['2015072214675611', '297876', 'ekyOlt6j4VLipThy'], ['59079768', '289074', 'lVMmfvcdVHKt1OeA'],]
for id1 in id:
    print id1
    fight(*id1)
