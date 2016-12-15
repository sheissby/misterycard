# encoding:utf-8
from Login import *


# 获得每层信息
def getlayerinfo(layer, map_id):
    item = []   # 需要攻击的格子集合
    count = 0   # 计算格子号
    data = "Layer=" + ('%d' % layer) + '&MapStageId=' + ('%d' % map_id)
    print ('%d' % map_id), '塔' + ('%d' % layer), '层'
    url = host + '/maze.php?do=Info&v=8995&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
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
            fightdata = "Layer=" + ('%d' % layer) + "&ItemIndex=" + ('%d' % cord) + "&manual=0&OpenCardChip=1" + "&MapStageId=" + ('%d' % map_id)
            url = host + '/maze.php?do=Battle&v=8996&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
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
def play_tower(id):
    for map_id in [8, 7, 6]:
        login(id)
        for layer in range(1, 6):
            item = getlayerinfo(layer, map_id)
            if item:
                fightresult = fight(layer, map_id, item)
                if fightresult == 0:
                    return


ids = Cmid()

for id in ids:
    if verification(id) == 1:
        print id[0], 'start'
        play_tower(id)
        print id[0], 'end'
# raw_input('The End')
