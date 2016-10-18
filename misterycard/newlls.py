# encoding: utf-8
import con_log as login
from id import Cmid

ids = Cmid()

# 获取莉莉丝信息并判断，无lls需要探索返回1，有lls不需要探索返回0
# 返回一个llsid用于查询cd信息
def get_lls_info(id):
    # 获取lls信息
    while 1:
        data =''
        url = 'http://s1.xiaomi.mysticalcard.com/Journey.php?do=GetUserJourneysStatus&v=1522&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
        flg, jsonresponse = login.connection(url, data)
        if flg == 1:
            # 判断lls信息
            Lilisiinfo = jsonresponse.get('data', 0).get('journeyList', 0).get('journeyList', 0)
            currentuid = id[0].decode('utf-8')
            enableAwardList = []  # 未领分list
            if Lilisiinfo:
                for lls in Lilisiinfo:
                    llsNickName = lls.get('NickName', 0)  # 发现者
                    llsstatus = lls.get('Status', 0)  # lls状态
                    llsfleetime = lls.get('FleeTime', 0)  # lls逃跑时间
                    llshpcurrent = lls.get('HPCurrent', 0)  # lls当前血量
                    llsgrade = lls.get('Grade', 0)  # lls级别
                    llsid = lls.get('UserJourneyId', 0)  # lls的id
                    llsenableAward = lls.get('enableAward', 0)  # 是否可领分:1表示可以领分；0表示不可领分
                    if llsenableAward == 1:
                        enableAwardList.append(llsid)
                    # 判断有lls未死或未跑，不需探索
                    if (llsNickName == currentuid and llsstatus == 1 and llshpcurrent > 0 and llsfleetime > 0) \
                            or (llsNickName == currentuid and llsstatus == 0 and llsfleetime > 0):
                        # 有自己的lls
                        return 0, llsgrade, llsid, enableAwardList
                # 没有自己的lls， llsgrade为0
                return 1, 0, llsid, enableAwardList
            else:
                # lls列表为空
                return 1, 0, 0, []
        else:
            print id[0], 'get_lls_info', jsonresponse


def get_cd(llsid):
    # login.con_log(id)
    if llsid == 0:
        return
    while 1:
        data = 'userJourneyId=' + str(llsid)
        url = 'http://s1.xiaomi.mysticalcard.com/Journey.php?do=GetUserJourneyInfo&v=1523&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
        flg, jsonresponse = login.connection(url, data)
        if flg == 1:
            cd = jsonresponse['data']['userJourneyInfo']['CDTimeStatus']  # 1表示没进cd, 0表示进cd
            return cd
        else:
            print id[0], 'get_cd', jsonresponse


# 返回cd和1表示lls死亡，0表示lls没死
def fight_lls(llsid):
    while 1:
        data = 'userJourneyId=' + str(llsid)
        url = 'http://s1.xiaomi.mysticalcard.com/Journey.php?do=JourneyFight&v=1525&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
        flg, jsonresponse = login.connection(url, data)
        if flg == 1:
            llsstatus = jsonresponse.get('data').get('Win')
            fight_cd = get_cd(llsid)
            return fight_cd, llsstatus


