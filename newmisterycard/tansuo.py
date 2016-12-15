# encoding:utf-8
from Login import *

if autofight == 'true':
    print 'auto fight is opened'
else:
    print 'auto fight is closed'


# 得到盗贼信息
def GetThieves(id):
    if verification(id) == 1:
        flg = 0
        t = 0  #计算重试次数
        url = host + '/arena.php?do=GetThieves&v=8313&phpp=phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
        # 获取盗贼信息
        while flg == 0 and t < 5:
            flg, jsonresponse = connection(url, data='')
            if flg != 0:
                break
            else:
                time.sleep(5)
                t += 1

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
    else:
        return 2


# 得到最高三星地图id
def getmapid():
    MapStageId =[]    #3星地图id集合
    MapStageIdAll =[] #所有已开地图集合
    flg = 0
    url = host + '/mapstage.php?do=GetUserMapStages&v=3885&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
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
def mapstage(id):
    if verification(id) == 1:
        mapid = getmapid()
        flg = 0
        url = host + '/mapstage.php?do=Explore&v=4581&phpp=phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
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
                    # print id1[0], 'unknown error, continue exploring'
                    time.sleep(1)
                    flg = 0
    else:
        return 0


# 攻击盗贼
def thievesfight(thiefid):
    # 将userthievesid转为string类型
    thievesid = '&UserThievesId=' + str(thiefid)
    data = 'OpenCardChip=1' + thievesid
    url = host + '/arena.php?do=ThievesFight&v=9785&phpp=phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    flg, jsonresponse = connection(url, data)
    if jsonresponse == u'冷却时间未到，请耐心等待！您也可以使用晶钻立即结束冷却时间！':
        print id1[0], 'CDing'
        return 0

# 账户列表
ids = Amid()
alwaystansuo = raw_input('有贼是否探索：1.否 2.是：')
if alwaystansuo.strip() == '' or not alwaystansuo.isdigit():
    print 'error'
elif alwaystansuo == '1':
    for id in ids:
        ExistThief = GetThieves(id)   # 0表示不需要探索，1表示需要探索
        if ExistThief == 1:
            thiefid = mapstage(id)
            if thiefid != 0 and autofight == 'true':
                thievesfight(thiefid)
        elif ExistThief == 2:
            break
        else:
            print id[0], 'has thief', str((ExistThief/60))+'mins left'
elif alwaystansuo == '2':
    for id1 in id:
        thiefid = 1
        while thiefid != 0:
            thiefid = mapstage(*id1)
            if thiefid != 0 and autofight == 'true':
                thievesfight(thiefid)
