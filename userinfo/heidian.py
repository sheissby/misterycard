# encoding:utf-8
from userinfo.con_log import *

def getHeiDianpoints(*id1):
    con_log(*id1)
    url = 'http://s1.xiaomi.mysticalcard.com/devoteMazeActivity.php?do=GetActStatus&v=9208&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    flg, jsonresponse = connection(url, data='')
    if flg == 1:
        shougu = jsonresponse.get('data').get('actStatus').get('goods')[0].get('totalPoint')
        shouya = jsonresponse.get('data').get('actStatus').get('goods')[1].get('totalPoint')
        changedpoints = jsonresponse.get('data').get('actStatus').get('recordPoint', 0)
        print id1[0], shougu, '+', shouya, '+', changedpoints, '=', shougu+shouya+changedpoints
    else:
        print id1[0], jsonresponse


def changeHeiDianPoints(*id1):
    con_log(*id1)
    url = 'http://s1.xiaomi.mysticalcard.com/devoteMazeActivity.php?do=GetReward&v=9236&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&pl'
    flg, jsonresponse = connection(url, data='')
    if flg == 0:
        print id1[0], jsonresponse
