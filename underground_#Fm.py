import httplib,urllib,urllib2,re,time,json,StringIO,gzip

def con():
    header1={'Host':'master.xiaomi.mysticalcard.com','Cookie':'_sid=ul167mlqjipsp524sevujeks26',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    param0="uid=2015031960117052&sessionid=tbmXwubvxzvP4nHa&Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA="
    conn=httplib.HTTPConnection("master.xiaomi.mysticalcard.com")
    conn.request("POST","/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",param0,header1)
    mpassport=conn.getresponse()
    x=mpassport.read()
    y=json.loads(x)
    ppsign=y.get('data',0).get('uinfo',0).get('ppsign',0)
    sign=y.get('data',0).get('uinfo',0).get('sign',0)
    times=y.get('data',0).get('uinfo',0).get('time',0)
    return y
    conn.close()

def con_log():
    y=con()
    ppsign=y.get('data',0).get('uinfo',0).get('ppsign',0)
    sign=y.get('data',0).get('uinfo',0).get('sign',0)
    times='%d'%y.get('data',0).get('uinfo',0).get('time',0)
    header1={'Host':'s2.xiaomi.mysticalcard.com','Cookie':'_sid=0aqv77oen00gcgpbs3k4fdq0k1',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    params=urllib.urlencode({'access%5Ftoken':'','plat':'ANDROID%5FXIAOMI','nick':'2015031960117052','newguide':'1',
                             'time':times,'ppsign':ppsign,'sign':sign,'MUid':'294557','Devicetoken':'','Origin':'xiaomi',
                             'IDFA':'','uin':'2015031960117052','Udid':'64%3A09%3A80%3AD3%3AF3%3A0E'})
    a='&ppsign='+ppsign
    b='&sign='+sign
    c='&time='+times
    param0="access%5Ftoken=&plat=ANDROID%5FXIAOMI&MUid=294557&newguide=1&uin=2015031960117052&Devicetoken=&Origin=xiaomi&IDFA=&nick=2015031960117052&Udid=64%3A09%3A80%3AD3%3AF3%3A0E"+c+b+a
    conn=httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
    conn.request("POST","/login.php?do=mpLogin&v=3338&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",param0,header1)
    x=conn.getresponse()
    conn.close()

def sweep():
    con_log()
    header1={'Host':'s2.xiaomi.mysticalcard.com','Cookie':'_sid=0aqv77oen00gcgpbs3k4fdq0k1',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    conn=httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
    conn.request("POST","/dungeon.php?do=Sweep&v=8889&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",'',header1)
    x=conn.getresponse()
##    print x.status,x.reason,x.read()
    conn.close()


def get_status():
    con_log()
    header1={'Host':'s2.xiaomi.mysticalcard.com','Cookie':'_sid=0aqv77oen00gcgpbs3k4fdq0k1',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    param0=''
    conn=httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
    conn.request("POST","/dungeon.php?do=GetUserDungeon&v=8890&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",'',header1)
    getstatus=conn.getresponse()
 ##   print getstatus.status,getstatus.reason,getstatus.getheaders()
 ##   x=getstatus.read().decode("utf-8")
    buf = StringIO.StringIO(getstatus.read())
    x = gzip.GzipFile(fileobj=buf)
    y=json.loads(x.read())
 ##   print y
    conn.close()
    return y
 ## conn.close()

def fight():
    sweep()
    y=get_status()
    layer=y.get('data',0).get('UserDungeon',0).get('CurrentLayer',0)+1
    header1={'Host':'s2.xiaomi.mysticalcard.com','Cookie':'_sid=0aqv77oen00gcgpbs3k4fdq0k1',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    temp=con_log()
    while 1:            
        param0="Layer="+('%d' %layer)+"&isManual=0"
 ##     print param0
        conn=httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
        conn.request("POST","/dungeon.php?do=Fight&v=8891&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",param0,header1)
        getwin=conn.getresponse()
        y=get_status()
        if y.get('data',0).get('UserDungeon',0).get('CurrentLayer',0)>=layer:
            layer+=1
        if y.get('data',0).get('UserDungeon',0).get('Resurrection',0)<=-1:
            return 0
 ##     print x.status,x.reason,x.read()
        print layer
        conn.close()

fight()        

