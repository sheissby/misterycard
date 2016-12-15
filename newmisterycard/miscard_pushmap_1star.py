# encoding: utf-8
from Login import *
import httplib,json,StringIO,gzip

def Get_User_Info():
    header1={'Host':'s1.jinzhan.mysticalcard.com','Cookie':'_sid=1d7bcrm0s2nv3vfsomd1ipvb67',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    param0="pvpNewVersion=1"
    conn=httplib.HTTPConnection("s1.jinzhan.mysticalcard.com")
    conn.request("POST","/user.php?do=GetUserinfo&OpenCardChip=1&v=6499&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'",param0,header1)
    Info=conn.getresponse()
    buf = StringIO.StringIO(Info.read())
    x = gzip.GzipFile(fileobj=buf)
    y=json.loads(x.read())
    return y.get('data',0).get('Cash',0)
    conn.close()

def Get_Map_Stages():
    header1={'Host':'s1.jinzhan.mysticalcard.com','Cookie':'_sid=1d7bcrm0s2nv3vfsomd1ipvb67',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    conn=httplib.HTTPConnection("s1.jinzhan.mysticalcard.com")
    conn.request("POST","/mapstage.php?do=GetUserMapStages&v=7140&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'",'',header1)
    map=conn.getresponse()
    buf = StringIO.StringIO(map.read())
    x = gzip.GzipFile(fileobj=buf)
    y=json.loads(x.read())
    return y
 ## conn.close()

def push_star1(id):
    if verification(id) == 1:
        header1={'Host':'s1.jinzhan.mysticalcard.com','Cookie':'_sid=1d7bcrm0s2nv3vfsomd1ipvb67',
                 'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
                 'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
                 'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
                 }
        map_id=input("please enter the map_id: ")
        for i in range(1,30):
            param0="MapStageDetailId="+('%d' %map_id)+"&isManual=0"
            # print param0
            z=Get_Map_Stages()
            # if (z.get('data',0).get(('%d' %map_id),0) == 0):
            conn=httplib.HTTPConnection("s1.jinzhan.mysticalcard.com")
            conn.request("POST","/mapstage.php?do=EditUserMapStages&v=7141&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'",param0,header1)
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
            # con_log(uid,MUid)
        return 0


def Do_maps():
    print "program begins"
    id = ['Am', 'sheiss', '123456']
    push_star1(id)
    print "program ends"
    return 0

Do_maps()