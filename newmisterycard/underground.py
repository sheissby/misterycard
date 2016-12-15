# encoding:utf-8
import gzip
import httplib

import StringIO

from Login import *


def sweep(*id):
    if verification(*id) == 1:
        header1 = {'Host': 's1.jinzhan.mysticalcard.com', 'Cookie': '_sid=s0ob55jn6kf8v36veh7vbqltk2',
                   'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
                   'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
                   'x-flash-version': '18,0,0,161',
                   'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        conn = httplib.HTTPConnection("s1.jinzhan.mysticalcard.com")
        conn.request("POST",
                     "/dungeon.php?do=Sweep&v=8889&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1",
                     '', header1)
        x = conn.getresponse()
        ##print x.status,x.reason,x.read()
        conn.close()
    return 0


def get_status(*id):
    login(*id)
    header1 = {'Host': 's1.jinzhan.mysticalcard.com', 'Cookie': '_sid=s0ob55jn6kf8v36veh7vbqltk2',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    param0 = ''
    conn = httplib.HTTPConnection("s1.jinzhan.mysticalcard.com")
    conn.request("POST",
                 "/dungeon.php?do=GetUserDungeon&v=8890&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1",
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
    if sweep(*id) == 0:
        return
    y = get_status()
    layer = y.get('data', 0).get('UserDungeon', 0).get('CurrentLayer', 0) + 1
    header1 = {'Host': 's1.jinzhan.mysticalcard.com', 'Cookie': '_sid=s0ob55jn6kf8v36veh7vbqltk2',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    temp = login(*id)
    while 1:
        param0 = "Layer=" + ('%d' % layer) + "&isManual=0"
        ##     print param0
        conn = httplib.HTTPConnection("s1.jinzhan.mysticalcard.com")
        conn.request("POST",
                     "/dungeon.php?do=Fight&v=8891&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1",
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

id = Cmid()

for id1 in id:
    print id1[0]
    fight(*id1)
raw_input('End')
