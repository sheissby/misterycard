import httplib,urllib,urllib2,re,time,json,requests

def con(uid):
    header1={'Host':'master.xiaomi.mysticalcard.com','Cookie':'_sid=57t4jueeikn507j59png1gq7q1',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    uid1='&uid='+uid
    param0="sessionid=tbmXwubvxzvP4nHa&Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA="+uid1
##    print 'con uid:',uid
##    print 'con param0:',param0
    conn=httplib.HTTPConnection("master.xiaomi.mysticalcard.com")
    conn.request("POST","/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",param0,header1)
    mpassport=conn.getresponse()
 ##   print mpassport.status
    x=mpassport.read()
    y=json.loads(x)
    ppsign=y.get('data',0).get('uinfo',0).get('ppsign',0)
    sign=y.get('data',0).get('uinfo',0).get('sign',0)
    times=y.get('data',0).get('uinfo',0).get('time',0)
    return y
    conn.close()

def con_log(*id1):
    uid=id1[0]
    Muid=id1[1]
##    print 'con_log:',uid,Muid
    y=con(uid)
    ppsign=y.get('data',0).get('uinfo',0).get('ppsign',0)
    sign=y.get('data',0).get('uinfo',0).get('sign',0)
    times='%d'%y.get('data',0).get('uinfo',0).get('time',0)
    header1={'Host':'s2.xiaomi.mysticalcard.com','Cookie':'_sid=27vjshsgsfpsglp14ts5hba4s5',
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
    d='&MUid='+Muid
    e='&uin='+uid
    f='&nick='+uid
##    print 'con_log:',a,b,c,d,e,f
    param0="access%5Ftoken=&plat=ANDROID%5FXIAOMI&newguide=1&Devicetoken=&Origin=xiaomi&IDFA=&Udid=64%3A09%3A80%3AD3%3AF3%3A0E"+d+e+f+c+b+a
##    print 'con_log:param0=',param0
    conn=httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
    conn.request("POST","/login.php?do=mpLogin&v=3338&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",param0,header1)
    x=conn.getresponse()
    conn.close()

def play_tower(*id1):
    for map_id in [8,7,6]:
        for layer in range(1,6):
            con_log(*id1)
            for cord in range(1,31):               
                header1={'Host':'s2.xiaomi.mysticalcard.com','Cookie':'_sid=27vjshsgsfpsglp14ts5hba4s5',
                 'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
                 'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
                 'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
                 }
                param0="Layer="+('%d' %layer)+"&ItemIndex="+('%d' %cord)+"&manual=0&OpenCardChip=1"+"&MapStageId="+('%d' %map_id)
                conn=httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
                conn.request("POST","/maze.php?do=Battle&v=8995&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1",param0,header1)
                x=conn.getresponse()
                conn.close() 
            print map_id, layer
				
def AwardSalary(*id1):
    con_log(*id1)
    header1={'Host':'s2.xiaomi.mysticalcard.com','Cookie':'_sid=27vjshsgsfpsglp14ts5hba4s5',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0','x-flash-version':'18,0,0,161',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    param0=''
    conn=httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
    conn.request("POST","/user.php?do=AwardSalary&v=9760&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",param0,header1)
    x=conn.getresponse()
    conn.close()

def SendEnergy(*id1):
    con_log(*id1)
    header1={'Host':'s2.xiaomi.mysticalcard.com','Cookie':'_sid=djg1bsuufau300ukr8o3jlbuc3',
             'Accept':'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
             'User-Agent':'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/16.0','x-flash-version':'16,0,0,276',
             'Connection':'Keep-Alive','Cache-Control':'no-cache','Referer':'app:/assets/CardMain.swf','Content-Type':'application/x-www-form-urlencoded'
             }
    param0='Fid=111873'
    conn=httplib.HTTPConnection("s2.xiaomi.mysticalcard.com")
    conn.request("POST","/fenergy.php?do=SendFEnergy&v=5874&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",param0,header1)
    x=conn.getresponse()
    conn.close()

id=[['2014092692358474','285154'],['2014121327096245','288121'],['2015031960117052','294557']]
for id1 in id:
##    con_log(*id1)
    AwardSalary(*id1)
    SendEnergy(*id1)
    print 'id1====================',id1
    play_tower(*id1)