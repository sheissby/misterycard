# encoding:utf-8
from userinfo.con_log import *
from prettytable import PrettyTable

# 获取个人基本信息
def GetUserInfo(*id1):
    con_log(*id1)
    data = 'pvpNewVersion=1'
    url = host + '/user.php?do=GetUserinfo&OpenCardChip=1&v=1522&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    flg, jsonresponse = connection(url, data)
    if flg == 0:
        print id1[0], jsonresponse
        return
    return jsonresponse


# 解析个人基本信息
def basicInfo(*id1):
    userinfo = GetUserInfo(*id1)
    if userinfo != None:
        userLevel = userinfo.get('data', 0).get('Level', 0)    #等级
        userCoins = userinfo.get('data', 0).get('Coins', 0)    #金币
        userCash = userinfo.get('data', 0).get('Cash', 0)      #晶钻
        userTicket = userinfo.get('data', 0).get('Ticket', 0)  #屌丝券
        userEnergy = userinfo.get('data', 0).get('Energy', 0)  #体力
        userThievesTimes = userinfo.get('data', 0).get('ThievesTimes', 0) #不明
        userName = userinfo.get('data', 0).get('NickName', 0)  #游戏名字
        # userPrevExp = userinfo.get('data', 0).get('PrevExp', 0)
        # userNextExp = userinfo.get('data', 0).get('NextExp', 0)
        # LevelUpExp = int(userNextExp) - int(userPrevExp)
        LeaderShip = userinfo.get('data', 0).get('LeaderShip', 0)  #Cost
        # print userName, userLevel, userCoins, userCash, userTicket, userEnergy, userThievesTimes, LeaderShip
        data = [userName.encode('utf-8'), userLevel, userCoins, userCash, userTicket, userEnergy, userThievesTimes, LeaderShip]
        return data
        # print('{0: ^18}{1: ^5}{2: ^15}{3: ^8}{4: ^8}{5: ^5}{6: ^5}{7: ^6}'
        #       .format(userName.encode('utf-8'), userLevel, userCoins, userCash, userTicket, userEnergy, userThievesTimes, LeaderShip))
