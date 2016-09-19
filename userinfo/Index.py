# encoding:utf-8
from misterycard.id import *
from userinfo.Energy import *
from userinfo.GetUserBasciInfo import *
from userinfo.LLS import *
from userinfo.heidian import *


id = Cmid()

property = input('1. 查询基本信息\n'
                 '2. 查询lls腿毛\n'
                 '3. 领取全部腿毛\n'
                 '4. 查询lls积分排名\n'
                 '5. 送自己体力\n'
                 '6. 查询黑店积分\n'
                 '7. 兑换黑店积分\n'
                 '8. 领取体力\n'
                 '查询类型:')
if property == 1:
    row = PrettyTable(['id', '等级', '金币', '晶钻', '屌丝券', '体力', '不明', 'cost'])
    # print ('{0: ^18}{1: ^7}{2: ^18}{3: ^8}{4: ^12}{5: ^10}{6: ^10}{7: ^10}'.format('id', '等级', '金币','晶钻','屌丝券','体力','不明','cost'))
    for id1 in id:
        row.add_row(basicInfo(*id1))
    print row
    raw_input()
elif property == 2:
    for id1 in id:
        AllfriendidAndpointList, sum = getFriendContribute(*id1)   #获得腿毛列表
        print id1[0], sum
elif property == 3:
    AllfriendidAndpointList = []
    for id1 in id:
        AllfriendidAndpointList, sum = getFriendContribute(*id1)   #获得腿毛列表
        GetContributePoints(AllfriendidAndpointList, sum, *id1)         #拔腿毛
elif property == 4:
    for id1 in id:
        UserJourneysInfo = GetUserJourneysStatus(*id1)
        if UserJourneysInfo != None:
            getUserJourneysInfo(UserJourneysInfo, *id1)
elif property == 5:
    for id1 in id:
        giveEnergy(*id1)
elif property == 6:
    for id1 in id:
        getHeiDianpoints(*id1)
elif property == 7:
    for id1 in id:
        changeHeiDianPoints(*id1)
elif property == 8:
    id = [['Am', '1592626', '279696', 'ZmeyMlMTIaQoo1vn']]
    for id1 in id:
        getEnergy(*id1)
