# encoding:utf-8
from userinfo.con_log import *

# 获取好友腿毛信息
def GetFriendContributeList(*id1):
    con_log(*id1)
    url = host + '/Journey.php?do=GetFriendContributeList&v=8501&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    flg, jsonresponse = connection(url, data='')
    if flg == 0:           #非正常返回值
        print id1[0], jsonresponse
        return
    return jsonresponse


# 解析好友腿毛信息
def getFriendContribute(*id1):
    friendidAndpointAll = []
    con_log(*id1)
    jsonresponse = GetFriendContributeList(*id1)
    if jsonresponse != None:
        try:
            ContributeList = jsonresponse.get('data', 0).get('friendPointsList', 0)
        except Exception:
            print id1[0], 'unkown error'
            return
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
        return friendidAndpointAll, sum
    else:
        return



# 领取好友腿毛
def GetContributePoints(friendidAndpontList, sum, *id1):
    con_log(*id1)
    for FriendContributeId in friendidAndpontList:
        url = host + '/Journey.php?do=GetContributePoints&v=8502&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
        data = 'friendUid=' + '%d' %FriendContributeId[0]
        flg, jsonresponse = connection(url, data)
        if flg == 1:
            print id1[0], '领取', sum
        else:
            print id1[0], jsonresponse

# 获取个人lls信息
def GetUserJourneysStatus(*id1):
    con_log(*id1)
    url = host + '/Journey.php?do=GetUserJourneysStatus&v=4701&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    flg, jsonresponse = connection(url, data='')
    if flg == 0:
        print id1[0], jsonresponse
        return
    return jsonresponse

# 解析个人lls信息
def getUserJourneysInfo(UserJourneysInfo, *id1):
    data = UserJourneysInfo.get('data', 0).get('journeyList', 0)
    userpoint = data.get('userPoints', 0)    #个人lls积分
    userrank = data.get('userPointRank', 0)  #个人lls排名
    type = data.get('nextPointAward', 0).get('type', 0)
    value = data.get('nextPointAward', 0).get('value', 0)
    print ('{0: ^8}{1: ^10}{2: ^5}' .format(id1[0], userpoint, userrank))