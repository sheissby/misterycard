# encoding: utf-8
import requests
import json
import time
from login import con_log
from login import connection


#选择地图号
def map_choice():
    url = 'http://s1.xiaomi.mysticalcard.com/towerdup.php?do=Show&v=6533&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
    data = 'MapStageId=9'
    jsonresponse = connection(url, data)

#选择元素塔，建立房间：返回关键信息tid
def build_room(tower_id):
    url = 'http://s1.xiaomi.mysticalcard.com/towerdup.php?do=GetTeamId&v=6534&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
    data = "did="+tower_id
    jsonresponse = connection(url, data)
    return jsonresponse

#进入房间并初始化信息：返回关键信息WallRows & WallCols【墙的信息】+Grids & Monster【怪物位置信息】+stance【人物所在位置信息】+IsFinish【是否通关】
#【进入地图时需初始化2次】
def init_tower(tower_id,tid,uid):
    uids="&uids="+uid
    tids="tid="+tid
    dids="&did="+tower_id
    url = 'http://s1.xiaomi.mysticalcard.com/towerdup.php?do=InTower&v=6535&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
    data = tids+uids+dids
    print data
    jsonresponse = connection(url, data)
    return jsonresponse

#移动命令：从cseat移动到nseat
def move(start,target,tower_id,tid):
    a = int(start)
    b = int(target)
    direct = '0'
    #left='1';right='2';up='3';down='4'
    if (a-b==1):
        direct='1'
    if (a-b==-1):
        direct='2'
    if (a-b==10):
        direct='3'
    if (a-b==-10):
        direct='4'
        
    tids="tid="+tid
    dids="&did="+tower_id
    nseat="&nseat="+target
    cseat="&cseat="+start
    mtype="&type="+direct
    data = tids+dids+nseat+mtype+cseat
    url="http://s1.xiaomi.mysticalcard.com/towerdup.php?do=Move&v=6537&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1"
    jsonresponse = connection(url, data)
    print "move from "+start+" to "+target
    return jsonresponse

#回复体力：返回关键信息sta【体力值】
def recover(tower_id,tid):
    tids="tid="+tid
    dids="&did="+tower_id
    data = tids+dids
    url="http://s1.xiaomi.mysticalcard.com/towerdup.php?do=RecoverSta&v=6538&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1"
    jsonresponse = connection(url, data)
    return jsonresponse

#发动战斗：返回关键信息Win
def battle(target,tower_id,tid):
    tids="tid="+tid
    dids="&did="+tower_id
    siteid="&siteid="+target
    data = tids+siteid+dids
    url="http://s1.xiaomi.mysticalcard.com/towerdup.php?do=Battle&v=6539&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1"
    jsonresponse = connection(url, data)
    return jsonresponse

#阵亡重启：先init地图然后retrieve回到原点
def retrieve(tower_id,tid):
    tids="tid="+tid
    dids="&did="+tower_id
    type="&type=2"
    data = tids+type+dids
    url="http://s1.xiaomi.mysticalcard.com/towerdup.php?do=Revive&v=6540&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1"
    jsonresponse = connection(url, data)
    return jsonresponse

#领取奖励：先init地图查看是否通关，通关就领取奖励
def getaward(tower_id,tid):
    tids="tid="+tid
    dids="&did="+tower_id
    data = tids+dids
    url="http://s1.xiaomi.mysticalcard.com/towerdup.php?do=Award&v=6541&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1"
    jsonresponse = connection(url, data)
    return jsonresponse

#主动退出
def quit():
    tids="tid="+tid
    dids="&did="+tower_id
    data = tids+dids
    url="http://s1.xiaomi.mysticalcard.com/towerdup.php?do=Quit&v=10586&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1"
    jsonresponse = connection(url, data)
    return jsonresponse
 
    
