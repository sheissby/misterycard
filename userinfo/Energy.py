# encoding:utf-8
from userinfo.con_log import *

# 送自己体力
def giveEnergy(*id1):
    con_log(*id1)
    url = host + '/fenergy.php?do=SendFEnergy&v=2007&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    data = 'Fid=105009'
    flg, jsonresponse = connection(url, data)
    if flg == 0:
        print id1[0], jsonresponse


# 领取体力
def getEnergy(*id1):
    con_log(*id1)
    EnergySurplusList = []      # 定义送体力好友list
    url = host + '/friend.php?do=GetFriends&v=9804&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    # 获取好友列表
    flg, jsonresponse = connection(url, data='')
    if flg != 0:
        friends = jsonresponse.get('data').get('Friends')
        # 遍历好友信息
        for friend in friends:
            frienduid = friend.get('Uid')   #获得好友id
            friendname = friend.get('NickName')
            friendEnergySurplus = friend.get('FEnergySurplus')    #获得好友送体力信息
            # print frienduid, friendname
            if friendEnergySurplus == 1:
                EnergySurplusList.append(frienduid)     #送体力好友id集合
    else:
        print id1[0], jsonresponse

    # 送好友体力
    url = host + '/fenergy.php?do=SendFEnergy&v=9804&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    EnergySendList = ['104681','104886', '105245', '105265', '105290', '105545',
                      '106192', '106396', '106798', '106752', '107217', '107504',
                      '107663', '108118']
    for EnergySend in EnergySendList:
        data = 'Fid=' + EnergySend
        flg, jsonresponse = connection(url, data=data)
        if flg == 0:
            if jsonresponse == u'今日已经赠送过该好友！':
                break
            print id1[0], jsonresponse

    # 领取体力
    url = host + '/fenergy.php?do=GetFEnergy&v=9806&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    for EnergySurplus in EnergySurplusList:
        data = 'Fid=' + EnergySurplus
        flg, jsonresponse = connection(url, data=data)
        if flg == 0:
            if jsonresponse == u'今日领取达到上限！':
                print jsonresponse
                break
            print id1[0], jsonresponse
