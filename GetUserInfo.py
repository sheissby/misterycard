# encoding:GBK
import httplib
import json
import StringIO
import gzip
import urllib2


def con(uid, sessionid):
    header1 = {'Host': 'master.xiaomi.mysticalcard.com', 'Cookie': '_sid=57t4jueeikn507j59png1gq7q1',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    uid1 = '&uid=' + uid
    sessionid1 = '&sessionid=' + sessionid
    param0 = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + uid1 + sessionid1
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
    # print id1[0], 'con success!'
    ppsign = y.get('data', 0).get('uinfo', 0).get('ppsign', 0)
    sign = y.get('data', 0).get('uinfo', 0).get('sign', 0)
    times = y.get('data', 0).get('uinfo', 0).get('time', 0)
    conn.close()
    return y


def con_log(*id1):
    uid = id1[1]
    Muid = id1[2]
    sessionid = id1[3]
    y = con(uid, sessionid)
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
    param0 = "access%5Ftoken=&plat=ANDROID%5FXIAOMI&newguide=1&Devicetoken=&Origin=xiaomi&IDFA=&Udid=64%3A09%3A80%3AD3%3AF3%3A0E" + d + e + f + c + b + a
    con_log_status = 0
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    while con_log_status == 0:
        conn.request("POST",
                     "/login.php?do=mpLogin&v=1521&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null",
                     param0, header1)
        res = conn.getresponse()
        x = res.read()
        if len(x) != 0:
            y = json.loads(x)
            con_log_status = y.get('status', 0)
        else:
            con_log_status = 0
    # print id1[0], 'con_log success!'
    conn.close()

#获取个人基本信息
def GetUserInfo(*id1):
    con_log(*id1)
    header1 = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
           'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
           'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
           'x-flash-version': '18,0,0,161',
           'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
           'Content-Type': 'application/x-www-form-urlencoded'
           }
    param2 = 'pvpNewVersion=1'
    conn = httplib.HTTPConnection("s1.xiaomi.mysticalcard.com")
    GetUserinfo_status = 0
    while GetUserinfo_status == 0:
        conn.request("POST",
                     "/user.php?do=GetUserinfo&OpenCardChip=1&v=1522&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1",
                     param2, header1)
        GetUserinfo = conn.getresponse()
        responseheader = GetUserinfo.getheaders()
        isgzipped = responseheader[0]
        if isgzipped[1] == 'gzip':
            compresseddata = GetUserinfo.read()
            compressedstream = StringIO.StringIO(compresseddata)
            gzipper = gzip.GzipFile(fileobj=compressedstream)
            userinfo = gzipper.read()
            userinfojson = json.loads(userinfo)
            GetUserinfo_status = userinfojson.get('status', 0)
        else:
            userinfo = GetUserinfo.read()
            userinfojson = json.loads(userinfo)
            GetUserinfo_status = userinfojson.get('status', 0)
    # print id1[0], 'GetUserinfo sucess!'
    conn.close()
    return userinfojson

#解析个人基本信息
def basicInfo(*id1):
    userinfo = GetUserInfo(*id1)
    userLevel = userinfo.get('data', 0).get('Level', 0)    #等级
    userCoins = userinfo.get('data', 0).get('Coins', 0)    #金币
    userCash = userinfo.get('data', 0).get('Cash', 0)      #晶钻
    userTicket = userinfo.get('data', 0).get('Ticket', 0)  #屌丝券
    userEnergy = userinfo.get('data', 0).get('Energy', 0)  #体力
    userThievesTimes = userinfo.get('data', 0).get('ThievesTimes', 0) #不明
    # userPrevExp = userinfo.get('data', 0).get('PrevExp', 0)
    # userNextExp = userinfo.get('data', 0).get('NextExp', 0)
    # LevelUpExp = int(userNextExp) - int(userPrevExp)
    LeaderShip = userinfo.get('data', 0).get('LeaderShip', 0)  #Cost
    # print id1[0], userLevel, userCoins, userCash, userTicket, userEnergy, userThievesTimes, LeaderShip
    print('{0: ^8}{1: ^5}{2: ^11}{3: ^8}{4: ^8}{5: ^5}{6: ^5}{7: ^6}'.format(id1[0], userLevel, userCoins, userCash, userTicket, userEnergy, userThievesTimes, LeaderShip))

