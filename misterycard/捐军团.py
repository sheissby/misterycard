# encoding:utf-8
import time,json,requests
from id import *
header = {'Host': 'master.xiaomi.mysticalcard.com', 'Cookie': '_sid=qg675n070s5pdb9beaosuhdgo4', 
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5', 
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0', 
               'x-flash-version': '18,0,0,161', 
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf', 
               'Content-Type': 'application/x-www-form-urlencoded'}

# 配置文件
host = 'http://s1.xiaomi.mysticalcard.com'



def connection(url, data):
    status = 0
    while status == 0:
        try:
            response = requests.post(url, data=data, headers=header)
            jsonresponse = json.loads(response.content)
            status = jsonresponse.get('status', 0)
            if status == 0:
                message = jsonresponse.get('message', 0)
                if message == '':
                    print '登录失败'
                    time.sleep(1)
                else:
                    return message
        except requests.ConnectionError, e:
            print e
            status = 0
            time.sleep(1)
        except requests.HTTPError, e:
            print e
            status = 0
            time.sleep(1)
    return jsonresponse


def con(uid, sessionid):
    con_data = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + '&uid=' + uid + '&sessionid=' + sessionid
    url = 'http://s1.xiaomi.mysticalcard.com/mpassport.php?do=plogin&v=3468&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
    jsonresponse = connection(url, con_data)
    return jsonresponse


def con_log(*id1):
    uid = id1[1]
    Muid = id1[2]
    sessionid = id1[3]
    y = con(uid, sessionid)
    ppsign = y.get('data', 0).get('uinfo', 0).get('ppsign', 0)
    sign = y.get('data', 0).get('uinfo', 0).get('sign', 0)
    times = '%d' % y.get('data', 0).get('uinfo', 0).get('time', 0)
    a = '&ppsign=' + ppsign
    b = '&sign=' + sign
    c = '&time=' + times
    d = '&MUid=' + Muid
    e = '&uin=' + uid
    f = '&nick=' + uid
    conlog_data = "access%5Ftoken=&plat=ANDROID%5FXIAOMI&newguide=1&Devicetoken=&Origin=xiaomi&IDFA=&Udid=64%3A09%3A80%3AD3%3AF3%3A0E" + d + e + f + c + b + a
    url = 'http://s1.xiaomi.mysticalcard.com/login.php?do=mpLogin&v=3469&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
    jsonresponse = connection(url, conlog_data)



def donate(techType,coins):
    #等级TechType=1，金币2，经验3，强化4，森林5，王国6，蛮荒7，地狱8，商店9
    url='http://s1.xiaomi.mysticalcard.com/legion.php?do=GetLegions&v=9753&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
    jsonresponse = connection(url,'Start=0&Amount=10')
    myLegion=jsonresponse.get('data').get('MyLegion').get('Name')
    print myLegion
    if(techType!=0):
        donate = 'http://s1.xiaomi.mysticalcard.com/legion.php?do=Donate&v=9754&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
        data = 'TechType='+str(techType)+'&Coins='+str(coins)+'&Type=3'
        jsonresponse = connection(donate, data)
    if(techType==0):
        assets = 'http://s1.xiaomi.mysticalcard.com/legion.php?do=Resources&v=9754&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
        assetsData = 'Coins='+str(coins)
        jsonresponse = connection(assets,assetsData)
    
    
  

id = Cmid()

techType=input('''请选择捐款类型：
0.军团资产
1.军团等级
2.金币加成
3.经验加成
4.强化加成
5.森林加成
6.王国加成
7.蛮荒加成
8.地狱加成
9.商店等级
''')
coins = input('''input the donate amount：
''')

for id1 in id:
    con_log(*id1)
    print id1[0],'start'
    donate(techType,coins)
    print id1[0],'end'
