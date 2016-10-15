# encoding:utf-8
import requests
import json
import time
import ConfigParser

import sys

from id import *

header = {'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s1'}

curpath = sys.path[0]
initpath = curpath + '/init.conf'

# 从配置文件获取指定参数
config = ConfigParser.ConfigParser()
config.read(initpath)
host = config.get('Host', 'host')
threshold = config.get('threshold', 'threshold')
autofight = config.get('auto fight', 'autofight')
if autofight == 'true':
    print 'auto fight is opened'
else:
    print 'auto fight is closed'


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
                    return 0, message
        except requests.ConnectionError, e:
            print e
            status = 0
            time.sleep(1)
        except requests.HTTPError, e:
            print e
            status = 0
            time.sleep(1)
    return 1, jsonresponse


def con(uid, sessionid):
    con_data = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + '&uid=' + uid + '&sessionid=' + sessionid
    url = host + '/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
    flg, jsonresponse = connection(url, con_data)
    if flg == 0:
        print jsonresponse
        return
    return jsonresponse


def con_log(*id1):
    uid = id1[1]
    Muid = id1[2]
    sessionid = id1[3]
    y = con(uid, sessionid)
    if y != None:
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
        url = host + '/login.php?do=mpLogin&v=1521&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
        jsonresponse = connection(url, conlog_data)
        # print id1[0], 'con_log success!'


# 得到盗贼信息
def GetThieves(*id1):
    con_log(*id1)
    flg = 0
    t = 0  #计算重试次数
    url = host + '/arena.php?do=GetThieves&v=8313&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    # 获取盗贼信息
    while flg == 0 and t < 5:
        flg, jsonresponse = connection(url, data='')
        if flg != 0:
            break
        else:
            time.sleep(5)
            t = t + 1

    # 解析盗贼信息
    Thievesinfo = jsonresponse.get('data', 0).get('Thieves', 0)
    currentuid = id1[0]
    currentuid = currentuid.decode('utf-8')
    for a in Thievesinfo:
        thievesNickName = a.get('NickName', 0)
        thievesstatus = a.get('Status', 0)
        thievesfleetime = a.get('FleeTime', 0)
        thieveshpcurrent = a.get('HPCurrent', 0)
        # 判断有贼未死或有贼未跑，不需探索
        if (thievesNickName == currentuid and thievesstatus == 1 and thieveshpcurrent > 0 and thievesfleetime > 0) \
                or (thievesNickName == currentuid and thievesstatus == 0 and thievesfleetime > 0):
            return thievesfleetime
    return 1


# 得到最高三星地图id
def getmapid():
    MapStageId =[]    #3星地图id集合
    MapStageIdAll =[] #所有已开地图集合
    flg = 0
    url = host + '/mapstage.php?do=GetUserMapStages&v=3885&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
    while flg == 0:
        flg, jsonresponse = connection(url, data='')
        if flg != 0:
            mapinfoall = jsonresponse.get('data')
            for i in mapinfoall:
                MapStageDetailId = mapinfoall[i].get('MapStageDetailId')
                star = mapinfoall[i].get('FinishedStage')
                MapStageIdAll.append(int(MapStageDetailId))
                if star == u'3':
                    MapStageId.append(int(MapStageDetailId))
            topid = sorted(MapStageIdAll)[-1]
            if len(MapStageId) != 0:
                threestarid = sorted(MapStageId)[-1]
                if topid - threestarid > int(threshold):
                    return topid
                else:
                    return threestarid
            else:
                return topid


# 进行探索
def mapstage(*id1):
    con_log(*id1)
    mapid = getmapid()
    flg = 0
    url = host + '/mapstage.php?do=Explore&v=4581&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    data = "MapStageDetailId=" + str(mapid)
    while flg == 0:
        flg, jsonresponse = connection(url, data)
        # 探索成功
        if flg != 0:
            # 判断出现盗贼
            try:
                jsonresponse = jsonresponse.get('data')
            except Exception:
                print 'unknown error'
            if 'ThievesInfo' in jsonresponse:
                try:
                    Type = jsonresponse.get('ThievesInfo', 0).get('Type', 0)
                    userthievesid = jsonresponse.get('ThievesInfo', 0).get('UserThievesId', 0)
                    if Type == 2:
                        print id1[0], 'appear elite thief!!!'
                    if Type == 1:
                        print id1[0], 'appear normal thief'
                    return userthievesid
                except Exception:
                    print 'unknown error'
                    return 0
            # 未出现盗贼
            else:
                flg = 0
        else:
            if jsonresponse == u'行动力不足!每10分钟可恢复1点!您也可以使用晶钻购买行动力哦!':
                print id1[0], 'out of power!'
                return 0
            if jsonresponse == u'关卡尚未开启!':
                print id1[0], jsonresponse
                return 0
            else:
                print id1[0], 'unknown error, continue exploring'
                time.sleep(5)
                flg = 0


# 攻击盗贼
def thievesfight(thiefid):
    # 将userthievesid转为string类型
    thievesid = '&UserThievesId=' + str(thiefid)
    data = 'OpenCardChip=1' + thievesid
    url = host + '/arena.php?do=ThievesFight&v=9785&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    flg, jsonresponse = connection(url, data)
    if jsonresponse == u'冷却时间未到，请耐心等待！您也可以使用晶钻立即结束冷却时间！':
        print id1[0], 'CDing'
        return 0

# 账户列表
id = Cmid()
alwaystansuo = raw_input('有贼是否探索：1.否 2.是：')
if alwaystansuo.strip() == '' or not alwaystansuo.isdigit():
    print 'error'
elif alwaystansuo == '1':
    for id1 in id:
        ExistThief = GetThieves(*id1)   # 0表示不需要探索，1表示需要探索
        if ExistThief == 1:
            thiefid = mapstage(*id1)
            if thiefid != 0 and autofight == 'true':
                thievesfight(thiefid)
        else:
            print id1[0], 'has thief', str((ExistThief/60))+'mins left'
elif alwaystansuo == '2':
    for id1 in id:
        thiefid = 1
        while thiefid != 0:
            thiefid = mapstage(*id1)
            if thiefid != 0 and autofight == 'true':
                thievesfight(thiefid)