#获取好友腿毛信息
def GetFriendContributeList(*id1):
    con_log(*id1)
    url = 'http://s1.xiaomi.mysticalcard.com/Journey.php?do=GetFriendContributeList&v=8501&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    # values = {'username' : 'cqc',  'password' : 'XXXX' }
    headers = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    data = ''
    ContributeStatus = 0
    while ContributeStatus == 0:
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        if response.info().get('Content-Encoding') == 'gzip':
            compresseddata = response.read()
            compressedstream = StringIO.StringIO(compresseddata)
            gzipper = gzip.GzipFile(fileobj=compressedstream)
            data = gzipper.read()
            if 'message' in data:           #非正常返回值
                Contribute = json.loads(data)
                ContributeStatus = Contribute.get('status', 0)
                Contributemessage = Contribute.get('message', 0)
                if ContributeStatus == 0 and cmp(Contributemessage.encode('utf-8'), '活动未开启'):  #无法参加活动
                    return 0
                else:
                    print '这是什么情况' #未见过的返回值
                    return 0
            else:
                Contribute = json.loads(data)
                ContributeStatus = Contribute.get('status', 0)
        else:
            data = response.read()
            if 'message' in data:
                Contribute = json.loads(data)
                ContributeStatus = Contribute.get('status', 0)
                Contributemessage = Contribute.get('message', 0)
                if ContributeStatus == 0 and cmp(Contributemessage.encode('utf-8'), '活动未开启'):
                    return 0
                else:
                    print '这是什么情况'
                    return 0
            else:
                Contribute = json.loads(data)
                ContributeStatus = Contribute.get('status', 0)
    return Contribute

#解析好友腿毛信息
def getFriendContribute(*id1):
    friendidAndpointAll = []      #所有好友id，分数集合
    sum = 0
    FriendContribute = GetFriendContributeList(*id1)
    if FriendContribute == 0:
        if property == 2:
            print id1[0], '无法参加活动'
    else:
        ContributeList = FriendContribute.get('data', 0).get('friendPointsList', 0)
        for friendPointsList in ContributeList:
            friendidAndpoint = []          #每个好友id，分数集合
            friendId = friendPointsList.get('friendId', 0)
            contributePoint = friendPointsList.get('contributePoint', 0)
            nickName = friendPointsList.get('nickName', 0)
            avatar = friendPointsList.get('avatar', 0)
            totalPoint = friendPointsList.get('totalPoint', 0)
            sum = sum + int(contributePoint)
            friendidAndpoint.append(friendId)
            friendidAndpoint.append(int(contributePoint))
            friendidAndpointAll.append(friendidAndpoint)
        if property == 2:
            print id1[0], sum
    return friendidAndpointAll, sum

#领取好友腿毛
def GetContributePoints(friendidAndpontList, sum):
    con_log(*id1)
    for FriendContributeId in friendidAndpontList:
        url = 'http://s1.xiaomi.mysticalcard.com/Journey.php?do=GetContributePoints&v=8502&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
        headers = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
                   'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
                   'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
                   'x-flash-version': '18,0,0,161',
                   'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        data = 'friendUid=' + '%d' %FriendContributeId[0]
        GetPointsStatus = 0
        while GetPointsStatus == 0:
            request = urllib2.Request(url, data, headers)
            response = urllib2.urlopen(request)
            if response.info().get('Content-Encoding') == 'gzip':
                compresseddata = response.read()
                compressedstream = StringIO.StringIO(compresseddata)
                gzipper = gzip.GzipFile(fileobj=compressedstream)
                data = gzipper.read()
                GetPoints = json.loads(data)
                GetPointsStatus = GetPoints.get('status', 0)
            else:
                data = response.read()
                GetPointsStatus = json.loads(data)
                GetPointsStatus = GetPointsStatus.get('status', 0)
    print id1[0], '领取', sum

