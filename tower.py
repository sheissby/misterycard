# encoding:utf-8
import requests
import json
import time

header = {'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5'}


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
                    print message
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
    url = 'http://s1.xiaomi.mysticalcard.com/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
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
    url = 'http://s1.xiaomi.mysticalcard.com/login.php?do=mpLogin&v=1521&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
    jsonresponse = connection(url, conlog_data)
    # print id1[0], 'con_log success!'


# 获得每层信息
def getlayerinfo(layer, map_id):
    item = []   # 需要攻击的格子集合
    count = 0   # 计算格子号
    data = "Layer=" + ('%d' % layer) + '&MapStageId=' + ('%d' % map_id)
    print ('%d' % map_id), '塔' + ('%d' % layer), '层'
    url = 'http://s1.xiaomi.mysticalcard.com/maze.php?do=Info&v=8995&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1'
    jsonresponse = connection(url, data)
    if jsonresponse == u'上一层迷宫还没打完呢!':
        return
    else:
        items = jsonresponse.get('data', 0).get('Map', 0).get('Items', 0)  # 所有格子的信息
        for cords in items:                            # 循环所有格子，获得需要攻击的信息
            cords = int(cords)
            if cords == 2 or cords == 3 or cords == 5:
                item.append(count)                       # 添加格子号到攻击集合
            count += 1                           # 计算需要攻击的格子号
        return item


# 进行攻击
def fight(layer, map_id, item):
    for cord in item:
        fightdata = "Layer=" + ('%d' % layer) + "&ItemIndex=" + ('%d' % cord) + "&manual=0&OpenCardChip=1" + "&MapStageId=" + ('%d' % map_id)
        url = 'http://s1.xiaomi.mysticalcard.com/maze.php?do=Battle&v=8996&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1'
        jsonresponse = connection(url, fightdata)
        if jsonresponse == u'行动力不足!每10分钟可恢复1点!您也可以使用晶钻购买行动力哦!':
            # print ('out of power!')
            return 0


# 循环刷塔
def play_tower(*id1):
    for map_id in [8, 7, 6]:
        for layer in range(1, 6):
            con_log(*id1)
            item = getlayerinfo(layer, map_id)
            if item:
                try:
                    fightresult = fight(layer, map_id, item)
                    if fightresult == 0:
                        return
                except Exception:
                    fightresult = fight(layer, map_id, item)
                    if fightresult == 0:
                        return
            else:
                return


id = [

      ]
for id1 in id:
    print id1[0], 'start'
    play_tower(*id1)
    print id1[0], 'end'
raw_input('The End')
