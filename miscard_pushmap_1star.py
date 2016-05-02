import httplib,urllib,urllib2,re,time,json,StringIO,gzip

def con(uid):
    header1={'Host':'master.xiaomi.mysticalcard.com','Cookie':'_sid=tevb5auedirqipkuck8l52cuh0',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    param0="uid="+uid+"&sessionid=IggFdDB5eE6uERXL&Udid=E0%3A69%3A95%3A82%3A9A%3AD0&plat=ANDROID%5FXIAOMI&newguide=1&IDFA="
    conn=httplib.HTTPConnection("master.xiaomi.mysticalcard.com")
    conn.request("POST","/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",param0,header1)
    mpassport=conn.getresponse()
 ##   print mpassport.status
 ##   print mpassport.reason
    x=mpassport.read()
    # print x
    y=json.loads(x)
    conn.close()
    return y

def con_log(uid,MUid):
    while 1:
        y=con(uid)
        if (y.get('status',0) == 1):
            break
    ppsign=y.get('data',0).get('uinfo',0).get('ppsign',0)
    sign=y.get('data',0).get('uinfo',0).get('sign',0)
    times='%d'%y.get('data',0).get('uinfo',0).get('time',0)
 ##   print ppsign,sign,times
    header1={'Host':'s1.xiaomi.mysticalcard.com','Cookie':'_sid=1d7bcrm0s2nv3vfsomd1ipvb67',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    params=urllib.urlencode({'access%5Ftoken':'','plat':'ANDROID%5FXIAOMI','nick':'2015061387108303','newguide':'1',
                             'time':times,'ppsign':ppsign,'sign':sign,'MUid':'296766','Devicetoken':'','Origin':'xiaomi',
                             'IDFA':'','uin':'2015061387108303','Udid':'E0%3A69%3A95%3A82%3A9A%3AD0'})
    a='&ppsign='+ppsign
    b='&sign='+sign
    c='&time='+times
    param0="access%5Ftoken=&plat=ANDROID%5FXIAOMI&MUid="+MUid+"&newguide=1&uin="+uid+"&Devicetoken=&Origin=xiaomi&IDFA=&nick="+uid+"&Udid=E0%3A69%3A95%3A82%3A9A%3AD0"+c+b+a
##    print param0
##    print params
    conn=httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    conn.request("POST","/login.php?do=mpLogin&v=3338&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",param0,header1)
    x=conn.getresponse()
 ##   print x.status,x.reason,x.read()
    conn.close()

def Get_User_Info():
    header1={'Host':'s1.xiaomi.mysticalcard.com','Cookie':'_sid=1d7bcrm0s2nv3vfsomd1ipvb67',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    param0="pvpNewVersion=1"
    conn=httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    conn.request("POST","/user.php?do=GetUserinfo&OpenCardChip=1&v=6499&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",param0,header1)
    Info=conn.getresponse()
    buf = StringIO.StringIO(Info.read())
    x = gzip.GzipFile(fileobj=buf)
    y=json.loads(x.read())
    return y.get('data',0).get('Cash',0)
    conn.close()

def Get_Map_Stages():
    header1={'Host':'s1.xiaomi.mysticalcard.com','Cookie':'_sid=1d7bcrm0s2nv3vfsomd1ipvb67',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    conn=httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    conn.request("POST","/mapstage.php?do=GetUserMapStages&v=7140&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",'',header1)
    map=conn.getresponse()
    buf = StringIO.StringIO(map.read())
    x = gzip.GzipFile(fileobj=buf)
    y=json.loads(x.read())
    return y
 ## conn.close()

def push_star1(uid,MUid):
    con_log(uid,MUid)
    header1={'Host':'s1.xiaomi.mysticalcard.com','Cookie':'_sid=1d7bcrm0s2nv3vfsomd1ipvb67',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    map_id=input("please enter the map_id: ")
    for i in range(1,10):
        param0="MapStageDetailId="+('%d' %map_id)+"&isManual=0"
        # print param0
        z=Get_Map_Stages()
        # if (z.get('data',0).get(('%d' %map_id),0) == 0):
        conn=httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
        conn.request("POST","/mapstage.php?do=EditUserMapStages&v=7141&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",param0,header1)
        beat=conn.getresponse()
        buf = StringIO.StringIO(beat.read())
        x = gzip.GzipFile(fileobj=buf)
        y=json.loads(x.read())
##           y=json.loads(beat.read())
        if(y.get('data',0).get('Win',0)!=2):
            print "win"
            return 1
        else:
            print "fail"
        con_log(uid,MUid)
    return 0


def Do_maps():
    print "program begins"
    #enter your own uid and MUid
    uid='1592626';MUid='279696'
    push_star1(uid,MUid)
    print "program ends"
    return 0;
      
Do_maps()