# 返回cd状态或out of power
def need_explore(cd):
    # login.con_log(id)
    while 1:
        data = "MapStageDetailId=53"
        url = 'http://s1.xiaomi.mysticalcard.com/mapstage.php?do=Explore&v=1524&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
        flg, jsonresponse = login.connection(url, data)
        string = u'行动力不足!每10分钟可恢复1点!您也可以使用晶钻购买行动力哦!'
        if jsonresponse == string:
            print id[0], 'out of power'
            return 2, 'out of power'
        elif flg == 1 and 'JourneyInfo' in jsonresponse['data'].keys():
            lilisiHP = jsonresponse.get('data', 0).get('JourneyInfo', 0).get('HPCount', 0)
            llsid = jsonresponse.get('data', 0).get('JourneyInfo', 0).get('UserJourneyId', 0)
            # 噩梦和炼狱
            if lilisiHP > 150000:
                if lilisiHP == 236520:
                    print id[0], 'Nightmare of fire!'
                    fight_cd, llsstatus = fight_lls(llsid)
                    return fight_cd, llsstatus
                elif lilisiHP == 238980:
                    print id[0], 'Nightmare of xiexi!'
                    fight_cd, llsstatus = fight_lls(llsid)
                    return fight_cd, llsstatus
                elif lilisiHP == 232340:
                    print id[0], 'Nightmare of Dual Snipe!'
                    fight_cd, llsstatus = fight_lls(llsid)
                    return fight_cd, llsstatus
                elif lilisiHP == 226540:
                    print id[0], 'Nightmare of Teleportation!'
                    fight_cd, llsstatus = fight_lls(llsid)
                    return fight_cd, llsstatus
                elif lilisiHP == 241060:
                    print id[0], 'Nightmare of Concentration!'
                    fight_cd, llsstatus = fight_lls(llsid)
                    return fight_cd, llsstatus
                elif lilisiHP == 353600:
                    print id[0], 'Purgatory of Trap！！！'
                    fight_cd, llsstatus = fight_lls(llsid)
                    return fight_cd, llsstatus
                elif lilisiHP == 350450:
                    print id[0], 'Purgatory of Exile！！！！！！'
                    fight_cd, llsstatus = fight_lls(llsid)
                    return fight_cd, llsstatus
                elif lilisiHP == 356800:
                    print id[0], 'Purgatory of Magic Reosion！！！'
                    fight_cd, llsstatus = fight_lls(llsid)
                    return fight_cd, llsstatus
                elif lilisiHP == 350275:
                    print id[0], 'Purgatory of Retaliation！！！'
                    fight_cd, llsstatus = fight_lls(llsid)
                    return fight_cd, llsstatus
                elif lilisiHP == 352800:
                    print id[0], 'Purgatory of xiexi！！！'
                    fight_cd, llsstatus = fight_lls(llsid)
                    return fight_cd, llsstatus
                else:
                    print id[0], 'unknown lightning'
                    fight_cd, llsstatus = fight_lls(llsid)
                    return fight_cd, llsstatus
            # 困难
            elif lilisiHP > 140000 and lilisiHP < 150000:
                print id[0], 'difficult'
                fight_cd, llsstatus = fight_lls(llsid)
                return fight_cd, llsstatus
            # 简单和普通
            else:
                llsstatus = 2
                while llsstatus == 2 and cd == 1:
                    cd, llsstatus = fight_lls(llsid)
                return cd, llsstatus
        # elif flg == 0:
        #     print id[0], 'explore', jsonresponse


def noneed_explore(cd, llsgrade):
    if cd == 0:
        print id[0], 'CDing'
        return
    if llsgrade == 1 or llsgrade == 2:
        print id[0], 'Easy or Normal!'
    elif llsgrade == 3:
        print id[0], 'Difficult'
    elif llsgrade == 4:
        print id[0], 'Nightmare!'
    elif llsgrade == 5:
        print id[0], 'Purgatory!!!'
    # 处理在cd中并且lls列表为空或没有lls的情况
    elif llsgrade == 0:
        return


def GetJourneyPointReward(enableAwardList):
    url = 'http://s1.xiaomi.mysticalcard.com/Journey.php?do=GetJourneyPointReward&v=9156&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1'
    for awardllsid in enableAwardList:
        data = 'userJourneyId=' + str(awardllsid)
        flg, jsonresponse = login.connection(url, data)


if __name__ == "__main__":
    for id in ids:
        fightresult = 1
        login.con_log(id)
        llsflag, llsgrade, llsid, enableAwardList = get_lls_info(id)
        cd = get_cd(llsid)
        if llsflag == 0 or cd == 0:
            noneed_explore(cd, llsgrade)
        else:
            while cd == 1 and fightresult == 1:
                cd, fightresult = need_explore(cd)
            if cd == 0:
                print id[0], 'CDing'
        if enableAwardList:
            GetJourneyPointReward(enableAwardList)
