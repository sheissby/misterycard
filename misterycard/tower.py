# encoding:utf-8
import requests
import json
import time
from id import *
# import logging
# import logging.handlers
#
# LOG_FILE = 'log.log'
#
# handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
# fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
#
# formatter = logging.Formatter(fmt)   # 实例化formatter
# handler.setFormatter(formatter)      # 为handler添加formatter
#
# logger = logging.getLogger('log')    # 获取名为tst的logger
# logger.addHandler(handler)           # 为logger添加handler
# logger.setLevel(logging.DEBUG)

header = {'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5'}

def connection(url, data):
    status = 0
    while status == 0:
        try:
            response = requests.post(url, data=data, headers=header)
            x = 0
            while x == 0:
                try:
                    jsonresponse = json.loads(response.content)
                    # logger.info(response.content)
                    x = 1
                except Exception:
                    x = 0
            status = jsonresponse.get('status', 0)
            if status == 0:
                message = jsonresponse.get('message', 0)
                if message == '':
                    print '登录失败'
                    time.sleep(1)
                else:
                    # print message
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
    # print jsonresponse
    if jsonresponse == u'上一层迷宫还没打完呢!':
        print jsonresponse
        return
    elif jsonresponse == u'迷宫尚未开启.':
        print jsonresponse
        return
    else:
        items = jsonresponse.get('data', 0).get('Map', 0).get('Items', 0)  # 所有格子的信息
        for cords in items:                            # 循环所有格子，获得需要攻击的信息
            cords = int(cords)
            if cords == 2 or cords == 3 or cords == 5:
                item.append(count)                       # 添加格子号到攻击集合
            count += 1                           # 计算需要攻击的格子号
        print item
        return item


# 进行攻击
def fight(layer, map_id, item):
    for cord in item:
        i = 0
        while i < 2:
            # logger.info(cord)
            fightdata = "Layer=" + ('%d' % layer) + "&ItemIndex=" + ('%d' % cord) + "&manual=0&OpenCardChip=1" + "&MapStageId=" + ('%d' % map_id)
            url = 'http://s1.xiaomi.mysticalcard.com/maze.php?do=Battle&v=8996&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1'
            jsonresponse = connection(url, fightdata)
            print type(jsonresponse)
            if jsonresponse == u'行动力不足!每10分钟可恢复1点!您也可以使用晶钻购买行动力哦!':
                i += 1
                time.sleep(1)
                if i == 2:
                    print ('out of power!')
                    return 0
            else:
                break


# 循环刷塔
def play_tower(*id1):
    for map_id in [8, 7, 6]:
        con_log(*id1)
        # logger.info(map_id)
        for layer in range(1, 6):
            # con_log(*id1)
            # logger.info(layer)
            item = getlayerinfo(layer, map_id)
            if item:
                fightresult = fight(layer, map_id, item)
                if fightresult == 0:
                    return


id = Cmid()
# id = [['Bm', '2016030615546648', '304592', 'ZmeyMlMTIaQoo1vn'],['Dsus4', '2013122514488598', '290176', 'LnQ6qpKCyY95nIrg']]
for id1 in id:
    print id1[0], 'start'
    # logger.info(id1[0])
    play_tower(*id1)
    print id1[0], 'end'
# raw_input('The End')