#获取个人lls信息
def GetUserJourneysStatus(*id1):
    con_log(*id1)
    url = 'http://s1.xiaomi.mysticalcard.com/Journey.php?do=GetUserJourneysStatus&v=4701&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    # values = {'username' : 'cqc',  'password' : 'XXXX' }
    headers = {'Host': 's1.xiaomi.mysticalcard.com', 'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5',
               'Accept': 'text/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, text/css, image/png, image/jpeg, image/gif;q=0.8, application/x-shockwave-flash, video/mp4;q=0.9, flv-application/octet-stream;q=0.8, video/x-flv;q=0.7, audio/mp4, application/futuresplash, */*;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/18.0',
               'x-flash-version': '18,0,0,161',
               'Connection': 'Keep-Alive', 'Cache-Control': 'no-cache', 'Referer': 'app:/assets/CardMain.swf',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    data = ''
    UserJourneysStatus = 0
    while UserJourneysStatus == 0:
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        if response.info().get('Content-Encoding') == 'gzip':
            compresseddata = response.read()
            compressedstream = StringIO.StringIO(compresseddata)
            gzipper = gzip.GzipFile(fileobj=compressedstream)
            data = gzipper.read()
            if 'message' in data:           #非正常返回值
                print 'error'
                return 0
            else:
                UserJourneys = json.loads(data)
                UserJourneysStatus = UserJourneys.get('status', 0)
        else:
            data = response.read()
            if 'message' in data:
                print id1[0], 'error'
                return 0
            else:
                UserJourneys = json.loads(data)
                UserJourneysStatus = UserJourneys.get('status', 0)
    return UserJourneys


#解析个人lls信息
def getUserJourneysInfo(UserJourneysInfo):
    data = UserJourneysInfo.get('data', 0).get('journeyList', 0)
    userpoint = data.get('userPoints', 0)    #个人lls积分
    userrank = data.get('userPointRank', 0)  #个人lls排名
    type = data.get('nextPointAward', 0).get('type', 0)
    value = data.get('nextPointAward', 0).get('value', 0)
    print ('{0: ^8}{1: ^10}{2: ^5}' .format(id1[0], userpoint, userrank))



id = [
      ['Am', '1592626', '279696', 'ILjEr8jamXWQSf4v'],
    ['#Cm', '2014092692358474', '285154', 'ILjEr8jamXWQSf4v'],
      ['Em', '2014121327096245', '288121', 'ILjEr8jamXWQSf4v'], ['#Fm', '2015031960117052', '294557', 'ILjEr8jamXWQSf4v'],
      #
      ['樱木', '5047214', '198633', '0jOBCWaqFzYqZsNi'], ['利佐伊', '2013072511431198', '209850', '0jOBCWaqFzYqZsNi'],
      ['雷贝拉', '2013072511431214', '209852', '0jOBCWaqFzYqZsNi'],

      # ['赤刀', '26402923', '283622', 'jAKPM8ITjIyHr5At'],
      # ['骷髅大王', '2014082282360039', '283647', 'jAKPM8ITjIyHr5At'], ['獠牙', '2014082382723128', '283732', 'jAKPM8ITjIyHr5At'],
      # ['血刃', '2014082382762366', '283739', 'jAKPM8ITjIyHr5At'], ['军刺', '2014082382896209', '283757', 'jAKPM8ITjIyHr5At'],
      # ['袖箭', '2014082382896212', '283765', 'jAKPM8ITjIyHr5At'],

      ['杰尼龟','2014041855227765','273122', 'L2QLMsVNoY4VYwND'],
      ['小火龙','2014042155811563','273419', 'L2QLMsVNoY4VYwND'], ['妙蛙种子','2014052561883286','278956', 'L2QLMsVNoY4VYwND'],
      ['绿毛虫','2014061766465489','278958', 'L2QLMsVNoY4VYwND'], ['大针蜂','2014061866519659','278984', 'L2QLMsVNoY4VYwND'],
      ['比比鸟','2014061866519756','278986', 'L2QLMsVNoY4VYwND'], ['超音蝠','2014061866528941','279006', 'L2QLMsVNoY4VYwND'],
      ['隆隆岩','2014061866529032','279007', 'L2QLMsVNoY4VYwND'], ['大岩蛇','2014061866529097','279009', 'L2QLMsVNoY4VYwND'],
      ['乘龙','2014061866529223','279045', 'L2QLMsVNoY4VYwND'], ['耿鬼','2014061866529231','279049', 'L2QLMsVNoY4VYwND'],
      ['烈焰马','2014061866529288','279053', 'L2QLMsVNoY4VYwND'], ['吸盘魔偶','2014061866529337','279054', 'L2QLMsVNoY4VYwND'],
      ['胖丁','2014061866529346','279080', 'L2QLMsVNoY4VYwND'], ['阿柏蛇','2014061866529379','279081', 'L2QLMsVNoY4VYwND'],
      ['椰蛋树','2014061866529407','279083', 'L2QLMsVNoY4VYwND'], ['火爆猴','2014061866529462','279085', 'L2QLMsVNoY4VYwND'],
      ['派拉斯','2014061866529470','279086', 'L2QLMsVNoY4VYwND'], ['比雕','2014061866529500','279117', 'L2QLMsVNoY4VYwND'],
      ['雷精灵','2014061866529554','279119', 'L2QLMsVNoY4VYwND'], ['皮卡西','2014061866529628','279122', 'L2QLMsVNoY4VYwND'],
      ['水精灵','2014061866529641','279131', 'L2QLMsVNoY4VYwND'], ['火精灵','2014061866529643','279137', 'L2QLMsVNoY4VYwND'],
      ['胡地','2014061866529675','279164', 'L2QLMsVNoY4VYwND'], ['风速狗','2014061866529735','279165', 'L2QLMsVNoY4VYwND'],
      ['喷火龙','2014061866529744','279166', 'L2QLMsVNoY4VYwND'],

      ['钢板', '3586030', '212385', 'fgTUvLEu1B3rVcUk'],
      ['木板', '2013082711940981', '225069', 'fgTUvLEu1B3rVcUk'], ['石板', '2013083112015559', '226603', 'fgTUvLEu1B3rVcUk'],
      ['铜板', '2013100612632387', '234854', 'fgTUvLEu1B3rVcUk'], ['铁板', '2013100912693148', '236003', 'fgTUvLEu1B3rVcUk']
      ]
print '1. 查询基本信息'
print '2. 查询lls腿毛'
print '3. 领取全部腿毛'
print '4. 查询lls积分排名'
property = input('查询类型:')
if property == 1:
    print ('{0: ^8}{1: ^5}{2: ^11}{3: ^8}{4: ^8}{5: ^5}{6: ^6}{7: ^6}'.format('id', '等级', '金币','晶钻','屌丝券','体力','不明','cost'))
    for id1 in id:
        basicInfo(*id1)
elif property == 2 or property == 3:
    AllfriendidAndpointList = []
    for id1 in id:
        AllfriendidAndpointList, sum = getFriendContribute(*id1)   #获得腿毛列表
        if property == 3:
            GetContributePoints(AllfriendidAndpointList, sum)         #拔腿毛
elif property == 4:
    for id1 in id:
        UserJourneysInfo = GetUserJourneysStatus(*id1)
        if UserJourneysInfo == 0:
            continue
        else:
            getUserJourneysInfo(UserJourneysInfo)
