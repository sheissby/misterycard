# encoding: utf-8
import con_log as login
from id import *

ids = Cmid()


# 获取莉莉丝信息并判断，无lls需要探索返回1，有lls不需要探索返回0
# 返回一个llsid用于查询cd信息
def get_lls_info(id):
    # 获取lls信息
    while 1:
        data =''
        url = 'http://s1.xiaomi.mysticalcard.com/Journey.php?do=GetUserJourneysStatus&v=8313&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
        flg, jsonresponse = login.connection(url, data)
        if flg == 1:
            # 判断lls信息
            Lilisiinfo = jsonresponse.get('data', 0).get('journeyList', 0).get('journeyList', 0)
            currentuid = id[0].decode('utf-8')
            enableAwardList = []  # 未领分list
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
                    return 0, llsgrade, llsid, enableAwardList, llsstatus
                else:
                    return 1, llsgrade, llsid, enableAwardList, llsstatus
        else:
            print id[0], 'get_lls_info', jsonresponse


def get_cd(llsid):
    login.con_log(id)
    while 1:
        data = 'userJourneyId=' + str(llsid)
        url = 'http://s1.xiaomi.mysticalcard.com/Journey.php?Journey.php?do=GetUserJourneyInfo&v=3338&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
        flg, jsonresponse = login.connection(url, data)
        if flg == 1:
            cd = jsonresponse['data']['userJourneyInfo']['CDTimeStatus']  # 1表示没进cd
            return cd
        else:
            print id[0], 'get_cd', jsonresponse


# 返回cd和1表示lls死亡，0表示lls没死
def fight_lls(llsid):
    data = 'userJourneyId=' + str(llsid)
    url = 'http://s1.xiaomi.mysticalcard.com/Journey.php?do=JourneyFight&v=9785&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    flg, jsonresponse = login.connection(url, data)
    llsstatus = jsonresponse['data']['Win']
    fight_cd = get_cd(llsid)
    return fight_cd, llsstatus


# 返回cd状态或out of power
def need_explore():
    while 1:
        data = "MapStageDetailId=53"
        url = 'http://s1.xiaomi.mysticalcard.com/mapstage.php?do=Explore&v=4581&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
        flg, jsonresponse = login.connection(url, data)
        if flg == 1:
            if 'JourneyInfo' in jsonresponse:
                lilisiHP = jsonresponse.get('data', 0).get('JourneyInfo', 0).get('HPCount', 0)
                llsid = jsonresponse.get('data', 0).get('JourneyInfo', 0).get('UserJourneyId', 0)
                # 噩梦和炼狱
                if lilisiHP > 150000:
                    if lilisiHP == 236520:
                        print id[0], 'Nightmare of fire!', llsid
                        fight_cd = fight_lls(llsid)
                        return fight_cd
                    elif lilisiHP == 238980:
                        print id[0], 'Nightmare of xiexi!', llsid
                        fight_cd = fight_lls(llsid)
                        return fight_cd
                    elif lilisiHP == 232340:
                        print id[0], 'Nightmare of Dual Snipe!', llsid
                        fight_cd = fight_lls(llsid)
                        return fight_cd
                    elif lilisiHP == 226540:
                        print id[0], 'Nightmare of Teleportation!', llsid
                        fight_cd = fight_lls(llsid)
                        return fight_cd
                    elif lilisiHP == 241060:
                        print id[0], 'Nightmare of Concentration!', llsid
                        fight_cd = fight_lls(llsid)
                        return fight_cd
                    elif lilisiHP == 353600:
                        print id[0], 'Purgatory of Trap！！！', llsid
                        fight_cd = fight_lls(llsid)
                        return fight_cd
                    elif lilisiHP == 350450:
                        print id[0], 'Purgatory of Exile！！！！！！', llsid
                        fight_cd = fight_lls(llsid)
                        return fight_cd
                    elif lilisiHP == 356800:
                        print id[0], 'Purgatory of Magic Reosion！！！', llsid
                        fight_cd = fight_lls(llsid)
                        return fight_cd
                    elif lilisiHP == 350275:
                        print id[0], 'Purgatory of Retaliation！！！', llsid
                        fight_cd = fight_lls(llsid)
                        return fight_cd
                    elif lilisiHP == 352800:
                        print id[0], 'Purgatory of xiexi！！！', llsid
                        fight_cd = fight_lls(llsid)
                        return fight_cd
                    else:
                        print id[0], 'unknown lightning', llsid
                        fight_cd = fight_lls(llsid)
                        return fight_cd
                # 困难
                elif lilisiHP > 140000 and lilisiHP < 150000:
                    fight_cd = fight_lls(llsid)
                    print id[0], '出现困难莉莉丝'
                    return fight_cd
                # 简单和普通
                else:
                    fight_cd = fight_lls(llsid)
                    return fight_cd
        elif 'message' in jsonresponse:
            message = jsonresponse['message']
            string = u'行动力不足!每10分钟可恢复1点!您也可以使用晶钻购买行动力哦!'
            if message == string:
                print id[0], 'out of power'
                return 'out of power'
        else:
            print id[0], 'explore', jsonresponse


def noneed_explore(llsgrade, llsid):
    if llsgrade == 1 or llsgrade == 2:
        while cd == 1 or llsstatus == 0:
            cd, fightresult_cd = fight_lls(llsid)
    elif llsgrade == 3:
        print id[0], 'Difficult', llsid
    elif llsgrade == 4:
        print id[0], 'Nightmare!', llsid
    elif llsgrade == 5:
        print id[0], 'Purgatory!!!', llsid


if __name__=="__main__":
    for id in ids:
        login.con_log(id)
        llsflag, llsgrade, llsid, enableAwardList, llsstatus = get_lls_info(id)
        cd = get_cd(llsid)
        if llsflag == 0 or cd != 1:
            noneed_explore(llsgrade, llsid, llsstatus)
        else:
            fightresult = need_explore()
